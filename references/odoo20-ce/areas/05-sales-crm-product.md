# Sales, CRM, Product, Pricing, Loyalty & Delivery — Odoo 20 CE

Method: manifests (`data/manifests_19.json` / `manifests_20.json`), `diff -r odoo19/addons/X odoo20/addons/X`, and a field-level diff of `fields.*` declarations per module. All paths are relative to `odoo20/` unless prefixed `odoo19/`. Everything is [code] verified unless tagged [web]; no web sources were used. Confidence: High = read in code; Medium = inferred from code structure; Low = guess.

## 1. Scope (modules covered, count)

47 modules in `addons/` were examined (46 present in v20 + 1 removed-in-20 successor check):

- **Sales (28):** sale, sale_management, sale_crm, sale_loyalty, sale_loyalty_delivery, sale_margin, sale_pdf_quote_builder, sale_product_matrix, sale_project, sale_project_margin (NEW), sale_project_stock, sale_project_stock_account, sale_service, sale_stock, sale_stock_margin, sale_stock_product_expiry, sale_mrp, sale_mrp_margin, sale_purchase, sale_purchase_project, sale_purchase_stock, sale_timesheet, sale_timesheet_margin, sale_expense, sale_expense_margin, sale_sms, sale_edi_ubl, sale_gelato, sale_gelato_stock.
- **CRM (7):** crm, crm_iap_enrich, crm_iap_mine, crm_livechat, crm_mail_plugin, crm_sms, crm_sale_project (NEW).
- **Product/UoM (6):** product, product_matrix, product_expiry, product_margin, product_email_template, uom.
- **Loyalty/Delivery:** loyalty, delivery (+ sale_loyalty_delivery above). Removed: delivery_mondialrelay, delivery_stock_picking_batch.
- **Other:** sales_team, partnership, website_partnership (NEW), purchase_alternative / purchase_alternative_sale / purchase_alternative_stock (all NEW), mysubscription (NEW).

## 2. Module catalogue

"Δ size" = number of changed diff lines excluding i18n, as a rough change indicator.

