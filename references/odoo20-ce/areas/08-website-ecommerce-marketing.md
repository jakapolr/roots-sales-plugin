# Website, eCommerce, Events, eLearning, Surveys & Marketing — Odoo 20 CE

Method: diff of `/home/user/odoo-src/odoo19/addons/X` vs `odoo20/addons/X` (manifests, `models/*.py`, controllers, file lists). Paths are relative to `odoo20/` unless prefixed `odoo19/`. [code] = verified in source; [web] = not used (no web cross-check was done; everything below is code-derived). Confidence tags: High/Medium/Low.

## 1. Scope

About 80 modules in `addons/` (website*, event*, survey*, mass_mailing*, marketing_card*, html_builder, *slides*), of which 5 are NEW (`marketing_card_event`, `website_address_autocomplete`, `website_mass_mailing_event`, `website_partnership`, `website_sale_project`) and 7 are REMOVED (the website_sale wishlist/comparison/autocomplete/mondialrelay family). Related new module outside the list: `mail_tracking_mass_mailing` (depends `mail_tracking`, `mass_mailing`). Also touched: `html_builder`, `portal` (new `portal.entry`), `partnership` (exists in both 19 and 20).

Big cross-cutting facts about the 19->20 delta in this area:
1. Security files were converted from `security/ir.model.access.csv` + `ir_rules.xml` to a single `security/ir.access.csv` (columns `id,name,model_id,group_id/id,operation,domain`) or `ir_access.xml` — in practically every module here (e.g. `event/security/ir.access.csv`, `website_sale/security/ir_access.xml`). `base` loads `security/ir.access.csv` (`odoo/addons/base/__manifest__.py:81`). [code] High.
2. Manifests drop `'installable': True` and the `# -*- coding` header (cosmetic).
3. Many "tracking / visitor" links were refactored onto new mixins in `website` (`website.trackable.mixin`, `website.structured_data.mixin`, `website.located.mixin`).
4. Digest KPIs added to `event`, `survey`, `website_slides` (`models/digest.py`, `data/digest_data.xml`, `views/digest_views.xml`; manifests now depend on `digest`).
5. Customer-portal home tiles are now data records of `portal.entry` (`portal/models/portal_entry.py`), used by `event`, `website_slides`, `mass_mailing`, `website_crm_partner_assign`, `sale`, `project`, etc.

## 2. Module catalogue

Legend: Status = New / Changed (substantial) / Minor (small diff, mostly ACL/manifest/assets) / Removed. "Lines" = rough size of non-i18n diff (+/- lines).

