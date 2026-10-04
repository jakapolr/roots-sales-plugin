# Odoo 20 Community Edition: A Study Paper

**What changed, what it means, and how to act on it**

*Prepared for: Trinity Roots Co., Ltd., Bangkok (internal)*
*Snapshot: 3 October 2026. Source: `odoo/odoo` branch `20.0` (HEAD `b100a87`) compared with branch `19.0`*
*Companion material: [README](README.md) · [module catalogue](01-module-catalog.md) · [10 area reports](areas/)*

---

## How to read this paper

This paper is meant to be read from start to finish (about 45 minutes). The detail sits in the area reports, and each section links to its source report.

Every material claim comes from reading the code. Where a claim relies on something else, it says so:

- **[code]**: verified in the 20.0 source tree (paths are cited in the area reports).
- **[web]**: a published claim that could not be verified against code.
- **CE / EE**: Community vs Enterprise Edition. Only CE source is public. An EE feature can only be described as "not in CE"; its contents cannot be seen.

Confidence is graded **High / Medium / Low** where it matters.

---

## Part 0: Executive summary

Odoo 20 is the first long-term major release since 19.0 (2025). It also bundles everything Odoo released online-only in between (saas-19.1 to saas-19.4), which is why **598 of the 657 CE modules changed** and **473 changed heavily**. Odoo 20 CE has **657 modules (all LGPL-3) and 34 installable "apps"**. Since 19.0, **58 modules were added and 63 removed**. Most removals are merges into a parent module, not lost features.

Ten things matter most:

1. **Security model rewritten: `ir.access` replaces both access rights (`ir.model.access`) and record rules (`ir.rule`).** One table now holds a CRUD operation string plus an optional domain. Rows tied to a group *grant* (OR-ed) and group-less rows *restrict* (AND-ed). Every module ships `security/ir.access.csv`. This is the largest change for custom-module porting. [code] High
2. **Front-end moves to Owl 3 (3.0.0-alpha.49) with an Owl 2 compatibility layer.** jQuery, legacy public widgets, QUnit and FontAwesome are gone, and services become "plugins". All custom JavaScript must be reviewed. [code] High
3. **Offline mode in the CE web client and a rebuilt offline Point of Sale (POS).** Visited records are cached in encrypted IndexedDB, and saves and deletes queue up and replay when the connection returns. [code] High
4. **Platform modernisation.** Python ≥ 3.12, the SQL-generation layer rewritten, the old dict-returning `read_group` removed, deprecated 18/19 APIs deleted, and **the HTTP server binds to 127.0.0.1 by default** (was 0.0.0.0). [code] High
5. **Report engine is pluggable.** wkhtmltopdf moves out of core into `base_report_wkhtmltox` (auto-installed). The new optional engine `base_report_paper_muncher` arrives, and so does a `printer` module for direct printing. [code] High
6. **Accounting data model changes.** Account groups are replaced by parent/child accounts, `res.bank` is removed (bank accounts denormalised), there is a per-document tax mode, a refactored payment core, Peppol generalised, and stock valuation and closing moved into `account`. [code] High
7. **Supply chain simplification.** Batch/wave transfers are merged into `stock`, scrap becomes a flagged stock move, `product_uom` is renamed `uom_id` everywhere, packagings become units of measure, and the pricelist engine is rewritten (discount/markup/fixed). [code] High
8. **POS no longer requires Inventory** (new `pos_stock`). The IoT Box is removed from CE, receipts are rendered on the server, and session accounting is redesigned with optional daily closing. [code] High
9. **HR restructured.** Time-off types are merged into work-entry types, there is a new `hr.time.rule` engine for overtime, resource calendars are redesigned (fixed/variable/undefined), and org chart and home-working are folded into `hr`. [code] High
10. **No AI in CE.** AI agents, MCP connectivity, call recording and transcription are absent from the CE code (hooks exist for an Enterprise module). The repo does ship a `skills/` folder: official coding-agent guidelines for *developers* using Claude Code, Copilot, Codex and similar tools. [code] High

**Bottom line for Trinity Roots:** a 19→20 upgrade is a **porting project, not a version bump**, for any customer with custom modules. The four cost drivers are security files, front-end JavaScript, renamed fields/models, and changed accounting/HR data models. Odoo ships automated code rewriters (`odoo-bin upgrade_code`) that handle a meaningful share of the mechanical work.

**ESG gap:** CE 20 is a capable, free core for AgriTech and FoodTech companies (lots, expiry, by-products, POS, eCommerce, offline field use), but **it has no ESG or carbon-accounting capability** beyond a per-vehicle CO₂ figure. That gap is a product opportunity (Part 7.2).

---

## Part 1: Context and method

### 1.1 Odoo's release model

Odoo releases one *major* version a year (the "x.0" branches, usually announced at Odoo Experience in September or October) and several *online-only* SaaS versions in between. Version 20.0 is the cumulative merge of `saas-19.1 … saas-19.4` plus 20.0-specific work. That is why many "new in 20" items are, strictly speaking, new since 19.0, having first appeared in Odoo Online (the SaaS product) months earlier. The release date of September 2026 is stated by third-party sources [web]. The 20.0 branch exists and was receiving fixes on 3 October 2026 [code].

### 1.2 Community vs Enterprise

