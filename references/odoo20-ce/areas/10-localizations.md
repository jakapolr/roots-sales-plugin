# Localizations (l10n_*) — Odoo 20 CE

Source: `odoo20/` (20.0, HEAD b100a87) vs `odoo19/`. Claims tagged [code] were verified by reading/diffing the two trees; [web] = not used (no web cross-check done); items marked "inference" are reasoned, not proven. Paths are relative to `odoo20/` unless stated.

## 1. Scope

- 229 `addons/l10n_*` modules in v20 (231 in v19): 17 new, 19 removed (net −2). Some "removals" are folds into a sibling module, not lost features (section 5).
- Of the 229: 127 are chart-of-accounts modules (category "Account Charts"), ~47 are EDI/e-reporting modules, ~28 are POS-specific modules, 19 are cross-country helpers (name-matched counts).
- Deep dive: Thailand `l10n_th` (+ `l10n_account_withholding_tax`, `account_qr_code_emv`), ASEAN (VN, ID, MY, PH, SG, MM, KH), Hong Kong `l10n_hk`.
- There is no `l10n_la` (Laos), `l10n_bn` (Brunei), `l10n_tl` in v20 (not in v19 either). [code] `ls addons | grep l10n_`
- Payroll localizations (`l10n_*_hr_payroll`) are not in CE at all; only leave-type helpers (`l10n_fr_hr_holidays`, `l10n_in_hr_holidays`) exist. Odoo's payroll is Enterprise. [code: no hr_payroll* in addons/]

## 2. Module catalogue

### 2.1 Country coverage by region

Legend: CoA = module with category "Account Charts"; EDI = e-invoicing / e-reporting / tax-authority submission modules (name-matched; countries served only by the generic UBL/CII/Peppol modules `account_edi_ubl_cii` / `account_peppol` show "-", e.g. AT, DE, NL, BE, NO, SE; many l10n charts depend on `account_edi_ubl_cii`); POS = POS-specific l10n bridge; "New" = module not present in v19. Prefix `l10n_` omitted. Generated from `data/manifests_20.json` vs `manifests_19.json`.

Caveat [background knowledge, not code-verified here]: Mexico CFDI, Brazil NF-e and LATAM e-invoicing (CL/PE/CO/UY/EC) are not in this CE repo (no `l10n_mx_edi*`, no `l10n_br_edi*`), so they are Enterprise or absent. CE ships the chart, taxes, tax-report definitions and, for ~25 countries, an authority connector.


### Europe

| CC | Modules (v20) | CoA | EDI / e-reporting | POS | New in 20 |
|---|---|---|---|---|---|
| AT | at | Y | - | - | - |
| BE | be, be_pos, be_pos_restaurant, be_pos_sale | Y | - | pos, pos_restaurant, pos_sale | be_pos |
| BG | bg, bg_ledger | Y | - | - | - |
| CH | ch, ch_pos | Y | - | pos | - |
| CY | cy | Y | - | - | - |
| CZ | cz | Y | - | - | - |
| DE | de | Y | - | - | - |
| DK | dk, dk_fik | Y | - | - | - |
| EE | ee | Y | - | - | - |
| ES | es, es_edi_facturae, es_edi_sii, es_edi_tbai, es_edi_tbai_pos, es_edi_verifactu, es_edi_verifactu_pos, es_pos, es_website_sale | Y | edi_facturae, edi_sii, edi_tbai, edi_tbai_pos, edi_verifactu, edi_verifactu_pos | edi_tbai_pos, edi_verifactu_pos, pos | es_website_sale |
| FI | fi, fi_sale | Y | - | - | - |
| FR | fr, fr_account, fr_facturx_chorus_pro, fr_hr_holidays, fr_payment, fr_pdp, fr_pdp_pos, fr_pos_cert | Y | facturx_chorus_pro, pdp, pdp_pos | pdp_pos, pos_cert | fr_payment |
| GE | ge | Y | - | - | - |
| GR | gr, gr_edi, gr_edi_delivery_note, gr_edi_e_invoo | Y | edi, edi_delivery_note, edi_e_invoo | - | gr_edi_delivery_note |
| HR | hr, hr_edi, hr_kuna | Y | edi | - | - |
| HU | hu, hu_edi | Y | edi | - | - |
| IE | ie | Y | - | - | - |
| IT | it, it_edi, it_edi_doi, it_edi_sale, it_stock_ddt | Y | edi, edi_doi, edi_sale | - | - |
| LT | lt | Y | - | - | - |
| LU | lu | Y | - | - | - |
| LV | lv | Y | - | - | - |
| MC | mc | Y | - | - | - |
| MK | mk | Y | - | - | mk |
| MT | mt, mt_pos | Y | - | pos | - |
| NL | nl | Y | - | - | - |
| NO | no | Y | - | - | - |
| PL | pl, pl_edi, pl_edi_jst | Y | edi, edi_jst | - | - |
| PT | pt | Y | - | - | - |
| RO | ro, ro_edi, ro_edi_stock | Y | edi, edi_stock | - | - |
| RS | rs, rs_edi | Y | edi | - | - |
| SE | se | Y | - | - | - |
| SI | si | Y | - | - | - |
| SK | sk | Y | - | - | - |
| UA | ua | Y | - | - | - |
| UK | uk | Y | - | - | - |

### Asia-Pacific

| CC | Modules (v20) | CoA | EDI / e-reporting | POS | New in 20 |
|---|---|---|---|---|---|
| AU | au | Y | - | - | - |
| BD | bd | Y | - | - | - |
| CN | cn | Y | - | - | - |
| HK | hk | Y | - | - | - |
| ID | id, id_efaktur_coretax, id_pos, id_pos_self_order_qris | Y | efaktur_coretax | pos, pos_self_order_qris | id_pos_self_order_qris |
| IN | in, in_boe, in_edi, in_ewaybill, in_ewaybill_irn, in_ewaybill_stock, in_hr_holidays, in_pos, in_purchase_stock, in_sale, in_sale_stock, in_stock | Y | edi, ewaybill, ewaybill_irn, ewaybill_stock | pos | in_boe |
| JP | jp, jp_ubl_pint | Y | ubl_pint | - | - |
| KH | kh | Y | - | - | - |
| KR | kr, kr_sale | Y | - | - | kr_sale |
| KZ | kz | Y | - | - | - |
| LK | lk | Y | - | - | - |
| MM | mm | Y | - | - | mm |
| MN | mn | Y | - | - | - |
| MY | my, my_edi, my_edi_pos, my_ubl_pint | Y | edi, edi_pos, ubl_pint | edi_pos | - |
| NZ | nz | Y | - | - | - |
| PH | ph, ph_invoice, ph_sale | Y | - | - | ph_invoice, ph_sale |
| PK | pk, pk_edi, pk_edi_pos | Y | edi, edi_pos | edi_pos | pk_edi, pk_edi_pos |
| SG | sg, sg_ubl_pint | Y | ubl_pint | - | - |
| TH | th | Y | - | - | - |
| TW | tw, tw_edi_ecpay, tw_edi_ecpay_pos, tw_edi_ecpay_sale, tw_edi_ecpay_website_sale | Y | edi_ecpay, edi_ecpay_pos, edi_ecpay_sale, edi_ecpay_website_sale | edi_ecpay_pos | tw_edi_ecpay_sale |
| UZ | uz | Y | - | - | - |
| VN | vn, vn_edi_viettel, vn_edi_viettel_pos, vn_edi_viettel_stock | Y | edi_viettel, edi_viettel_pos, edi_viettel_stock | edi_viettel_pos | vn_edi_viettel_stock |

### Middle East & Turkey

