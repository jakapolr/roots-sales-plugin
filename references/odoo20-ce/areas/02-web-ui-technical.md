# Web Client, UI, Productivity & Technical Addons — Odoo 20 CE

Method: tree diff odoo19 vs odoo20 (i18n excluded), manifest diffs, grep. Claims are [code] unless marked [web]. Paths are relative to `odoo20/`. No web research was done.

## 1. Scope
About 105 modules were screened: web, web_tour, web_hierarchy, web_unsplash, html_editor, html_builder, bus, board, digest, onboarding, base_* (setup, import, import_module, automation, geolocalize, install_request, sparse_field, address_extended, report_paper_muncher, report_wkhtmltox), iot_*, printer, spreadsheet* (about 17 modules), data_recycle, attachment_indexation, barcodes*, http_routing, api_doc, rpc, cloud_storage*, auth_* (11 modules), google_*/microsoft_*, privacy_lookup. New in 20: 4 modules (base_report_paper_muncher, base_report_wkhtmltox, printer, iot_webserial). Removed: iot_base, iot_box_image, transifex.

Diff-noise note: nearly every module differs only by i18n files and by the security file rename (see 4.1). Real change is concentrated in web, html_editor, html_builder, bus, spreadsheet, the calendar sync modules, auth_totp/passkey and iot_drivers.

## 2. Module catalogue

| Module | App? | What it does | Status vs 19 |
|---|---|---|---|
| web | no | Web client (OWL), views, reports plumbing | **Heavily changed** (see 4) |
| web_tour | no | Tours and onboarding widgets | Changed: rewritten into plugin architecture (`tour_plugin.js`, `tour_automatic/`, `tour_interactive/`, `tour_recorder/`, `tour_pointer/`) |
| web_hierarchy | no | Hierarchy (org-chart) view | Unchanged-ish (15 files, mostly tests/plugin port) |
| web_unsplash | no | Unsplash image picker | Unchanged-ish |
| html_editor | no | Html editor component and plugin system | Changed: new `components/color_picker`, `suggestion`, `iframe_input`, `dynamic_field`, `dom_observer_plugin`, `controllers/svg_utils.py`. Summary text rewritten. The color picker moved here from web/core. |
| html_builder | no | Website snippet builder (replaces legacy website editor) | Changed: depends now only `html_editor` (was base, html_editor, mail); new `models/`, new shapes (Geometric, Blurry 07-12, devices) |
| html_field_history | - | not present in 20 and not in 19 either | n/a |
| bus | no | Websocket and notifications | Changed: new `bus_dispatcher.py`, `session_helpers.py`; services converted to plugins; security folder moved |
| board | no | Legacy dashboards | Unchanged-ish (security rename only) |
| digest | no | KPI digest emails | Changed: new `wizard/digest_test.py` (`digest.test` model) |
| onboarding | no | Onboarding steps | Unchanged-ish |
| base_setup | no | Settings | Unchanged-ish |
| base_import / base_import_module | no | Import wizard / module import | Unchanged-ish (28 / 14 file diffs, mostly JS port) |
| base_automation | no | Automated actions | Unchanged-ish (access file only) |
| base_geolocalize, base_install_request, base_sparse_field | no | geocoding, install requests, sparse fields | Unchanged-ish |
| base_address_extended | no | Street name/number split | Changed: depends now `['web']` (was base, contacts); `portal` now depends on it; view renamed `res_partner_views.xml` |
| base_report_wkhtmltox | no | **NEW** wkhtmltopdf/wkhtmltoimage engine, extracted from base | New |
| base_report_paper_muncher | no | **NEW** Paper Muncher engine | New |
| printer | no | **NEW** external printers (ZPL, ePOS) | New |
| iot_webserial | no | **NEW** Web Serial devices | New |
| iot_drivers | no | IoT box code | Changed; manifest `installable: False`; large driver reshuffle |
| iot_base, iot_box_image | - | | Removed |
| spreadsheet, spreadsheet_dashboard, spreadsheet_account, 11 dashboard modules | no | Spreadsheet core and BI dashboards | Changed (see 3.5) |
| data_recycle | no | Data recycling | Changed: new `cog_menu`, list view XML removed |
| attachment_indexation | no | Text indexing of attachments | Unchanged-ish |
| barcodes, barcodes_gs1_nomenclature | no | Barcode handling | Changed: service to `barcode_plugin.js`; `barcode_events_mixin.py`, `barcode_handler_field.js` and `float_scannable_field` removed; new `barcode_input`/`barcode_view` components |
| http_routing, rpc | no | Routing / RPC | Small (rpc: `bearer_scope='rpc'`, `odoo.http.router.dispatch_rpc`, `MappingProxyType`) |
| api_doc | no | /doc API playground | Changed (32 files), new `main.js`; JSON2 bearer route `/doc-bearer/index.json` |
| cloud_storage, _azure, _google, _migration | no | Attachments in cloud | Changed: new `controllers/rtc.py`; chatter patches moved from `web_portal` to `web` |
| auth_* (ldap, oauth, passkey, signup, totp, timeout, password_policy*) | no | Auth | Changed: `auth_totp` new `models/ir_http.py`, `static/src/services`; `auth_timeout` login views/controllers removed; passkey/totp security.xml dropped |
| google_calendar, microsoft_calendar | no | Calendar sync | **Changed** (multi-calendar, see 4.7) |
| google_account/gmail/address_autocomplete/recaptcha, microsoft_account/outlook | no | | Unchanged-ish |
| privacy_lookup | no | GDPR lookup | Unchanged-ish |
| transifex | - | | Removed |

