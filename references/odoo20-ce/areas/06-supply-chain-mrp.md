# Supply Chain, Manufacturing, Repair, Maintenance & Fleet — Odoo 20 CE

Source of truth: `/home/user/odoo-src/odoo20` (branch 20.0, HEAD b100a87) diffed against `/home/user/odoo-src/odoo19`. All paths below are relative to `odoo20/` unless stated. [code] = verified in source. [web] = not used; no web cross-check was performed, so everything here is code-verified or flagged as inference.

## 1. Scope

About 49 modules in `addons/` matched the supply-chain family patterns (manifest diff, 19 vs 20):

- Inventory: `stock`, `stock_account`, `stock_landed_costs`, `stock_dropshipping`, `stock_sms`, `stock_delivery`, `stock_fleet`, `stock_maintenance`, `barcodes`, `barcodes_gs1_nomenclature`, `product_expiry`, `delivery`
- Purchase: `purchase`, `purchase_stock`, `purchase_mrp`, `purchase_requisition`, `purchase_requisition_stock`, `purchase_alternative`, `purchase_alternative_stock`, `purchase_alternative_sale`, `purchase_product_matrix`, `purchase_repair`, `purchase_edi_ubl_bis3`
- Manufacturing: `mrp`, `mrp_account`, `mrp_landed_costs`, `mrp_product_expiry`, `mrp_repair`, `mrp_delivery`, `mrp_subcontracting`, `mrp_subcontracting_account`, `mrp_subcontracting_dropshipping`, `mrp_subcontracting_landed_costs`, `mrp_subcontracting_purchase`
- Repair, maintenance and fleet: `repair`, `maintenance`, `fleet`, `fleet_maintenance`
- Sale bridges and PoS: `sale_stock`, `sale_mrp`, `sale_mrp_margin`, `sale_stock_margin`, `sale_purchase`, `sale_purchase_stock`, `sale_purchase_project`, `sale_stock_product_expiry`, `website_sale_stock`, `pos_stock`, `pos_sale_stock`
- Removed in 20: `stock_picking_batch`, `delivery_stock_picking_batch`, `purchase_requisition_sale`, `mrp_subcontracting_repair`, `delivery_mondialrelay`, `website_sale_stock_wishlist`, `l10n_ec_stock`, `l10n_ro_edi_stock_batch`

Not in CE: there is no `quality` module in `addons/`. `mrp_workorder`, `quality_control`, `mrp_plm`, `mrp_mps`, `stock_barcode`, `mrp_workorder_hr` and `mrp_subcontracting_account` Enterprise add-ons are not in this repo. `mrp/models/res_config_settings.py` still exposes `module_quality_control`, `module_mrp_plm`, `module_mrp_mps` toggles that install them only on Enterprise.

## 2. Module catalogue