| Module | App? | Summary | What it does | Status vs 19 |
|---|---|---|---|---|
| sale | no (technical) | Sales internal machinery | Quotations/SO, lines, invoicing, portal, payments, pricelist glue, analytic reinvoicing | **Changed (very large, Δ~32k)** |
| sale_management | **yes** (Sales) | From quotations to invoices | Quotation templates, upsell/optional products, digest | **Changed (large)** |
| sales_team | no | Sales Teams | `crm.team`, team members | Changed (small: access CSV, search domain) |
| crm | **yes** | Track leads and close opportunities | Leads/opps, pipeline, PLS scoring, auto-assignment, activities | **Changed** (new dep `base_install_request`) |
| crm_iap_enrich / crm_iap_mine | no | IAP enrichment / lead mining | Enrich leads by email domain; generate leads (IAP credits) | Unchanged-ish |
| crm_livechat / crm_mail_plugin / crm_sms | no | Lead from chat / mail plugin / SMS | Bridges | Unchanged-ish |
| crm_sale_project | no (auto_install) | Project generation from opportunities | `project.project.lead_id`, "Create a Project" button on lead | **New** |
| sale_crm | no | Opportunity to quotation | Quotation from opp | Unchanged-ish (Δ107) |
| product | no | Products & Pricelists | Templates/variants, attributes, combos, pricelists, packaging, docs, labels | **Changed (large)** |
| uom | no | Units of measure | `uom.uom` with relative factor | Changed (small, see §4) |
| product_matrix | no | Matrix implementation | Grid entry widget | Unchanged-ish |
| sale_product_matrix | no | Variants on SO via grid | Grid on SO | Unchanged-ish |
| product_expiry | no | Expiry dates | Lots expiry (needs stock) | Unchanged-ish |
| product_margin | no | Margins by product | Product margin report | Unchanged-ish |
| product_email_template | no | Product email template | Per-product mail on invoice | Unchanged-ish |
| loyalty | no | Discounts, gift cards, eWallets, loyalty | Programs, rules, rewards, cards, history | **Changed** (points expiry) |
| sale_loyalty | no | Loyalty on SOs | Coupon/reward application on SO | Changed (large, Δ~11.8k; mostly security/JS/refactor) |
| sale_loyalty_delivery | no | Free shipping reward | Reward type free shipping | Changed (small) |
| delivery | no | Delivery Costs | Carriers, price rules, choose-carrier wizard, COD | **Changed** (delivery note wizard, COD, rates button) |
| sale_stock | no | SO ↔ delivery | Delivery on SO, lead times, availability | **Changed** (portal returns) |
| sale_mrp / sale_mrp_margin | no | MRP bridge | Kits on SO | Unchanged-ish |
| sale_purchase (+_project/_stock) | no | Service outsourcing | SO line → PO | Changed (field rename `service_to_purchase`→`service_tracking`) |
| sale_project | no | Task/project from SO | Service products → project/task | **Changed** |
| sale_project_margin | no (auto_install) | Sales margins in projects | Estimated cost/margin on project | **New** |
| sale_project_stock / _account | no | Profitability bridges | Stock traceability in project profitability | Unchanged-ish |
| sale_service | no | Project/planning interplay | Glue | Unchanged-ish |
| sale_timesheet (+_margin) | no | Sell based on timesheets | Billable timesheets, T&M, fixed price | **Changed** (analytic-line refactor) |
| sale_margin | no | Margins on SO | `purchase_price`, `margin` | Changed (small) |
| sale_stock_margin / sale_stock_product_expiry | no | Bridges | | Unchanged-ish |
| sale_expense (+_margin) | no | Reinvoice expenses | Expense → SO | Changed (receipt attachments) |
| sale_pdf_quote_builder | no | PDF quotation builder | Header/footer PDFs, form fields in quote | Changed (`utils.py` removed, doc option moved) |
| sale_sms / sale_edi_ubl | no | SMS / UBL order import | | Unchanged-ish |
| sale_gelato (+_stock) | no | Gelato print-on-demand | Place orders via Gelato | Changed (variant images) |
| partnership | no | Partnership / Membership | `res.partner.grade`, pricelist per level, product → "membership" tracking | Unchanged-ish |
| website_partnership | no | Publish partners on website | `/partners` pages, publish grades | **New** |
| purchase_alternative (+_sale, +_stock) | no | Call-for-tender via alternative RFQs | Compare lines across RFQs | **New** (successor of `purchase_requisition_sale`, see §5) |
| mysubscription | no (auto_install) | Backend Subscription App | Client action showing Enterprise subscription/IAP status | **New** — not a subscription billing app (§3.10) |

## 3. Feature deep-dive

### 3.1 Quotations / Sales Orders (`sale`, `sale_management`)

Core flow unchanged: quotation (`draft`/`sent`) → confirm (`sale`) → deliver → invoice, with `invoice_status`, locking (`group_auto_done_setting`), pro-forma, discount per line, order warnings, mass cancel, accrued-orders wizard (`addons/sale/wizard/`).

New or reworked in v20 (all [code], `addons/sale/models/sale_order.py` and `sale_order_line.py`):