| Module | App? | Summary (manifest) | What it does | Status vs 19 |
|---|---|---|---|---|
| website | App | Website builder | Pages, menus, themes, snippets, SEO, forms, visitors, multi-website | Changed (~54k diff lines): 48 new snippets, LLMs.txt, header search, cookie-policy page, structured-data mixins |
| html_builder | – | Generic html builder | OWL builder framework used by website and mass_mailing | Changed (~21k): deps trimmed to `html_editor`; new `ir.qweb`/`ir.ui.view` models (`t-snippet` directives, save/rename/delete snippet), new building blocks (list dialog, search select, sliding panel), many new image shapes |
| website_sale | App (eCommerce) | Sell products online | Shop, product pages, cart, checkout, pricing, SEO, GMC feed | Changed heavily (~25k): absorbed wishlist, comparison, back-in-stock, donation, availability, withdrawal request |
| website_sale_stock | – | Product availability | Stock levels/pickup-warehouse on the shop | Changed (~2k): availability fields moved to website_sale; now hosts pickup-location support/location selector |
| website_sale_collect | – | Click & Collect | In-store pickup | Changed (~3k): pickup data stored on shipping partner; new `payment_method`, `sale_order_line` models; backend pickup-location many2one |
| website_sale_loyalty | – | Coupons/loyalty on eCommerce | Promo/gift-card in cart | Changed (~3k): payment controller removed; new cart-notification and promotion-progress-bar components |
| website_sale_gelato | – | Gelato print-on-demand | Gelato fulfilment | Minor+: new `res.partner` extension & views |
| website_sale_mrp | – | Kit availability | Kit inventory on shop | Minor (interactions refactor) |
| website_sale_slides | – | Sell courses online | Course products | Minor |
| website_sale_mass_mailing | – | Newsletter at checkout | Opt-in | Minor |
| website_sale_project | – (auto) | Bridge website_sale <-> project | Withdrawal-request form can create a project task | NEW |
| website_address_autocomplete | – (auto) | Address autocomplete (Google Places) | Autocomplete in website address forms, per-website API key | NEW (replaces website_sale_autocomplete) |
| website_payment | – | Payment integration with website | Payment pages | Changed: donation snippet/models moved out to website_sale |
| website_blog | – | Blog | Blog posts | Changed (~5.7k): blog carousel snippet, "recommended next post", visitor tracking, `post_date`/`published_date` fields removed |
| website_forum | – | Forum / Q&A | Karma-based forum | Changed (~3.3k): comments are now a dedicated `forum.post.comment` model; `forum.post` is `mail.thread`; follow templates |
| website_slides | App (eLearning) | eLearning platform | Courses, slides, quizzes, certifications | Changed (~5.4k): owl "interactions" rewrite, visitor/track tracking, digest KPIs, completion_date, portal entry |
| website_slides_survey / _forum | – | Certifications / course forum | | Minor |
| website_event | App (Events) | Publish events, sell tickets | Event website | Changed (~1.7k): scheduled publishing, events carousel snippet, visitor tracking, search bar snippet removed |
| website_event_track | – | Tracks/agenda | | Changed (~0.8k): location display screens |
| website_event_exhibitor | – | Sponsors/exhibitors | | Minor+ |
| website_event_sale / _booth / _booth_sale / _booth_exhibitor / _booth_sale_exhibitor / _crm / _track_live / _track_quiz / _track_live_quiz | – | Event bridges | | Minor |
| event | App | Events | Events, tickets, registrations, slots, mail scheduler | Changed (~0.9k): multi-entry tickets, digest, portal "My events" |
| event_sale / event_product / event_booth / event_booth_sale / event_crm / event_crm_sale / event_sms | – | Event bridges | | Changed: event_product gets "additional products" on tickets and total-price fields; others minor |
| survey | App | Surveys & certifications | | Changed (~5.4k): new certificate templates, scheduled invitations, digest, leaderboard up to 250 |
| survey_crm | – | Leads from surveys | | Unchanged-ish (not examined in depth) |
| mass_mailing | App (Email Marketing) | Design, send, track emails | | Changed (~6.5k): templates = `is_template` mailings, multi-filter, new builder, list merge wizard removed |
| mass_mailing_sms | App | SMS marketing | | Changed (~0.5k): UTM refactor, `iap_paid_service` flag |
| mass_mailing_themes | – | Email themes | | Changed (~1.4k, images/theme assets) |
| mass_mailing_crm / _sale / _slides / _event / _event_track (+ _sms variants) | – | UTM/bridge | | Minor (demo removed in mass_mailing_crm) |
| website_mass_mailing | – | Newsletter subscription snippets | | Minor (`res.company` model extension removed) |
| website_mass_mailing_sms | – | | | Minor |
| website_mass_mailing_event | – (auto) | Event snapshot snippet for emails | | NEW |
| marketing_card | App | Dynamic shareable cards | | Changed (~0.8k): LinkedIn sharing, frontend interactions, wkhtmltox dependency |
| marketing_card_event | – (auto) | Cards for events | | NEW |
| website_crm / _iap_reveal / _livechat / _sms | – | Lead gen | | Minor |
| website_crm_partner_assign | – | Resellers & lead forwarding | | Changed (~1k): publishing of grades moved to website_partnership; uses `portal.entry` |
| website_partnership | – (not auto) | Publish partners | | NEW |
| website_partner / website_customer | – | Partner & reference pages | | Minor (customer: `ir_rule.xml` removed; partner uses structured-data mixin) |
| website_livechat | – | Livechat on website | | Changed (~2k): `discuss.channel.member` extension, `current_livechat_agent_ids`, frontend moved `core/` |
| website_hr_recruitment | App | Jobs page | | Changed (~2.3k): job snippet filter + snippet templates; searchbar plugins removed in favor of header search |
| website_links / website_google_map / website_mail / website_mail_group / website_profile / website_project / website_cf_turnstile / website_sms / website_timesheet | – | Utilities | | Minor (website_google_map: maps service moved into `website/static/src/services/google_maps_service.js`) |
| hr_skills_slides, spreadsheet_dashboard_website_sale_slides, test_website_slides_full | – | | | Minor |
| website_sale_wishlist, website_sale_comparison, website_sale_comparison_wishlist, website_sale_stock_wishlist, website_sale_collect_wishlist, website_sale_autocomplete, website_sale_mondialrelay | – | | | REMOVED (see section 5) |

