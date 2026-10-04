# Point of Sale, Restaurant & Self-Order — Odoo 20 CE

Evidence base: Odoo 20.0 CE (HEAD b100a87, "[FIX] point_of_sale: protect offline data from browser eviction") diffed against 19.0. Paths are relative to `odoo20/` unless stated. Claims are code-verified [code] unless labelled [web]. No web research was done for this file. Confidence tags: High / Medium / Low.

## 1. Scope

Directory `addons/` modules matching `point_of_sale` and `pos_*`: **46 modules in v20** (1 core + 45 `pos_*`), versus 43 in v19.
- New in 20: `pos_stock`, `pos_sale_stock`, `pos_sale_delivery`, `pos_partner_autocomplete`, `pos_bancontact_pay`, `pos_self_order_bancontact_pay`, `pos_self_order_event`, `pos_self_order_sms` (8).
- Removed in 20: `pos_restaurant_adyen`, `pos_restaurant_stripe`, `pos_self_order_adyen`, `pos_self_order_stripe`, `pos_self_order_viva_com` (5).
- Related and out of this file's depth: `iot_webserial` (new), `iot_base` and `iot_box_image` (removed; `iot_drivers` stays); the 20+ `l10n_*_pos*` modules (see 2.5, covered by another agent).
- `pos_epson_printer` and `pos_iot` do not exist in v19 CE or v20 CE (see 5).

## 2. Module catalogue

### 2.1 Core and business-flow modules

| Module | App? | Summary | What it does | Status vs 19 |
|---|---|---|---|---|
| `point_of_sale` | Yes | Checkouts and payments for shops and restaurants | Core POS: configs, sessions, orders, payments, presets, printers, receipts, session accounting, offline-capable OWL frontend | Changed heavily (616 files differ). No longer depends on stock |
| `pos_stock` | No (auto_install) | Stock integration for PoS | Pickings, lots/serials, warehouse and picking type per config, ship later, stock valuation/COGS | New (carved out of `point_of_sale`) |
| `pos_restaurant` | Yes | Restaurant extensions | Floors/tables, floor-plan editor, courses, order transfer/merge, table-linked orders | Changed (new `pos.course`, JSON floor plan) |
| `pos_self_order` | No (auto_install with pos_restaurant) | Mobile menu and kiosk | QR/mobile ordering and kiosk, delivery preset, optional products, snoozing | Changed |
| `pos_loyalty` | No (auto_install) | Coupons, gift cards, loyalty in POS | Loyalty engine in POS, reward application, receipts | Changed (receipt/plugin refactor; field removals) |
| `pos_discount` | No | Simple global discount | Discount button/product | Changed (report and receipt additions) |
| `pos_hr` | No (auto_install) | POS and HR link | Employee login/PIN, cashier roles per config | Changed (role model renamed) |
| `pos_sale` | No (auto_install) | POS and Sales link | Settle/down-payment on quotes in POS | Changed (default product, `pos_order_line`, receipts) |
| `pos_sale_stock` | No (auto_install) | Link `pos_stock` and `pos_sale` | Updates SO-linked pickings and demand quantities on sync | New (carved out of `pos_sale`) |
| `pos_sale_delivery` | No (auto_install, Hidden) | Link `pos_sale` and `stock_delivery` | Cancels pending pay-on-delivery transactions when a SO is settled in POS | New |
| `pos_sale_loyalty` / `pos_sale_margin` | No | Glue modules | Loyalty on SO lines; margin on POS orders | Unchanged-ish |
| `pos_restaurant_loyalty` / `pos_hr_restaurant` | No | Glue modules | Restaurant plus loyalty; HR plus restaurant | Unchanged-ish |
| `pos_mrp` | No | POS and MRP | Kits/BoM in POS orders | Changed: now depends on `pos_stock` and `mrp` |
| `pos_repair` | No | POS and Repair | Repair link | Changed: now depends on `pos_stock` and `repair` |
| `pos_event`, `pos_event_sale` | No | POS and Events | Sell event tickets in POS | Changed (new `uuid`, `pos_price_total`; print popup) |
| `pos_sms` | No | SMS receipt | Send SMS order confirmation | Changed (send-receipt popup) |
| `pos_edi_ubl` | No | UBL in POS | UBL for POS invoices | Unchanged-ish |
| `pos_account_tax_python` | No (auto_install) | Python tax link | Links POS and Python-code taxes | Unchanged-ish |
| `pos_online_payment` (+ `_self_order`) | No (auto_install) | Online payment via payment providers | Customer pays by link/QR from phone; kiosk/self-order support | Changed (see 3.7) |
| `pos_partner_autocomplete` | No (auto_install) | POS and Partner Autocomplete | Loads `partner_autocomplete` assets into the POS bundle | New |