- **Tax-included/excluded per document**: `document_tax_mode` on order and line, defaulting from `company.account_price_include` and propagated to invoices (`sale_order.py:191, 1884`).
- **Over-invoicing / overages**: `has_overages`, `invoice_overages`, `qty_overage` on lines, and `allow_invoice_overages`/`invoice_overages` on the "Create invoice" wizard (`wizard/sale_make_invoice_advance.py`).
- **Close for invoicing**: `invoicing_closed` ("Manually Closed For Invoicing") forces an order to be treated as fully invoiced.
- **Delivery status now in `sale`**: `delivery_status` (pending/started/partial/full), `is_unfulfilled`, `show_ship_button`, `delivery_date` and `qty_delivered_percent` live in `sale` (v19: `delivery_status`, `incoterm` lived in `sale_stock`). Incoterm and location also moved to `sale` (and `res.partner.incoterm_id`).
- **Services & Materials mode**: new group `sale.group_services_and_material` / setting "Services & Materials"; adds `reinvoice_policy` (renamed from `expense_policy`) visibility, analytic `from_services_and_material` context, and a "Services and Materials" dashboard styling (`sale/static/src/scss/services_and_material.scss`). `sale.order.analytic_account_id` and `account.analytic.line.order_id/so_line/reinvoice_move_id` are now in `sale` (new `models/account_analytic_line.py`, replaces v19 `analytic.py`).
- **Company-level invoicing policy**: `res.company.sale_invoice_policy` and `sale_automatic_invoice` (replace config params `default_invoice_policy`/`automatic_invoice` in settings). Product-level `invoice_policy` remains (ordered/delivered).
- **Accruals**: company accounts `account_invoiced_not_delivered_id` / `account_invoices_to_issue_id` plus category-level equivalents (`models/product_category.py`); lines get `accrual_move_ids`, filters `deferred_revenue` / `invoice_to_be_issued`. This is the "revenue recognition by SO" extension of the accrued-orders wizard.
- **UX**: line numbers (`show_sol_numbers`), product images on SO (`display_product_images_on_so`), "Mandatory Product" setting (`sale.mandatory_product` config param activates view `sale.view_order_form_mandatory_product`), sub-sections (`line_subsection`, `section_qty`, `section_uom_id`), product catalog "previously bought by customer" (`previously_bought_by_customer`), new Sales Dashboard cards (To Confirm / To Deliver / To Invoice / To Upsell) in `sale/static/src/js/dashboard/`, and portal entries (`data/portal_entry_data.xml`: "Quotations to review", "Your Orders").
- **Unpaid amount**: `amount_unpaid` (computed from online transactions and non-paid invoice lines) — "amount left to pay to avoid double payment or double invoicing".

### 3.2 Online signature & payment, upsell

- **Online payment**: `require_payment` is gone from `sale.order` (v19 `sale_order.py:117`); payment requirement now follows `prepayment_percent` (>0) / new `prepayment_amount` (inverse field) via `_has_to_be_paid` (`sale_order.py:2405`). Quotation template no longer has `require_payment` either. [code, High] — partners must re-check "online payment" settings after migration.
- **Online signature**: `require_signature` retained (template field `require_signature`, `portal_confirmation_sign`).
- **Upsell**: still Sales Order based; the dashboard has a "To Upsell" card (`dashboard.js`). Upsell via recurring/subscription is Enterprise (see §3.10).
- **Optional products** remain on quotation templates and portal.

### 3.3 Quotation templates (`sale_management`)

- Two template types now: `template_type` = "quotation" or "section" (`sale_order_template.py:24`). **Section templates** are reusable blocks inserted into any quotation (`prepare_section_template_order_lines`, `get_section_templates`-style RPC at line ~346).
- Access control: `share_template` + `team_ids` (restrict to sales teams) + `user_has_access`; creators always have access; salesmen may delete their own section templates.
- Template lines are much richer: `price_unit`, `discount`, `tax_ids`, `label`, `mandatory_product`, `section_qty`/`section_uom_id`, collapse flags (`collapse_composition`, `collapse_prices`), and product attribute values incl. custom/no-variant (new `product.attribute.custom.value.sale_order_template_line_id`). Template currency (`currency_id`). With `sale_margin`, template lines carry `purchase_price`.
- Settings removed: `group_sale_order_template` and `res.company.sale_order_template_id` / `company_so_template_id` (v19 `sale_management/models/res_company.py`, `res_config_settings.py` are gone) — templates are no longer an opt-in group and there is no company default template field. [code, High for removal; "always on" is inferred, Medium]
- `has_productless_lines` flags lines without product/section (warning in UI).

### 3.4 Product, variants, UoM and packaging