| Module | App? | Summary | What it does | Status vs 19 |
|---|---|---|---|---|
| stock | Yes | Inventory | Warehouses, locations, routes/rules, transfers, quants, lots/serials, packages, reordering, scrap, traceability, **now also batch and wave transfers** | Changed (major) |
| stock_account | – | Inventory valuation | Perpetual/periodic valuation of stock moves, `product.value` cost history, AVCO and FIFO, lot valuation | Changed (major) |
| stock_landed_costs | – | Landed costs | Allocate freight/duties to receipts, split by qty/weight/volume/value/equal | Changed |
| stock_dropshipping | – | Drop shipping | Dropship operation type and route (vendor to customer) | Changed (small) |
| stock_delivery | – | Delivery connectors glue | Carriers on transfers, labels, packages, now also batch and wave limits by weight | Changed (large) |
| delivery | – | Delivery methods | Carrier definitions and rating | Changed |
| stock_sms | – | SMS on delivery | SMS sent when a delivery is validated | Unchanged-ish |
| stock_fleet | – | Stock Transport | Docks, vehicles and drivers on batches, CMR consignment note | Changed (depends on `stock`, not `stock_picking_batch`) |
| stock_maintenance | – | Lots used in maintenance | Link lots to maintenance equipment | Unchanged-ish |
| barcodes / barcodes_gs1_nomenclature | – | Barcode parsing | Barcode nomenclatures, scanner JS | Changed (JS refactor) |
| product_expiry | – | Expiry dates | Expiration, best-before, removal and alert dates on lots; FEFO removal | Unchanged-ish (tracking value `none` becomes `False`) |
| purchase | Yes | Purchase | RFQ, PO, vendor bill matching, vendor pricelists | Changed (accruals, matching) |
| purchase_stock | – | Receipts for POs | Receipts, vendor lead time, price difference, MTO and buy rules | Changed |
| purchase_mrp | – | PO and MO glue | Kit handling on POs, MO and BoM overview shows PO lines | Unchanged-ish |
| purchase_requisition | – | Agreements | Blanket orders and call for tender only | Changed (alternatives split out) |
| purchase_requisition_stock | – | Requisition and stock | Requisition-driven procurement | Changed (wizard removed) |
| purchase_alternative | – | Alternative RFQs | Call for tender via alternative RFQs, line comparison | **New** (extracted from `purchase_requisition`) |
| purchase_alternative_stock | – | Bridge | Lead time and receipt data in comparison | **New** (replaces part of `purchase_requisition_stock`) |
| purchase_alternative_sale | – | Bridge | Alternatives for subcontracted services | **New** (replaces `purchase_requisition_sale`) |
| purchase_repair | – | Repair and PO | Link POs and repair orders | Unchanged-ish |
| mrp | Yes | Manufacturing | BoMs, kits, by-products, work centers, routings, MOs, work orders, unbuild, scrap, BoM and MO overview | Changed (major) |
| mrp_account | – | Manufacturing accounting | Analytic cost of work centers, WIP accounting wizard, BoM cost | Changed (extra cost, production account) |
| mrp_landed_costs | – | Landed costs on MO | Apply landed costs to MOs | Changed (small) |
| mrp_product_expiry | – | Expiry in MO | Finished-lot expiry and consumed lot expiry checks | Unchanged-ish |
| mrp_repair | – | MO and repair | Link repair and MO traceability | Changed (small) |
| mrp_delivery | – | Delivery and kits | Carrier data (weight) for kit products on move lines | **New** |
| mrp_subcontracting | – | Subcontracting | Subcontracting BoMs, resupply, subcontractor portal | Changed (MO overview, security merged into csv) |
| mrp_subcontracting_account / _dropshipping / _landed_costs / _purchase | – | Bridges | Valuation, dropship, landed costs, PO for subcontracting | Changed (depends rewired) |
| repair | Yes | Repair | Repair orders, parts, **service lines**, invoicing | Changed (major) |
| maintenance | Yes | Maintenance | Equipment, requests, preventive scheduling, teams | Changed (state model) |
| fleet | Yes | Fleet | Vehicles, contracts, services, odometer, costs | Changed (small) |
| fleet_maintenance | – | Bridge | Equipment assigned to a vehicle | **New** |
| pos_stock / pos_sale_stock | – | PoS stock | PoS integration with stock | **New** modules (carved out of PoS, outside this area) |

## 3. Feature deep-dive

### 3.1 Inventory (`stock`)

Core models in v20 (from `_name` scan): `stock.warehouse`, `stock.location`, `stock.route`, `stock.rule`, `stock.picking.type`, `stock.picking`, `stock.move`, `stock.move.line`, `stock.quant`, `stock.lot`, `stock.package`, `stock.package.type`, `stock.package.history`, `stock.putaway.rule`, `stock.storage.category`, `stock.warehouse.orderpoint`, `stock.reference`, `stock.scrap.reason.tag`, plus the newly merged `stock.picking.batch`.

Key workflows:

- **Transfers**: receipt, internal, delivery, plus `mrp_operation` and `repair_operation` types from the other apps. Back-orders, zero-demand confirmation (new wizard `stock.zero.demand.confirmation`), return pickings and return slips.
- **Operation types** moved into their own file `stock/models/stock_picking_type.py`. They hold reservation method, auto-print flags, batch and wave rules, and the new `auto_show_allocation_report` and `allocated_location_id`.
- **Batch, wave and cluster transfers** (see 3.1.1).
- **Replenishment**: reordering rules now carry `daily_demand`, `min_max_based_on` (last 7 days, 30 days, 3 months, 12 months, same month last year, custom) and `min_max_based_on_factor`. A new wizard `stock.orderpoint.suggest` recomputes min and max from past demand (`stock/models/stock_orderpoint.py`, `stock/wizard/stock_orderpoint_suggest.py`). [code]
- **Traceability**: `stock.traceability.report` and lot/serial genealogy; `product_expiry` extends it with expiry columns.
- **Packages**: `stock.package` with history (`stock.package.history`), and `mrp` now extends both (`mrp/models/stock_package.py`).
- **Allocation report**: the old "Reception Report" (`report.stock.report_reception`, group `stock.group_reception_report`) is replaced by `stock.allocation.report` (`stock/report/stock_allocation_report.py`), inherited by `mrp` so it also works for MOs. [code]
- **Labels**: new label layout wizards for locations, packages and operation types; `mrp.finished.product.label.layout` prints finished-product labels from a done MO.

#### 3.1.1 Batch and wave transfers (merged into `stock`)

Verified: `stock_picking_batch` is gone from `addons/` and its model `stock.picking.batch` now lives in `stock/models/stock_picking_batch.py`. Wizards `stock.add.to.wave` and `stock.picking.to.batch` are under `stock/wizard/`, views in `stock/views/stock_picking_batch_views.xml`, report in `stock/report/report_picking_batch.xml`, demo in `stock/data/stock_demo3_batch.xml`.

Activation is no longer a module install. `stock.group_stock_picking_batch` is a setting group (`group_stock_picking_batch`, "Batch, Wave & Cluster Transfers") in `stock/models/res_config_settings.py`; the old `module_stock_picking_batch` field is gone. `stock_fleet` and `stock_delivery` extend `stock.picking.batch` directly. `delivery_stock_picking_batch` is removed; its function (batch limits by weight) is now `batch_max_weight` handling in `stock_delivery/models/stock_picking_batch.py` and `stock_picking_type.py`. [code]

Picking-type automation fields: `auto_batch`, `batch_creation_type` (manual or automatic), group-by partner, destination country, source or destination location, wave group-by product, category, location or date, `batch_max_lines`, `batch_max_pickings`, `batch_auto_confirm`.

#### 3.1.2 Scrap (model removed, now a move)

`stock.scrap` no longer exists as a model (absent from `_name` scan; `stock/models/stock_scrap.py` deleted). Scrap is now a `stock.move` with `is_scrap=True`, `scrap_reason_tag_ids` and `should_replenish_scrapped`, executed via `stock.move.action_scrap()` and `_action_scrap()` (`stock/models/stock_move.py` ~l.2958). Pickings and MOs open a scrap move form (`stock.view_scrap_move_form`). Scrap sequence code `stock.scrap` and `res.company.scrap_location_id` remain. The wizard `stock.warn.insufficient.qty.scrap` handles insufficient quantity. [code] Consequences: reports, automations and SQL on `stock_scrap` break; `stock.move.line` has `is_scrap`; `stock.lot` has `is_scrap`.

#### 3.1.3 Tracking and storable semantics

`is_storable` ("Track Inventory") now lives on `product.template` in the `product` module (`product/models/product_template.py` l.127), not in `stock`. `tracking` on `stock` products is now only `lot` or `serial` (falsy means by quantity), and `stock/models/product.py` adds a derived selection `store_by` (`untracked`, `quantity`, `lot`, `serial`) with an inverse that writes `is_storable` and `tracking`. `product_expiry` changed `vals.get('tracking') == 'none'` to `not vals['tracking']`. Any custom code or domain using `tracking = 'none'` or `!= 'none'` must change. [code, High]

### 3.2 Valuation (`stock_account` and `account`)

Architecture comparison:

- **Layers**: v19 and v20 both have no `stock.valuation.layer`. Valuation is held on `stock.move.value` plus `product.value` (cost history, `stock_account/models/product_value.py`) plus `stock.avco.report`. So the "SVL to new approach" shift already happened in 19; 20 refines it. [code]
- **Cost methods**: `standard`, `average` (AVCO), and `fifo` (added by `stock_account` via `selection_add` on `res.company.cost_method`). Category-level `property_cost_method` unchanged.
- **Valuation modes**: `periodic` (at closing) and `real_time` (perpetual, at invoicing) are the two values of `inventory_valuation`. Unchanged names.
- **Big shift**: the company-level valuation and closing machinery moved from `stock_account` into core `account` (`account/models/company.py`): `inventory_valuation`, `inventory_period` (manual, daily, monthly), `account_stock_journal_id`, `account_stock_valuation_id`, base `cost_method` (standard, average), `action_close_stock_valuation`, `_action_close_stock_valuation`, `_cron_post_stock_valuation`, accrual data `_get_accrual_data`, `get_inventory_value`, `get_inventory_accounting_value`. New report `account.stock.valuation.report` (`account/report/account_stock_valuation_report.py`) replaces `stock_account.stock.valuation.report`. `stock_account` now just overrides hooks (`use_stock_account`, `get_inventory_value`, `_get_inventory_valuation_products`). [code, High]
- **Closing entries**: `account.move.inventory_closing` flag, and `closing_datetime` on moves in `stock_account` replaces the old `ir.config_parameter` list of last closing ids (`{company}.stock_valuation_closing_ids`). [code]
- **Anglo-Saxon COGS**: COGS lines are now created by the base `_create_cogs_lines` in `account`, with `line._use_inventory_valuation()` as the hook (`stock_dropshipping/models/account_move_line.py` overrides it). `stock_account` no longer builds them itself (`_stock_account_prepare_realtime_out_lines_vals` removed).
- **Purchase accruals**: `purchase` adds category accounts `property_account_bills_to_receive_id` and `property_account_billed_not_received_id`, and company accounts `account_bills_to_receive_id` and `account_billed_not_received_id`, used by the closing entry (`purchase/models/product_category.py`, `purchase/models/res_company.py`). `purchase.order.line` filters `prepaid_expense` and `bill_to_receive`.
- **Product cost history**: `product.value` gained `quantity`, `old_cost`, `new_cost`, `old_value`, `new_value`, `adjustment` and `account_move_id`, so manual cost changes show a before/after audit trail.
- **Lot valuation**: `lot_valuated` (valuation per lot) carried over from 19.
- **Landed costs**: `stock.landed.cost` no longer rejects non-FIFO/AVCO products; it has per-cost-line `apply_on_product_ids`, `pickings_count` and `allowed_product_ids` (`stock_landed_costs/models/stock_landed_cost.py`).
- **Production account**: `mrp_account` adds `stock_account_production_cost_id` (WIP "Production Account") on company and category, and `extra_cost` on BoMs, included in BoM cost computation (`mrp_account/models/mrp_bom.py`, `product.py`).

### 3.3 Purchase

- **RFQ to PO**, vendor price lists, vendor lead times, approval, portal confirmation. PO gains `receipt_status`, `show_receive_button`, `document_tax_mode`, `incoterm_location` (moved up from `purchase_stock` into `purchase`), `bill_matched_ratio`, `date_promised` (in `purchase_stock`).
- **Vendor-bill matching** (`purchase.bill.line.match`) extended: `matching_id`, `display_matching_tag`, `qty_to_invoice_raw`, `product_uom_qty_to_invoice`, new JS components `matching_tag` and `purchase_line_match_field`, and bill fields `purchase_matched_ratio`, `purchase_matching_issue_msg`. [code]
- **Product**: `sold_by_vendor_id`; the product catalog flag `is_in_purchase_order` removed. `purchase.order.line.label` replaces `translated_product_name`.
- **Partners** get default incoterm and incoterm location for purchases (`res.partner.purchase_incoterm_id`).
- **Requisitions** (`purchase_requisition`): now only blanket orders and call for tender (`purchase.requisition`, `requisition_type`). Line model gained `display_type` (sections and notes), `sequence`, `parent_id`.
- **Alternatives** (`purchase_alternative`, see section 5): compare lines across alternative RFQs, create alternatives via wizard `purchase.alternative.create`, warn on confirmation via `purchase.alternative.warning`, group via `purchase.order.group`.
- **Dropshipping / MTO**: `sale_purchase_stock`, `stock_dropshipping`.

### 3.4 Manufacturing (`mrp`)

Models: `mrp.bom`, `mrp.bom.line`, `mrp.bom.byproduct`, `mrp.routing.workcenter`, `mrp.workcenter`, `mrp.workcenter.productivity`, `mrp.production`, `mrp.workorder`, `mrp.unbuild`, wizards for consumption warning, backorder, split, serial numbers, change qty.