| | Community (this study) | Enterprise |
|---|---|---|
| Licence | LGPL-3, source on GitHub | Proprietary, separate repo, subscription |
| Scope | Framework, web client, ~34 apps, 229 localisation modules | Adds ~300+ modules on top of CE |
| Examples absent from CE [code: confirmed absent] | Full Accounting reports and the bank-reconciliation widget, Assets, Budget, Studio, Payroll, Planning, Appraisal, Helpdesk, Field Service, Documents, Sign, Subscriptions, Rental, Quality, PLM, Shop Floor, IoT Box, AI agents, Barcode app, carrier connectors (DHL/FedEx/UPS…), mobile app shell | |

In CE the accounting app is **"Invoicing"**. It includes the full double-entry engine (journals, taxes, payments, multi-currency, lock dates, the report *data model*), but the rich financial-report UI and reconciliation widget are Enterprise ([04](areas/04-accounting-finance.md)).

### 1.3 Method

- Both branches were shallow-cloned on 2026-10-03 (`20.0` @ `b100a87`, `19.0`).
- Every `__manifest__.py` was parsed to build the [catalogue](01-module-catalog.md) and the [CSV](data/module_catalog_19_vs_20.csv). Change intensity per module = files that differ ÷ files in the module.
- Ten study agents each took one functional area and diffed the two trees: models, fields, views, controllers, JS and manifests. They traced every removed module to its successor and recorded file-level evidence. The shared instruction set is in [`data/agent-brief.md`](data/agent-brief.md).
- The orchestrator re-verified headline claims directly against the code before writing this paper, for example: `ir.access` model and CSV format, Python minimum 3.12, HTTP default bind, Owl version, removal of `stock.scrap`/`hr.leave.type`/`account.group`, POS dependency list, and the pricelist `compute_price` values.

### 1.4 Limitations (read before relying on this)

- **No commit history** (shallow clone), so changes are inferred from tree differences, not commit messages.
- **Official release notes and documentation on odoo.com were not reachable** from the study environment. A third-party summary [web] made several claims. Each was tested against code:
  - Record rules replaced by domains on access rights: ✅ confirmed.
  - Parent accounts replace account groups: ✅ confirmed.
  - Offline record editing: ✅ confirmed.
  - "Account codes become optional": ⚠️ not a change (`code` was already non-required in 19).
  - Depreciation models: ❓ EE-only, cannot verify.
  - AI agents / MCP: ❌ not in CE.
- **Data migration scripts** for Odoo's upgrade service are not public. Where this paper says "data is preserved", that is an inference.

---

## Part 2: The platform (what developers and architects must know)

*Source: [01 framework](areas/01-framework-core.md), [02 web/UI](areas/02-web-ui-technical.md)*

### 2.1 Security: `ir.access` (the headline change)

In Odoo ≤ 19, access was two layers:
- `ir.model.access` (CSV): "group G may read/write/create/delete model M".
- `ir.rule` (XML): "…but only records matching domain D". Global rules were AND-ed, group rules OR-ed.

In Odoo 20 both are a single model, **`ir.access`** [code: `odoo/addons/base/models/ir_access.py`]:

```csv
id,name,model_id,group_id/id,operation,domain
access_decimal_precision_config,decimal.precision configuration,decimal.precision,base.group_system,ru,
ir_attachment_public_rule,read public attachments,ir.attachment,base.group_user,r,"[('public', '=', True)]"
```
*(real lines from `odoo/addons/base/security/ir.access.csv`)*

- `operation` is a subset of the letters `c r u d`.
- A row **with a group is a permission**: permissions are OR-ed.
- A row **without a group is a restriction**: restrictions are AND-ed. This is the equivalent of the old global rules.
- A new domain operator `'access'` lets a domain say "records the user may access".
- `res.groups.access_ids` lists the access rows of a group.
- APIs such as `check_access_rights`, `check_access_rule` and `_filter_access_rules` (deprecated in 18/19) are removed. Use `check_access()` / `has_access()` / `_filtered_access()`.
- A migration script `odoo/upgrade_code/19.4-00-ir-access.py` rewrites old CSV and XML automatically.

**Why it matters:** every custom module ships security files, so every custom module must be converted. The script handles the syntax. A human must still re-validate the *semantics*, especially modules that combined global rules with group rules: test with real users per group.

### 2.2 Python, ORM and API

| Change | Impact |
|---|---|
| Python **≥ 3.12** (≤ 3.14); PEP 695 syntax; `pypdf` replaces PyPDF2; `xlrd`, `xlwt` and `pytz` dropped | Ubuntu 22.04 and Debian 11 images are out. Rebuild Docker/OS baselines. |
| SQL generation rewritten around `TableSQL`/`FieldSQL`; `Query` moved to `odoo.orm.query`; new `compute_sql` field attribute; `osv.expression` removed | Custom overrides of `_condition_to_sql`, `_order_to_sql`, `_read_group_*` need manual porting. |
| Dict-returning `read_group` removed (a new tuple-returning `read_group` exists; `_read_group` and `formatted_read_group` remain) | Reporting code and controllers break. |
| Removed: `toggle_active`, `_check_recursion`, `api.deprecated`, `registry.clear_cache`, `get_param`/`set_param` (replaced by typed `get_str`/`get_int`/`get_bool`), and the `<>` / `==` domain operators | Mostly mechanical fixes. |
| `odoo/http.py` became the package `odoo/http/`; **default `http_interface` = 127.0.0.1**; bearer scope mandatory on the JSON-2 API (`/json/2`, module `rpc`) | Deployments without a reverse proxy that relied on 0.0.0.0 will become unreachable. Set the interface explicitly. |
| `res.bank` removed; `res.partner.bank` denormalised (`account_number`, `holder_name`); IBAN and VAT checks moved into `odoo/tools` and `base` | Bank data, imports and integrations must be remapped. |
| CLI: new `populate` addon (data "blueprints") and a `duplicate` command; `module list`, `--dry-run`, `--db-system`, `--gevent-workers` | Better tooling for test databases and staging copies. |
| Core test modules consolidated (24→15: `test_base`, `test_web`, `test_tests`…) | CI scripts referencing `test_orm` etc. must change. |