- **UoM model simplification**: `uom.uom.rounding` is removed (v19 `uom_uom.py:39`); rounding is delegated to the decimal precision "Product Unit" (`digits='Product Unit'` is used on all qty fields). `round()/compare()/is_zero()` remain on `uom.uom` (`addons/uom/models/uom_uom.py:108-130`). Group `uom.group_uom` is now a "light" group (`uom/models/res_groups.py`).
- **Packagings = UoMs**: template `uom_ids` ("Packagings", already in 19), new variant-level `extra_uom_ids`; `product.supplierinfo.product_uom_id` renamed `uom_id`; sale lines restrict `product_uom_id` to `allowed_uom_ids` (`product_id._get_available_uoms()`), and pricelist rules can be limited to one unit (`product.pricelist.item.uom_id` "Packaging", `allowed_uom_ids`).
- **Price per base unit**: new model `product.base.unit` and fields `base_unit_count/id/name/price` on template/variant, setting `group_show_uom_price`.
- **Inventory quantities in `product`**: `qty_available`, `virtual_available`, `incoming_qty`, `outgoing_qty`, `free_qty`, `is_storable` now declared in `product` (`product_product.py:94-110`), so non-stock modules (e.g. POS/sale) can read them; `stock` overrides compute. [code, High; consequence for custom code Medium]
- **Attribute exclusions**: model `product.template.attribute.exclusion` is deleted; replaced by `product.template.attribute.value.excluded_value_ids` (many2many) (`product_template_attribute_value.py:50`). Also `sequence` and `show_price_extra` on PTAV; `product.document.variant_attribute_value_ids` lets documents target variants.
- **Labels**: `product.label.layout` gains ZPL printing (`barcode_format`, `zpl_template`, `zpl_preview`), packaging selection, `with_price`.
- **Catalog**: new `product.catalog.line.mixin` (`product_id`) and variant `catalog_is_in_order` (replaces `is_in_selected_section_of_order`), used by sale/purchase catalogs.
- `product.category.company_id` (multi-company categories), `module_product_barcodelookup` setting (barcode lookup is an add-on module not in this repo list — treat as Enterprise/IAP; Low), `res.partner.is_pricelist_manually_set`.

### 3.5 Pricelist engine

Rewritten rule model (`addons/product/models/product_pricelist_item.py`):

- `compute_price` selection changed from **percentage / formula / fixed** (v19: `odoo19/.../product_pricelist_item.py:106`) to **discount / markup / fixed** (v20 `:107`). `percent_price` and `display_applied_on` are removed; "formula" rules are expressed with `price_discount` (percent), new `price_markup` (computed/inverse of the surcharge percent), `price_round`, `price_surcharge` (extra fee), `price_min_margin`, `price_max_margin`, plus `base` = Sales Price / Cost / Other Pricelist.
- New `is_plain_discount` (rule lowers price by exactly its percentage) drives "discount shown to customer"/strike-through; `_compute_price_before_discount` walks chained pricelists while the base rule is a plain discount.
- `_is_applicable_for(product, quantity, *, uom=None, **kwargs)` takes a UoM; quantity is converted to the product UoM unless the rule is bound to a packaging.
- New product-template `fixed_pricelist_rule_ids` and `show_sales_price_page`; `product.pricelist.item._compute_price` now takes `**kwargs` (`date`, `currency`, `depth`) — custom overrides of v19 signatures will break (`_compute_price(product, quantity, uom, date, currency=None, **kwargs)` in v19).
- Pricelist assignment: SO "update pricelist"/"update fiscal position" banner fields (`show_update_pricelist`, `show_update_fpos`) removed from `sale.order`; `res.partner.is_pricelist_manually_set` added. [code, High; replacement UX Low]
- Pricelists remain a CE feature (no Enterprise dependence). `loyalty.program` still supports `pricelist_ids`.

### 3.6 CRM

- **Lead conversion**: wizard `crm.lead2opportunity.partner` removed (`addons/crm/wizard/crm_lead_to_opportunity.py` only in v19); single-lead "Convert to Opportunity" is now a direct method `action_convert_to_opportunity` (`crm_lead.py:1320`) with partner matching/creation. Mass conversion wizard stays and gains `link_to_matching_customer`, `duplicated_lead_ids`, `team_id`; `deduplicate`/`action` options dropped. 
- **Auto-assignment UX**: `crm.team.member.assignment_rules` (unlimited / limited / out of rotation) replaces `assignment_optout`; capacity `assignment_max` kept; team `show_assignment_max`, `opportunity_count`, `alias_full_name`.
- Removed fields: `crm.lead.commercial_partner_id`, `is_partner_visible`, `stage_id_color`, `crm.stage.color`.
- New: `/lead` command hook `discuss.channel._prepare_lead_create_values` (live chat), PWA share target (`controllers/webmanifest.py`), upsell-style module-install request mail (`crm` now depends on `base_install_request`, template `crm_module_access_request_template`), team switcher/lead-generation dropdown/mail-plugin promo components in `static/src/components/`.
- Config: `module_website_partnership` ("Partners Website Page") setting next to `module_partnership`.
- `sale.crm.team` dashboards: `invoiced` and `invoiced_target` are gone from `crm.team` (`addons/sale/models/crm_team.py` now has only `sale_order_count` and dashboard button helpers). Sales-team revenue targets no longer exist in CE sale. [code, High; replaced by the new Sales dashboard, Medium]
- **crm_sale_project (NEW)**: `project.project.lead_id`; lead gets `project_ids`, `project_count`, `task_count`; "Create a Project" opens the project-template wizard prefilled with the lead's customer, first service SO line and `allow_billable` (`crm_sale_project/models/crm_lead.py`). Auto-installed with `sale_project`+`crm`.
- Lead assignment (PLS, rule-based assignment) and IAP modules are functionally unchanged; Enterprise-only CRM extras (e.g. VoIP, SMS marketing campaigns, appointments, Lead Generation visitors) are not in this repo.