## 3. Feature deep-dive

### 3.1 Website (`website`, `html_builder`)
- Builder: `html_builder` now depends only on `html_editor` (`html_builder/__manifest__.py`). It owns `ir.qweb` directive `t-snippet` / `t-snippet-call` with new attributes `t-image-preview`, `t-drag-image-preview`, `t-forbid-sanitize`, `t-grid-column-span` (`html_builder/models/ir_qweb.py`) and `ir.ui.view` snippet save/rename/delete (`html_builder/models/ir_ui_view.py`). New reusable controls: list dialog, search-select, sliding panel, number-input base, options-section.
- Design library: 48 new section snippets in `website/views/snippets/` (bento features/grid, banner glow/contained, hero about/maintenance/minimalist, launch countdown, whatsapp, age-verification popup, animated cover/number, awards/achievements lists, projects grid/list, services grid/pack, references lite/tiles, text/chart blocks, avatars, icon, manifesto, etc.), plus large new libraries of image shapes (Blurry, Geometric, Lines, Nature, Travel, Miscellaneous, devices). `s_btn` removed. New `views/theme_colors_preview.xml`.
- SEO: `website.structured_data.mixin` (JSON-LD generation, `_prepare_jsonld_vals`, `_render_jsonld`, Breadcrumb) implemented by `website`, products, blog, forum, event, exhibitor sponsors, courses/slides, partners, jobs (`website/models/mixins.py`; users in `website_sale/models/product_template.py`, `website_blog/models/website_blog.py`, `website_forum`, `website_event/models/event_event.py`, `website_slides`, `website_partner`, `website_hr_recruitment/models/hr_job.py`). `website.located.mixin` standardizes `website_url`/`website_absolute_url`. New `LLMs.txt` editor: `website.llms_txt` + wizard `website.llms` (`website/wizard/website_llms.py`, settings action `action_open_llms`), complementing the existing robots.txt wizard. `website.cookie_policy_id` (Cookie Policy page) in settings; Google Analytics setting renamed "Google Tag Manager/Google Analytics".
- Header search: new website-level settings `header_search_type`, `header_search_order_by`, `header_search_limit` (`website/models/website.py`); the per-app searchbar snippets (`s_searchbar` in website_event, searchbar options in website_slides and website_hr_recruitment) are removed (files absent in v20) — apps now plug into the header search. Medium confidence on exact UX.
- `website.trackable.mixin` + `website.track` extension in blog/slides/event replace ad-hoc visitor link tables (new `visitor_*_count` fields).
- Settings: `module_website_address_autocomplete` (checkbox installing the new module).