**Automated rewriters (`odoo-bin upgrade_code`).** Scripts in `odoo/upgrade_code/` cover:
- ir.access
- ormcache-on-transaction
- `t-call` changes
- base64 → bytes in XML
- `_rec_names_search` tuple form
- search date filters
- account groups
- the **Owl 3 migration**

Run them first on any custom codebase.

### 2.3 Web client: Owl 3, offline, and UI

- **Owl 3.0.0-alpha.49** replaces Owl 2.8.4, with a compatibility layer in `web/static/src/owl2/`. Many services became *plugins* (web, POS and tours all follow this pattern). Shipping an *alpha*-tagged framework in a stable release is unusual. Expect point-release churn in JavaScript behaviour during 20.0's first months (Medium risk).
- **Removed from the default bundles:** jQuery, legacy `publicWidget`, QUnit (tests move to *Hoot*), and FontAwesome. **Material Symbols** replace the icons, with a mapping shim for `fa-*` classes.
- **Offline mode (CE)** lives in `web/static/src/core/offline/offline_plugin.js`. Visited views and records are cached in **encrypted IndexedDB** (key from `session.browser_cache_secret`). `web_save` and `web_unlink` calls are queued while offline and replayed on reconnect, with a service worker and an offline page. Offline search only covers what was cached. This needs HTTPS (a secure browser context).
- **PWA share target:** files or text shared from a phone into Odoo (for example, a photo into a CRM lead).
- **New `card` view arch** in kanban (used in project, mrp, stock, maintenance). New widgets include `badges_selection`, `relative_date` and `many2one_binary`.
- **Spreadsheet 20.0.1:** datasource-based charts, saved dashboard filters.
- **Calendar:** new multi-calendar model (`calendar.calendar`, `calendar.user`) with per-calendar Google/Microsoft sync and sharing roles.
- **Reports:** engine-neutral API (`get_pdf_engine_state`, `_run_pdf_engine`). wkhtmltopdf stays the default via auto-installed `base_report_wkhtmltox`. **Paper Muncher** is the new optional engine, and POS and Marketing Card receipts/images are now rendered server-side through it.
- **IoT:** `iot_base` and `iot_box_image` are removed from CE. `iot_webserial` (browser Web Serial for scales) and `printer` are new. The IoT Box is Enterprise only.

### 2.4 AI in Odoo 20: what is (and is not) in CE

- **No `ai*` module, no LLM/MCP code, and no AI action in automation rules** in CE [code]. The only trace is a reference in the Owl 3 migration script to an `ai` module living outside this repository, which suggests an Enterprise/IAP module.
- Third-party sources describe agents that create records from PDFs, run from automated actions, connect over MCP, and consume IAP credits [web]. **Treat these as Enterprise/SaaS features.**
- **What CE does have, and what is useful to Trinity Roots:**
  - **`skills/`** at the repo root: Odoo's official *agent skills* (`odoo-guidelines`, `odoo-review`, `odoo-security`, `odoo-web-guidelines`), designed to be copied into `.claude/skills/` or `.agents/skills/`. Install them in our own AI-assisted development setup immediately. They encode Odoo's house rules for review and security.
  - **`llms.txt` editor** in Website (SEO for AI crawlers) and a JSON-LD structured-data mixin.
  - The **JSON-2 API** (`rpc` module), the supported way to connect an external agent or MCP server you build yourself to a CE database.

---

## Part 3: The business apps

### 3.1 Accounting / Invoicing ([04](areas/04-accounting-finance.md))

**What CE 20 gives you:**
- Customer and vendor invoices, credit notes, payments, payment terms, taxes (including Python-coded taxes), fiscal positions, multi-currency, lock dates and audit trail.
- Analytic accounting, cash rounding, Peppol/UBL e-invoicing, QR-code payments, and online payment providers.
- **What it lacks:** the Enterprise financial-reports UI and reconciliation widget.

**What changed:**
- **Chart of accounts hierarchy:** `account.group` is gone. Accounts now have `parent_id`, `parent_path`, `code_path` and `name_path`, so a chart is a *tree of accounts* (parents may be inactive). Customers who grouped accounts for reporting must have groups mapped to parent accounts. The Thai chart `l10n_th` never used groups, so there is nothing to convert at the template level.
- **Bank accounts:** `res.bank` is removed. `acc_number` → `account_number` and `acc_holder_name` → `holder_name`. IBAN logic moves to `odoo/tools/bank_account_number.py`.
- **Tax engine:** a per-document `document_tax_mode` (tax-included vs tax-excluded on each document), with changed `compute_all` signatures. Custom tax code will break.
- **Payments:** providers use `is_live`/`active` instead of `state`, each payment method belongs to one provider, and webhooks are processed asynchronously through a `payment.data` queue with bus-driven status updates. New `account_payment_custom` auto-confirms wire transfers.
- **E-invoicing:** Peppol identifiers are generalised (`routing_scheme`, `routing_endpoint`). `account_peppol_response` and `account_add_gln` are merged in, and `account_peppol_advanced_fields` is dropped.
- **VAT:**
  - Offline format checks are in `base`.
  - Online EU VIES validation is a separate new module, `l10n_eu_account_vies`.
