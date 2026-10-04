# Odoo CE vs EE — official edition matrix (app level)

> **`[web]` — NOT code-verified.** Source: `odoo.com/page/editions` (vendor comparison, app/edition level), captured 2026-10.
> This complements the code-verified KB: the `[code]` facts in `STUDY-PAPER.md` / `areas/*` describe what Community actually ships; this file adds the **Enterprise side**, which cannot be read from the public CE source. Treat edition labels here as vendor claims, app-level, not per-feature.

## Enterprise-only apps
Studio · Payroll · Documents · Sign · Quality · PLM · Shopfloor · Barcode · Field Service · Helpdesk · Planning · Appointments · Knowledge · Marketing Automation · Social Marketing · Subscriptions · Rental · Approvals · Appraisals · Referrals · VoIP · IoT · ESG · Amazon Connector

## Enterprise-only — platform & service
- Full Accounting (General Ledger, bank reconciliation, Vendor Bill OCR, budgets, consolidation, financial reports, AI) — CE ships **Invoicing** (full double-entry engine + report *data model*) but not the EE financial-reports UI / reconciliation widget
- Payroll OCR / reimbursement in payslip
- Mobile apps (Android & iOS)
- Hosting · Version upgrades · Unlimited functional support

## In both Community & Enterprise
Invoicing · Expenses · CRM · Sales · Point of Sale · Website Builder · eCommerce · Blog · Forum · Live Chat · eLearning · Inventory · Manufacturing (MRP) · Purchase · Maintenance · Employees · Recruitment · Time Off · Fleet · Email Marketing · SMS Marketing · Events · Surveys · Project · Timesheet · Discuss · To-Do · Calendar

## Notes
- App-level only. For *how much* of a shared app is in CE (e.g. MRP without Shopfloor/PLM/MPS/Quality; Website without Marketing Automation), see the code-verified `areas/*` §5 and each area's `not_in_ce`.
- This matrix is the general Odoo editions page (not version-stamped); align with `l10n_th` specifics in `areas/10-localizations.md` for Thailand (e-Tax, PND reports, Payroll are gaps in CE).