### 2.2 Payment terminals, QR and cash machines

| Module | Type | Status |
|---|---|---|
| `pos_adyen` | Terminal. Now also covers tipping and kiosk (see 5) | Changed. It no longer depends only on `point_of_sale`: it adds `payment_adyen` |
| `pos_stripe` | Terminal. Tipping and kiosk actions folded in | Changed |
| `pos_viva_com` | Terminal. Kiosk actions folded in | Changed |
| `pos_razorpay`, `pos_mollie`, `pos_mercado_pago`, `pos_pine_labs`, `pos_qfpay`, `pos_dpopay`, `pos_safaricom` | Terminal | Unchanged-ish (small diffs) |
| `pos_bancontact_pay` | External QR ("Quick Pay"), Bancontact Pay and Wero (Payconiq) | New |
| `pos_cashdro`, `pos_cashmatic`, `pos_glory_cash` | Cash machine | Unchanged-ish |
| `pos_imin` | iMin ePOS printers | Unchanged-ish |
| `pos_self_order_razorpay`, `_pine_labs`, `_qfpay` | Kiosk payment glue | Unchanged-ish. These still exist as modules, unlike the Adyen/Stripe/Viva ones |
| `pos_self_order_bancontact_pay` | Kiosk payment glue | New |
| `pos_self_order_sale`, `pos_self_order_event`, `pos_self_order_sms` | Self-order glue | `_event` and `_sms` new, `_sale` unchanged |

### 2.3 Hardware and IoT
- `pos_epson_printer` and `pos_iot` are not in the repo for either version. ePoS printing is in core `point_of_sale` (`models/pos_printer.py`). IoT-box terminals (`pos_iot_worldline`, `pos_iot_six`) are only referenced as install cards (`models/pos_payment_method.py:113-120`) and are not in CE.

### 2.4 Provider "app store" cards
`pos.payment.method.get_payment_providers()` lists 18 provider cards (terminal, `external_qr`, `cash_machine`). Some modules referenced are not in CE: `pos_iot_worldline`, `pos_iot_six`, `pos_tyro`.

### 2.5 Localization POS modules (other agent covers them)
New: `l10n_be_pos`, `l10n_eg_edi_pos`, `l10n_id_pos_self_order_qris`, `l10n_pk_edi_pos`. Removed: `l10n_uy_pos`. Existing: `l10n_ae_pos`, `l10n_ar_pos`, `l10n_be_pos_restaurant`, `l10n_be_pos_sale`, `l10n_ch_pos`, `l10n_co_pos`, `l10n_es_*_pos`, `l10n_fr_pos_cert`, `l10n_fr_pdp_pos`, `l10n_gcc_pos`, `l10n_id_pos`, `l10n_in_pos`, `l10n_jo_edi_pos`, `l10n_mt_pos`, `l10n_my_edi_pos`, `l10n_pe_pos`, `l10n_sa_*_pos`, `l10n_tw_edi_ecpay_pos`, `l10n_vn_edi_viettel_pos`, `l10n_account_withholding_tax_pos`, `l10n_test_pos_qr_payment`.

## 3. Feature deep-dive