## 3. Feature deep-dive

### 3.1 Report engine split (wkhtmltopdf)
- wkhtmltopdf code left core `ir.actions.report`. `base_report_wkhtmltox` (auto_install, post_init_hook sets `ir.config_parameter report.pdf_engine_default = wkhtmltopdf`; `addons/base_report_wkhtmltox/__init__.py`) adds `report_type` value `qweb-pdf-wkhtmltopdf` and holds `_run_wkhtmltopdf`, `_split_table` and the `WkhtmlInfo` binary check (`models/ir_actions_report.py`).
- Core (`odoo/addons/base/models/ir_actions_report.py`) now has an engine-agnostic API: `get_pdf_engine_state(engine_name)` (replaces v19 `get_wkhtmltopdf_state`), `_get_pdf_engine()`, `_run_pdf_engine()`, `_run_pdf_engine_without_processing()`, `_run_image_engine()`. Defaults raise NotImplementedError or return state `install` until an engine module overrides them.
- Web: route `/report/get_pdf_engine_state` (`addons/web/controllers/report.py`); JS messages are now engine-neutral (`web/static/src/webclient/actions/reports/utils.js`).
- `base_report_paper_muncher` (depends base_setup) adds `qweb-pdf-paper-muncher` ("PDF (Paper Muncher)") and runs Paper Muncher >= 0.6 as a subprocess ([code] README). It is Odoo's in-house engine ([web] odoo.github.io/paper-muncher/ per the manifest). It is selectable per report; there is no sign of it becoming the default.
- Answer to "is wkhtmltopdf replaced?": No. It is still the default engine but is now an optional, separated module, loaded via auto_install. `point_of_sale` and `marketing_card` depend on it explicitly. A DB with report type plain `qweb-pdf` resolves to `report.pdf_engine_default` (falls back to wkhtmltopdf).

### 3.2 printer (new)
`printer.printer` (name, ip_address, type zpl|epos, report_ids). `ir.actions.report` gets `printer_ids`; `get_print_jobs()` renders ZPL text reports as-is and renders PDF reports for ePOS printers through `_run_image_engine("wkhtmltopdf", ...)` into a 576px dithered 1-bit image in an ePOS SOAP envelope. Printing happens browser-side: `print_action_handler.js` POSTs straight to the printer (Zebra `/pstprnt`, Epson `/cgi-bin/epos/service.cgi`). Includes a "select printers" wizard, cached printer selection and a reset client action. Designed to be extended by IoT-type modules. Depended on by point_of_sale and stock_delivery (manifests).

### 3.3 IoT
- `iot_webserial` (depends web): Web Serial API access from the browser, no IoT box needed. Contains `WebSerialDevice`, a `WebSerialScale` (9600 baud even parity, status bits) and a "connect web serial scale" widget. Used by point_of_sale and stock_delivery.
- `iot_base` removed. Its only v19 dependent in CE was point_of_sale; no module in 20 references it. Evidence of successor is weak: `iot_drivers` (box code, `installable: False`) was reorganised (serial drivers renamed, `websocket_client.py`, `connection_manager.py`). I did not find where the `device_controller.js` / network utils went. **No successor found.**
- `iot_box_image` removed (was `installable: False` already in 19), no successor in this repo.