- **BoM types**: only `normal` ("Manufacture this product") and `phantom` (Kit). Subcontracting adds `subcontract`. New BoM fields: `continuous` (continuous production), `note` (shown in Shop Floor per its help), `uom_id` (renamed from `product_uom_id`).
- **Work orders**: new `cost`, `cost_mode` (actual or estimated), `priority`, `color`, `properties` (`wo_properties_definition` on the operation type), `picking_type_id`, `has_planning_issues`, `has_conflicts`, `remaining_time`, `qty_to_produce`, `production_lot_producing_id`. Work center gains `barcode`. Dependencies (`blocked_by_workorder_ids`, `allow_workorder_dependencies`) kept.
- **MO**: new `note`, `package_history_ids`, `packages_count`, `active_workcenter_ids`, `is_due_today`, `product_name`, `product_default_code`, `previous_date_start`, `mrp_production_all_child_count`, `validate_button_style`. Operation type gets `auto_confirm_production` (create draft MOs from replenishment).
- **Unbuild**: `mrp.unbuild` now supports multiple lots (`lot_ids` replaces `lot_id`), limited to lots in the MO's `lot_producing_ids`.
- **Overviews**: BoM overview and MO overview reports; `mrp_account`, `mrp_subcontracting` and `purchase_mrp` extend them with cost, subcontracting and PO info (new `mo_overview*` JS under `mrp_subcontracting/static/src/components`).
- **Consumption control removed from CE**: the BoM field `consumption` (flexible, warning, strict) and the move field `manual_consumption` are absent from v20 CE; only the consumption warning wizard (`mrp.consumption.warning`) remains. [code, Medium; may be an Enterprise-only move, not verifiable]
- **Scrap in MO**: `mrp.production.scrap_ids` removed; the scrap count is computed from `stock.move.is_scrap`.

### 3.5 Subcontracting

`mrp_subcontracting` keeps the subcontractor portal (new `portal_entry_data.xml`), resupply routes, and subcontracting records. Removed `subcontracting_has_been_recorded`. `mrp_subcontracting_purchase` now depends on `mrp_subcontracting_account`, and `mrp_subcontracting_landed_costs` depends on `mrp_landed_costs` instead of `stock_landed_costs`.

### 3.6 Repair

Major rework (`repair/models/repair.py`, `repair_service_line.py`):

- **State**: `under_repair` is removed; states are `draft`, `confirmed`, `done`, `cancel`. `Repaired` became `Done`. Start-repair action is gone; "End repair" (`action_repair_end`) runs a new consumption check wizard `repair.consumption.warning`, replacing `stock.warn.insufficient.qty` for repair.
- **Service lines**: new model `repair.service.line` (product of type service, quantity, UoM, sale line and invoice line links) replaces service-type move lines.
- **Invoicing without sale**: `account.move.repair_order_id`, `repair.invoice_ids`, `action_create_invoice` builds a customer invoice directly; smart buttons on partner (`repair_order_count`) and on invoices.
- Product catalog on repair orders was reworked (`product_catalog_product_is_in_repair` removed).
- `mrp_subcontracting_repair` is gone (see section 5).

### 3.7 Maintenance

- **Request state**: `maintenance.request` now has an explicit `state` (`normal`, `changes_requested`, `approved`, `done`, `cancelled`), replacing `kanban_state`, `archive`, stage-level `done` flag and `request_date`. Single `technician_user_id` is replaced by `user_ids` (multiple technicians); equipment gains `maintenance_team_ids` on stages and categories.
- Instruction types (PDF, Google Slide) removed; only `instruction_text`.
- **Properties**: `equipment_req_properties_definition` on equipment lets each equipment define custom fields for its requests.
- **Assignment**: `equipment_assign_to` selection (`other`) with `is_assigned`; `fleet_maintenance` adds `vehicle`. Maintenance stage data is: New Request, In Progress, Repaired, Scrap.
- New widgets: `maintenance_request_state_selection`, a radio field, calendar recurrence popover.

### 3.8 Fleet