### 3.7 Loyalty / coupons / gift cards / eWallet

- **Points expiry**: `loyalty.program.expire_after` (days; constraint >=0) → each earned `loyalty.history` row gets `expiration_date` and `points_changed_date`; consumption order is FIFO by `expiration_date` then date (`FIFO_ORDER` in `loyalty_history.py:9`); `linked_loyalty_history_id` ties usage lines to the earning entry; `program_type` on history. Expiry applies to `loyalty` programs only (`card.program_type == "loyalty"`).
- **Per-customer limit**: `once_per_user` and `partner_ids` ("Used by") on programs.
- `sale_order.loyalty_data` JSON removed; `sale_loyalty` gets controllers (`controllers/gift_card.py`, `portal.py` for portal gift-card redemption) and new `interactions/` frontend code.
- Program types unchanged (coupons, promotions, gift cards, loyalty, eWallet, buy X get Y, next-order coupons, promo-code/pricelist-based).

### 3.8 Delivery

- New wizard models `delivery.note.wizard` / `.line` (`addons/delivery/wizard/delivery_note*.py`): record a shipment from the SO (sales-only, no stock) with carrier, tracking ref/URL, shipping date, shipped quantities and "remaining qty to ship"; sends a shipping confirmation e-mail (`data/mail_template_data.xml`) and prints a report (`report/ir_actions_report.xml`). Sequence in `data/ir_sequence_data.xml`. [code, High; intended for services/dropship without Inventory, Medium]
- Cash on delivery: `delivery.carrier.allow_cash_on_delivery` + `supports_cash_on_delivery` (fixed and rule-based carriers only), `payment.method` hook `_get_pay_on_delivery_method_codes`.
- Choose-carrier wizard: `carrier_prices` JSON + "Get rates" button when more than one carrier is available (`show_delivery_rates_button`).
- Price rules: `variable_unit` computed from carrier weight/volume UoM. `delivery.carrier.delivery_cost` / `delivery_currency_id` display fields.
- Portal controller `location_selector` (pickup point selector) no longer in `delivery`; `pickup_location_data` moved from `sale.order` to `res.partner` in `stock_delivery` (`stock_delivery/models/res_partner.py:9`), consumed by `website_sale_collect`. Carrier connectors (DHL, FedEx, UPS, USPS, bpost, Easypost, Sendcloud, Shiprocket, Starshipit, Envia…) are not in this repo any more as `module_delivery_*` toggles were removed from `sale` settings; they remain Enterprise connectors, and `ir.module.module.action_view_delivery_methods` is used from the module card. [code for removed toggles; Enterprise status Medium]

### 3.9 Sales → Project / Timesheet / Expense / Purchase

- **sale_project**: new `project.project` fields `real_cost`, `real_cost_ratio`, `sale_order_amount_total`, `sale_warning_text`; `sale.order.project_required`; `account.analytic.line.billable_type/category_report` moved here (`sale_project/models/account_analytic_line.py`); `project_update.py` removed (the "profitability" update template still loaded from `views/project_update_template.xml`).
- **sale_project_margin (NEW)**: `estimated_cost` and `estimated_cost_ratio` on projects computed from `sale.order.line.purchase_price × qty` of open-task SO items; action "Forecast Margins" with report view (`sale_project_margin/report/sale_report_views.xml`).
- **sale_timesheet**: `hr_timesheet.py` split — `timesheet_invoice_id`/`timesheet_invoice_type` replaced by `reinvoice_move_id` and `billable_type` (generic analytic billable types: Timesheets Fixed Price/T&M/Milestones/Manual/Non-Billable); `account_move_send.py` added; timesheets analysis report adapted.
- **sale_expense**: wizard `expense_attachment_selection_wizard`; `hr.expense.attach_receipts_to_invoice` attaches receipts to the customer invoice generated from the SO.
- **sale_purchase**: `product.template.service_to_purchase` (boolean) replaced by `service_tracking` selection extension.