### 3.4 Web client architecture
- **Owl 2.8.4 to Owl 3.0.0-alpha.49** (`addons/web/static/lib/owl/owl.js`, built 2026-07-10; v19: `version = "2.8.4"`). `web/static/src/owl2/owl3_compatibility_layer.js` + `utils.js` bridge Owl 2 code (`t-portal` to `t-custom-portal`, `t-model` to `t-custom-model`, `useEffect` to `useLayoutEffect`) and are loaded in every bundle after owl.js. Core code already uses Owl 3 signals/plugins: `signal`, `computed`, `proxy`, `useProps`, `t.*` prop validators, `Plugin`/`usePlugin`. A migration script exists: `odoo/upgrade_code/owl3-migration.py`.
- **Services to Plugins**: dialog, notification, overlay, popover, ui, hotkey, localization, orm, action, effect, bottom_sheet, title, sortable, currency, frequent emoji, bus parameters, multi-tab and barcode all changed from `*_service.js` to `*_plugin.js`. A `core/services.js` and `legacy_service_starter.js` keep `useService` working for legacy services.
- **jQuery and legacy public widgets removed from web**: `web/static/lib/jquery`, `web/static/src/legacy/**` (public_widget, class.js), `web._assets_jquery` and the qunit lib are gone. `public/public_root*.js`, `lazyloader.js` and `website_form_submit.js` now live in `web/static/src/public/`. `web/static/src/legacy` tests are removed. Hoot is the only test runner. Custom code using `publicWidget`, `$`, or QUnit in a web bundle will break.
- **Icons**: FontAwesome CSS and `fontawesome_overridden.scss` removed from bundles. New bundle `web.icons_fonts` = Material Symbols (outlined/rounded/sharp subsets) + `odoo_ui_icons` + `webclient/icons_mappings/**` (maps old `fa-*` classes). `web/icons.py` (generated, `ICONS` metadata) plus `tooling/icons/generate_icons.py` back an icon picker. `libs/materialsymbols` in static.
- **Offline mode, PWA** (CE): see 3.6.
- New core pieces: `core/session/check_identity` (re-auth dialog), `core/phone/phone_call.js`, `permission_prompt_dialog`, `notification_alert_dialog`, `core/signature/signature_viewer`, `core/crypto.js`, `core/utils/chart_hook.js`, `image_library.js`, `text_truncate_tooltip_plugin`, `webclient/clickbot/clickbot_overlay`, `webclient/share_target/*`, `core/pwa/install_prompt`, `libs/luxon.js`, `search/search_bar_dropdown`, `search/control_panel/embedded_actions.js`, `views/multi_drag.js`.
- **New view type `card`** (`ir.ui.view.type` gets 'card', `odoo/addons/base/models/ir_ui_view.py:164`). `web/static/src/views/card/*` (Card component, arch parser, compiler, renderer, popover). A `<card>` arch can be embedded in kanban via `card_id` attribute (`ir_ui_view.py:1774`). Used already in maintenance, mrp (production), project (project, task, sharing task) and stock picking batch views. It is a reusable card inside kanban, not a stand-alone view mode: no `card` view_mode was found.
- New/renamed field widgets: `badges_selection` and `badges_many2one` (replace `badge_selection`, `badge_selection_with_filter`), `boolean_checkbox`, `float_time_tz`, `many2many_tags_color_dot`, `many2one_binary`, `many2x_binary`, `additional_identifiers`, `relative_date` (replaces `remaining_days`), `translation/` folder (translation_model etc.), `properties_definition_field`, `property_selection`. Removed: `kanban_progress_bar_field`, `list_boolean_toggle_field`. Calendar: `calendar_schedule_section`. Settings widgets `demo_data_service`/`user_invite_service` removed (moved).
- `web/models/ir_attachment.py` adds `web_create_image_variants` (batch image variants).

### 3.5 Spreadsheet
`spreadsheet` bundles o_spreadsheet **20.0.1** (v19: 19.0.51). The Odoo-specific chart classes (`odoo_bar_chart`, `odoo_line_chart`, pie, radar, funnel, geo, sunburst, treemap, ...) were removed and replaced by a datasource-driven design: `odoo_chart_datasource.js`, `odoo_dataset_styles.js`, `odoo_chart_zoomable_component.js`. `spreadsheet_dashboard` gets `spreadsheet.dashboard.favorite.filters` (saved dashboard filters), a dashboard search bar menu, filter list and global-filter widget; `chart_dashboard_menu` is renamed `chart_menu`. `spreadsheet_dashboard_account` now depends on `spreadsheet_account` (new auto_install chain: `spreadsheet_account` auto_install on `['account']`, dashboard_account on `['spreadsheet_account']`). Editing spreadsheets (documents/spreadsheet app) is Enterprise.