| CC | Modules (v20) | CoA | EDI / e-reporting | POS | New in 20 |
|---|---|---|---|---|---|
| AE | ae, ae_pos | Y | - | pos | - |
| BH | bh | Y | - | - | - |
| EG | eg, eg_edi_eta, eg_edi_pos | Y | edi_eta, edi_pos | edi_pos | eg_edi_pos |
| IL | il | Y | - | - | - |
| IQ | iq | Y | - | - | - |
| JO | jo, jo_edi, jo_edi_pos | Y | edi, edi_pos | edi_pos | - |
| KW | kw | Y | - | - | - |
| LB | lb_account | Y | - | - | - |
| OM | om | Y | - | - | - |
| QA | qa | Y | - | - | - |
| SA | sa, sa_edi, sa_edi_pos, sa_pos | Y | edi, edi_pos | edi_pos, pos | - |
| TR | tr | Y | - | - | - |

### Africa

| CC | Modules (v20) | CoA | EDI / e-reporting | POS | New in 20 |
|---|---|---|---|---|---|
| BF | bf | Y | - | - | - |
| BJ | bj | Y | - | - | - |
| CD | cd | Y | - | - | - |
| CF | cf | Y | - | - | - |
| CG | cg | Y | - | - | - |
| CI | ci | Y | - | - | - |
| CM | cm | Y | - | - | - |
| DZ | dz | Y | - | - | - |
| ET | et | Y | - | - | - |
| GA | ga | Y | - | - | - |
| GN | gn | Y | - | - | - |
| GQ | gq | Y | - | - | - |
| GW | gw | Y | - | - | - |
| KE | ke, ke_edi_tremol | Y | edi_tremol | - | - |
| KM | km | Y | - | - | - |
| MA | ma | Y | - | - | - |
| ML | ml | Y | - | - | - |
| MR | mr | Y | - | - | - |
| MU | mu_account | Y | - | - | - |
| MZ | mz | Y | - | - | - |
| NE | ne | Y | - | - | - |
| NG | ng | Y | - | - | - |
| RW | rw | Y | - | - | - |
| SN | sn | Y | - | - | - |
| TD | td | Y | - | - | - |
| TG | tg | Y | - | - | - |
| TN | tn | Y | - | - | - |
| TZ | tz_account | Y | - | - | - |
| UG | ug | Y | - | - | - |
| ZA | za | Y | - | - | - |
| ZM | zm_account | Y | - | - | - |

### Latin America & Caribbean

| CC | Modules (v20) | CoA | EDI / e-reporting | POS | New in 20 |
|---|---|---|---|---|---|
| AR | ar, ar_pos, ar_stock, ar_website_sale, ar_withholding | Y | - | pos | - |
| BO | bo | Y | - | - | - |
| BR | br, br_sales, br_website_sale | Y | - | - | - |
| CL | cl | Y | - | - | - |
| CO | co, co_pos | Y | - | pos | - |
| CR | cr | Y | - | - | - |
| DO | do | Y | - | - | - |
| EC | ec, ec_sale | Y | - | - | - |
| GF | gf | Y | - | - | - |
| GP | gp | Y | - | - | - |
| GT | gt | Y | - | - | - |
| HN | hn | Y | - | - | - |
| MQ | mq | Y | - | - | - |
| MX | mx | Y | - | - | - |
| PA | pa | Y | - | - | - |
| PE | pe, pe_pos | Y | - | pos | - |
| RE | re | Y | - | - | - |
| UY | uy | Y | - | - | - |
| VE | ve | Y | - | - | - |
| YT | yt | Y | - | - | - |

### North America

| CC | Modules (v20) | CoA | EDI / e-reporting | POS | New in 20 |
|---|---|---|---|---|---|
| CA | ca | Y | - | - | - |
| US | us, us_account | Y | - | - | - |

### Cross-country / generic modules

| Module | Summary | New? |
|---|---|---|
| l10n_account_edi_ubl_cii_tests | Testing the Import/Export invoices with UBL/CII |  |
| l10n_account_withholding_tax | Withholding Tax |  |
| l10n_account_withholding_tax_pos | Withholding Tax on Payment - PoS |  |
| l10n_anz_ubl_pint | Australia & New Zealand - UBL PINT |  |
| l10n_din5008 | DIN 5008 |  |
| l10n_din5008_expense | DIN 5008 - Expenses |  |
| l10n_din5008_purchase | DIN 5008 - Purchase |  |
| l10n_din5008_repair | DIN 5008 - Repair |  |
| l10n_din5008_sale | DIN 5008 - Sale |  |
| l10n_din5008_stock | DIN 5008 - Stock |  |
| l10n_eu_account_vies | VAT VIES Validation | NEW |
| l10n_eu_oss | EU One Stop Shop (OSS) |  |
| l10n_gcc_invoice | Gulf Cooperation Council - Invoice |  |
| l10n_gcc_invoice_stock_account | Gulf Cooperation Council WMS Accounting |  |
| l10n_gcc_pos | Gulf Cooperation Council - Point of Sale |  |
| l10n_latam_check | Checks Management |  |
| l10n_latam_invoice_document | LATAM Document Types |  |
| l10n_syscohada | OHADA - Accounting |  |
| l10n_test_pos_qr_payment | POS QR Tests |  |
Country-level counts worth remembering: the Francophone OHADA block (BF, BJ, CD, CF, CG, CI, CM, GA, GN, GQ, GW, KM, ML, NE, SN, TD, TG) all sit on `l10n_syscohada` (they depend on it, e.g. `l10n_bf` depends `l10n_syscohada`). French overseas (GF, GP, MQ, RE, YT, MC) depend on `l10n_fr_account`. GCC (AE, BH, KW, OM, QA, SA) share `l10n_gcc_invoice`. [code] manifests.

### 2.2 Summary of cross-cutting patterns in v20

| Pattern | Evidence |
|---|---|
| Security files renamed `security/ir.model.access.csv` -> `security/ir.access.csv` (new columns `operation`, `domain`; record rules folded in) | 52 l10n modules ship `ir.access.csv` in v20 vs 50 `ir.model.access.csv` in v19; e.g. `addons/l10n_th/security/ir.access.csv` carries the multi-company rule inline. [code] High |
| `account.group` model gone; charts use `parent_id` hierarchy on `account.account` | 54 `account.group-*.csv` in v19 l10n modules, 0 in v20; `addons/account/models/account_account.py:133` has `parent_id`; v19 line 1515 defined `account.group`. HK/VN/KH charts now have a `parent_id` column. [code] High |
| `base_vat` and `base_iban` modules removed; VAT validation (`check_vat_*`) now in core `res.partner` | `odoo/addons/base/models/res_partner.py:2190` `check_vat_th`; l10n manifests no longer depend on `base_vat`/`base_iban` (l10n_id, l10n_ph, l10n_pl, l10n_cl, l10n_pe, l10n_ec, l10n_hu_edi, l10n_do). [code] High |
| New core `res.partner.additional_identifiers` (JSON) + registry `odoo/tools/partner_identifiers.py` (127 identifier types; TH_VAT, TH_BRANCH_CODE, SG_UEN, MY_EN, HK_BRN, ID_TIN, ID_TKU, PH_TIN...) | `odoo/tools/partner_identifiers.py:435,894`; `odoo/addons/base/models/res_partner.py:331`. Replaces `l10n_latam_base`. [code] High |
| `res.partner.bank.acc_number` -> `account_number`; EMV QR proxy fields relabelled "Account Identifier Type/Value"; `_get_emv_qr_code_names()` hook gives each country's QR its scheme name (PromptPay, FPS, MMQR, ...) | `diff` of `l10n_th/models/res_bank.py`, `l10n_hk/models/res_bank.py`, `addons/account_qr_code_emv/models/res_bank.py`. [code] High |
| Many l10n charts rewritten bigger with parent accounts, depreciation models, fiscal positions | account counts v19 -> v20: VN 218->301, ID 114->199, KH 106->191, MY 77->239, PH 104->166, HK 76->218; depreciation-model CSVs in 35 charts (0 in v19). [code] High |
| Generic Withholding Tax module (`l10n_account_withholding_tax`) reworked and adopted by more countries | dependents 5 (v19) -> 12 (v20): AR (`l10n_ar_withholding`), BD, EG, IN, KH, LK, MM, PH, PK, SA, TH (+ PoS bridge). [code] High |
| Settings views `res_config_settings_views.xml` added in 50 l10n modules (33 in v19) | manifest grep. [code] Medium (cosmetic) |