### 3.1 `pos_stock`: what moved out of `point_of_sale` (answer: POS no longer hard-depends on stock)
- v19 `point_of_sale` depended on `stock_account`. v20 depends on `resource, product, account, barcodes_gs1_nomenclature, html_editor, digest, phone_validation, google_address_autocomplete, base_report_wkhtmltox, iot_webserial` (`addons/point_of_sale/__manifest__.py`). Hence POS can run without Inventory [code, High].
- `pos_stock` (`depends: point_of_sale, stock_account`, `auto_install: True`) therefore installs automatically whenever Inventory and Accounting valuation are present. The upgrade of an existing DB with stock should simply pull in `pos_stock`.
- Models and fields moved to `addons/pos_stock/models/`:
  - `pos.pack.operation.lot` (lot/serial lines) and `pos.order.line.pack_lot_ids`.
  - `stock.picking.type` POS extension, `stock.warehouse.pos_type_id`, `stock.picking.pos_order_id/pos_session_id`, `stock.reference`, `stock.rule`, `product.removal`, `product.category`.
  - `pos.config`: `picking_type_id`, `warehouse_id`, `route_id`, `ship_later`, `picking_policy`.
  - `pos.session`: `picking_ids`, `picking_count`, `failed_pickings`, `update_stock_at_closing`.
  - `pos.order`: `picking_ids`, `picking_type_id`, `stock_reference_ids`, `shipping_date`.
  - `res.company.point_of_sale_update_stock_quantities` (stock updated in real time vs at closing).
  - Frontend lot popup, receipt and customer-display bits, and `account.move`/`account.move.line` COGS handling (`_get_pos_anglo_saxon_price_unit`).
- Security: `group_pos_manager` implies `stock.group_stock_user` only when `pos_stock` is installed (`pos_stock/security/pos_stock_security.xml`).
- `point_of_sale` keeps hook comments: "Overridden in pos_stock" (`models/pos_order.py:1204,1588`; `models/pos_session.py:978`).
- Dependents rebased: `pos_mrp`, `pos_repair` now depend on `pos_stock`; `pos_sale_stock` was split out of `pos_sale` (`pos_sale` v19 had `models/stock_picking.py` and `views/stock_template.xml`, gone in v20).
- `pos_stock` has an `uninstall_hook` that removes the "Picking POS" sequences.