### 3.2 eCommerce (`website_sale` and satellites)
Key models (v20): `product.wishlist`, `product.stock.notification`, `product.attribute.category`, `withdrawal.request`, `website.checkout.alert.mixin` plus existing `product.ribbon`, `product.public.category`, `website.checkout.step`, `website.sale.extra.field`, `product.feed`.
- Wishlist (`website_sale/models/product_wishlist.py`, `controllers/wishlist.py`, `templates/wishlist_templates.xml`): per partner/session, stores price/pricelist when added, `website` fields `wishlist_grid_columns`, `wishlist_mobile_columns`, `wishlist_gap`, design classes — editable via builder option `wishlist_page_option.xml`. No separate install anymore.
- Comparison (`controllers/comparison.py`, `templates/comparison_templates.xml`, `product.attribute.category` for grouping rows, `static/src/interactions/comparison_*.js`). Settings flags in `website_sale/views/res_config_settings_views.xml`. Note `group_product_price_comparison` (strikethrough price) is a different feature.
- Back-in-stock: `product.stock.notification` (product, partner, website, unique) replaces the `stock_notification_partner_ids` m2m of v19 website_sale_stock; cron "Product: send email regarding products availability" (`website_sale/data/ir_cron_data.xml`).
- Availability: `allow_out_of_stock_order`, `available_threshold`, `show_availability`, `out_of_stock_message`, and settings `default_*`, `group_unpublish_out_of_stock` now live in website_sale (`models/product_template.py:190-192`), acting on `is_storable`. website_sale_stock (auto-install) now focuses on warehouse/pickup: `support_pickup_locations`, `is_pickup_required`, `pickup_delivery_method_id`, `location_selector.py`. Medium-High.
- Hide add-to-cart: v19 `prevent_zero_price_sale` -> v20 `prevent_sale` + `prevent_sale_for` (zero price / specific categories) + `prevent_sale_for_categories` (`models/website.py:248-261`). `contact_us_button_url` renamed `contact_us_link_url`.
- Suggested products: new automation — `suggest_accessory/alternative/optional_products`, `suggested_products_last_update`, cron "eCommerce: Update suggested products", setting `group_automate_suggested_products`.
- Delivery estimate: `delivery.carrier` gets `enable_delivery_estimate`, `delivery_estimate_lead_days`, `delivery_estimate_range_days`, `delivery_calendar_id`; shown in checkout address/delivery step (`templates/checkout/address_templates.xml:73`).
- Order rating e-mails: website setting `send_order_rating_emails`, `rating_email_delay` (default 5 days), template, cron `ir_cron_send_order_rating_emails`. Abandoned cart renamed `send_abandoned_cart_followup`.
- Units: website base-unit model/fields (`website.base.unit`, `base_unit_*`, `group_show_uom_price`) removed from website_sale; base-unit price now from `product` (`product/models/product_product.py:177`, `_get_base_unit_price`); new setting `show_product_reference_price`/`website_show_reference_price`, `restricted_uom_ids` (UoMs hidden on the shop).
- Pricelist `tax_display` (tax-included/excluded per pricelist), `min quantity`, ribbons data (`data/product_ribbon_data.xml`), checkout steps data, snippet filters data.
- Donation: donation snippet, controller `controllers/donation.py`, `is_donation` on sale.order/line, product/payment — moved from website_payment into website_sale (`website_sale/templates/snippets/s_donation.xml`, `data/donation_data.xml`; website_payment loses `account_payment.py`, `payment_transaction.py`, `s_donation`). High.
- Withdrawal request (EU "right of withdrawal"): public form -> `withdrawal.request` model (email + order reference check, logs message on order chatter, confirmation e-mail to customer, internal notification, `website_sale/models/withdrawal_request.py`); `website_sale_project` adds `project_id`/`task_id` so each request can open a project task.
- Pickup (Click & Collect): pickup location data stored on shipping partner (`partner_shipping_id.pickup_location_data`) instead of the order; new `payment.method` link and payment-provider view; backend many2one for pickup location (`website_sale_collect/models/sale_order.py`).
- Portal: `controllers/portal.py` in website_sale (new).

### 3.3 Events (`event`, `website_event*`)
- Multi-entry tickets: `event.event.ticket.entry_limit` ("0/1 = disabled, >=2 = max entries"), `event.registration.remaining_entries`, `main_registration_id`; scanning a badge in the barcode app (`event/static/src/client_action/*`) creates sub-registrations marked done until the limit is hit (`event/models/event_registration.py:82-84,191-203,329-335`). High.
- Terminology: "Limited Seats / Limit Attendees" -> "Limit Registrations"; `address_inline` -> `contact_address_inline`.
- Digest KPI "Registrations"; portal page `/my/events` (`event/controllers/portal.py`, `portal_entry_data.xml`) and `website_event/views/portal_templates.xml`.
- Slots: slot calendar view replaced by `views/event_slot` (list).
- Scheduled publication: `website_event` adds `is_published`, `publish_on` (tracked) with subtypes event scheduled/unscheduled/published/unpublished (`website_event/models/event_event.py:60-62,478-488`). Medium (cron not verified).
- New "Events carousel" dynamic snippet (`s_events_carousel`), event-visitor tracking via `website.track.event_id`.
- Tickets can carry "additional products" (`event_product`), and registration lines compute total prices (`total_price`, `total_price_incl`); `price_incl` removed — report/pricing customizations should be checked.
- Location display (website_event_track): per-location screen `/event/<id>/location-display/<loc>` with background image and upcoming-track count (`website_event_track/controllers/location_display.py`) — digital signage for rooms.
- `marketing_card_event`: "Send Cards" action on event (`action_open_card_mailing`) builds a mailing to registrations pre-filtered to the event; card campaigns for `event.*` models redirect to `event_share_url`. `website_mass_mailing_event`: event snapshot snippet in mailing builder.