## 3. Feature deep-dive

### 3.1 THAILAND (`l10n_th`) — v19 vs v20 in detail

**Module inventory.** Thailand has exactly one l10n module, `l10n_th` ("Thailand - Accounting", author Almacom, version 2.0, auto_install with `account`). There is no `l10n_th_pos`, no `l10n_th_edi`/e-Tax, no payroll, no ภ.พ.30 e-filing, no Thai SMS/ID-card integration. Grep for `e-tax|etax|rd.go.th|ETDA` across `addons/` hits only `l10n_id_efaktur_coretax`. [code] High

Dependencies: v19 `account_qr_code_emv, account`; v20 adds `l10n_account_withholding_tax` (the generic WHT-on-payment engine). Also new: `post_init_hook` unchanged (`_preserve_tag_on_taxes`). `addons/l10n_th/__manifest__.py`.

Size of the localization: Python models total 873 lines in v20 (v19: 5 small model files, no wizards/reports/security); 5 test files covering EMV QR, tax invoice (7 scenarios), credit/debit-note PDF, WHT payment condition, partner `is_company`. [code]

**Side-by-side**

| Area | Odoo 19 | Odoo 20 |
|---|---|---|
| Chart of accounts | 145 accounts (6-digit, `code_digits=6`), Thai names in `name@th_TH`, flat (no parents) | 146 accounts; one added: `213304 Tax Withheld - PND 54` (foreign remittance). Descriptions bilingual. Still flat, no `parent_id`, no depreciation models, 13-line `account.asset-th.csv` (Enterprise assets) unchanged. `data/template/account.account-th.csv` |
| Chart-template defaults | same | `template_th.py` sets 20+ defaults incl. `tax_exigibility: True` (cash-basis enabled for the company), `downpayment_account_id`, stock valuation 113100, cash-difference accounts, plus two **no-gap sequences** (see tax invoice) |
| VAT taxes | 6 (7%, 0%, EXEMPT, each input/output), tax groups carry payable/receivable accounts | 6 + 4 new: `tax_input_vat_service`/`tax_output_vat_service` (7% **on_payment** exigibility = deferred VAT for services), `tax_input_vat_nd` (Undeductible input VAT, price-included), `tax_input_vat_rc` (VAT 7% P.P. 36 reverse charge — **inactive by default**). Tax tags now `PP30_sale`, `PP30_sale_zero`, `PP30_sale_exempt`, `PP30_tax_output`, `PP30_purchase_deductible`, `PP30_tax_input`, `PP30_tax_excess`. |
| Fiscal positions | none | **5 auto-apply positions**: Domestic Company (VAT required), Domestic Individual, Foreign Entity, Foreign Individual, Government Entity/State enterprise — each maps VAT and WHT taxes (e.g. the Domestic Company position swaps PND3 WHT taxes for their PND53 twins via `original_tax_ids`; the foreign positions map VAT 7% to 0%). `account.fiscal.position-th.csv`, `account.tax-th.csv` cols `fiscal_position_ids`/`original_tax_ids` |
| Withholding tax (WHT) | 8 ordinary negative-rate purchase taxes (1/2/3/5% x company PND53 / individual PND3) + 4 sale-side "WHT Income" taxes, deducted **on the invoice** (reduces payable immediately); tags `PND3`/`PND53` | **38 taxes flagged `is_withholding_tax=True`** (purchase and sale/creditable), covering 15 income-type categories (40(2) services, commission, 40(3) royalties, 40(4) interest/dividend, 40(5) rent, 40(6) professional, 40(7) contract, 40(8) transport/advertising/insurance/public actor/prize/hire of work, foreign remittance PND54 15%/10% DTA, associations 10%...). Rates 1/2/3/5/10/15%. 16 of the 48 taxes are **inactive by default** (rare ones: interest, royalties, dividends, public actor, prize, PND54, associations...). WHT is now applied **at payment time** via the generic "Withhold" flow (Pay button -> Withhold and Pay / Withhold Only / Payment Only), not at invoice time. New field `l10n_th_income_tax_type` on `account.tax` (required on purchase WHT taxes) drives the certificate. `models/account_tax.py` |
| WHT condition | n/a | `l10n_th_wth_condition` on payment and register wizard: **at_source / forever (gross-up, payer bears always) / one_time (payer bears once)** — the three ภ.ง.ด. conditions (หัก ณ ที่จ่าย / ออกให้ตลอดไป / ออกให้ครั้งเดียว), defaulted `at_source`. Only affects the printed certificate. `models/account_payment.py`, `wizards/account_payment_register.py` |
| WHT certificate (หนังสือรับรองการหักภาษี ณ ที่จ่าย, "50 ทวิ") | none (only PND3/PND53 tax-report lines) | **Report "50 Tawi"** (QWeb PDF, dedicated paper format, forced Thai language fallback to English, amount-in-words via `THB.amount_to_text`). Button "Print 50 Tawi" on paid outbound payments with withholding lines; **bulk list action "Thailand: Print 50 tawi"** zips one PDF per payment (`controllers/download_tawi_reports.py`, route `/l10n_th/download_tawi_reports/<ids>`). `report/report_tawi.xml`, `models/account_payment.py` |
| PND forms (ภ.ง.ด.1/2/3/53/54) | Two tax reports **PND3** and **PND53** (Total Income / Total Remittance / Total) | **Both reports removed**; tags `PND3`, `Income PND3`, `PND53`, `Income PND53` kept in `data/account_tax_tags_data.xml` and the WHT taxes are classified by `l10n_th_income_tax_type` and ATC-like grouping, but **no PND report or RD e-filing export exists in CE 20**. Net: v19 had a (basic) PND3/PND53 view; v20 has only the per-payment 50 Tawi. [code] High; interpretation as a regression = Medium |
| VAT return (ภ.พ.30) | "Tax Report" built from per-line tag names (tags literally named "1. Sales amount") | Renamed **"P.P. 30 - VAT Report"** (Thai `รายงานภาษี`), tags renamed to codes `PP30_*`, adds line code `OUTPUTTAX_TAXABLESALE`; 12 lines (items 1-12 of the form) in 3 sections (Output / Input / Net). `data/account_tax_report_data.xml` |
| **Tax invoice (ใบกำกับภาษี) engine** | Only a Thai-styled invoice report ("Tax Invoice" title) + "Commercial Invoice" action | **New model `l10n_th.tax.invoice`** (draft/posted/cancel) with own **gap-free sequences** `TINV/%(year)s/#####` and `RCT/%(year)s/#####` (receipt/tax invoice), per company, date-ranged. Generated on posting customer invoices/receipts when the company has `l10n_th_is_vat_registered`; for **on_payment (cash-basis VAT)** taxes one Receipt/Tax Invoice is created **per (partial) payment** from the CABA entry (`account.partial.reconcile._create_tax_cash_basis_moves`), with ratio-adjusted lines, `amount_residual`, `is_partially_paid`; cancelled when invoice reset/cancelled/CABA reversed. Mixed on-invoice/on-payment taxes in one invoice and group taxes are handled (tests). Printable via `action_report_tax_invoice` (title "Receipt / Tax Invoice", "Draft"/"Cancelled" prefixes, QR/payment-link blocks suppressed). `models/l10n_th_tax_invoice.py`, `models/account_move.py`, `models/account_partial_reconcile.py`, `tests/test_l10n_th_tax_invoice.py` |
| Credit/debit note layout | n/a | `_l10n_th_get_credit_debit_note_amounts()` prints **"Original Amount / Correct Amount"** reconciliation (ใบลดหนี้/ใบเพิ่มหนี้ requirement) on credit and debit notes, accounting for earlier notes. `models/account_move.py:34-` |
| Invoice report | `report_invoice_document` + separate "Commercial Invoice" report (restricted by `ir_actions_report.py` to invoices) | Thai invoice document kept (`_get_name_invoice_report`), "Commercial Invoice" report and `ir.actions.report` override **removed**; document uses `document_tax_mode` (tax excl./incl., new core field `account.move.document_tax_mode`) and `l10n_th_address_no_country`. `views/report_invoice.xml` |
| PromptPay QR | EMV QR via `account_qr_code_emv`; proxy types **Ewallet ID, Merchant Tax ID (13 digits), Mobile (10 digits, 0 -> 66 prefix)**, AID `A000000677010111`, merchant tag 29, THB only | Same logic; label now **"PromptPay QR Code"** via `_get_emv_qr_code_names`, `acc_number` -> `account_number`, new setting block "PromptPay QR Code" in Accounting settings (`views/res_config_settings_views.xml`, replaces generic QR switch for TH companies). Known cosmetic bug: THB-only error text still says "PayNow" (copy-paste, `models/res_bank.py`). Works for invoice QR and POS "Bank App (QR Code)" payment methods (core POS `bank_qr_code` + `qr_code_method`). |
| Partners | none | `l10n_th_title` (Khun/Mr./Ms./Mrs.), `l10n_th_company_type` (Co. Ltd., Public Co., Limited Partnership, Foundation, Association, Joint Venture, Others), computed **"Branch NNNNN / Headquarter"** from core identifier `TH_BRANCH_CODE` (5-digit, validated in `odoo/tools/partner_identifier_validation.py`), `is_company` forced False when TH VAT does not start with 0 (individual TIN), TH address view (street = "House no. Moo Soi Yaek Road", city = Sub-district/District, state = Province) via `res.country.address_view_id`. VAT format: `check_vat_th` (stdnum `th.tin`) in core. |
| Company | none | `l10n_th_is_vat_registered` (enables tax invoices) |
| Security | none | `ir.access.csv`: tax invoice CRUD for invoicing group, read for readonly, multi-company rule |
| Migrations | none present in either version (`find l10n_th -name migrations` empty) | none — see gotchas |