Small: `plan_to_change_bike` and `plan_to_change_car` merged into `plan_to_change_vehicle`; `horsepower_tax` removed from vehicle and model; `trailer_hook` and `color` removed from model; services have `date_from` and `date_to` instead of `date`; unique license plate SQL constraint (`UNIQUE(license_plate)`) with a test; `company_id` on model and service type; partner smart button `partner_cars_count`.

### 3.9 Process manufacturing guide (sugar, food, lots, expiry)

This section is written for a sugar manufacturer using v20 CE.

- **Lots and expiry**: install `product_expiry`. Per lot: expiration date, best-before, removal date, alert date. FEFO removal strategy ships in `product_expiry/data/product_expiry_data.xml`; other strategies in CE: FIFO, LIFO, closest location, least packages (`stock/data/stock_data.xml`). `mrp_product_expiry` handles expiry of consumed and finished lots. Expired lots trigger a confirm-expiry wizard on delivery. Set tracking to "By Lots" on the product (the `Tracking` field, `store_by` in v20).
- **Multiple lots per MO**: `mrp.production.lot_producing_ids` is a many2many, so one MO can yield several lots (crop batches). Unbuild accepts multiple lots from that list.
- **By-products**: group `mrp.group_mrp_byproducts` ("By-Products" setting). Sugar example: bagasse, molasses and filter cake as by-products with cost share on the BoM. The UoM allow-list now also includes by-product UoMs (`mrp/models/product_uom.py`).
- **Kits (phantom BoMs)**: bags or retail packs as kits, exploded in pickings. With delivery, `mrp_delivery` carries kit weights to carrier data. For valuation, `mrp_account` excludes kits (`is_kits`) in v19; in v20 `_get_valuation_product_domain` moved to `account` as `_get_inventory_valuation_products_domain`, so verify kit exclusion in your DB.
- **Work centers and routings**: enable "MRP Work Orders" (`group_mrp_routings`). Capacity, OEE, cost per hour, and `cost_mode` actual or estimated. Continuous production (`continuous` flag on BoM) suits process lines where the next operation starts as output is registered. Planning Gantt and Shop Floor are Enterprise (not in CE; the CE field `note` mentions Shop Floor).
- **Scrap**: use the scrap move from MO or transfer, with reason tags (`stock.scrap.reason.tag`) and optional replenish. Production loss is by scrap move, not by a `stock.scrap` document.
- **Unbuild**: for returns or rework; it reverses an MO with its original BoM and lots.
- **Quality**: no quality module in CE (Enterprise `quality_control`); use lots and expiry plus custom fields or properties on operations (`wo_properties_definition`).
- **Costing**: AVCO suits commodity inputs (cane, raw sugar); standard price suits finished goods with variance reporting; `extra_cost` on BoM covers energy and labour; WIP via `mrp_account` WIP wizard.
- **Packaging**: `stock.package` (formerly "result packages") with history and `mrp.finished.product.label.layout` for finished product labels.

## 4. What's new / changed vs Odoo 19