- **Other changes:**
  - Journal groups are inverted (`included_journal_ids`).
  - `review_state` replaces the `checked` flag.
  - Self-billing support.
  - Draft-duplicate detection.
- **Inventory valuation & closing** (perpetual vs periodic, closing entries, accrual accounts "bills to receive / billed not received") now live in **core `account`**. There is a new `account.stock.valuation.report`.

### 3.2 Sales, CRM and Product ([05](areas/05-sales-crm-product.md))

- **Pricelists rewritten:** each rule is a *discount*, *markup* or *fixed price*, with margin bounds, per-UoM rules and an `is_plain_discount` flag. `percent_price` is gone. Migration must map old "percentage/formula" rules.
- **Quotation templates:**
  - Reusable section templates.
  - Sharing restricted by team.
  - Template lines can carry prices, discounts, taxes and attributes.
  - No opt-in group any more.
  - `require_payment` is replaced by `prepayment_amount`.
- **`sale` absorbs** delivery status, incoterm, re-invoicing (`expense_policy` → `reinvoice_policy`), a company-level invoicing policy, accruals and overage invoicing. A **new Sales dashboard** (To Confirm / Deliver / Invoice / Upsell) replaces sales-team invoiced targets.
- **UoM and packaging:** `uom.rounding` is removed. **Packagings are now UoMs** (including variant-level `extra_uom_ids`), and there is a base-unit price (price per kg or litre: useful for food and agri goods).
- **Customer portal returns** (`return.reason`, return labels) in `sale_stock`.
- **Loyalty:** FIFO point expiry, and programs limited to once per user.
- **CRM:**
  - One-click convert-to-opportunity (the wizard is removed).
  - Assignment rules.
  - `crm_sale_project` (create projects from opportunities).
- **New bridges:** `sale_project_margin`, `website_partnership` (partner programme pages), and `purchase_alternative_sale`.
- `mysubscription` is **not** subscription billing. It is a dashboard of the database's own Odoo plan and IAP credits. Recurring invoicing is still Enterprise.

### 3.3 Inventory, Purchase, Manufacturing ([06](areas/06-supply-chain-mrp.md))

- **Batch, wave and cluster transfers are in core `stock`** (enable via a setting). `stock_picking_batch` and `delivery_stock_picking_batch` are gone.
- **Scrap = a `stock.move` with `is_scrap`**, reason tags and optional automatic replenishment. The `stock.scrap` model is deleted.
- **`product_uom` → `uom_id`** on quants, lots, moves, BoMs, MOs, work orders, purchase lines and repairs. This is the single most pervasive rename.
- **Product tracking:** `tracking='none'` is gone (use `False`), and there is a new `store_by` field. `is_storable` moves to `product`.
- **Reordering:** reordering rules can **suggest min/max from demand history** (`daily_demand`, `min_max_based_on`).
- **Reports:** the reception report becomes an **allocation report**.
- **Purchase:**
  - Accrual accounts.
  - Bill-matching ratio and tags.
  - **Alternative RFQs** split into `purchase_alternative` (+ `_stock`, `_sale`).
- **Repair:**
  - No "Under Repair" state.
  - Service lines.
  - Direct invoicing.
- **Maintenance:**
  - Explicit request state.
  - Multiple technicians.
  - Per-equipment properties.
  - `fleet_maintenance` bridge.
- **MRP:**
  - Continuous-flow BoM flag.
  - BoM `extra_cost`.
  - Work-order `cost_mode` (actual or estimated).
  - Several lots per MO.
  - **BoM consumption policy (flexible/warning/strict) is no longer exposed in CE** (Medium confidence: verify before promising it).
- **Landed costs** are allowed regardless of costing method.
- `stock_fleet` is renamed **Transport Management** (CMR report). `stock_delivery` now requires `printer`.

**For process manufacturers (sugar, food, agri-processing):**

| Need | CE 20 answer |
|---|---|
| Batch traceability (cane lot → raw sugar → refined → bags) | Lot tracking, multiple lots per MO (`lot_producing_ids`), full up/downstream traceability |
| Shelf life | `product_expiry` (expiry, best-before, removal and alert dates); FEFO removal; `mrp_product_expiry` |
| Co- and by-products (molasses, bagasse, filter cake) | By-products with cost share on the BoM |
| Continuous process lines | BoM `continuous` flag, work centres with capacity/OEE/cost per hour |
| Yield loss | Scrap moves with reason tags; unbuild for rework |
| Costing | AVCO for commodity inputs; standard cost for finished goods; `extra_cost` on BoM for energy/labour; WIP via `mrp_account` |
| Sell by weight and pack | Packaging-as-UoM, base-unit price (per kg) |
| Quality checks | **Not in CE** (Enterprise `quality_control`). Use lots plus custom properties, or an OCA module |
| Shop floor tablet UI, MPS, PLM | **Enterprise** |