**How the new Thai flows work (consultant view)**

1. *Company setup*: install `l10n_th`, load the Thai chart, tick "Thailand: VAT Registered" on the company, add the PromptPay bank account (type + value), set company branch via partner identifier `TH_BRANCH_CODE` (00000 = HQ).
2. *Sales*: fiscal position picks VAT 7% / 0% / exempt. Services you only owe VAT on at receipt -> use "Output VAT 7% (Services)" (on_payment). Posting an invoice creates tax invoice `TINV/2026/00001` (on-invoice taxes). For cash-basis lines, each customer payment creates `RCT/2026/0000x` Receipt/Tax Invoice and the VAT moves from the transition account to 213200.
3. *Purchases / WHT*: vendor bill carries the WHT tax (e.g. "WHT 3% (P.N.D. 53) Services", ATC-style type = Services). On Pay, choose "Withhold and Pay", set condition (at source/gross-up), the engine posts WH base/tax lines, WHT payable accounts 213302 (PND3), 213303 (PND53), 213304 (PND54), assigns a withholding sequence number, and "Print 50 Tawi" produces the certificate.
4. *Customer-side WHT*: sale-side "WHT Creditable" taxes (1/2/3/5%, plus professional, commission, insurance, interest, royalties, dividends, government 1%) book to asset account 114300 "WHT Creditable" for credit against corporate income tax.
5. *Reporting*: P.P. 30 VAT report with tag-based lines; **no PND form output**.

**The generic WHT engine (`l10n_account_withholding_tax`)** — author Odoo S.A., depends only on `account`, now used by TH. v19 name "Withholding Tax on Payment" -> v20 "Withholding Tax". Key v20 changes (diff of `models/`): `is_withholding_tax_on_payment` -> `is_withholding_tax` (sign auto-enforced negative; positive amount resets flag); payment gets `withhold` selection (`withhold_pay` / `withhold` / `payment`, default `payment`) replacing boolean `should_withhold_tax`; new computed `withholding_amount`, `withholding_net_amount`; new `account.move` fields `withholding_total_amount_currency`, `withholding_deducted_amount_currency`, `withholding_residual_amount_currency`, `withholding_net_residual_amount_currency` (invoice shows "Net Due" after withholding) and an invoice report block; `amount_residual` redefined to include withholding due; sequences no longer mandatory at line entry (blank sequence ok); `post_init_hook` loads `withholding_tax_base_account_id`; new OWL components in `static/src/components`. Renamed field/column = **migration breakage for any custom module/report referencing `is_withholding_tax_on_payment` or `should_withhold_tax`**. [code] High

### 3.2 ASEAN set

Common: EMV merchant-presented QR for TH, SG, VN, KH, MM, HK (and BR Pix) comes from `account_qr_code_emv` (country adapters + `_get_emv_qr_code_names` naming). `l10n_my`, `l10n_ph`, `l10n_id`, `l10n_vn` and `l10n_sg` all got large chart expansions.

**Vietnam** (`l10n_vn`, `l10n_vn_edi_viettel`, `_pos`, `_stock` NEW)
- Chart 218 -> 301 accounts (parent hierarchy replaces `account.group-vn.csv`), taxes 15 -> 31, tax report updated, VietQR (EMV) retained (`l10n_vn/models/res_bank.py`), new settings view. [code]
- e-invoicing via Viettel **SInvoice** (the only VN provider in CE): v20 refactors API calls into `models/sinvoice_service.py` (`SInvoiceService`: create/lookup/cancel/update payment status/get PDF-XML/list templates/custom fields), adds journal-level default **symbol** (`account_journal.l10n_vn_edi_default_symbol_id`), drops `res_partner_views` and the **cancellation-request wizard** (`l10n_vn_edi_cancellation_request` removed; cancellation now via `cancel_invoice`/reversal flow). Medium confidence on exact replacement.
- NEW `l10n_vn_edi_viettel_stock` (auto-install with `stock`): "Delivery E-invoicing" — send **stock pickings** (phieu xuat kho / internal delivery note) to SInvoice: fields `l10n_vn_edi_is_sent`, `l10n_vn_edi_transaction_id`, `l10n_vn_edi_symbol_id` on `stock.picking`, company/warehouse config, `send_wizard` with template field lines. [code]