1. **Batch, wave and cluster transfers merged into `stock`** (no separate module; setting group `stock.group_stock_picking_batch`). [code] `stock/models/stock_picking_batch.py`, `stock/models/res_config_settings.py`. High.
2. **`stock.scrap` model deleted; scrap is a flagged `stock.move`** with reason tags. [code] `stock/models/stock_move.py` (`is_scrap`, `action_scrap`), `stock/models/stock_scrap_reason_tag.py`. High.
3. **Valuation and closing entries moved to core `account`** (fields `inventory_valuation`, `inventory_period`, closing methods, accruals, `account.stock.valuation.report`). [code] `account/models/company.py`. High.
4. **`product_uom` renamed to `uom_id`** across stock, mrp, repair, purchase, purchase_requisition (quant, lot, move, move line, BoM, BoM line, MO, work order, work center, unbuild, orderpoint, PO line, repair). [code] diff of field names. High; custom code and reports must be adapted.
5. **`ir.model.access.csv` replaced by `ir.access.csv`** with columns `operation` (crud) and `domain` (record rules folded in); e.g. `stock/security/ir.access.csv`, `repair/security/ir.access.csv`. [code] High.
6. **Purchase alternatives split out** of `purchase_requisition` into `purchase_alternative` (+ `_stock`, `_sale`). [code] High.
7. **Reception report becomes allocation report** (`stock.allocation.report`, `auto_show_allocation_report`, `allocated_location_id`); `group_reception_report` removed. [code] `stock/report/stock_allocation_report.py`. High.
8. **Repair rework**: no "Under Repair" state, `repair.service.line`, direct invoicing, consumption warning wizard. [code] High.
9. **Maintenance requests have an explicit state, multiple technicians and per-equipment properties**; `done` stage flag and `archive` removed. [code] `maintenance/models/maintenance.py`. High.
10. **Min/max suggestions from demand history** on reordering rules (`daily_demand`, `min_max_based_on`, wizard `stock.orderpoint.suggest`). [code] High.
11. **Purchase accruals and bill matching**: bills-to-receive and billed-not-received accounts, matching ratio and tags. [code] `purchase/models/*`. High.
12. **`is_storable` moves to `product`; `tracking` loses `none`** (adds `store_by`). [code] Medium-High.
13. **BoM consumption policy (`consumption`, `manual_consumption`) removed from CE**; BoM `continuous` flag, `note`, work order `cost_mode`, `properties`. [code] Medium.
14. **Landed costs allowed regardless of cost method**; per-line product filter. [code] Medium.
15. **New `printer` module required by `stock_delivery`** (label printing to external printers). [code] `stock_delivery/__manifest__.py`. Medium.
16. **`stock_fleet` renamed "Transport Management"**, depends on `stock`, CMR report. [code] Medium.
17. **Many new `mrp_account` features**: BoM `extra_cost`, production account. [code] Medium.
18. **Fleet and maintenance clean-ups** and `fleet_maintenance` bridge. [code] Medium.
19. **Settings/groups**: removal of `module_delivery_dhl`, `_fedex_rest`, `_ups_rest`, `_usps_rest`, `_bpost`, `_easypost`, `_sendcloud`, `_shiprocket`, `_starshipit`, `_envia` toggles from the stock settings; replaced by `action_view_delivery_methods`. [code] `stock/models/res_config_settings.py`. Medium. `picking_policy` now on company/settings and synced to picking types.
20. **Stock move `location_final_id` removed**; replaced by `forecasted_location_id`. [code] `stock/models/stock_move.py` l.86. Medium (also on MO and PO line).
21. **Barcode JS stack refactored** (`barcode_service.js` and `barcode_handler_field.js` removed; `barcode_plugin.js`, `barcode_input`, `barcode_view` added; `barcodes.barcode_events_mixin` removed). [code] `barcodes/`. Medium.

## 5. Removed / merged modules

| Removed module (19) | Evidence of successor | Verdict |
|---|---|---|
| stock_picking_batch | `stock.picking.batch`, wizards `stock.add.to.wave`, `stock.picking.to.batch`, views and report now under `stock/`; group `stock.group_stock_picking_batch`; `l10n_ar_stock`, `stock_delivery`, `stock_fleet` extend the model from `stock` | **Merged into `stock`** |
| delivery_stock_picking_batch | `stock_delivery/models/stock_picking_batch.py` (`batch_max_weight` limits), `stock_picking_type.py` | Merged into `stock_delivery` |
| purchase_requisition_sale | `purchase_alternative_sale` has the same `sale_purchase` bridge role (depends `purchase_alternative` + `sale_purchase`) | Renamed or replaced by `purchase_alternative_sale` (inferred from identical bridge function) |
| mrp_subcontracting_repair | 19 manifest was a no-code bridge (depends `mrp_subcontracting`, `repair`; no models); in 20 only `i18n/` remains in the directory | Removed, no successor needed |
| delivery_mondialrelay | Not in 20 `addons/`; `website_sale_mondialrelay` also removed | Removed, no successor found in this area |
| website_sale_stock_wishlist | Listed in `removed_in_20.txt`; website wishlist modules removed | Removed, no successor found |
| l10n_ec_stock | Listed in `removed_in_20.txt` | Removed, no successor found |
| l10n_ro_edi_stock_batch | `l10n_ro_edi_stock/models/stock_picking_batch.py` now exists | Merged into `l10n_ro_edi_stock` |