### 3.2 Core POS (`point_of_sale`)
Config and session (`pos.config`, `pos.session`):
- **Session closing redesign.** v19 per-session cash register fields (`cash_journal_id`, `cash_register_balance_*`, `bank_payment_ids`, `move_id`) are replaced by an `account.bank.statement` per session (`bank_statement_id`, `opening_balance`, `closing_balance`, `closing_difference`) plus split journal entries: `sale_move_ids`, `refund_move_ids`, `correction_move_ids` (`models/pos_session.py:66-125`). The wizard `pos.close.session.wizard` was removed (`wizard/pos_close_session_wizard.xml` is gone from the manifest). Closing is `close_session_from_ui` (line 479). [High]
- **Daily closing mode.** `session_closing_mode` ('daily' or 'closing') and `session_closing_daily_hour` (default 4.0) on `pos.config`. A new cron "POS: Auto Order Invoicing" (every 10 min, `data/ir_cron_data.xml`) calls `_cron_generate_invoice_period` and validates session accounting without a manual close for configs in daily mode. [High]
- **Invoicing model.** `pos.order.is_singly_invoiced` vs `is_globally_invoiced`; invoicing an order after its session was closed reverses the corresponding amount from the global closing entry and posts a proper invoice (`_generate_invoice_after_session_closing`, `pos_order.py:1710+`). New `defer_invoice_pdf` flag defers PDF generation (`pos_order.py:333,655`). [High]
- New cron "POS: Process Order Tasks" every 5 min (`_cron_process_pos_orders`) and "POS: Product Snooze cleanup" daily.
- **Presets** (`pos.preset`) gained a service fee (`service_fee`, product, fixed/percent, based on pre/post discount) (`models/pos_preset.py:26-30`).
- **New models:** `pos.prep.order` / `pos.prep.line` (preparation orders and lines, with cancelled quantity and combo hierarchy) and `pos.snooze` (temporarily hide a product per config, `type='product'`; extended by self-order with `'self-ordering'`). Tipping config (`set_tip_after_payment`, `tip_percentage_1..3`) and `iface_printbill` moved from `pos_restaurant` to core (v19 `pos_restaurant` held them; see 5).
- **Printers** (`pos.printer`): `printer_type` is now only `epson_epos`. IoT-box printing is removed [code]. New `use_type` (preparation/receipt), `use_cashdrawer`, `use_lna` (browser Local Network Access), `paper_size`, `is_split_per_product`, `timeout`. Config printers split into `preparation_printer_ids` and `receipt_printer_ids`; `use_order_printer` replaces `is_order_printer`.
- **Renames** (affect custom code and settings): `iface_cashdrawer` -> `use_cashdrawer`, `is_kiosk_mode` -> `use_kiosk_mode`, `is_header_or_footer` -> `use_header_or_footer`, `is_closing_entry_by_product` -> `use_closing_entry_by_product`, `use_payment_terminal` -> `payment_provider`, `invoice_journal_id` removed, `iface_print_via_proxy`/`proxy_ip`/`is_posbox`/`iface_scan_via_proxy`/`iface_electronic_scale` removed (IoT box proxy gone), `order_edit_tracking` removed, `auto_validate_terminal_payment` -> `auto_validate_electronic_payment`, new `custom_logo/phone/email/website/receipt_address` ("use_custom_receipt_info"), new `default_partner_id`. [High for the names, Medium for exact semantic equivalence]
- **Payment methods** (`pos.payment.method`): `payment_method_type` selection (`none` / `terminal` / `external_qr` ("Quick Pay (QR Code)") / `cash_machine` / `bank_qr_code`) plus a single `payment_provider` field; providers are contributed by overriding `_get_terminal_provider_selection`, `_get_external_qr_provider_selection`, `_get_cash_machine_selection`. A backend widget `pos_payment_provider_cards` shows installable provider modules (`models/pos_payment_method.py:20-125`). The `bank_qr_code` type generates an offline default QR.
- **Combos:** `product.combo.is_upsell` (qty-min 0 upsell combos).
- **Receipts:** now rendered server-side by `pos.order.receipt` (`receipt/pos_order_receipt.py`) from QWeb templates (`receipt/*.xml`: order, change/preparation, ZPL label, tip, cash move, sale details) loaded into the frontend as "python templates" (`models/ir_ui_view.py`; `registerPythonTemplate` in `pos_data_plugin.js`). It can produce HTML, image or ePoS raster; hence the new dependency `base_report_wkhtmltox`. Receipt layout is shared by backend and frontend. [High]
- **Price inclusion wizard** `pos.price.inclusion.wizard` explains/changes tax-included vs excluded display with an example (`wizard/pos_price_inclusion_wizard.py`); new `views/product_pricelist_view.xml`.
- **Frontend architecture.** The POS app moved from OWL "services" to the new "plugin" framework: `app/plugins/*` (`pos_data_plugin`, `pos_router_plugin`, `pos_ticket_printer_plugin`, `access_right_plugin`, `pos_number_buffer_plugin`, `customer_display_terminal_plugin`, `offline_plugin`), with `bus_plugin`, `barcode_plugin`, and an OWL2/3 compatibility layer in the bundle (`__manifest__.py`). The store is still `app/services/pos_store.js`. Payment terminals are loaded through a dedicated bundle `point_of_sale.payment_terminals`, which `pos_self_order` includes. [High]
- Backend: new `lna_checklist`, `pos_open_ui_button`, lazy pivot/graph views, kanban dark SCSS; `pos.session.kanban_dashboard_graph`.

### 3.3 Offline-mode architecture (HEAD commit)
Layers, all in `addons/point_of_sale/static/src/app/`:
1. **Asset caching**: `service_worker.js` caches same-origin GET requests (cache `odoo-pos-cache`, network-first then cache fallback); it ignores `web/dataset` ("Dataset will be cached in indexedDB"), Chrome extensions and the Cashdro URL. The page posts `urlsToCache` to it.
2. **Data cache in IndexedDB**: `models/utils/indexed_db.js`. DB name `point-of-sale-<config_id>-<db>` (`pos_data_plugin.js: databaseName`). One object store per loaded model (key `id`, or a custom key from `data_service_options.js` for models created in the frontend, such as orders keyed by uuid). Features:
   - schema reconciliation (it adds missing stores and drops stores of uninstalled modules via version bump);
   - batched writes of 500 with a 5 s transaction timeout;
   - a `visibilitychange` probe that reconnects when the connection dies, and a reload dialog for the iOS/Safari "Connection to Indexed Database server lost" bug.