### 3.4 Point of Sale ([07](areas/07-point-of-sale.md))

- **POS is decoupled from Inventory.**
  - `point_of_sale` now depends on `account`, `product`, `resource`… but **not `stock`**.
  - The new auto-install `pos_stock` holds pickings, lots, warehouses, ship-later and COGS.
  - A café or kiosk can run POS without Inventory.
- **Hardware:**
  - The IoT Box is gone from CE.
  - Printers are **Epson ePoS over the network only** (needs HTTPS and the browser's Local Network Access permission).
  - Scales connect via **Web Serial** (Chromium browsers).
  - The cash drawer opens via the printer.
- **Offline mode rebuilt:**
  - Data is held in IndexedDB per POS config, with a write queue.
  - Paid orders are persisted immediately.
  - As of the latest commit, POS asks the browser for *persistent storage* so the data is not evicted.
  - **Operational rule:** never clear browser data before the device has re-synced.
- **Session accounting:**
  - Each session has a bank statement, with split sale/refund/correction entries.
  - Optional **daily closing mode** via cron (Medium confidence: the closing hour appears to be compared in UTC, so test it for Bangkok/HK timezones).
  - Orders are invoiced singly or globally, and invoice PDFs are deferred.
- **Receipts are rendered server-side** from QWeb templates (custom v19 OWL receipt templates must be rewritten).
- **Payments:** a provider model with a new `external_qr` type (Bancontact Pay, Wero). This matters for Thai PromptPay and Indonesian QRIS patterns (see `l10n_id_pos_self_order_qris`).
- **Restaurant and self-order:**
  - A JSON floor plan with a new editor.
  - Courses.
  - Self-order **delivery presets**, product snoozing, SMS receipts and event tickets.
- **Employee roles (`pos_hr`):** a four-level role matrix (supervised / restrictive / cashier / manager).

### 3.5 Website, eCommerce, Events, Marketing ([08](areas/08-website-ecommerce-marketing.md))

- **eCommerce consolidation:**
  - Wishlist, product comparison, back-in-stock alerts, donations, an availability display and a new **withdrawal-request (right of withdrawal) form** are all inside `website_sale`.
  - Six `website_sale_*` modules are removed.
  - Address autocomplete becomes generic (`website_address_autocomplete`).
- **Website builder:** 48 new snippets on `html_builder`, and legacy front-end libraries removed (custom themes need porting).
- **SEO:**
  - JSON-LD structured data across apps.
  - An **`llms.txt` editor**.
  - Header-search settings.
  - A cookie-policy page.
- **Email marketing:** templates (`is_template`) replace "favorites", multiple saved filters, and a new email builder.
- **Events:**
  - Multi-entry tickets.
  - Scheduled publishing.
  - Room display screens.
  - A portal "My events" page.
  - `pos_self_order_event` sells tickets at kiosks.
- **Surveys and eLearning:**
  - Survey certificate redesign and scheduled invitations.
  - Digest KPIs for events, surveys and eLearning.

### 3.6 HR, Project, Services ([09](areas/09-hr-project-services.md))

- **Time Off types are now Work Entry types:**
  - `hr.leave.type` is deleted.
  - `holiday_status_id` → `work_entry_type_id` everywhere.
  - Time off and attendance now depend on `hr_work_entry`.
  - **The `hr.work.entry` records themselves are no longer in CE.** Payroll connectors built on CE work entries must be redesigned.
- **New `hr.time.rule` engine** for overtime and time rules, with compensation into leave. It replaces attendance overtime rulesets. Existing overtime balances need a conversion plan.
- **Attendance:**
  - Validation states.
  - Breaks.
  - Selfie capture at check-in.
  - Automatic check-out at a fixed time.
- **Resource calendars:**
  - `calendar_type` is fixed, variable or undefined.
  - Attendances can recur.
  - Two-week calendars are removed.
  - Flexible-hours setups need re-modelling.
- **Folded into `hr`:** org chart, home-working locations and hourly cost.
- **Other HR changes:**
  - *Contract Type → Employee Type.*
  - Departure becomes a persisted record.
  - Expense limits per job position.
  - A public-holiday loader.
- **Project:**
  - Stage "rotting" (stalled-task signal).
  - A Time-by-Stage report.
  - Collaborator `access_mode`.
  - Margin per project (`sale_project_margin`).
  - Timesheet billing via `billable_type` / `reinvoice_move_id`.

### 3.7 Communication and collaboration ([03](areas/03-communication-collab.md))

- **Field-change tracking split out:**
  - `mail` still detects and displays changes in the chatter.
  - Structured tracking records (`mail.tracking.value`) live in the new optional **`mail_tracking`** module.
  - It is *not* auto-installed. **Install it on upgraded databases** if any report, integration or audit relies on tracking history.
- **Discuss:**
  - Polls.
  - Bookmarks (replace stars).
  - Read-only channels and channel owner/admin roles.
  - Categories.
  - A call debrief UI (recording storage is not in CE).
- **Activities:** role-based assignment (`res.role`).
- **CC handled natively** on messages.
- **Portal:**
  - Home cards are data records (`portal.entry`).
  - The new `portal_discuss` adds `/my/conversations`.
- **`snailmail`** is no longer auto-installed.

---

## Part 4: Localizations, with a focus on Thailand, ASEAN and Hong Kong

*Source: [10 localizations](areas/10-localizations.md)*

### 4.1 The big picture

- **229 localization modules** in 20.0 (231 in 19.0). **17 are new and 19 were removed.** Most removals were merged into the country's base module, for example:
  - Denmark Nemhandel/OIOUBL → `l10n_dk`
  - Hungary bill reception, Poland bank verification and Romania CPV → their base modules
- **Losses with no CE successor:** Turkey's Nilvera e-invoicing family, `l10n_uy_pos`, and the Philippines BIR 2307 wizard.
- **Core changes ripple into every country:**
  - Charts move from account groups to **parent accounts**, and many ASEAN charts gained hierarchies and depreciation models.
  - `base_vat` folds into `base` (VAT format checks via `stdnum`), and EU VIES goes into `l10n_eu_account_vies`.
  - LATAM identification types are replaced by core `additional_identifiers`.
  - A **generic withholding-tax engine** (`l10n_account_withholding_tax`) is now used by TH, PH, KH and others.
- **New countries:** North Macedonia (`l10n_mk`) and **Myanmar (`l10n_mm`, with MMQR)**.
- **Other new modules:**
  - Pakistan FBR e-invoicing (+ POS).
  - Philippines Senior Citizen/PWD discounts (invoice and sale).
  - India Bill of Entry.
  - Korea sales.
  - Taiwan ECPay on sales.
  - Vietnam e-invoicing of stock pickings.
  - **Indonesia QRIS on self-order kiosks.**
  - Egypt ETA on POS.
  - Greece delivery notes.
  - Belgium POS.
  - Spain eCommerce.
  - France payment (Worldline/CAWL).

### 4.2 Thailand (`l10n_th`): substantially rebuilt in v20

Thailand still has **one** module. In v20 it gains a dependency on the generic withholding engine and grows from a chart-plus-QR package into a real tax localization [code: `addons/l10n_th/**`]:

| Area | Odoo 19 | Odoo 20 |
|---|---|---|
| Tax invoice (ใบกำกับภาษี) | Thai-styled invoice layout only | **New `l10n_th.tax.invoice` register** with **gap-free sequences** `TINV/YYYY/#####` and `RCT/YYYY/#####`. Under **cash-basis VAT** (services), one *Receipt/Tax Invoice* is issued **per (partial) payment**. Cancelled automatically when the invoice or payment is reversed. Enabled by the company flag "VAT Registered". |
| VAT taxes | 6 | 10: adds 7% **on-payment VAT for services**, non-deductible input VAT, and P.P.36 reverse charge (inactive by default) |
| Withholding tax (หัก ณ ที่จ่าย) | Negative taxes deducted **on the bill** | **38 of 48 taxes flagged as withholding**, covering 15 income types under sections 40(2)–40(8) and PND3/53/54. Applied **at payment time** via "Withhold and Pay". The condition is at-source, gross-up "forever" or "one-time". |
| 50 ทวิ certificate | None | **"50 Tawi" PDF** per payment, plus a **bulk ZIP download** |
| Fiscal positions | None | 5 auto-apply positions (domestic company or individual, foreign entity or individual, government), which swap PND3↔PND53 and 7%→0% |
| Partners | n/a | Title, Thai company type, **branch code** (`TH_BRANCH_CODE`, 00000 = head office) printed as "Branch NNNNN / Headquarter", Thai address layout |
| VAT return | Generic tag report | **"P.P. 30 – VAT Report"** with coded tags |
| PND3/PND53 reports | Basic tax reports existed | **Removed** (only the 50 Tawi remains), which is a regression for filing |
| Credit/debit notes | n/a | "Original amount / Correct amount" block as required for ใบลดหนี้/ใบเพิ่มหนี้ |
| PromptPay | EMV QR | Same, relabelled "PromptPay QR Code", with its own settings block |

**Upgrade warning (High importance).** `l10n_th` ships **no migration scripts**, and its version number is unchanged. Existing v19 Thai databases therefore **keep their old taxes**: no WHT flags, no fiscal positions, no service on-payment VAT and no tax-invoice sequences. Reloading the chart template does not overwrite taxes already in use. Every Thai upgrade needs a planned remapping, and possibly a backfill of tax-invoice records for audit purposes. WHT also moves from bill time to payment time, which changes aging reports, "net payable" expectations and posting dates. Train both accountants and customers on this.

**What a Thai partner must still build or source in CE 20** (full table: [10-localizations §8](areas/10-localizations.md)):

1. **e-Tax Invoice & e-Receipt** (Revenue Department / ETDA, signed XML/PDF-A3). There is nothing in CE. Vietnam, Malaysia, Indonesia, Singapore, Taiwan and Pakistan *do* have authority connectors in CE; **Thailand does not**.
2. **PND 1/2/3/53/54 returns and e-filing exports.** The data exists on the WHT payment lines, but there is no report.
3. **Sales and purchase tax registers** (รายงานภาษีขาย/ซื้อ) in the Revenue Department layout, and P.P.30/P.P.36 e-filing.
4. **Branch-level tax invoice numbering.** Sequences are per company, so branches must be modelled as companies or extended.
5. **Payroll / SSO / provident fund / PND1** (Payroll is Enterprise only).
6. **Thai bank statement formats, bulk payment files, bill-payment QR (Ref1/Ref2)**. Only the PromptPay credit-transfer QR exists.
7. **Thai payment gateways** (2C2P, Opn). PromptPay is available via the Stripe, Adyen and Xendit providers.
8. **POS abbreviated tax invoice** (ใบกำกับภาษีอย่างย่อ). There is no `l10n_th_pos`.
9. **Depreciation models and hierarchy for the Thai chart** (still flat), Thai geodata (sub-district/postcode), Buddhist-era dates, DBD financial statements and XBRL, and import customs entries.

> **Pre-sales line:** "Odoo 20 CE for Thailand gives you VAT, a compliant tax-invoice register, withholding at payment with 50 Tawi certificates, and PromptPay. Revenue Department e-filing, e-Tax and payroll are Trinity Roots' add-ons." This is also Trinity Roots' **intellectual property moat**: a well-built Thai e-Tax plus PND/P.P.30 pack for v20 is a sellable product.

### 4.3 ASEAN and Hong Kong at a glance

| Country | CE 20 highlights | Authority connector in CE |
|---|---|---|
| Vietnam | Chart 218→301 accounts with hierarchy; VietQR; SInvoice refactor; **NEW e-invoicing of stock pickings** | ✅ Viettel SInvoice |
| Indonesia | Chart 114→199; fiscal positions; **NEW QRIS on kiosks** | ✅ e-Faktur Coretax |
| Malaysia | Chart 77→239; e-invoicing now **auto-installs with `l10n_my`**; consolidated invoices; POS customers can request an e-invoice from a receipt via the portal | ✅ MyInvois |
| Philippines | Chart 104→166; 50 WHT taxes; BIR CAS invoice; **NEW SC/PWD discounts**; *2307 wizard removed* | ❌ |
| Singapore | IRAS GST codes for PINT-SG; **InvoiceNow/Peppol wired into `l10n_sg`** | ✅ Peppol |
| Cambodia | Chart 106→191; T7001/WT003 forms; KHQR | ❌ |
| Myanmar | **NEW** chart and taxes, MMQR | ❌ |
| Thailand | See 4.2 | ❌ |
| **Hong Kong** | Chart **rebuilt** 76→218 accounts with **6-digit codes and new XML IDs**; 7 depreciation models; FPS QR (HKD). There is no VAT, so no tax report | n/a |

**Hong Kong upgrade warning.** Because account codes and XML IDs were rewritten, an existing HK company is **not remapped in place**. Treat a 19→20 HK upgrade as a chart re-coding exercise. HK payroll/MPF and profits-tax filing are not in CE.


---

## Part 5: What is *not* in Community 20 (decision table)

| Need | CE 20 | Typical route |
|---|---|---|
| Financial statements UI, bank reconciliation widget, follow-ups, assets, budgets | ❌ (data model only) | Odoo EE Accounting, or OCA `account-financial-reporting` / `account-reconcile` (check 20.0 port status) |
| Payroll (Thai SSO, PND1) | ❌ | EE (country-dependent) or local partner module |
| Quality control, PLM, MPS, Shop Floor | ❌ | EE or OCA `manufacture` repo |
| Subscriptions / recurring billing, Rental | ❌ | EE or OCA `contract` |
| Barcode app (mobile scanning UI) | ❌ (barcode *fields* and nomenclature are in CE) | EE |
| IoT Box | ❌ (Web Serial scales and ePoS printers only) | EE |
| AI agents, MCP, document AI | ❌ | EE/IAP, or build on JSON-2 API |
| Studio (no-code) | ❌ | EE |
| ESG / carbon accounting | ❌ (only fleet CO₂ g/km) | Custom or third party: **product opportunity** |
| Helpdesk, Field Service, Planning, Appraisal, Documents, Sign | ❌ | EE |

---

## Part 6: Upgrade playbook 19 → 20 (for Trinity Roots projects)

### 6.1 Effort drivers, ranked

| # | Driver | Who | Effort |
|---|---|---|---|
| 1 | Security files → `ir.access.csv`; re-test per role | Dev + QA | Medium (script-assisted) |
| 2 | Custom JS (Owl 3, no jQuery/publicWidget, services→plugins, Hoot tests) | Front-end dev | **High** for JS-heavy customers (POS, website themes) |
| 3 | Field/model renames: `product_uom`→`uom_id`, `holiday_status_id`→`work_entry_type_id`, `acc_number`→`account_number`, `expense_policy`→`reinvoice_policy`, pricelist fields, `checked`→`review_state`… | Dev | Medium; also affects Studio views, server actions, reports, BI SQL |
| 4 | Removed models: `account.group`, `res.bank`, `stock.scrap`, `hr.leave.type`, `hr.work.entry` (CE), overtime tables, attribute exclusions, CRM conversion wizard | Functional + Dev | Medium–High (data mapping decisions) |
| 5 | Removed module names in `depends` (`base_vat`, `base_iban`, `stock_picking_batch`, `website_sale_wishlist`, `hr_org_chart`, `iot_base`…) | Dev | Low |
| 6 | ORM internals (`read_group`, SQL API, `get_param`) | Senior dev | Low–High depending on code |
| 7 | Infra: Python 3.12 image, `http_interface`, report engine module installed, HTTPS for offline/POS printers | DevOps | Low |
| 8 | Hardware: IoT Box customers on CE | Functional + customer | **High impact**: needs EE IoT or ePoS/Web Serial replacement |

### 6.2 Recommended sequence

1. **Inventory:** list custom modules; grep for the removed or renamed items in §6.1.
2. **Automated rewrite:** `odoo-bin upgrade_code` on a branch, then commit.
3. **Manual porting:** ORM/SQL internals, then JS (run `owl3-migration.py` first), then reports and receipts.
4. **Test upgrade:** run the database through Odoo's upgrade service (or OpenUpgrade when 20.0 is supported) on a copy.
5. **Functional regression:**
   - Accounting: CoA tree, taxes in included/excluded mode, payments and webhooks, Peppol.
   - Stock: valuation closing.
   - POS: session close and daily mode.
   - HR: time off, overtime and calendars.
6. **Security regression:** log in as each role and confirm what they can and cannot see.
7. **Post-upgrade installs:**
   - `mail_tracking`, if tracking history matters.
   - `l10n_eu_account_vies`, for EU clients.
   - Confirm `base_report_wkhtmltox` and `pos_stock` are installed.
8. **Go-live hygiene:** POS devices fully synced before the switch, browser storage persistence granted.

### 6.3 Timing advice

- Odoo's practice is that major versions stabilise over the first 3–6 months. The `20.0` branch was still landing `[FIX]` commits daily at the time of study, and it ships an *alpha*-tagged Owl 3.
- **Recommendation:** start new implementations on 20.0 now. Schedule upgrades of complex, JavaScript-heavy 19.0 customers for **Q1–Q2 2027**, unless a specific v20 feature justifies earlier work (offline field use, POS without stock, the time-rules engine).
- Odoo supports the last three major versions. 17.0 customers should be planned onto 19 or 20 in 2027.

---

## Part 7: Strategic implications

### 7.1 For Trinity Roots (Odoo implementation partner)

- **New service lines CE 20 enables:**
  - *Offline field operations*: farm, plantation and depot staff working in low-connectivity areas.
  - *POS-only retail/F&B* without Inventory overhead.
  - *Server-rendered receipts and labels* (ZPL product labels, CMR transport docs).
- **Upgrade revenue:** §6.1 shows that every customer with custom modules needs real porting work. Productise a fixed-scope "19→20 readiness assessment" (inventory, then grep, then estimate) using this KB.
- **AI-assisted delivery:** install Odoo's official `skills/` in the team's coding agents. Combine them with the JSON-2 API to build internal tooling. Odoo's own AI is EE/IAP, so a Trinity Roots MCP connector for CE databases is a differentiator (validate the market before building).
- **Risk:** Enterprise keeps moving the line. Account groups, Shop Floor, IoT and AI all show that value increasingly sits in EE. Keep CE-vs-EE GAP analysis current (the existing `odoo-gap-analysis` sales skill targets Odoo 18 and should be refreshed to 20).

### 7.2 ESG and carbon accounting: a gap in CE

- CE has **no ESG, carbon or emission-factor capability**, only the manufacturer CO₂ g/km per vehicle in Fleet. Yet CE already captures the *activity data* a footprint needs:
  - fuel logs and odometers (fleet)
  - purchases by product and vendor (purchase)
  - energy cost lines (account)
  - mileage and travel expenses (hr_expense)
  - production volumes and by-products (mrp)
  - work-location data (hr)
- An **Odoo-native Scope 1/2/3 module** (emission-factor library plus activity-based calculation plus disclosure exports aligned with ISSB S2 / GHG Protocol) is a plausible partner product. Agri-supply-chain customers (for example EUDR traceability of commodity lots) are a natural first market.

### 7.3 Risks and constraints

| Risk | Likelihood | Mitigation |
|---|---|---|
| Early-release instability (alpha Owl 3, daily fixes) | High in first 3–6 months | Pilot on non-critical customers; pin to tested commits |
| Hidden data-migration gaps (models removed without public scripts) | Medium | Always run the upgrade service on a copy; reconcile key balances (stock value, AR/AP, leave balances) |
| Security semantic drift after `ir.access` conversion | Medium | Role-by-role test matrix |
| Customer expectations from marketing (AI, IoT, Shop Floor) that are EE-only | High | Use Part 5 in pre-sales; refresh the GAP-analysis asset |
| Browser-storage data loss in offline POS or web | Low–Medium | Persistent storage, staff training, sync before clearing |
| CE localisation gaps (Thai e-Tax, WHT certificates, payroll) | High for TH clients | See Part 4; budget local modules |

---

## Appendix A: Glossary

- **CE / EE**: Community / Enterprise Edition.
- **saas-19.x**: online-only intermediate releases folded into 20.0.
- **ir.access**: the v20 unified access-control model.
- **Owl**: Odoo's front-end component framework.
- **Hoot**: Odoo's JS test runner (replaces QUnit).
- **JSON-2 API**: v19+ external API (`/json/2/<model>/<method>`) with bearer API keys.
- **IAP**: In-App Purchase credits for Odoo cloud services (SMS, OCR, AI, partner autocomplete).
- **FEFO**: first-expired, first-out.
- **AVCO**: average cost.
- **OCA**: Odoo Community Association (third-party LGPL/AGPL modules).
- **Peppol**: pan-European e-invoicing network.

## Appendix B: Where to go next in this KB

- Need a module's status → [01-module-catalog.md](01-module-catalog.md) or the [CSV](data/module_catalog_19_vs_20.csv).
- Porting a custom module → §6 here, then section 6 ("migration gotchas") of the relevant [area report](areas/).
- Pre-sales for a Thai client → Part 4, Part 5, and [10-localizations.md](areas/10-localizations.md).