**Indonesia** (`l10n_id`, `l10n_id_efaktur_coretax`, `l10n_id_pos`, `l10n_id_pos_self_order_qris` NEW)
- Chart 114 -> 199 accounts, taxes 18 -> 21, **new fiscal positions** CSV, depreciation models, settings view (QRIS toggle), post-init hook, `base_vat`/`base_iban` deps dropped. [code]
- e-Faktur **Coretax** (replaces legacy DJP e-Faktur) unchanged in module name; v20 adds `ir.access.csv`, removes company-scope record rule file, adds `test_l10n_id_is_company` (individual NIK-style partner handling), product/UoM code mapping tweaks.
- QRIS: `l10n_id` bank QRIS fields/tests updated; NEW `l10n_id_pos_self_order_qris` (auto-install): kiosk (self-order) can take **QRIS** — extends `pos.payment.method` (`_is_kiosk_qris`: `bank_qr_code` + `qr_code_method == 'id_qr'`), adds QRIS to the kiosk payment domain, 180 s timeout and a 150 s QR-reuse window to avoid double codes, frontend `payment_qris.js/payment_page.xml`. [code]

**Malaysia** (`l10n_my`, `l10n_my_edi`, `l10n_my_edi_pos`, `l10n_my_ubl_pint`)
- Chart 77 -> **239** accounts, depreciation models, partner override (VAT starting `IG`, i.e. individual TINs, is not treated as a company), tests. MyInvois e-invoice: `l10n_my_edi` now **auto-installs with `l10n_my`**; adds journal dashboard shortcut to MyInvois documents, `res_partner.xml` data (a "General Public" partner, VAT EI00000000010, used when refunding orders inside a consolidated invoice), branch handling (`test_branch.py`), consolidated-invoice wizard reworked, security moved into `ir.access.csv`. `l10n_my_edi_pos` gains portal address page for customers to request an e-invoice from a POS receipt (portal controller + JS `address.js`, receipt validation screen). [code] High
- `l10n_my` tax report data and tax/tag CSVs also changed (not analysed line by line).

**Philippines** (`l10n_ph`, `l10n_ph_invoice` NEW, `l10n_ph_sale` NEW)
- Chart 104 -> 166, taxes 65 -> 99 (**50 now WHT-flagged** via `l10n_account_withholding_tax`; v19 had 0), `l10n_ph_atc` kept on taxes; new BIR **CAS invoice** report (`views/report_invoice.xml`, `l10n_ph_cas_*` tax-group buckets: VATable / zero-rated / VAT-exempt / percentage tax; `test_cas_invoice_report.py`); company `l10n_ph_rdo`, `l10n_ph_is_vat_registered`; partner Filipino name splitting (first/middle/last with Spanish prefixes); disbursement voucher internal template; "Philippines" reports menu.
- **Removed**: `generate_2307_wizard` (BIR Form 2307 certificate generator), `utils.py`, and invoice/payment views that supported it. No successor found in CE (the tax report still mentions Form 2307 as a line). Customers who relied on 2307 PDF/DAT generation must check Enterprise or rebuild. [code] Medium
- NEW `l10n_ph_invoice`: **Senior Citizen / PWD discount privileges** — model `l10n_ph.discount.privilege` (type pwd/sc/special, discount %, fiscal position to switch lines to the SC/PWD VAT-exempt taxes, account, product-category scope), wizard on invoices/credit notes, a shared line mixin storing original taxes/price/discount so the privilege can be reversed; amounts split into regular vs special discount (BIR reporting). NEW `l10n_ph_sale`: the same on quotations/sale orders (extends `sale.order.discount` wizard). [code] High

**Singapore** (`l10n_sg`, `l10n_sg_ubl_pint`)
- Chart/tax data refresh (taxes 41 -> 41, accounts rewritten, depreciation models, tags). **InvoiceNow/Peppol is now wired into `l10n_sg`**: it depends on `account_edi_ubl_cii` + `account_peppol`; post-init triggers the Peppol auto-register-services cron and uninstall de-registers; `account_edi_proxy_user` override auto-registers services for SG receivers (scheme `0195` UEN). `l10n_sg_ubl_pint` now depends on `l10n_sg` and auto-installs (it used to be a standalone dependency on `account_edi_ubl_cii`).
- `account.tax.ubl_cii_tax_category_code` extended with ~40 IRAS **GST codes** (SR, SRCA-S/C, ZR, ES33, ESN33, OS, NG, TX, TXCA, IM, IGDS, BL, NR, TX-ESS ... ) — mandatory classification for PINT-SG; **customer-accounting GST amount** field + SG invoice report additions (`l10n_sg_customer_accounting_gst_amount`, permit number/date). [code] High

**Myanmar** (`l10n_mm` NEW): see 4. **Cambodia** (`l10n_kh`): chart 106 -> 191 accounts, parent hierarchy, tax tables 47 -> 47, forms **T7001 (monthly tax) and WT003 (withholding)** data updated, uses generic WHT module, KHQR (EMV) retained, new settings view. [code] Medium (diff only at file level)

### 3.3 HONG KONG (`l10n_hk`)

- Depends `account_qr_code_emv, account`. Hong Kong has **no VAT/GST**, so the localization has no taxes, no tax report, no EDI — only chart, QR, and (v20) tags.
- v20 changes [code] High: chart **rebuilt from 76 to 218 accounts**, code scheme changed from 2-4 digit codes (`l10n_hk_1240` Account Receivable, `l10n_hk_41` income) to **6-digit** codes (`l10n_hk_120100`, `410100`) with `parent_id` hierarchy (cash group `110000`, `_get_account_parent_xmlid`); chart-template data now uses the 20-style keys (`receivable_account_id`, `payable_account_id`, suspense `110400`, transfer `110700`, cash difference 999001/999002, deferred revenue 210200 / deferred expense 125300); **7 depreciation models** (no depreciation, 3/4-year linear...) and per-asset-account depreciation/expense mapping (150100-160400); new account tags (Income Tax Expense, Finance Costs, Other Comprehensive Income) for the P&L presentation; new settings view for QR.
- **FPS QR** (Faster Payment System): proxy types FPS ID (7 or 9 digits), Mobile (+852-xxxxxxxx), Email; now labelled "FPS QR Code". HKD only.
- Gotchas for HK clients upgrading 19 -> 20: account codes/xmlids changed, so a standard upgrade does **not** remap an existing HK chart; treat as a re-code project (see 6).
- Not in CE: MPF/payroll, profits-tax computation, IRD e-filing (none exist in any Odoo edition as far as this repo shows).

### 3.4 Notable non-ASEAN changes (context)

- **Pakistan** (`l10n_pk_edi`, `l10n_pk_edi_pos` NEW): FBR digital invoicing v1.12, via IAP (`iap`), token in settings, SRO schedule/item models (`l10n_pk_edi.sro`, `.sro.item`), sale types, UoM mapping, product fields, debit-note wizard; POS version adds FBR data to POS orders and receipts (`receipt/pos_order_receipt.xml`).
- **India**: `l10n_in_boe` NEW (Bill of Entry for imports with landed costs); e-invoice/e-waybill/stock GST modules continue (67 file diffs in `l10n_in`, not analysed in detail).
- **Turkey**: `l10n_tr` gains tax office model (`l10n_tr.tax.office.csv`), fiscal positions, stamp-tax tax report, `contacts` dependency; **Nilvera e-invoice/e-dispatch removed** (section 5).
- **Denmark**: Nemhandel/OIOUBL folded into `l10n_dk`.
- **France**: PDP (e-invoicing approved platform, Flux 10 POS e-reporting), CAWL/Worldline branding `l10n_fr_payment`.
- **Spain**: Veri*Factu (+POS), TicketBAI, SII, Facturae; `l10n_es_website_sale` NEW.
- **Greece**: myDATA + e-invoo provider + delivery-note (NEW).
- **Poland**: KSeF FA(3) + JST variant; bank-account whitelist verification merged in.

### 3.5 New l10n modules in 20, explained