3. **Startup**: `loadInitialData` reads field/relations params from `localStorage` key `pos_data_params_<config_id>`, opens IndexedDB, loads cached server data, then (if online) calls `pos.session.load_data` passing cached ids/write dates to receive a delta, refreshes params, and re-syncs the cache. If offline, the POS boots from cache only (`dataLoadedFromCache` signal).
4. **Connectivity**: `network` state `{offline, loading, unsyncData}`; window `online/offline` events trigger `checkConnectivity()`, which pings `/pos/ping`, retries every 2 s while the browser claims to be online, and then calls `syncData()`.
5. **Write queue**: `execute()` raises `ConnectionLostError` when offline; calls flagged `queue` are appended to `network.unsyncData` with uuid/try count and replayed FIFO on reconnect (`syncData`, behind a mutex). `sync_from_ui` (order push) is handled separately: paid orders are written to IndexedDB immediately (a debounced 300 ms local sync, bypassed on payment validation: `utils/order_payment_validation.js:232`) and tracked in `localUnsyncedPaidOrderUuids` until the server confirms. [High]
6. **Eviction protection (HEAD commit)**: `requestPersistentStorage()` calls `navigator.storage.persisted()` then `navigator.storage.persist()` (best-effort, non-blocking, logged) at `initIndexedDB`, so the browser exempts the origin from automatic storage eviction under disk pressure (`pos_data_plugin.js:150-165`). Firefox may prompt; the browser may deny, so the risk is reduced and not eliminated. [High]
7. **Generic offline UI neutralised**: `plugins/offline_plugin.js` patches the web client's new `OfflinePlugin` so it skips its own setup (and its ORM cache crypto) when `odoo.pos_config_id` or `session.data.config_id` is set; POS keeps its own logic. The same bundle is used by self-order.
8. **Recovery tooling**: `components/loader/critical_pos_error/reset_local_data.js` and debug widget allow wiping local data; `resetIndexedDB()`.
- Offline limits: operations requiring the server (online payments, invoice PDF, terminals needing network, loyalty from server, `bank_qr_code` default QR is precomputed for offline) fail or queue. Orders are numbered with a device identifier sequence (`utils/devices_identifier_sequence.js`) to avoid collisions. [Medium: the exact per-feature offline behaviour was not exercised.]

### 3.4 Restaurant (`pos_restaurant`)
- Floor plan stored as JSON: `restaurant.floor.floor_plan_layout`, per-table `floor_plan_layout` (top/left/width/height/color/shape) and `pos.config.floor_plan_settings`; `pos.config.floor_plan` computed; `get_floor_plan` and `save_floor_plan` (`models/pos_config.py:14-217`). v19's `restaurant.table` columns `position_h/v`, `width`, `height`, `shape`, `color` and floor `background_*` fields are gone; new frontend `floor_plan_editor` with decor items and an `edit_floor/edit_table` toolbar. Migration impact: layout data must be converted. [High on structure; the migration script itself is not visible in this clone]
- **Courses:** new `pos.course` (name, sequence, linked to `pos.category.course_id`) with `use_course_allocation` and `use_show_items_on_course_ticket` options (`models/pos_course.py`, `pos_category.py`). Existing `restaurant.order.course` is kept.
- Tip handling and bill printing moved to core; `pos_payment.py`/`pos_payment.js` and `tip_screen` and `receipt_screen` overrides disappeared from the module. Storable default is switched off for products created from restaurant POS (`models/product_template.py`).

### 3.5 Self-order and kiosk (`pos_self_order`)
- **Delivery preset:** `pos.preset.service_at` now includes `delivery`, with origin address (street/city/zip/state/country, lat/long via `base_geolocalize`), `delivery_max_distance_km` and unit, `delivery_product_id`/`delivery_product_price` and `free_delivery_min_amount`. The module now depends on `google_address_autocomplete` and `base_geolocalize` (v19 depended on `link_tracker`/`http_routing` and kept those). Product `product_delivery_template` is activated when kiosk/mobile mode is on (`models/pos_config.py:170`). [High]
- Optional products page (`optional_product_page`) from `product.template.pos_optional_product_ids`; product cards, choose-combo popup, info popup, pills-selection and number popups, snooze tracker (self-ordering snoozing), a primary colour setting (`self_ordering_primary_color`), and a switch to the plugin architecture (`pos_data_plugin`, `pos_ticket_printer_plugin`). Receipts are generated server-side (`receipt/`).
- **Kiosk payment actions** go through `/kiosk/payment_method_action/<action>` (`controllers/orders.py:267`), which checks that the action is in `pos.payment.method._allowed_actions_in_self_order()`. This method is defined in core `point_of_sale` and overridden by each terminal module (`pos_adyen`, `pos_stripe`, `pos_viva_com`, `pos_mollie`, `pos_mercado_pago`, `l10n_id_pos_self_order_qris`). That is why the per-vendor `pos_self_order_*` modules for Adyen/Stripe/Viva are no longer needed (see 5).
- New glue: `pos_self_order_sms` adds `pos.preset.sms_receipt_template_id` and sends an SMS receipt after a paid mobile/kiosk order that has a phone number (`models/pos_order.py`); `pos_self_order_event` exposes `event.event`, `event.event.ticket`, `event.slot`, registrations and questions to the self-order app, plus an event page; `pos_self_order_bancontact_pay` adds Bancontact QR to kiosks.