### 3.10 Stock-side sales features (`sale_stock`)

- **Portal returns**: `return.reason` model (default reasons in `data/return_reason_data.xml`), company settings `allow_spontaneous_returns` and `return_validity_days` (default 14), portal route `/my/order/return_data` and `/my/orders/<id>/download_return_label`, return dialog JS, `stock.picking.return_reason_id`. Customers can create returns from the SO portal page and download a return label PDF.
- `delivery_status`, incoterm, and `qty_available_today`/`virtual_available_at_date` computation moved to `sale`/`product` (see 3.1).

### 3.11 Sales PDF quotation builder

Header/footer PDFs and form-field mapping retained (`sale.pdf.form.field`, `quotation.document`). Changes: `utils.py` deleted, the `attached_on_sale = 'inside'` ("Inside quote pdf") `selection_add` override no longer appears in `sale_pdf_quote_builder/models/product_document.py` and no `'inside'` value exists anywhere in `sale`/`sale_pdf_quote_builder` Python/XML in v20, so the placement mechanism for product PDFs changed (not determined; Low), form-field label renamed "Fields". Custom-content kanban-like widget JS reworked.

### 3.12 Partnership / membership

`partnership` (also in v19): `res.partner.grade` with `default_pricelist_id`, `product.template.service_tracking = 'partnership'` and `grade_id` — selling a membership product assigns the buyer's level and pricelist. **`website_partnership` (NEW)**: publishes grades/partners on the website (`website.published.mixin` on `res.partner.grade`, route `/partners/grade/<slug>`), CRM setting `module_website_partnership`. In v20 `website_crm_partner_assign` (reseller/partner assignment) now depends on `website_partnership` instead of owning the grade-publication code. [code, High]

### 3.13 mysubscription (NEW) — not a subscription engine

`mysubscription` (`addons/mysubscription/`, category Sales, `auto_install: True`, depends `base`, `web`) is a **backend "My Subscription" dashboard** only: abstract model `mysubscription.mysubscription` reads `database.enterprise_code` / `database.expiration_date` config parameters to tell whether the DB has an active Enterprise subscription, lists IAP accounts/credits (`get_iap_data`), and ships OWL components (user-menu entry, navbar, plan box, subscription/database dialogs with master-password actions). It has **no recurring plans, no invoicing schedule**. [code, High]. Odoo Subscriptions (`sale_subscription`), Rental (`sale_renting`) and Planning are not in the CE tree (no module with those names in `addons/`) — Enterprise-only. Also absent from CE: e-signature (`sign`), Amazon/eBay connectors, helpdesk, appointment, commissions (no commission module exists in CE).

### 3.14 Purchase alternatives (NEW trio)

`purchase_alternative` ("Call for tender": create alternative RFQs, compare lines, choose best combination — `wizard/purchase_alternative_create.py`), `purchase_alternative_sale` (carries `sale_line_id` into alternative lines), `purchase_alternative_stock`. These take over the "alternative RFQ" use case of `purchase_requisition` (see §5).

## 4. What's new / changed vs Odoo 19 (most impactful first)