### 3.6 Offline mode (answer to coordinator query 1) — EXISTS IN CE
[code] `core/offline/offline_plugin.js` (`OfflinePlugin`), `offline_error.js`, `webclient/offline_systray/`, `search/search_bar/offline_search_bar.js`, `views/offline_action_helper.*`, `service_worker.js`, `/odoo/offline` route (`web/controllers/webmanifest.py:108`). Behaviour:
- Detects connection loss (`ConnectionLostError`), pings the server, and disables UI via a DOM observer: `button:not([data-available-offline])` is disabled.
- Stores "visited" UI items (actions, view types, specific records, searches) in an **encrypted IndexedDB** (`Crypto`, key from `session.browser_cache_secret`; disabled in non-secure contexts via `FakeIndexedDB`). Only visited things are available offline; many2x searches are cached as well.
- Write operations made offline are queued (`scheduleORM`) and replayed on reconnect (`_syncORM`): `web_save` (create and edit), `web_unlink` (delete), and archive/unarchive (generic `method` in record.js and dynamic_list.js). Offline create works in form views and kanban/list quick-create.
- Offline search reruns only on cached many2x/search data (`getAvailableSearches`, `OfflineSearchBar`); it is not a general full-DB search.
- Service worker caches `/odoo` and an offline page; manifest declares `share_target`. Share-target dialog lets files shared from a phone be routed to registered `share_target_items` (e.g. attach to record, mail/Discuss). The web summary's "offline" claim is therefore **supported by CE code**. Whether it is marketed per-app or limited to certain models cannot be told from CE.

### 3.7 AI agents / MCP (answer to coordinator query 2) — NOT IN CE
[code] No `ai*` module exists in `addons/` (642 dirs). No MCP/LLM/OpenAI/Anthropic/Gemini code in addons/odoo (only placeholder text `"Odoo MCP"` for an API key name in `portal_security.xml` and `res_users_views.xml:359`). `base_automation` has no AI action type. Evidence AI exists in the wider product: `odoo/upgrade_code/owl3-migration.py` lists templates `ai.VoiceTranscriptionBlueprint` and `ai_website_livechat.s_ai_livechat_edit`, i.e. an `ai` module that lives outside this repo (Enterprise). IAP credits are the Enterprise/IAP layer (`iap` module in CE only provides the credit client). Conclusion: AI agents, MCP, and agent triggering from automated actions are **Enterprise-only (or IAP service) and unverifiable here**. The supporting CE hooks I did find: `auth='bearer'` routes with `bearer_scope` (`odoo/http/routing_map.py:160-206`, `rpc` module JSON-2 uses `bearer_scope='rpc'`), user API keys, and `api_doc` — usable for external agents but not an MCP server. `odoo20/skills/` ships agent "skills" for developers (odoo-guidelines, odoo-review, odoo-security, odoo-web-guidelines): dev tooling, not a product feature.

### 3.8 Other
- **bus**: `bus_dispatcher.py` and `session_helpers.py` (session-token checks now in a helper; `new_env`, `check_sessions`). Multi-tab/shared-worker/fallback services became plugins.
- **Calendar sync (calendar, google_calendar, microsoft_calendar)**: core `calendar` now has `calendar.calendar` ("User Calendar": events, recurrences, `calendar_default_privacy`, shared users, `is_primary`) and `calendar.user`; `calendar` gets `post_init_hook initialize_primary_calendars`. Google sync is per calendar (`calendar.calendar` inherits `google.sync`; `google.event.sync`; `controllers/google_auth.py`; `enable_primary_calendar_sync`; uninstall hook `remove_unimported_calendars`). Microsoft similar. This lets users have several (and shared) calendars with sync per calendar. Medium-High confidence on the intent; code evidence at `addons/calendar/models/calendar_calendar.py`, `addons/google_calendar/__manifest__.py`.
- **digest**: test-mail wizard model `digest.test`.