New in 20 in this area: `purchase_alternative`, `purchase_alternative_stock`, `purchase_alternative_sale`, `mrp_delivery`, `fleet_maintenance`, `pos_stock`, `pos_sale_stock` (the last two outside this audit's depth), `printer` (dependency of `stock_delivery`).

Note on `purchase_requisition_stock`: still exists, but its own wizard and view for alternatives were removed; the alternative-aware parts moved to `purchase_alternative_stock`.

## 6. Implementation notes, risks and migration gotchas (19 to 20)

1. **Database renames**: `product_uom` to `uom_id` columns and fields everywhere. Studio, reports (QWeb), server actions, `ir.rule` domains and SQL views using `product_uom_id` or `product_uom` must be rewritten. Run the standard migration scripts and grep custom code.
2. **Scrap data**: `stock_scrap` records need migrating to flagged moves; check the OpenUpgrade-equivalent scripts. Custom reports on scrap quantities by `scrap_id` need to switch to `stock.move.is_scrap`. `stock.move.scrap_id` and `stock.move.line.scrap_id` are removed.
3. **Batch transfers**: if you had `stock_picking_batch` installed, the module vanishes. Enable the batch group in Settings after migration and verify `batch_id` links. If you had `module_stock_picking_batch` toggles in custom views, replace with `group_stock_picking_batch`.
4. **Tracking domains**: replace `tracking = 'none'` with `tracking = False` and prefer `store_by`.
5. **Valuation**: keep the accounting policy (periodic vs perpetual) and test closing entries. `inventory_closing` and `closing_datetime` replace the config-parameter approach. COGS lines creation moved to `account`, so custom overrides of `_stock_account_prepare_realtime_out_lines_vals` will be dead. Review the new accrual accounts (bills to receive, billed not received) after enabling perpetual valuation.
6. **Security**: `ir.model.access.csv` and several `*_security.xml` rule files are folded into `ir.access.csv`. Custom modules inheriting the old CSV by xml id (`access_*`) may reference ids that no longer exist; test group-restricted users.
7. **Repair**: any customisation on `under_repair` state, repair lines of type "service", or `stock.warn.insufficient.qty` in repair must be redone. Invoices can now originate from a repair directly.
8. **Maintenance**: stage flag `done` and request `archive` are gone; reporting must use `state`. Single technician field replaced by `user_ids`.
9. **Reception report**: automations or templates relying on `stock.report_reception` or the setting `group_stock_reception_report` need review; the new report is `stock.allocation.report`.
10. **Carrier connectors**: the delivery connector toggles are no longer in the stock settings; set them up through the delivery methods action. `stock_delivery` now requires `printer`.
11. **Consumption policy**: if you relied on BoM "Flexible / Warning / Strict" consumption (CE 19), v20 CE no longer exposes the field. Verify behavior before go-live. [Medium confidence]
12. **Kits and valuation**: verify kits are still excluded from the valuation report (`is_kits` filter moved).
13. **Landed costs** are no longer blocked for standard-cost products; check that costing method choices remain intentional.
14. **Fleet**: unique license plate constraint may fail on data with duplicates; clean before upgrade. Bike/car plan-to-change flags merged.
15. **Process manufacturing**: test lot-per-MO flows, by-product cost share and FEFO after upgrade, since `product_expiry` and `stock.quant` were touched.

## 7. Open questions / not verifiable from CE code

- Whether `mrp_workorder` (Shop Floor), `quality_control`, `mrp_plm`, `mrp_mps`, `stock_barcode` changed in Enterprise 20; not in this repo.
- Reason for removal of BoM `consumption` and `manual_consumption` in CE (possible move to Enterprise); not provable here.
- Whether `purchase_requisition_sale` data migrates to `purchase_alternative_sale` (no migration scripts in the shallow clone; checked `addons/` only).
- Official Odoo 20 release notes were not consulted, so marketing names of new features are unconfirmed.
- Exact upgrade handling of `stock.scrap` records (migration scripts are not in CE source).
- Whether the new `pos_stock` and `pos_sale_stock` modules are pure extractions from `point_of_sale` and `pos_sale` (likely, but belongs to the PoS area).
- Behavior of cron `_cron_post_stock_valuation` in production (periodic daily or monthly auto-closing) needs functional testing.