### 3.4 eLearning (`website_slides*`)
- Front end rewritten as Odoo "interactions" (`static/src/interactions/slides_course_*.js`), components for join popup / quiz question form; `slide_icon_class` now emits Material-style names (`help_outline`, `picture_as_pdf`), field label "oi-class".
- `completion_date` on channel partner; `date_published` removed from `slide.slide`; digest KPIs (new attendees, certified attendees); visitor course tracking (`website_track.py`, `website_visitor.py`); latest-courses dynamic snippet filter (`data/website_snippet_filter_data.xml`); portal entry "courses".

### 3.5 Surveys (`survey`)
- Certification templates replaced: v19 modern/classic x purple/blue/gold -> v20 `modern`, `minimal`, `classic-1`, `classic-2` each in company-colour or black (`survey/models/survey_survey.py`). Default changes from `modern_purple` to `modern_company`. Old images deleted.
- Invitation wizard gets `scheduled_date` (send later, must be <= deadline) (`survey/wizard/survey_invite.py:64`).
- Live sessions: leaderboard capped at 250 (`SURVEY_LEADERBOARD_MAX_PARTICIPANTS`), `session_question_can_answer`, `min_current_score`; matrix/scale labels (`scale_mid_label` removed, min/max placeholders added); `has_image_only_suggested_answer` removed; title copy now `mark_as_copy` (the " (copy)" suffix override removed).
- Digest KPIs: participants, certified participants.

### 3.6 Marketing (`mass_mailing`, `mass_mailing_sms`, `marketing_card`)
- Mailing templates: instead of "favorite" mailings (`favorite`, `favorite_date` removed), a mailing can be flagged `is_template` (`mass_mailing/models/mailing.py:87,244,805`); "Save as template" cog-menu (`mass_mailing_save_as_template_cog_menu`), `action_fetch_templates`, `action_new_mailing_from_template`. Templates need no `email_from`.
- Filters: `mailing_filter_id` -> `mailing_filter_ids` (many2many; OR-combination of saved filter domains), `mailing.filter` dialog component.
- Lists: `mailing.list.merge` wizard removed (server action "Merge" now calls `records.action_mailing_lists_merge()`, `mass_mailing/data/ir_actions_server_data.xml`; verify it still works in your flow). Contact-to-list wizard now also in `mass_mailing_sms`.
- New fields: A/B `ab_testing_version_name`, ratios (opened, clicked, replied, received, cancelled), last opened/clicked/replied timestamps, `color`, `preview_text`, `preview_record_ref`.
- Builder: new mass-mailing builder under `mass_mailing.assets_builder` (record snapshot option, bento blocks, social-media links, signature, view-in-browser, add-snippet dialog); old per-category snippet files (`mass_mailing_*_snippets.xml`) removed in favor of `themes_templates_blocks.xml`; mass_mailing_themes get new themes (e.g. `theme_cta_centric`) and new imagery.
- `mass_mailing` `res.partner` views; portal entry; `mail_tracking_mass_mailing` (new, with `mail_tracking`) records message source = mailing.
- SMS: `iap_paid_service`, UTM split into `utm_campaign.py`/`utm_mixin.py`, `res_partner.py`.
- Marketing Card: LinkedIn sharing via OAuth/IAP (`controllers/marketing_card_linkedin.py`, `utils/linkedin_api.py`, fallback to share-offsite URL with `post_suggestion`), card frontend interactions, requires `base_report_wkhtmltox` (renders image with wkhtmltoimage; `models/card_campaign.py:414`).