## 4. What's new / changed vs Odoo 19 (most impactful first)
1. **Owl 3 (alpha.49) plus compat layer; services become plugins** — `addons/web/static/lib/owl/owl.js`, `web/static/src/owl2/`. High. Biggest custom-JS breakage risk.
2. **ir.access replaces `ir.model.access.csv` (and `security.xml` rules)** in every module: `ir.access.csv` has columns `id,name,model_id,group_id/id,operation,domain` with operations like `cru`, `crud`; model `ir.access` at `odoo/addons/base/models/ir_access.py`, e.g. `addons/web/security/ir.access.csv` merges record rules (domain column) into access lines. High (the web_security.xml rules are gone). Out of my area to explain fully.
3. **Offline mode and PWA share target** in web (3.6). High.
4. **jQuery, legacy public widgets, QUnit and FontAwesome removed** from web bundles; Material Symbols icon system (3.4). High.
5. **Report engine split**: wkhtmltox and Paper Muncher modules, engine-neutral API (3.1). High.
6. **`card` view/arch** in kanban (3.4). High.
7. **Calendar multi-calendar sync** (3.8). Medium.
8. **printer** and **iot_webserial** (3.2, 3.3); iot_base removed. High.
9. **Spreadsheet 20.0.1**, datasource-based charts, dashboard favorite filters (3.5). Medium.
10. New field widgets and renames (badges_selection, relative_date, many2one_binary...). High.
11. web_tour rewrite (plugin, recorder, automatic/interactive split). Medium.
12. `html_editor`/`html_builder` decoupled (builder depends only on html_editor; color picker moved to html_editor). High.
13. JSON-2 `rpc` bearer scope; `odoo.http.router.dispatch_rpc`; `odoo.models.get_public_method` (was `odoo.service.model`). High.
14. `base_address_extended` depends only on web; portal depends on it (street fields in portal address forms). Medium.
15. Dev skills folder `skills/` shipped in the repo. High (informational).

## 5. Removed / merged modules
| Module | Evidence / successor |
|---|---|
| iot_base | Removed; manifest only provided `network_utils`/`device_controller.js` for web; point_of_sale 20 no longer depends on it (19 manifest did). Successor: none found (`iot_drivers` is `installable: False`, `iot_webserial` is different scope). |
| iot_box_image | Was `installable: False` in 19 and is absent in 20; no successor in repo. |
| transifex | Removed; grep of 20 finds no module providing it. No successor found. |
| Wkhtmltopdf code in base | Not a module removal, but moved to `base_report_wkhtmltox`. |

## 6. Implementation notes, risks, migration gotchas
- Custom JS: run `odoo/upgrade_code/owl3-migration.py`; expect `useEffect` semantics, `t-model`, `t-portal` and services-vs-plugin changes. Replace `publicWidget` and jQuery with Interactions or vanilla DOM. QUnit tests must move to Hoot.
- Custom security CSV/XML: convert `ir.model.access.csv` and `ir.rule` to `ir.access.csv` (see `odoo/upgrade_code/19.4-00-ir-access.py` for the earlier hint; the 20.0 script `20.0-00-search-date-filters.py` is only about search date filters).
- Icons: custom templates using `fa fa-*` rely on the `icons_mappings` shim. Check any SCSS using FontAwesome variables; reports (`web.report_assets_common`) include `icons_report.scss`.
- Reports: after upgrade verify `report.pdf_engine_default` and that `base_report_wkhtmltox` is installed (auto_install). Modules calling `get_wkhtmltopdf_state` or `_run_wkhtmltopdf` on core must switch to the engine API. Custom report types `qweb-pdf` keep working.
- Report layout asset files renamed (`layout_assets/layout_*.scss` becomes `report_layouts.scss`); custom layouts inheriting those need review.
- Views: `badge_selection`, `remaining_days`, `boolean_toggle` in list (`list_boolean_toggle_field`) widget names changed; check `widget=` attributes in custom XML.
- Calendar sync: existing Google/Microsoft sync tokens must be re-checked after the `calendar.calendar` migration (primary-calendar hooks run at install/upgrade, not guaranteed for existing DBs).
- IoT: deployments using iot_base or building boxes from `iot_box_image` need to rely on Odoo's separate IoT image repo ([unverified]).
- Offline mode stores encrypted data in the browser IndexedDB; plan security reviews (key is `session.browser_cache_secret`).
- Third-party modules depending on `base_address_extended` and `contacts` implicitly lose `contacts` dependency; add it explicitly.

## 7. Open questions / not verifiable from CE
- AI agents, MCP, IAP credit consumption, AI in automated actions: Enterprise or SaaS-only; no CE code.
- Exact packaging of offline mode (all apps vs specific) and whether it is flagged per feature in Enterprise.
- Where iot_base functionality went; whether Odoo 20 IoT box moved to another repository.
- Whether Paper Muncher will become default in 20 (CE keeps wkhtmltopdf default).
- html_field_history: no module with that name in 19 or 20 CE; assumed Enterprise.
- Detailed html_builder snippet/option changes (351 file diffs) were not individually reviewed.
- Web research ([web] cross-check) was not performed.