| Module | Category / deps | What it does | Key models / files |
|---|---|---|---|
| `l10n_mk` | Account Charts; `account` | North Macedonia: chart (with fiscal positions), tax groups, taxes, tax report (`data/tax_report.xml`) | `models/template_mk.py` |
| `l10n_mm` | Account Charts; `account_qr_code_emv`, `l10n_account_withholding_tax` | Myanmar: chart, taxes, WHT support, **MMQR** (EMV) with 16-digit Merchant ID, terminal ID, merchant name/city in Myanmar Unicode; MMK added to EMV currency map | `models/res_bank.py` (`l10n_mm_terminal_id`, `l10n_mm_merchant_name/city`), `account_qr_code_emv/const.py` |
| `l10n_pk_edi` | EDI; `account_debit_note, iap, l10n_pk, stock_delivery` | Pakistan FBR e-invoicing v1.12: token in settings (sandbox/production), submit via Send & Print, SRO schedules/items, sale type, HS codes, UoM codes, debit notes, FBR data on the invoice PDF (`views/report_invoice.xml`) | `models/l10n_pk_edi_sro.py`, `account_move*.py`, `iap_account.py`, `res_company.py` |
| `l10n_pk_edi_pos` | PoS; `l10n_pk, pos_discount, iap, stock_delivery` | POS orders sent to FBR, receipt layout, payment-method mapping | `models/pos_order.py`, `pos_payment_method.py`, `static/src` |
| `l10n_ph_invoice` | `l10n_ph` | SC/PWD discount privileges on customer invoices/credit notes (see 3.2) | `l10n_ph.discount.privilege`, wizard, line mixin |
| `l10n_ph_sale` | `l10n_ph_invoice, sale` | Same on SO lines, extends `sale.order.discount` | `models/sale_order*.py` |
| `l10n_in_boe` | `l10n_in, stock_landed_costs` | **Bill of Entry** for imports: record BOE with shipping-bill/port code, link receipts, post BOE journal entry, account for customs duty through landed costs | `wizard/l10n_in_boe_wizard.py` (+line), `account_move.action_l10n_in_open_boe_wizard` |
| `l10n_kr_sale` | auto; `sale, l10n_kr` | Korean "proof of issuance" (`l10n_kr_issuance_type`, defaulted from the partner) on SOs, propagated to invoices; orders with different proofs are not merged into one invoice (grouping key) because they are reported in different VAT boxes | `models/sale_order.py` |
| `l10n_tw_edi_ecpay_sale` | auto; `sale, l10n_tw_edi_ecpay` | ECPay e-invoice data (print, love code donation, carrier type/number 1-5, tax ID) on sales orders | `models/sale_order.py` |
| `l10n_vn_edi_viettel_stock` | auto; `l10n_vn_edi_viettel, stock` | SInvoice delivery e-document from pickings (see 3.2) | `stock_picking.py`, `stock_warehouse.py`, wizard |
| `l10n_id_pos_self_order_qris` | auto; `pos_self_order, l10n_id_pos` | QRIS payments at self-order kiosks | `models/pos_payment_method.py`, `static/src/payment/*` |
| `l10n_eg_edi_pos` | auto; `point_of_sale, l10n_eg_edi_eta` | POS receipts submitted to Egypt ETA **eReceipt** API after payment; QR on accepted receipts, "RECEIPT WITHOUT FISCAL VALUE" otherwise; ETA state per order | `pos_order.py`, `pos_config.py`, `static/src/overrides` |
| `l10n_es_website_sale` | `l10n_es, website_sale` | eShop for Spain: simplified invoices (<= `l10n_es_simplified_invoice_limit`) use a dedicated journal (`website.simplified_invoice_journal_id`) and VAT/NIF is optional at checkout below the limit, mandatory above | `website.py`, `sale_order.py`, `res_partner.py` |
| `l10n_fr_payment` | auto; `l10n_fr, payment` | Applies **CAWL / Worldline** branding (name "CAWL (Worldline)" + logo) to Worldline providers of French companies | `payment_provider.py` |
| `l10n_gr_edi_delivery_note` | auto; `l10n_gr_edi, stock, sale, sale_stock` | Transmit Greek **delivery notes** (despatch) to myDATA; reports, partner/company fields | `stock_picking.py`, `l10n_gr_edi.document` extension |
| `l10n_be_pos` | auto; `point_of_sale, l10n_be` | When creating a POS config for a Belgian company, auto-enable cash rounding "Round to 0.05" (cash only) | `models/pos_config.py` |
| `l10n_eu_account_vies` | `account` | Optional VIES online VAT validation (`vat_check_vies`), `vies_valid`, IAP-backed async check with webhook controller, cron; carved out of `base_vat` | `models/res_partner.py`, `controllers/webhook.py` |

## 4. What's new / changed vs Odoo 19

1. **Core partner-identifier framework replaces LATAM identification types and `base_vat`/`base_iban`** — `additional_identifiers` JSON + `odoo/tools/partner_identifiers.py` (127 types incl. TH_VAT, TH_BRANCH_CODE, SG_UEN, HK_BRN, MY_EN, ID_TIN, PH_TIN); `check_vat_*` now in `odoo/addons/base/models/res_partner.py`. Per-country metadata modules (`l10n_ar/tools/partner_identifiers.py` etc. for AR, CL, CO, EC, GT, PA, PE, SA, ES). High
2. **`account.group` removed; charts use account `parent_id`** (all 54 group CSVs gone). High
3. **Thailand localization rebuilt**: tax invoice engine, cash-basis VAT per-payment receipts, WHT at payment (38 flagged taxes, 15 income types), 50 Tawi certificate (+bulk zip), fiscal positions, branch/title/company-type partner fields, P.P. 30 re-tagged; PND3/PND53 reports and Commercial Invoice dropped. `addons/l10n_th/**`. High
4. **Generic Withholding Tax module overhaul and wider adoption** (12 dependents; Myanmar, Pakistan, Egypt, India, Bangladesh, Saudi Arabia, Argentina added; Saudi `l10n_sa_withholding_tax` merged in). `addons/l10n_account_withholding_tax/`. High
5. **17 new modules**: new countries North Macedonia, Myanmar; new e-invoicing for Pakistan; new add-ons: PH SC/PWD discounts, IN Bill of Entry, VN delivery e-invoice, TW ECPay sales bridge, KR sales proof, ID QRIS kiosk, EG ETA POS receipts, ES web-shop simplified invoice, FR CAWL branding, GR delivery notes, BE POS rounding, EU VIES. (Section 3.5.) High
6. **Chart-of-accounts rewrites with depreciation models and hierarchies** across VN/ID/MY/PH/KH/HK/SG/KR/TR (and others); 35 charts now ship `account.depreciation.model-*.csv`. High
7. **Danish Nemhandel/OIOUBL, Hungarian receive-bills, Polish bank verification, Romanian CPV, Sri Lankan invoice, Chinese city data, French work-entry holidays consolidated into their base l10n modules** (section 5). High
8. **Singapore Peppol/InvoiceNow built in** with IRAS GST code list and customer accounting; Malaysia MyInvois auto-installs; Vietnam SInvoice service refactor + journal symbols. High/Medium
9. **EMV-QR naming and field relabelling** (`_get_emv_qr_code_names`, "Account Identifier Type/Value"; `acc_number` -> `account_number`). High
10. **Security file format change** (`ir.access.csv` with `operation`/`domain`) in 52 l10n modules. High
11. `l10n_eu_account_vies`: VIES VAT check split out of the removed `base_vat`. High

## 5. Removed / merged modules