### 3.7 Partners, leads, other website apps
- `website_partnership` (new, depends `partnership`, `website_partner`): `res.partner.grade` becomes `website.published.mixin` here, with `/partners` pages, "Level" publishing, builder options and demo data; `website_crm_partner_assign` now depends on it (`website_crm_partner_assign/__manifest__.py:16`) and no longer makes the grade published itself.
- `website_livechat`: `discuss.channel.member.current_livechat_agent_ids`; `livechat_operator_id` removed from channel in website_livechat (core moved in im_livechat).
- `website_hr_recruitment`: job snippet filter/snippets, `website.published.multi.mixin` override to open job URL in the right company's website.
- `website_forum`: dedicated `forum.post.comment` (body, post, karma checks for create/edit/delete, convert to answer) replacing mail.message-based comments; forum follow templates; `forum.post.create_date` index; migration of existing comments needed.

## 4. What's new / changed vs Odoo 19 (most impactful first)
1. Wishlist, comparison, back-in-stock, donation, withdrawal-request and availability logic folded into `website_sale` (module consolidation). [code] `website_sale/models/product_wishlist.py`, `product_stock_notification.py`, `controllers/{wishlist,comparison,donation}.py`. High.
2. Security re-platformed to `ir.access.csv`/`ir_access.xml`; `ir_rules.xml` and `ir.model.access.csv` removed across modules. [code] `event/security/ir.access.csv`, `website_sale/security/ir_access.xml`. High.
3. 48 new website snippets, new shapes, new html_builder components, `t-snippet` directives; zoomodoo lib and legacy `website_root.js`/`snippets.animation.js`/`xml/website*.xml` removed from frontend assets (`website/__manifest__.py`). [code] High.
4. SEO/AI: JSON-LD structured-data mixin across apps, `llms.txt` editor, header-search settings, cookie policy page. [code] `website/models/mixins.py`, `website/wizard/website_llms.py`. High.
5. Mass mailing: templates via `is_template`, multi-filter, A/B version name, new builder, list merge wizard dropped. [code] `mass_mailing/models/mailing.py`. High.
6. Events: multi-entry tickets, scheduled website publication, additional ticket products, digest KPIs, portal "My events", location display screens, slot UI changes. [code] High (publish cron Medium).
7. Surveys: new certificate designs, scheduled invites, bigger leaderboard, digest. High.
8. New modules: marketing_card_event, website_mass_mailing_event, website_partnership, website_sale_project, website_address_autocomplete. High.
9. Marketing Card LinkedIn sharing + wkhtmltox dependency. Medium-High.
10. eLearning/blog/event front-ends migrated to `interactions`; visitor tracking via `website.trackable.mixin`. Medium.
11. Click & Collect storage move (pickup data on partner), delivery estimate dates, suggested-products automation, prevent_sale by category, order rating emails. High.
12. Portal home tiles via `portal.entry` data. High.

## 5. Removed / merged modules

| v19 module | Verdict | Evidence |
|---|---|---|
| website_sale_wishlist | Merged into `website_sale` | Model `product.wishlist` (`website_sale/models/product_wishlist.py`), controller `wishlist.py`, templates `wishlist_templates.xml`, wishlist settings on `website` (`models/website.py:219-245`). v19 module had `product_wishlist.py`, `res_users.py`, `website.py`. |
| website_sale_comparison | Merged into `website_sale` | `controllers/comparison.py`, `templates/comparison_templates.xml`, `models/product_attribute_category.py` (name `product.attribute.category`, `attribute_ids` o2m), `product_attribute.py` has `category_id`. |
| website_sale_comparison_wishlist | Merged (bridge no longer needed) | both features now in website_sale. |
| website_sale_stock_wishlist | Merged | `product.stock.notification` in website_sale; `website_sale/models/product_product.py:455,511`. |
| website_sale_collect_wishlist | Merged / no bridge | wishlist in website_sale; the template `delivery_form_templates.xml` of the bridge not found as a separate module. Medium. |
| website_sale_autocomplete | Replaced by `website_address_autocomplete` | New module depends on `website` + `google_address_autocomplete`; per-website `google_places_api_key`; checkout address template carries `o_address_autocomplete` (`website_sale/templates/checkout/address_templates.xml:254`). Setting renamed `module_website_sale_autocomplete` -> `module_website_address_autocomplete`. Config key moved: re-enter the key per website. High. |
| website_sale_mondialrelay | Removed; no successor found (and `delivery_mondialrelay` also removed, see `removed_in_20.txt`). No "mondial" matches in v20 addons XML/Python. High. |