### 3.6 HR, loyalty, sale links
- **`pos_hr` role model renamed and re-scoped:** v19 `minimal/basic/advanced_employee_ids` are replaced by four mutually exclusive roles `supervised_employee_ids`, `restrictive_employee_ids`, `cashier_employee_ids`, `manager_employee_ids`. Definitions (field help): supervised = can sell but a higher level must approve before payment closes; restrictive = no discounts, refunds or cancels; cashier = full register access; manager = reports, cash management, session close. Managers (group `pos_manager` users) are forced into manager role (`pos_hr/models/pos_config.py`). New `logged_employee_ids` on sessions, an employee-level sales report (`report.pos_hr.single_employee_sales_report`), and cash moves with `employee_id`. [High]
- **`pos_loyalty`:** Python `res_partner` override removed; frontend models (`loyalty_program/reward/rule.js`) and a server `receipt/` generator added; the `coupon_id` and `reward_identifier_code` fields on POS lines were removed in favour of `card_id`-based logic (`models/pos_order.py`). [Medium: exact data migration unknown]
- **`pos_sale`:** `pos.config.default_product_id` (default product for SO lines settled in POS) plus `has_default_product`, `sale_order_line_name`; `amount_unpaid` field removed from `pos.order`. Stock-specific logic moved to `pos_sale_stock`; `pos_sale_delivery` cancels pending pay-on-delivery payment transactions on settlement.

### 3.7 Online payment, Bancontact, cash machines
- `pos_online_payment`: new controller `controllers/payment_status.py` and a portal "payment status dwell" page; per-order `online_payment_method_id` and `next_online_payment_amount`; the `pos.payment.method.is_online_payment` field and `pos.session` override were removed and the OWL popup was reworked into the payment-screen lines. Uses `account_payment` providers; demo creates an online payment method.
- `pos_bancontact_pay` (new): `bancontact_api_key`, `bancontact_ppid`, `bancontact_test_mode`, `bancontact_usage`, `pos.payment.bancontact_id`; webhook and signature controllers (`controllers/webhook.py`, `signature.py`); customer-display QR. It is an `external_qr` provider (Quick Pay) and not a terminal.
- Cash machines (`cashdro`, `cashmatic`, `glory_cash`) plug in through `_get_cash_machine_selection`.

## 4. What's new / changed vs Odoo 19 (most impactful first)