| Removed (v19) | Successor / where it went | Evidence | Verdict |
|---|---|---|---|
| `l10n_tr_nilvera`, `_base_vat`, `_einvoice`, `_einvoice_extended`, `_edispatch` (Turkey e-fatura/e-irsaliye via Nilvera) | **None in CE 20.** No `nilvera` string in `addons/` or `odoo/` (only translation tooling). `l10n_tr` gained tax-office/fiscal-position data but no EDI. Likely moved to Enterprise or dropped (inference). | `grep -rli nilvera odoo20/addons` -> empty; diff `l10n_tr` | Removed, no successor in CE |
| `l10n_dk_nemhandel`, `l10n_dk_nemhandel_response`, `l10n_dk_oioubl` | **Merged into `l10n_dk`**: now depends `account_edi_proxy_client, account_edi_ubl_cii`; contains `models/account_edi_xml_oioubl_21.py`, `account_edi_proxy_user.py`, `nemhandel_response.py`, `wizard/nemhandel_registration*.py`, `nemhandel_rejection_wizard`, controller `webhooks.py`, cron, onboarding tour | `addons/l10n_dk/__manifest__.py`, `models/`, `wizard/` | Merged |
| `l10n_latam_base` (identification type model, `l10n_latam_identification_type_id`) | **Replaced by core `additional_identifiers`** + per-country `tools/partner_identifiers.py` in l10n_ar/cl/co/ec/pe/pa/gt; `l10n_latam_identification_type_id` has 0 hits in v20 vs 19 python files in v19; `l10n_ar` etc. no longer depend on it | `odoo/tools/partner_identifiers.py`; `addons/l10n_ar/tests/test_res_partner.py:28` uses `{'AR_DNI': ...}` | Replaced (data-migration needed) |
| `l10n_cn_city` | Data merged into `l10n_cn` (`data/res_city_data.xml`, 17,104 lines; manifest lists it) | `addons/l10n_cn/__manifest__.py:42` | Merged |
| `l10n_ec_stock` | Merged into `l10n_ec`: `models/template_ec.py` has `_get_ec_stock_location` template (`@template('ec','stock.location')`) setting loss/production location accounts, guarded by `'stock.location' not in self.env` | `addons/l10n_ec/models/template_ec.py:88-93` | Merged |
| `l10n_hu_edi_receive` | Merged into `l10n_hu_edi`: `wizard/l10n_hu_edi_receive_bills_wizard.py`, `static/src/views/sync_with_nav_btn`, `queryInvoiceDigest` mocks/tests | `addons/l10n_hu_edi/wizard/`, `models/l10n_hu_edi_connection.py` | Merged |
| `l10n_lk_invoice` | Merged into `l10n_lk` (it now has `models/account_move.py`, `account_resequence.py`, `res_company.py`, `res_partner.py`, `views/report_invoice.xml`; Sri Lanka tax invoice sequence, VAT-registered flags) | `ls addons/l10n_lk/models` | Merged |
| `l10n_pl_bank_verification` | Merged into `l10n_pl` (`models/bank_account_verification.py`, `account_payment.py`, wizard, views, `tests/test_bank_account_verification.py`) | `addons/l10n_pl/` | Merged |
| `l10n_ro_cpv_code` | Merged into `l10n_ro_edi` (`models/cpv_code.py`, `product.py`, `views/product_views.xml`, ubl_ro override) | `addons/l10n_ro_edi/models/` | Merged |
| `l10n_ro_edi_stock_batch` | Merged into `l10n_ro_edi_stock` (`models/stock_picking_batch.py`, batch report, `test_batch_stock_etransport.py`); dependency on `stock_picking_batch` dropped because that module was removed from addons (batch transfers presumably folded into `stock`) | `addons/l10n_ro_edi_stock/`; `removed_in_20.txt` | Merged |
| `l10n_sa_withholding_tax` | Merged: `l10n_sa` now depends on `l10n_account_withholding_tax` directly (v19 module only forced the install) | manifests 19 vs 20 | Merged |
| `l10n_uy_pos` | **No successor found.** v19 only patched `PaymentScreen.onMounted` to force `setToInvoice(true)` for company country UY; no `UY` reference remains in `point_of_sale` or `l10n_uy` | `odoo19/addons/l10n_uy_pos/static/.../payment_screen.js` | Removed; behavior lost (Uruguayan POS no longer forced to invoice) |
| `l10n_fr_hr_work_entry_holidays` | Merged into `l10n_fr_hr_holidays` (`models/hr_version.py`, `tests/test_french_work_entries.py` carried over, code modernised to `datetime.UTC`/`zoneinfo`); `hr_work_entry_holidays` itself was removed from addons | `addons/l10n_fr_hr_holidays/models/hr_version.py` | Merged |
| (outside l10n but linked) `base_vat`, `base_iban` | Validation in core `res.partner`; VIES split to `l10n_eu_account_vies`; IBAN in core/`account` (inference) | manifests | Merged |

## 6. Implementation notes, risks & migration gotchas (19 -> 20)

General
- **Custom code touching bank accounts**: `acc_number` is now `account_number`; QR "proxy" labels renamed. Grep custom modules/reports.
- **`account.group` is gone**: any custom chart, report, or financial-report domain using account groups must move to `parent_id`. Standard charts already did.
- **Access rules**: `ir.model.access.csv` and `ir.rule` XML replaced by `ir.access.csv` in core addons; custom modules inheriting security files continue to work only if they follow the new loader (see core security area).
- **LATAM**: partner identification types are no longer a model; migrate `l10n_latam_identification_type_id` data into `additional_identifiers` (no migration script is visible in `l10n_ar/l10n_cl/l10n_pe`; only `end-migrate_*taxes` scripts exist). Customers with AR/CL/CO/EC/PE data need a data migration.
- Removed modules (Nilvera, UY POS, PH 2307) = capabilities that disappear; check Enterprise coverage before promising upgrade.
- Dropping `base_vat`: modules depending on it in custom code must change their manifests.

Thailand-specific
1. **No migration scripts** exist for `l10n_th`. Existing databases keep v19 taxes (ordinary negative WHT taxes, old tags, no `is_withholding_tax`, no on-payment services taxes, no fiscal positions, no tax-invoice sequences). New chart data is loaded only for new companies or by reloading templates (`account.chart.template.try_loading`), which does not overwrite existing taxes in use. Plan a script or manual re-mapping: flag WHT taxes, create fiscal positions, backfill `l10n_th.tax.invoice` for historical invoices if the RD audit needs it. (inference from absence of `migrations/`, [code] for the absence.)
2. **WHT behaviour change**: v19 WHT reduced the invoice at billing; v20 defers to payment (net due shown). AP/AR aging, cash-flow and customers' expectation of "net payable on the bill" change. Accounting for 213302/213303/213304 now posts at payment date — matches Thai practice of remitting by the 7th of next month but changes timing in books.
3. **PND3/PND53 reports are gone**; client must produce RD forms externally (see gaps).
4. **Tax invoice numbering**: `TINV/%(year)s/#####` and `RCT/...` are **separate** from the invoice number (INV/2026/...). Auditors expecting one number per tax invoice must set the sequence prefix per business rules; sequences are gap-free per company and year. Multi-branch (สาขา) clients need one sequence per company — branches as separate companies is the supported route.
5. **Cash-basis (on_payment) VAT** needs `tax_exigibility` company setting (Thai template sets it True) and a transition account on the tax; test partial payments and credit notes before go-live.
6. **QR on tax invoice PDF is suppressed** (`report_tax_invoice_document` replaces `#qrcode` and `#payment_link_qrcode` divs) — customers wanting PromptPay QR on the tax invoice must reintroduce it.
7. The 50 Tawi form fills only **purchase WHT** payments with `l10n_th_income_tax_type != 'na'`; customer-side certificates received are not generated (nor needed).
8. Thai language must be installed/active for Thai text; report falls back to English otherwise (`report_lang` in `report_tawi.py`).
9. Chart is flat: no parent hierarchy and no depreciation models, unlike HK/VN/ID/MY/KH in v20 — consider extending.