Also (not whole modules): website_payment donation pieces -> website_sale; `website.base.unit` -> core `product`; `mailing.list.merge` wizard -> server action only.

## 6. Implementation notes, risks & migration gotchas (19 -> 20)
- Custom modules that depend on `website_sale_wishlist`, `website_sale_comparison`, `website_sale_stock_wishlist`, `website_sale_collect_wishlist`, `website_sale_autocomplete`, `website_sale_mondialrelay` will fail to install: remove from `depends` (website_sale if suffices), repoint XML-ids (`website_sale_wishlist.*` -> `website_sale.*`) and view inheritance. DB migration must remap `ir_model_data` module names; `product_wishlist` table and attribute category table rows should carry over (same model names) — verify in upgrade scripts (none are in CE source).
- `website_sale_stock` fields moved (`allow_out_of_stock_order`, `available_threshold`, `show_availability`, `out_of_stock_message`) — data stays in the same columns only if the migration maps module ownership; check `product_template` values and `stock_notification_partner_ids` m2m -> `product_stock_notification_rel` (same table name was kept via `_table`, so data likely preserved; Medium).
- Renamed/removed: `prevent_zero_price_sale` -> `prevent_sale`(+`_for`), `contact_us_button_url` -> `contact_us_link_url`, `send_abandoned_cart_email` -> `send_abandoned_cart_followup`, `address_inline` -> `contact_address_inline` (event), `scale_mid_label`, `has_image_only_suggested_answer`, `date_published` (slides), `post_date`/`published_date` (blog), `mailing_filter_id`, `favorite`, `price_incl` (event_product). Update reports, server actions, automations and custom views.
- Mailing: saved "favorite" mailings are not templates; plan a data step to set `is_template` if users relied on favorites. Custom mail-themes/snippets targeting `mass_mailing_*_snippets` XML templates must be ported to the new builder (`mass_mailing.assets_builder`).
- Website customizations: legacy JS (zoomodoo, snippets.animation, `website_root.js`, `xml/website.xml`) and `s_searchbar` snippets are gone; custom themes/snippets using them break. Custom ACLs: convert to `ir.access.csv` format (rules become the `domain` column).
- Forum: comments moved to `forum.post.comment`; verify migration of former mail.message comments and any reporting.
- Survey certificate: selection values changed; old templates and background SVGs deleted - existing surveys with `modern_purple`, etc. need mapping.
- Marketing Card requires wkhtmltoimage engine module (`base_report_wkhtmltox`, new in 20) and, for LinkedIn posting, IAP credit; check hosting.
- Address autocomplete: API key now a website field; Google Places billing; GDPR/cookies.
- Withdrawal requests: public form creating records that email customers — rate-limit/spam (turnstile) review.
- UI regression testing: tours/selectors change widely (website_slides, blog, events). Re-test eCommerce checkout (checkout templates split into `templates/checkout/*`).

## 7. Open questions / not verifiable from CE code
- Enterprise-only features (not in this repo): website builder Enterprise extras (`website_sale_*` subscriptions, appointment, `website_generator`, studio, Odoo.sh features), Marketing Automation, Social Marketing, SMS provider IAP details. Marketing Card LinkedIn needs IAP (service side unknown).
- Data migration behaviour (upgrade scripts are not in CE).
- Exact header-search UX and which apps register scopes; whether `website_event` scheduled publish has a cron (not verified).
- Fate of `website_sale_collect_wishlist` template (bridge UX) — "out of stock at pickup -> add to wishlist" appears not preserved as a module; Low confidence.
- `survey_crm`, `website_links`, `website_google_map`, `website_cf_turnstile` showed only small diffs and were not read in depth.
- No [web] cross-check against odoo.com release notes was performed.