1. **POS decoupled from Inventory: new `pos_stock` (+ `pos_sale_stock`, `pos_mrp`/`pos_repair` rebased).** `point_of_sale/__manifest__.py` vs v19; `pos_stock/__manifest__.py`. High.
2. **IoT Box removed from CE POS; Epson ePoS network printing only; Web Serial for scales.** `iot_base` and `iot_box_image` removed; `point_of_sale` depends on `iot_webserial`; `pos_printer.printer_type` has only `epson_epos`; `proxy_ip`, `iface_print_via_proxy`, `is_posbox` removed. High.
3. **Offline architecture rebuilt on plugins + IndexedDB with persistent-storage request** (HEAD commit). `static/src/app/plugins/pos_data_plugin.js`, `models/utils/indexed_db.js`, `plugins/offline_plugin.js`. High.
4. **Session accounting redesign:** bank statement per session, split sale/refund/correction entries, daily auto-close (`session_closing_mode`), singly vs globally invoiced orders, deferred invoice PDF; `pos.close.session.wizard` gone. `models/pos_session.py`, `models/pos_order.py`. High.
5. **Server-side receipt engine** (`pos.order.receipt`, QWeb receipts incl. ZPL labels, image/raster output) plus new dep `base_report_wkhtmltox`; per-module `receipt/` folders in `pos_loyalty`, `pos_sale`, `pos_self_order`, `pos_discount`, `pos_stock`. High.
6. **Payment architecture: `payment_method_type` + `payment_provider`, provider cards, new `external_qr` type, Bancontact Pay/Wero, kiosk allow-list via `_allowed_actions_in_self_order`.** Consolidates five removed glue modules. High.
7. **Restaurant: JSON floor plan with a new editor (decor items), `pos.course` and course allocation; tips/bill printing moved to core.** `pos_restaurant/models/*`. High.
8. **Self-order delivery preset, optional products, snoozing, SMS receipt, event tickets.** `pos_self_order/models/pos_preset.py`, `pos_self_order_sms`, `pos_self_order_event`. High.
9. **New preparation data model (`pos.prep.order/line`) and product snoozing (`pos.snooze`).** Medium on intended downstream use (preparation display is not visible in CE).
10. **`pos_hr` four-level role matrix** replaces minimal/basic/advanced. High.
11. **Presets with service fee; combos with upsell; price-inclusion wizard; custom receipt info; `use_lna`.** High.
12. **Partner autocomplete split out (`pos_partner_autocomplete`); `barcodes` -> `barcodes_gs1_nomenclature` dependency; GS1/EPC models loaded in POS.** `__manifest__.py`. High.
13. **Mass renames of `iface_*`, `is_*`, `pos_*` config/settings fields** (see 3.2). High.
14. Framework-level: OWL3 compatibility layer, `*_plugin` replacements for services in the POS bundle. Medium on exact impact for third-party code.

## 5. Removed / merged modules

| Removed module | Evidence of successor | Verdict |
|---|---|---|
| `pos_restaurant_adyen` ("American style tipping for Adyen") | v19 added `adyen_merchant_account` and capture/adjust endpoints. In v20, `pos_adyen` has `adyen_ask_customer_for_tip` with constraint on tip product (`pos_adyen/models/pos_config.py`), tip logic in `pos_adyen/models/pos_order.py` (`set_tip_after_payment`) and `pos_adyen/static/.../payment_adyen.js`. `set_tip_after_payment` and tip screen now live in core `point_of_sale` | Merged into `pos_adyen` + core tipping (High) |
| `pos_restaurant_stripe` | v20 `pos_stripe/static/src/app/payment_stripe.js` mentions tipping; the tip screen is in core | Merged into `pos_stripe` + core (High on destination, Medium on parity of behaviour) |
| `pos_self_order_adyen` | `pos_adyen/models/pos_payment_method.py:46` `_allowed_actions_in_self_order` returns `proxy_adyen_request`, `get_latest_adyen_status`; `/kiosk/payment_method_action/<action>` in `pos_self_order/controllers/orders.py:267` | Merged into `pos_adyen` + `pos_self_order` (High) |
| `pos_self_order_stripe` | `pos_stripe/models/pos_payment_method.py:23` allows `stripe_connection_token`, `stripe_payment_intent`, `stripe_capture_payment`; the `point_of_sale.payment_terminals` bundle is included by `pos_self_order/__manifest__.py:139` | Merged into `pos_stripe` (High) |
| `pos_self_order_viva_com` | `pos_viva_com/models/pos_payment_method.py:65` allows `viva_com_send_payment_request`, `viva_com_get_payment_status`; `pos_viva_com/__manifest__.py` has the `payment_terminals` bundle | Merged into `pos_viva_com` (High) |
| `iot_base`, `iot_box_image` (non-`pos_*`) | `point_of_sale` no longer depends on `iot_base`; `iot_webserial` added | Removed; no CE successor besides `iot_webserial` (`iot_drivers` still ships) (Medium) |
| `l10n_uy_pos` | not investigated | Other agent |
| `pos_epson_printer` / `pos_iot` | never in v19/v20 CE tree (not in `new_in_20` or `removed_in_20`) | Not applicable; they appear to be Enterprise-only (inferred: Low); Epson printing is built into core |

Pattern to remember: payment-terminal modules no longer need per-vendor "restaurant" or "self-order" add-ons. Terminal modules self-register for kiosk by overriding `_allowed_actions_in_self_order`, and the frontend payment classes are loaded through the shared `point_of_sale.payment_terminals` bundle.

## 6. Implementation notes, risks and migration gotchas (19 -> 20)

