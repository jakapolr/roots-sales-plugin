# Odoo 20 Community Edition — Knowledge Base

Internal knowledge base for **Trinity Roots** (Odoo partner, Bangkok).
It was built by reading the Odoo source code directly. Snapshot taken **2026-10-03**.

| Item | Value |
|---|---|
| Source studied | [`odoo/odoo`](https://github.com/odoo/odoo), branch `20.0`, HEAD `b100a87` (2026-10-03) |
| Compared against | branch `19.0` (shallow clone, same day) |
| Edition | **Community (CE)**. All 657 modules are LGPL-3. Enterprise (EE) code is not in this repo. |
| Method | 10 parallel agents, one per functional area. Each diffed the 19.0 and 20.0 trees module by module. The orchestrator spot-checked key claims against the code. |
| Evidence tags | **[code]** = verified in the source tree (file paths cited). **[web]** = third-party/online claim, not verified. Confidence: High / Medium / Low. |

## Start here

1. **[STUDY-PAPER.md](STUDY-PAPER.md)**: the long-form study paper. Read this first.
2. **[01-module-catalog.md](01-module-catalog.md)**: every CE module (20.0 plus the ones removed since 19.0), with status NEW / REMOVED / CHANGED, summary and dependencies.
3. Area deep-dives (each has the same 7 sections: scope, catalogue, feature deep-dive, what's new vs 19, removed/merged, migration gotchas, open questions):

| # | Area | File |
|---|---|---|
| 01 | Framework & platform core (ORM, ir.access, HTTP, CLI, Python 3.12) | [areas/01-framework-core.md](areas/01-framework-core.md) |
| 02 | Web client, UI, reports, spreadsheet, IoT, technical addons | [areas/02-web-ui-technical.md](areas/02-web-ui-technical.md) |
| 03 | Discuss, mail, calendar, portal, contacts | [areas/03-communication-collab.md](areas/03-communication-collab.md) |
| 04 | Accounting / Invoicing, payments, e-invoicing | [areas/04-accounting-finance.md](areas/04-accounting-finance.md) |
| 05 | Sales, CRM, product, pricelists, loyalty, delivery | [areas/05-sales-crm-product.md](areas/05-sales-crm-product.md) |
| 06 | Inventory, purchase, manufacturing, repair, maintenance, fleet (incl. a guide for sugar/food process manufacturing) | [areas/06-supply-chain-mrp.md](areas/06-supply-chain-mrp.md) |
| 07 | Point of Sale, restaurant, self-order | [areas/07-point-of-sale.md](areas/07-point-of-sale.md) |
| 08 | Website, eCommerce, events, eLearning, surveys, marketing | [areas/08-website-ecommerce-marketing.md](areas/08-website-ecommerce-marketing.md) |
| 09 | HR, project, timesheets, services (incl. an ESG scan) | [areas/09-hr-project-services.md](areas/09-hr-project-services.md) |
| 10 | Localizations: 229 l10n modules, with deep dives on Thailand, ASEAN and Hong Kong | [areas/10-localizations.md](areas/10-localizations.md) |

## Raw data (`data/`)

- `module_catalog_19_vs_20.csv`: machine-readable catalogue (module, status, files changed, category, app flag, summary, depends).
- `new_in_20.txt`, `removed_in_20.txt`: addon directory diffs.
- `agent-brief.md`: the exact method and instructions given to the study agents, for reproducibility.

## How to refresh this KB

```bash
git clone --depth 1 -b 20.0 https://github.com/odoo/odoo.git odoo20
git clone --depth 1 -b 19.0 https://github.com/odoo/odoo.git odoo19
comm -13 <(ls odoo19/addons) <(ls odoo20/addons)   # new modules
diff -rq odoo19/addons/<module> odoo20/addons/<module>
```
The 20.0 branch still receives fixes. Re-run the catalogue after major point updates.

## Known limitations

- Shallow clones have no git history, so changes are inferred by diffing trees, not from commit messages. Migration scripts for the official upgrade service are not public.
- odoo.com (official release notes and documentation) was blocked from the study environment. Release-note claims were therefore not cross-checked with Odoo S.A.'s own text. Where a third-party claim was tested against code, the result is stated.
- Enterprise features (Accounting reports and reconciliation, Studio, AI agents, IoT, Payroll, Planning, Helpdesk, Field Service, Quality, PLM, Subscriptions, Rental, Documents, Sign, Shop Floor, etc.) are **out of scope** and can only be described as "absent from CE".