Hong Kong
- Chart code/XML-ID rewrite means **no in-place mapping** for existing HK companies; plan a chart-remap (account merge) before or after upgrade. Opening-balance and tax-return code lists in custom reports need updates.

## 7. Open questions / not verifiable from CE code

- Whether Nilvera (Turkey) and Brazil/Mexico/LATAM EDI exist as Enterprise modules in v20 (not in this repo). [web not checked]
- Whether Enterprise v20 adds Thai e-Tax Invoice & e-Receipt (RD), PND e-filing, or Thai payroll/SSO — nothing in CE; as of v19/v20 CE there is none, and Thai Odoo partners historically rely on OCA/ third-party modules. [unverified]
- Details of 2307 (PH) replacement; precise VN cancellation flow after wizard removal; l10n_in's 67 changed files; exact data-migration path for `additional_identifiers`.
- Official v20 release notes were not consulted [web].

## 8. Gaps a Thai Odoo partner must fill (custom / OCA / third-party)

Status in CE 20 for Thailand, by need. "Gap" = nothing in `addons/` covers it.

| # | Need | CE 20 status | What the partner must do |
|---|---|---|---|
| 1 | **e-Tax Invoice & e-Receipt** (Revenue Department, XML/PDF-A3 signed with certificate, ETDA standard, submission via RD/service-provider API) | **Gap.** No module, no `ETDA`/`etax` strings. `l10n_th.tax.invoice` only produces a printable record. | Build a connector (own, or via a certified Thai service provider API such as common e-Tax providers), signing with a CA certificate; reuse `l10n_th.tax.invoice` as the number source. |
| 2 | **PND 1 / 2 / 3 / 53 / 54 monthly returns + RD e-filing file/CSV/text** | **Gap (regressed vs 19).** v19 had basic PND3/PND53 tax reports; v20 removed them. Data is available: WHT lines carry `l10n_th_income_tax_type`, tax group, payee VAT/branch. | Build report/export from `account.withholding.line` (payment WHT lines): PND3/PND53/PND54 layouts and RD upload format; add PND1/PND2 (payroll/royalty-for-individuals). |
| 3 | **ภ.พ.30 e-filing, ภ.พ.36 (reverse charge) workflow** | Partial: P.P. 30 report exists; reverse-charge tax `tax_input_vat_rc` is inactive by default; no P.P. 36 form/payment | Activate/test the RC tax, build P.P. 36 form and payment; P.P. 30 export file for RD. |
| 4 | **Purchase tax report / sales tax report (รายงานภาษีซื้อ/ภาษีขาย)** in RD-mandated layout (date, doc no., payee name, TIN, branch, base, VAT) | **Gap.** Tax report is balance-by-tag, not the register format. | Add tax-register reports (sale/purchase/undue VAT) as `account.report` or SQL views; include branch code from `TH_BRANCH_CODE`. |
| 5 | **Branch (สาขา) handling**: separate tax invoice numbering per branch, branch on all documents, per-branch P.P. 30 | Partial: branch code identifier + "Branch NNNNN/Headquarter" on partner. Sequences are per company. | Model branches as companies or extend sequences/report per branch; ensure PDFs show address+branch of the issuing establishment. |
| 6 | **Thai payroll, social security (SSO), provident fund, PND1 / Kor.Yor. forms, 50 ทวิ for salaries** | **Gap** (Payroll is Enterprise, no Thai rules in CE) | OCA/custom payroll (rules, SSO 5% cap, PND1, 50 ทวิ for employees); Thai calendar / public holidays. |
| 7 | **Fixed assets & Thai depreciation rates (e.g. RD limits), asset register** | Partial: `account.asset-th.csv` only (13 lines, assets app is Enterprise); no depreciation-model CSV for TH (HK/VN/ID/MY/KH/SG have it) | Add `account.depreciation.model` data with RD maximum rates. |
| 8 | **Thai financial statements (DBD / TFRS for NPAEs) and DBD e-Filing XBRL**, corporate income tax PND50/51 | **Gap** | Account tags/financial-report definitions mapped to the DBD chart; CIT working papers. |
| 9 | **Bank statement import for Thai banks** (KBank, SCB, BBL, Krungsri etc. file formats), **bulk payment files / SMART/ BahtNet**, bill-payment (Bill Payment barcode / "Pay slip" QR with Ref1/Ref2) | **Gap.** Only PromptPay credit-transfer QR (tag 29). Bill-payment QR (Ref1/Ref2, tag 30) is not implemented in `res_bank.py` (merchant account info only builds tag 29). | Custom bank import parsers (OCA bank-statement-import patterns), bill-payment QR. |
| 10 | **Payment gateways**: PromptPay via Stripe/Adyen/Xendit exist; Thai-specific (2C2P, Omise/Opn, KBank PGW, SCB, TrueMoney, LINE Pay direct) | Partial: `payment_stripe`, `payment_adyen`, `payment_xendit` define PromptPay method (`payment_xendit/const.py:27`; `payment_*/data/payment_method_data.xml`); no 2C2P/Opn provider | Custom/third-party providers. |
| 11 | **POS for Thailand**: tax-invoice abbreviated (ใบกำกับภาษีอย่างย่อ), RD-approved POS/e-receipt machine rules, fiscal printers | **Gap.** No `l10n_th_pos`; tax invoices are created only for out_invoice/out_receipt moves, not POS orders directly. | Custom POS receipt layout/numbering; map POS orders to `l10n_th.tax.invoice` (or invoice from POS). |
| 12 | **Customer side**: Thai-address autocomplete (sub-district/district/province/postcode), DBD company lookup by 13-digit TIN, RD VAT-registration check | Partial: Thai address view only; VAT format check via stdnum; no district/sub-district/postcode master data was found in `l10n_th` (provinces come from base state data; `l10n_cn` by contrast ships ~17k city records) | Load Thai geodata (OCA `base_address_extended` style / `l10n_th_*`), optional RD/DBD API lookup. |
| 13 | **Fiscal-year Buddhist-era (B.E.) date display on forms, Thai number-to-text on invoices** | Partial: 50 Tawi uses `amount_to_text` in Thai; B.E. (Buddhist-era) year printing was not found in the reports | Custom report tweaks. |
| 14 | **Stock/customs**: Thai import entry (ใบขนสินค้า), export documents, bonded warehouse | **Gap** (India has BOE, Thailand none) | Custom landed-cost workflow similar to `l10n_in_boe`. |
| 15 | **Thai accounting chart variants** (DBD standard chart, TFRS for PAEs, group-account hierarchy) | Single flat chart (`code_digits=6`), no parent accounts | Extend chart with hierarchy to match reporting. |
| 16 | **WHT edge cases**: threshold rule (small-amount WHT exemption, [background, not checked]), different rates per payee/ATC, dividends 10%, e-WHT (RD e-Withholding scheme, [background]) | Partial: rates present, many taxes inactive by default; e-WHT and threshold not coded | Configure active taxes per client; add threshold logic if required. |

**Pre-sales message** for a Bangkok partner: CE 20 Thailand is "accounting + VAT + WHT-at-payment + 50 Tawi + PromptPay + tax-invoice register". Everything RD-facing beyond that (e-Tax, PND/PP30/PP36 e-filing, payroll) remains partner IP. Compare: Vietnam (SInvoice), Malaysia (MyInvois), Indonesia (Coretax e-Faktur), Singapore (Peppol), Taiwan (ECPay), Pakistan (FBR) all have authority connectors in CE 20; Thailand does not.