- **Data migration of moved models.** `pos.pack.operation.lot`, `product.removal`, `stock.picking.type` POS fields and others are now defined by `pos_stock`. Check that `ir.model.data` and columns are carried over (migration scripts are not in this shallow clone). Also verify that `pos_stock` auto-installs on upgraded DBs with Inventory. Install-time `pos_stock` pulls `stock_account`.
- **Pure-POS databases (no Inventory)** now install and run without `stock`; products' storable/valuation settings and "ship later" are unavailable. Custom modules that `_inherit = 'pos.config'` and use `picking_type_id`, `warehouse_id`, etc. must now depend on `pos_stock`.
- **Custom modules depending on `point_of_sale` that use stock models** (pickings, lots, `stock.move`), or `iot_base` JS, will break: add `pos_stock` and drop IoT assets.
- **Renamed fields** (3.2): update server actions, reports, automated actions, Studio-like customisations, export templates and any SQL/BI views (`pos_session.cash_register_*`, `pos_config.iface_*`, `is_kiosk_mode`, `use_payment_terminal`, `printer_ids`, `pos_hr` basic/advanced lists, `restaurant.table` geometry).
- **Hardware:** customers on IoT Box printers/scales/terminals in CE must move to Epson ePoS network printers (needs HTTPS and Local Network Access, see `use_lna` and the `lna_checklist` backend component) or Enterprise IoT. Scales via Web Serial (Chromium only, [web]-style browser dependency, not verified). Cash-drawer opens through the printer (`use_cashdrawer`).
- **Accounting:** the session closing flow, journal entry structure and cash statement logic changed. Re-test closing, partial refunds after closing, global vs single invoicing and reporting; test daily closing mode and that the cron's server timezone/hour assumptions fit your shops (the closing hour is compared with UTC `now` in `_cron_generate_invoice_period`; no timezone conversion seen: Medium).
- **Floor plans:** restaurant layouts need conversion to JSON layout; test the editor with large floors.
- **Printing:** receipts and kitchen tickets are now generated by server QWeb templates and wkhtmltoimage; custom receipt templates written as OWL/XML inheritance in v19 (`order_receipt.xml`, `order_change_receipt_template_inherit.xml`) must be rewritten for `receipt/*.xml`.
- **Third-party POS JS:** services -> plugins refactor (`pos_data_plugin`, `pos_router_plugin`, `*_plugin`), OWL3 compat layer and new patched paths (e.g. `pos_store.js` override points, `data_service.js` deleted from `pos_self_order`). Any module patching `PosStore`, `DataService`, `printer_service`, `pos_router_service` or `receipt_screen` will need rework. High.
- **Browser storage:** IndexedDB per config and DB. Clearing browser data loses unsynced orders. Train staff to re-sync before clearing and keep devices online before closing the session. Persistent storage may be denied; Firefox may prompt.
- **Self-order:** new Google address autocomplete and geolocalize dependencies for delivery. Verify API keys if the delivery preset is used. Kiosk terminals need only their vendor `pos_*` module now.
- **Security:** kiosk calls are whitelisted per action; custom terminal modules must override `_allowed_actions_in_self_order` or kiosk calls return 403.
- **Role mapping:** map v19 minimal/basic/advanced employee lists to supervised/restrictive/cashier/manager deliberately; roles are mutually exclusive.

## 7. Open questions / not verifiable from CE code
- Migration scripts (`upgrade/` data moves for `pos_stock`, floor plan JSON conversion, field renames) are not visible (shallow clone, no history). Behaviour of upgraded databases is unverified.
- Enterprise modules referenced by CE code but absent: `pos_iot_worldline`, `pos_iot_six`, `pos_tyro`, `pos_enterprise` features (preparation display consuming `pos.prep.order`, restaurant add-ons, IoT box printing). Whether `pos_epson_printer` and `pos_iot` still exist in Enterprise 20 is not verifiable here.
- Exact mapping of v19 `pos_loyalty` field removals (`coupon_id`, `loyalty_card_count`, `reward_identifier_code`) to the new logic.
- Whether v19 `iface_print_skip_screen`, `order_edit_tracking` and `split_transactions` have replacements (not found; assumed dropped).
- Release-note claims from odoo.com for Odoo 20 were not cross-checked (no [web] research performed).
- The HEAD commit's diff is not available (no history); the eviction protection description is inferred from the code in `pos_data_plugin.js:150-165`.