1. **Pricelist rule model rewritten**: `compute_price` = discount/markup/fixed, `percent_price`/`display_applied_on` removed, markup & margin bounds, per-UoM rules, `is_plain_discount`. `addons/product/models/product_pricelist_item.py` — High.
2. **Global security-file format change**: every module ships `security/ir.access.csv` (columns `operation` = crud letters and `domain`), replacing `ir.model.access.csv` + record rules (`ir_rules.xml`, e.g. `loyalty_security.xml`, `sale_management_security.xml` removed). New model `ir.access` (`odoo/addons/base/models/ir_access.py`). 226 modules use it; 0 in v20 still use the old file in `addons/*/security`. Custom modules' CSV/XML ACL files must be converted. — High.
3. **Quotation templates**: section templates, team-restricted/shared templates, per-line price/discount/taxes/attributes, no opt-in group. `sale_management/models/sale_order_template*.py` — High.
4. **Services & Materials + analytics/reinvoicing in `sale`**; `expense_policy` → `reinvoice_policy`; company-level invoice policy; accruals accounts; overages; `document_tax_mode`; `delivery_status`/incoterm in `sale`; `require_payment` removed in favour of `prepayment_amount`. `addons/sale/models/*` — High.
5. **UoM/packaging**: `uom.rounding` removed; packaging = `uom.uom` incl. variant `extra_uom_ids`; supplierinfo `uom_id`; base unit price (`product.base.unit`); qty fields in `product`. — High.
6. **Customer-portal returns** (`return.reason`, label PDF) in `sale_stock`. — High.
7. **Delivery note wizard + COD + rate selection** in `delivery`; pickup-location data moved to `stock_delivery`; `delivery_mondialrelay` and `delivery_stock_picking_batch` removed (§5). — High.
8. **Loyalty point expiry (FIFO), once-per-user programs.** `addons/loyalty/models/loyalty_history.py`. — High.
9. **CRM**: direct convert-to-opportunity (wizard removed), assignment rules selection, `crm_sale_project` (NEW), PWA share target. — High.
10. **New project-margin/profitability bridges**: `sale_project_margin` (NEW), `sale_project` real cost fields, timesheet billing via `reinvoice_move_id`. — High.
11. **New Sales dashboard** (To Confirm/Deliver/Invoice/Upsell cards) replaces sales-team invoiced target (`crm.team.invoiced*` removed). — Medium.
12. **Sale expense receipts on invoices**, ZPL product labels, `website_partnership`, `purchase_alternative*`, `mysubscription`. — High.
13. Removal of `product.template.attribute.exclusion` model (replaced by many2many). — High.

## 5. Removed / merged modules

| Removed in 20 | Evidence | Successor |
|---|---|---|
| `delivery_stock_picking_batch` | Its logic (`batch_group_by_carrier`, `batch_max_weight`, `_is_picking_auto_mergeable`) now lives in `stock_delivery/models/stock_picking_batch.py` and `stock_picking_type.py:23-35`; v19 module depended on `stock_delivery` + `stock_picking_batch` | **Merged into `stock_delivery`** (and `stock_picking_batch` itself merged into `stock`: `stock/models/stock_picking_batch.py`, `stock/views/stock_picking_batch_views.xml`; `stock_picking_batch` also removed in 20) — High |
| `delivery_mondialrelay` | Grep of `odoo20/` for "mondialrelay" in py/xml/js: no hits; `website_sale_mondialrelay` also removed | **Removed, no successor found**. Generic pickup-point selection now via `website_sale_collect` + `pickup_location_data` in `stock_delivery`; the MR widget integration is not replaced — Medium |
| `purchase_requisition_sale` (adjacent) | `odoo19/.../wizard` content is identical to `purchase_alternative_sale/wizard/purchase_alternative_create.py` | **Renamed/refactored → `purchase_alternative_sale`** (`purchase_requisition_stock` → `purchase_alternative_stock`; `purchase_requisition` remains for blanket orders) — Medium |
| `website_sale_wishlist`, `website_sale_comparison`, `*_wishlist`, `website_sale_autocomplete` (e-commerce, outside scope) | in `removed_in_20.txt`; `website_address_autocomplete` & `pos_partner_autocomplete` are NEW | Autocomplete → `website_address_autocomplete` (name match only, Low); wishlist/comparison: no successor found |

Not removed but relocated: `sale/models/analytic.py` → `account_analytic_line.py` + `account_analytic_applicability.py`; `sale_timesheet/models/hr_timesheet.py` → `account_analytic_line.py`; `sale_management/models/res_company.py` & `res_config_settings.py` deleted.

## 6. Implementation notes, risks & migration gotchas (19 → 20)

1. **ACL conversion**: any custom `ir.model.access.csv` / `ir.rule` records must move to `ir.access.csv` (new columns). Test with non-admin roles; salesman access to `account.account`, `account.analytic.account` is granted from `sale/security/ir.access.csv`.
2. **Pricelist data migration**: map v19 `compute_price` `percentage` → `discount` (using `percent_price` → `price_discount`), `formula` → `discount`/`markup` with `price_surcharge`/`price_round`/margins. Any custom code reading `percent_price`, `display_applied_on`, or overriding `_compute_price(..., date, currency)` must be updated. Verify Enterprise/website_sale overrides.
3. **`expense_policy` → `reinvoice_policy`** (and `visible_*`) on `product.template`; custom views/reports/domains referencing the old name break.
4. **Quotation templates**: `require_payment` is gone; set prepayment explicitly. The template-group setting and company default template disappear — check any automation that sets `sale_order_template_id` by company. Template lines now have taxes/prices; review existing templates for currency/multi-company checks.
5. **`require_payment`, `show_update_pricelist`, `show_update_fpos`, `amount_undiscounted`, `translated_product_name`** fields removed from `sale.order`/line — update reports/QWeb/Studio views.
6. **UoM**: `uom.rounding` removed; reports or code using `uom.rounding` / `float_round(precision_rounding=uom.rounding)` must use `uom.round()/compare()`. Check decimal precision "Product Unit". `product.supplierinfo.product_uom_id` → `uom_id`.
7. **Attribute exclusions**: data stored in `product.template.attribute.exclusion` must be converted to `excluded_value_ids`; custom code on the old model fails at import.
8. **`sale.order.incoterm`, `delivery_status`** are now in `sale`; if `sale_stock` is customized with the same fields, fields may be defined twice/override. `sale_stock` no longer defines `is_storable`, `qty_available_today`, etc. on SO line.
9. **Sales team targets** (`crm.team.invoiced_target`, `invoiced`) are gone from `sale`; data and dashboards based on them are lost.
10. **CRM**: lead conversion wizard model removed — custom buttons/server actions that open `crm.lead2opportunity.partner` must call `action_convert_to_opportunity`. `assignment_optout` replaced by `assignment_rules`.
11. **Delivery**: `delivery_mondialrelay` data (Point Relais carriers) has no module in 20 → uninstall/clean before upgrade, plan alternative. Carrier connectors are Enterprise; verify licence. `pickup_location_data` moved.
12. **Loyalty**: new columns on `loyalty.history` (`expiration_date`, `points_changed_date`); existing history rows have no expiry. Review `sale_loyalty` customizations that used `loyalty_data`.
13. **Timesheets**: `timesheet_invoice_id` / `timesheet_invoice_type` renamed; BI/SQL reports need updates; `billable_type` values now defined via `_get_billable_types` (`sale_timesheet/models/account_analytic_line.py`).
14. **Purchase requisition**: alternative RFQ flows now need `purchase_alternative*`; verify auto-install of the bridge modules.
15. `mysubscription` auto-installs; it only shows Enterprise status. Do not promise subscription billing in CE — recurring invoicing still requires Enterprise or custom/OCA modules.
16. Frontend JS: many sale/sale_management components were renamed (e.g. `sale_product_field.js` → `sale_product_field/` + `sale_product_mixin.js`; `sale_management/static/src/fields/...`), so custom JS patches may fail.

## 7. Open questions / things not verifiable from CE code

- Exact functional description and screenshots of Odoo 20 release notes were not cross-checked [web]; claims are code-derived only.
- Which Odoo modules supply the real carrier connectors (DHL/FedEx/UPS/…): not in this repo, assumed Enterprise (`module_delivery_*` settings removed from `sale`); confirm per carrier.
- Whether `product.template.attribute.exclusion` data is auto-migrated: no migration scripts are in the CE tree (`product/migrations` absent); handled by Odoo's upgrade service, not visible.
- Whether the Sales dashboard fully replaces team invoicing targets (not verified in UI).
- `module_product_barcodelookup` target module and `website_address_autocomplete` as the successor of `website_sale_autocomplete` — name evidence only.
- Enterprise-only features (subscriptions, rental, planning, VoIP, Sign, appointments, commissions, advanced IAP lead scoring/enrichment features) cannot be inspected here; only their absence from `addons/` is verified.
