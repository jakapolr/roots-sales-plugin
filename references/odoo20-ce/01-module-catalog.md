# Odoo 20.0 Community Edition — Complete Module Catalogue (vs 19.0)

> Generated straight from the code: `odoo/odoo` branch `20.0` (HEAD `b100a87`, 2026-10-03) and branch `19.0`, using every `__manifest__.py`. All 657 modules in v20 are licensed **LGPL-3**, which confirms this is the **Community Edition (CE)**. Enterprise modules are not in this repo.

**How to read the status column**

- **NEW**: the module exists in 20.0 but not in 19.0.
- **REMOVED**: the module exists in 19.0 but not in 20.0. See the area reports for where its features went.
- **CHANGED-MAJOR**: at least 30% of the module's files (and at least 10 files) differ.
- **CHANGED**: some files differ.
- **UNCHANGED**: no file differs.
- `files_changed` = files that differ / total files in v20.

Note: 20.0 also includes everything from the online-only releases saas-19.1 to saas-19.4. That is why nearly every module shows changes.

## Headline numbers

| Metric | Count |
|---|---|
| Modules in 20.0 (addons + core) | 657 |
| NEW in 20.0 | 58 |
| REMOVED since 19.0 | 63 |
| CHANGED-MAJOR | 473 |
| CHANGED (minor) | 125 |
| UNCHANGED | 1 |
| Installable *Apps* (application=True) | 34 |

## The CE apps (application = True)

| App module | Name | Summary | Status |
|---|---|---|---|
| `account` | Invoicing | Invoices & Payments | CHANGED-MAJOR |
| `calendar` | Calendar | Schedule employees' meetings | CHANGED-MAJOR |
| `contacts` | Contacts | Centralize your address book | CHANGED-MAJOR |
| `crm` | CRM | Track leads and close opportunities | CHANGED-MAJOR |
| `data_recycle` | Data Recycle | Find old records and archive/delete them | CHANGED-MAJOR |
| `fleet` | Fleet | Manage your fleet and track car costs | CHANGED-MAJOR |
| `hr` | Employees | Centralize employee information | CHANGED-MAJOR |
| `hr_attendance` | Attendances | Track employee attendance | CHANGED-MAJOR |
| `hr_expense` | Expenses | Submit, validate and reinvoice employee expenses | CHANGED-MAJOR |
| `hr_holidays` | Time Off | Allocate time off and follow leave requests | CHANGED-MAJOR |
| `hr_recruitment` | Recruitment | Track your recruitment pipeline | CHANGED-MAJOR |
| `hr_skills` | Skills Management | Manage skills, knowledge and resume of your employees | CHANGED-MAJOR |
| `im_livechat` | Live Chat | Chat with your website visitors | CHANGED-MAJOR |
| `lunch` | Lunch | Handle lunch orders of your employees | CHANGED-MAJOR |
| `mail` | Discuss | Chat, mail gateway and private channels | CHANGED-MAJOR |
| `maintenance` | Maintenance | Track equipment and manage maintenance requests | CHANGED-MAJOR |
| `marketing_card` | Marketing Card | Generate dynamic shareable cards | CHANGED-MAJOR |
| `mass_mailing` | Email Marketing | Design, send and track emails | CHANGED-MAJOR |
| `mass_mailing_sms` | SMS Marketing | Design, send and track SMS | CHANGED-MAJOR |
| `mrp` | Manufacturing | Manufacturing Orders & BOMs | CHANGED-MAJOR |
| `point_of_sale` | Point of Sale | Handle checkouts and payments for shops and restaurants. | CHANGED-MAJOR |
| `pos_restaurant` | Restaurant | Restaurant extensions for the Point of Sale | CHANGED-MAJOR |
| `project` | Project | Manage tasks and collaborate on projects | CHANGED-MAJOR |
| `project_todo` | To-Do | Organize your work with memos and to-do lists | CHANGED-MAJOR |
| `purchase` | Purchase | Purchase orders, tenders and agreements | CHANGED-MAJOR |
| `repair` | Repairs | Repair damaged products | CHANGED-MAJOR |
| `sale_management` | Sales | From quotations to invoices | CHANGED-MAJOR |
| `stock` | Inventory | Manage your stock and logistics activities | CHANGED-MAJOR |
| `survey` | Surveys | Send your surveys or share them live. | CHANGED-MAJOR |
| `website` | Website | Enterprise website builder | CHANGED-MAJOR |
| `website_event` | Events | Publish events, sell tickets | CHANGED-MAJOR |
| `website_hr_recruitment` | Online Jobs | Manage your online hiring process | CHANGED-MAJOR |
| `website_sale` | eCommerce | Sell your products online | CHANGED-MAJOR |
| `website_slides` | eLearning | Manage and publish an eLearning platform | CHANGED-MAJOR |

## Accounting (48)

| Module | Status | Files changed | App | Summary | Depends |
|---|---|---|---|---|---|
| `account_payment_custom` | 🆕 NEW |  |  | Bridge between payment_custom and account_payment. | account_payment, payment_custom |
| `account_add_gln` | ❌ REMOVED |  |  | This module adds the Global Location Number to the partner. Used on delivery addresses, it is used to identify stock locations and is mandatory on the UBL/CII eInvoices (but not only). The module is intended be merged with account, later on, in master | account |
| `account_peppol_advanced_fields` | ❌ REMOVED |  |  | Merged prematurly, not working correctly. Please don't use. Better solution coming soon. | account, account_edi_ubl_cii |
| `account_peppol_response` | ❌ REMOVED |  |  | This module is used to send/receive responses to documents received/sent with PEPPOL | account_peppol |
| `base_iban` | ❌ REMOVED |  |  | IBAN Bank Accounts | account, web |
| `base_vat` | ❌ REMOVED |  |  | VAT Number Validation | account |
| `account` | CHANGED-MAJOR | 431/550 | ✅ | Invoices & Payments | base_setup, onboarding, product, analytic, portal, digest |
| `account_check_printing` | CHANGED-MAJOR | 79/88 |  | Check printing basic features | account |
| `account_debit_note` | CHANGED-MAJOR | 59/64 |  | Debit Notes | account |
| `account_edi` | CHANGED-MAJOR | 58/70 |  | Import/Export Invoices From XML/PDF | account |
| `account_edi_proxy_client` | CHANGED-MAJOR | 60/61 |  | Proxy features for account_edi | account, certificate |
| `account_edi_ubl_cii` | CHANGED-MAJOR | 153/312 |  | Import/Export electronic invoices with UBL/CII | account |
| `account_fleet` | CHANGED-MAJOR | 65/69 |  | Manage accounting with fleets | fleet, account |
| `account_payment` | CHANGED-MAJOR | 91/96 |  | Enable customers to pay invoices on the portal and post payments when transactions are processed. | account, payment |
| `account_payment_interco` | CHANGED-MAJOR | 52/58 |  | Enable Intercompany payments to reconcile with their invoices on post. | account_payment |
| `account_peppol` | CHANGED-MAJOR | 97/121 |  | This module is used to send/receive documents with Peppol | account_edi_proxy_client, account_edi_ubl_cii |
| `account_qr_code_emv` | CHANGED-MAJOR | 54/55 |  | account_qr_code_emv | account |
| `account_qr_code_sepa` | CHANGED-MAJOR | 53/55 |  | Account SEPA QR Code | account |
| `account_tax_python` | CHANGED-MAJOR | 71/64 |  | Use python code to define taxes | account |
| `account_update_tax_tags` | CHANGED-MAJOR | 56/58 |  | Allow updating tax grids on existing entries | account |
| `analytic` | CHANGED-MAJOR | 96/112 |  | Analytic Accounting | base, mail, uom |
| `payment_adyen` | CHANGED-MAJOR | 83/77 |  | A Dutch payment provider covering Europe and the US. | payment |
| `payment_aps` | CHANGED-MAJOR | 66/69 |  | An Amazon payment provider covering the MENA region. | payment |
| `payment_asiapay` | CHANGED-MAJOR | 66/70 |  | An payment provider based in Hong Kong covering most Asian countries. | payment |
| `payment_authorize` | CHANGED-MAJOR | 84/77 |  | An payment provider covering the US, Australia, and Canada. | payment |
| `payment_buckaroo` | CHANGED-MAJOR | 79/70 |  | A Dutch payment provider covering several countries in Europe. | payment |
| `payment_custom` | CHANGED-MAJOR | 84/87 |  | A payment provider for custom flows like wire transfers. | payment |
| `payment_demo` | CHANGED-MAJOR | 70/77 |  | A payment provider for running fake payment flows for demo purposes. | payment |
| `payment_dpo` | CHANGED-MAJOR | 65/68 |  | A Kenyan payment provider covering several African countries. | payment |
| `payment_ecpay` | CHANGED-MAJOR | 62/67 |  | A payment provider covering the Taiwanese market. | payment |
| `payment_flutterwave` | CHANGED-MAJOR | 67/72 |  | A Nigerian payment provider covering several African countries. | payment |
| `payment_iyzico` | CHANGED-MAJOR | 67/69 |  | A payment provider covering Turkey. | payment |
| `payment_mercado_pago` | CHANGED-MAJOR | 69/75 |  | A payment provider covering several countries in Latin America. | payment |
| `payment_mollie` | CHANGED-MAJOR | 66/69 |  | A Dutch payment provider covering several European countries. | payment |
| `payment_nuvei` | CHANGED-MAJOR | 66/69 |  | A payment provider covering Latin America. | payment |
| `payment_paymob` | CHANGED-MAJOR | 64/69 |  | An Egyptian payment provider for the Middle East. | payment |
| `payment_paypal` | CHANGED-MAJOR | 87/79 |  | An American payment provider for online payments all over the world. | payment |
| `payment_payu` | CHANGED-MAJOR | 62/70 |  | A payment provider covering India. | payment |
| `payment_razorpay` | CHANGED-MAJOR | 67/74 |  | A payment provider covering India. | payment |
| `payment_redsys` | CHANGED-MAJOR | 66/68 |  | A payment provider covering the Spanish market. | payment |
| `payment_stripe` | CHANGED-MAJOR | 75/81 |  | An Irish-American payment provider covering the US and many others. | payment |
| `payment_toss_payments` | CHANGED-MAJOR | 61/69 |  | A payment provider covering the South Korea market | payment |
| `payment_worldline` | CHANGED-MAJOR | 65/69 |  | A French payment provider covering several European countries. | payment |
| `payment_xendit` | CHANGED-MAJOR | 66/72 |  | A payment provider for Indonesian and the Philippines. | payment |
| `pos_account_tax_python` | CHANGED-MAJOR | 53/57 |  | Allow custom taxes in POS | account_tax_python, point_of_sale |
| `product_email_template` | CHANGED-MAJOR | 68/68 |  | Product Email Template | account |
| `project_account` | CHANGED-MAJOR | 55/56 |  | project profitability items computation | account, project |
| `spreadsheet_account` | CHANGED-MAJOR | 67/78 |  | Spreadsheet Accounting formulas | spreadsheet, account |

## Sales (97)

| Module | Status | Files changed | App | Summary | Depends |
|---|---|---|---|---|---|
| `crm_sale_project` | 🆕 NEW |  |  | Project Generation from Opportunities | sale_project, crm |
| `mysubscription` | 🆕 NEW |  |  | Backend Subscription App | base, web |
| `pos_bancontact_pay` | 🆕 NEW |  |  | Accept Bancontact Pay and Wero QR code payments in POS (Payconiq). | point_of_sale |
| `pos_partner_autocomplete` | 🆕 NEW |  |  | Link module between Partner Autocomplete and Point of Sale | partner_autocomplete, point_of_sale |
| `pos_sale_stock` | 🆕 NEW |  |  | Link module between PoS Stock and Sales | pos_stock, pos_sale |
| `pos_self_order_bancontact_pay` | 🆕 NEW |  |  | Accept Bancontact Pay and Wero QR code payments in a kiosk (Payconiq). | pos_self_order, pos_bancontact_pay |
| `pos_self_order_event` | 🆕 NEW |  |  | Link module between PoS Self Order and PoS Event | pos_self_order, pos_event |
| `pos_self_order_sms` | 🆕 NEW |  |  | POS Self Order SMS | pos_self_order, pos_sms |
| `pos_stock` | 🆕 NEW |  |  | Stock integration for PoS | point_of_sale, stock_account |
| `sale_project_margin` | 🆕 NEW |  |  | Bridge module between Sales Margin and Project | sale_margin, sale_project |
| `pos_restaurant_adyen` | ❌ REMOVED |  |  | Adds American style tipping to Adyen | pos_adyen, pos_restaurant, payment_adyen |
| `pos_restaurant_stripe` | ❌ REMOVED |  |  | Adds American style tipping to Stripe | pos_stripe, pos_restaurant, payment_stripe |
| `pos_self_order_adyen` | ❌ REMOVED |  |  | Addon for the Self Order App that allows customers to pay by Adyen. | pos_adyen, pos_self_order |
| `pos_self_order_stripe` | ❌ REMOVED |  |  | Addon for the Self Order App that allows customers to pay by Stripe. | pos_stripe, pos_self_order |
| `pos_self_order_viva_com` | ❌ REMOVED |  |  | Addon for the Self Order App that allows customers to pay with Viva.com terminals. | pos_viva_com, pos_self_order |
| `base_address_extended` | CHANGED-MAJOR | 76/65 |  | Add extra fields on addresses | web |
| `base_automation` | CHANGED-MAJOR | 84/92 |  | Automation Rules | base, digest, resource, mail, sms |
| `base_geolocalize` | CHANGED-MAJOR | 74/68 |  | Partners Geolocation | base_setup |
| `contacts` | CHANGED-MAJOR | 69/68 | ✅ | Centralize your address book | base_address_extended, mail, web_hierarchy |
| `crm` | CHANGED-MAJOR | 179/237 | ✅ | Track leads and close opportunities | base_setup, base_install_request, sales_team, mail, calendar, resource, utm, web_tour, contacts, digest, phone_validation |
| `crm_iap_enrich` | CHANGED-MAJOR | 57/62 |  | Enrich Leads/Opportunities using email address domain | iap_crm, iap_mail |
| `crm_iap_mine` | CHANGED-MAJOR | 69/77 |  | Generate Leads/Opportunities based on country, industries, size, etc. | iap_crm, iap_mail |
| `crm_livechat` | CHANGED-MAJOR | 91/85 |  | Create lead from livechat conversation | crm, im_livechat |
| `crm_mail_plugin` | CHANGED-MAJOR | 61/57 |  | Turn emails received in your mailbox into leads and log their content as internal notes. | crm, mail_plugin |
| `crm_sms` | CHANGED-MAJOR | 57/55 |  | Add SMS capabilities to CRM | crm, sms |
| `delivery` | CHANGED-MAJOR | 120/120 |  | Delivery Costs | sale, payment_custom |
| `gamification_sale_crm` | CHANGED-MAJOR | 66/62 |  | CRM Gamification | gamification, sale_crm |
| `loyalty` | CHANGED-MAJOR | 100/109 |  | Use discounts, gift cards, eWallets and loyalty programs in your sales channels | product, portal, account |
| `mail_plugin` | CHANGED-MAJOR | 67/65 |  | Allows integration with mail plugins. | digest, web, contacts |
| `partnership` | CHANGED-MAJOR | 59/71 |  | Partnership / Membership | crm, sale |
| `point_of_sale` | CHANGED-MAJOR | 676/876 | ✅ | Handle checkouts and payments for shops and restaurants. | resource, product, account, barcodes_gs1_nomenclature, html_editor, digest, phone_validation, google_address_autocomplete, base_report_wkhtmltox, iot_webserial |
| `pos_adyen` | CHANGED-MAJOR | 67/70 |  | Integrate your POS with an Adyen payment terminal | point_of_sale, payment_adyen |
| `pos_cashdro` | CHANGED-MAJOR | 60/62 |  | Integrate your POS with a Cashdro automatic cash payment device | point_of_sale |
| `pos_cashmatic` | CHANGED-MAJOR | 58/61 |  | Integrate your POS with a cash matic automatic cash payment device | point_of_sale |
| `pos_discount` | CHANGED-MAJOR | 83/91 |  | Simple Discounts in the Point of Sale | point_of_sale |
| `pos_dpopay` | CHANGED-MAJOR | 55/58 |  | Integrate your POS with DPO payment terminal. | point_of_sale |
| `pos_edi_ubl` | CHANGED-MAJOR | 52/53 |  | UBL in the Point of Sale | point_of_sale, account_edi_ubl_cii |
| `pos_glory_cash` | CHANGED-MAJOR | 62/70 |  | Integrate your POS with a Glory automatic cash payment device | point_of_sale |
| `pos_hr` | CHANGED-MAJOR | 104/115 |  | Link module between Point of Sale and HR | point_of_sale, hr |
| `pos_hr_restaurant` | CHANGED | 5/54 |  | Link module between pos_hr and pos_restaurant | pos_hr, pos_restaurant |
| `pos_imin` | CHANGED-MAJOR | 61/58 |  | iMin ePOS Printers in PoS | point_of_sale |
| `pos_loyalty` | CHANGED-MAJOR | 138/149 |  | Use Coupons, Gift Cards and Loyalty programs in Point of Sale | loyalty, point_of_sale |
| `pos_mercado_pago` | CHANGED-MAJOR | 60/62 |  | Integrate your POS with the Mercado Pago Smart Point terminal | point_of_sale |
| `pos_mollie` | CHANGED-MAJOR | 59/64 |  | Integrate your POS with a Mollie payment terminal | point_of_sale, payment_mollie |
| `pos_mrp` | CHANGED-MAJOR | 61/61 |  | Link module between Point of Sale and Mrp | pos_stock, mrp |
| `pos_online_payment_self_order` | CHANGED-MAJOR | 78/78 |  | Support online payment in self-order | pos_online_payment, pos_self_order |
| `pos_pine_labs` | CHANGED-MAJOR | 57/61 |  | Integrate your POS with Pine Labs payment terminals | point_of_sale |
| `pos_qfpay` | CHANGED-MAJOR | 57/64 |  | Integrate your POS with the QFPay terminal in Hong Kong | point_of_sale |
| `pos_razorpay` | CHANGED-MAJOR | 59/65 |  | Integrate your POS with a Razorpay payment terminal | point_of_sale |
| `pos_restaurant` | CHANGED-MAJOR | 192/293 | ✅ | Restaurant extensions for the Point of Sale | point_of_sale |
| `pos_restaurant_loyalty` | CHANGED | 5/56 |  | Link module between pos_restaurant and pos_loyalty | pos_restaurant, pos_loyalty |
| `pos_safaricom` | CHANGED-MAJOR | 69/73 |  | Integrate your POS with the Safaricom Payment Provider | point_of_sale |
| `pos_sale` | CHANGED-MAJOR | 104/116 |  | Link module between Point of Sale and Sales | point_of_sale, sale_management |
| `pos_sale_loyalty` | CHANGED-MAJOR | 59/61 |  | Link module between pos_sale and pos_loyalty | pos_sale, pos_loyalty |
| `pos_sale_margin` | CHANGED-MAJOR | 53/55 |  | Link module between Point of Sale and Sales Margin | pos_sale, sale_margin |
| `pos_self_order` | CHANGED-MAJOR | 273/332 |  | Addon for the POS App that allows customers to view the menu on their smartphone. | pos_restaurant, http_routing, link_tracker, google_address_autocomplete, base_geolocalize |
| `pos_self_order_pine_labs` | CHANGED-MAJOR | 54/58 |  | An addon for the Self Order App (KIOSK) that allows customers to pay using the Pine Labs POS Terminal. | pos_pine_labs, pos_self_order |
| `pos_self_order_qfpay` | CHANGED-MAJOR | 57/58 |  | Addon for the Self Order App that allows customers to pay by QFPay. | pos_qfpay, pos_self_order |
| `pos_self_order_razorpay` | CHANGED-MAJOR | 54/58 |  | Addon for the Self Order App that allows customers to pay by Razorpay POS Terminal. | pos_razorpay, pos_self_order |
| `pos_self_order_sale` | CHANGED-MAJOR | 52/55 |  | POS Self Order Sale | pos_sale, pos_self_order |
| `pos_sms` | CHANGED-MAJOR | 58/63 |  | POS - SMS | point_of_sale, sms |
| `pos_stripe` | CHANGED-MAJOR | 56/58 |  | Integrate your POS with a Stripe payment terminal | point_of_sale, payment_stripe |
| `pos_viva_com` | CHANGED-MAJOR | 66/71 |  | Integrate your PoS with a Viva.com payment terminal | point_of_sale |
| `product` | CHANGED-MAJOR | 172/256 |  | Products & Pricelists | base, mail, uom |
| `product_margin` | CHANGED-MAJOR | 71/75 |  | Margins by Products | account |
| `product_matrix` | CHANGED-MAJOR | 62/64 |  | Technical module: Matrix Implementation | account |
| `sale` | CHANGED-MAJOR | 256/304 |  | Sales internal machinery | sales_team, account_payment, utm |
| `sale_crm` | CHANGED-MAJOR | 73/77 |  | Opportunity to Quotation | sale, crm |
| `sale_edi_ubl` | CHANGED-MAJOR | 59/61 |  | Import electronic orders with UBL | sale, account_edi_ubl_cii |
| `sale_expense` | CHANGED-MAJOR | 71/75 |  | Quotation, Sales Orders, Delivery & Invoicing Control | sale_management, hr_expense |
| `sale_expense_margin` | CHANGED-MAJOR | 52/56 |  | Sales Expense Margin | sale_expense, sale_margin |
| `sale_gelato` | CHANGED-MAJOR | 75/82 |  | Place orders through Gelato's print-on-demand service | sale, delivery |
| `sale_gelato_stock` | CHANGED-MAJOR | 52/53 |  | Gelato/Stock bridge | sale_gelato, sale_stock |
| `sale_loyalty` | CHANGED-MAJOR | 91/94 |  | Use discounts and loyalty programs in sales orders | sale, loyalty |
| `sale_loyalty_delivery` | CHANGED-MAJOR | 61/62 |  | Adds free shipping mechanism in sales orders | sale_loyalty, delivery |
| `sale_management` | CHANGED-MAJOR | 102/125 | ✅ | From quotations to invoices | sale, digest |
| `sale_margin` | CHANGED-MAJOR | 79/78 |  | Margins in Sales Orders | sale_management |
| `sale_mrp` | CHANGED-MAJOR | 88/82 |  | Sales and MRP Management | mrp, sale_stock |
| `sale_mrp_margin` | CHANGED | 3/53 |  | Sale Mrp Margin | sale_mrp, sale_stock_margin |
| `sale_pdf_quote_builder` | CHANGED-MAJOR | 82/96 |  | Sales PDF Quotation Builder | sale_management |
| `sale_product_matrix` | CHANGED-MAJOR | 61/60 |  | Add variants to Sales Order through a grid entry. | sale, product_matrix |
| `sale_project` | CHANGED-MAJOR | 103/107 |  | Task Generation from Sales Orders | sale_management, sale_service, project_account |
| `sale_project_stock` | CHANGED-MAJOR | 61/59 |  | Adds a full traceability of inventory operations on the profitability report. | sale_project, sale_stock, project_stock_account |
| `sale_purchase` | CHANGED-MAJOR | 65/66 |  | Sale based on service outsourcing. | sale, purchase |
| `sale_purchase_project` | CHANGED-MAJOR | 54/56 |  | Technical Bridge | sale_purchase, project_purchase, sale_project |
| `sale_purchase_stock` | CHANGED-MAJOR | 57/63 |  | SO/PO relation in case of MTO | sale_stock, purchase_stock, sale_purchase |
| `sale_service` | CHANGED-MAJOR | 53/56 |  | Interaction between Sales and services apps (project and planning) | sale_management |
| `sale_sms` | CHANGED | 5/52 |  | Ease SMS integration with sales capabilities | sale, sms |
| `sale_stock` | CHANGED-MAJOR | 128/132 |  | Quotation, Sales Orders, Delivery & Invoicing Control | sale, stock_account |
| `sale_stock_margin` | CHANGED-MAJOR | 53/55 |  | Sale Stock Margin | sale_stock, sale_margin |
| `sale_stock_product_expiry` | CHANGED-MAJOR | 58/60 |  | Sale Stock Product Expiry | sale_stock, product_expiry |
| `sale_timesheet` | CHANGED-MAJOR | 138/139 |  | Sell based on timesheets | sale_project, hr_timesheet |
| `sale_timesheet_margin` | CHANGED-MAJOR | 52/55 |  | Bridge module between Sales Margin and Sales Timesheet | sale_margin, sale_timesheet |
| `sales_team` | CHANGED-MAJOR | 80/91 |  | Sales Teams | base, mail |
| `sms` | CHANGED-MAJOR | 100/123 |  | SMS Text Messaging | base, iap_mail, mail, phone_validation |
| `uom` | CHANGED-MAJOR | 68/69 |  | Units of measure | base |
| `website_crm_iap_reveal` | CHANGED-MAJOR | 62/69 |  | Generate Leads/Opportunities from your website's traffic | iap_crm, iap_mail, crm_iap_mine, website_crm |

## Supply Chain (41)

| Module | Status | Files changed | App | Summary | Depends |
|---|---|---|---|---|---|
| `mrp_delivery` | 🆕 NEW |  |  | Carrier with kits | mrp, stock_delivery |
| `purchase_alternative` | 🆕 NEW |  |  | Purchase Alternative | purchase |
| `purchase_alternative_sale` | 🆕 NEW |  |  | Purchase Alternative Sale | purchase_alternative, sale_purchase |
| `purchase_alternative_stock` | 🆕 NEW |  |  | Purchase Alternative Stock | purchase_alternative, purchase_stock |
| `delivery_mondialrelay` | ❌ REMOVED |  |  | Let's choose a Point Relais® as shipping address | stock_delivery |
| `delivery_stock_picking_batch` | ❌ REMOVED |  |  | Batch Transfer, Carrier | stock_delivery, stock_picking_batch |
| `mrp_subcontracting_repair` | ❌ REMOVED |  |  | MRP Subcontracting Repair | mrp_subcontracting, repair |
| `purchase_requisition_sale` | ❌ REMOVED |  |  | Purchase Requisition Sale | purchase_requisition, sale_purchase |
| `stock_picking_batch` | ❌ REMOVED |  |  | Warehouse Management: Batch Transfer | stock |
| `barcodes` | CHANGED-MAJOR | 93/98 |  | Scan and Parse Barcodes | web |
| `barcodes_gs1_nomenclature` | CHANGED-MAJOR | 58/65 |  | Parse barcodes according to the GS1-128 specifications | barcodes, uom |
| `maintenance` | CHANGED-MAJOR | 84/98 | ✅ | Track equipment and manage maintenance requests | mail |
| `mrp` | CHANGED-MAJOR | 235/282 | ✅ | Manufacturing Orders & BOMs | product, stock, resource |
| `mrp_account` | CHANGED-MAJOR | 102/98 |  | Analytic accounting in Manufacturing | mrp, stock_account |
| `mrp_landed_costs` | CHANGED-MAJOR | 54/56 |  | Landed Costs on Manufacturing Order | stock_landed_costs, mrp |
| `mrp_product_expiry` | CHANGED-MAJOR | 53/58 |  | Manufacturing Expiry | mrp, product_expiry |
| `mrp_repair` | CHANGED-MAJOR | 56/60 |  | Mrp Repairs | repair, mrp |
| `mrp_subcontracting` | CHANGED-MAJOR | 89/117 |  | Subcontract Productions | mrp |
| `mrp_subcontracting_account` | CHANGED-MAJOR | 59/57 |  | Subcontracting Management with Stock Valuation | mrp_subcontracting, mrp_account |
| `mrp_subcontracting_dropshipping` | CHANGED-MAJOR | 58/68 |  | Dropship and Subcontracting Management | mrp_subcontracting, stock_dropshipping |
| `mrp_subcontracting_landed_costs` | CHANGED-MAJOR | 52/56 |  | Advanced views to manage landed cost for subcontracting orders | mrp_landed_costs, mrp_subcontracting |
| `mrp_subcontracting_purchase` | CHANGED-MAJOR | 66/69 |  | Purchase and Subcontracting Management | mrp_subcontracting_account, purchase_mrp |
| `product_expiry` | CHANGED-MAJOR | 85/104 |  | Products Expiration Date | stock |
| `project_mrp_stock_landed_costs` | CHANGED-MAJOR | 51/53 |  | Technical Bridge | project_mrp_account, mrp_landed_costs |
| `project_stock_landed_costs` | CHANGED-MAJOR | 51/53 |  | Technical Bridge | project_stock_account, stock_landed_costs |
| `purchase` | CHANGED-MAJOR | 142/167 | ✅ | Purchase orders, tenders and agreements | account |
| `purchase_edi_ubl_bis3` | CHANGED-MAJOR | 57/61 |  | Import/Export electronic orders with UBL | purchase, account_edi_ubl_cii |
| `purchase_mrp` | CHANGED-MAJOR | 70/72 |  | Purchase and MRP Management | mrp, purchase_stock |
| `purchase_product_matrix` | CHANGED-MAJOR | 60/61 |  | Add variants to your purchase orders through an Order Grid Entry. | purchase, product_matrix |
| `purchase_repair` | CHANGED-MAJOR | 54/58 |  | Keep track of linked purchase and repair orders | repair, purchase_stock |
| `purchase_requisition` | CHANGED-MAJOR | 83/80 |  | Purchase Agreements | purchase |
| `purchase_requisition_stock` | CHANGED-MAJOR | 61/60 |  | Purchase Requisition Stock | purchase_requisition, purchase_stock |
| `purchase_stock` | CHANGED-MAJOR | 127/140 |  | Purchase Orders, Receipts, Vendor Bills for Stock | stock_account, purchase |
| `repair` | CHANGED-MAJOR | 106/111 | ✅ | Repair damaged products | sale_stock, sale_management |
| `stock` | CHANGED-MAJOR | 303/345 | ✅ | Manage your stock and logistics activities | product, barcodes_gs1_nomenclature, digest |
| `stock_account` | CHANGED-MAJOR | 120/117 |  | Inventory, Logistic, Valuation, Accounting | stock, account |
| `stock_delivery` | CHANGED-MAJOR | 95/102 |  | Delivery - Stock | printer, sale_stock, delivery |
| `stock_dropshipping` | CHANGED-MAJOR | 71/75 |  | Drop Shipping | sale_purchase_stock |
| `stock_landed_costs` | CHANGED-MAJOR | 86/91 |  | Landed Costs | stock_account, purchase_stock |
| `stock_maintenance` | CHANGED-MAJOR | 53/56 |  | See lots used in maintenance | stock, maintenance |
| `stock_sms` | CHANGED-MAJOR | 58/61 |  | Send text messages when final stock move | stock, sms |

## Website (48)

| Module | Status | Files changed | App | Summary | Depends |
|---|---|---|---|---|---|
| `website_address_autocomplete` | 🆕 NEW |  |  | Assist your users with automatic completion & suggestions when filling their address | website, google_address_autocomplete |
| `website_partnership` | 🆕 NEW |  |  | Publish your partners on your website | partnership, website_partner |
| `website_sale_project` | 🆕 NEW |  |  | Bridge module between website_sale and project | website_sale, project |
| `website_sale_autocomplete` | ❌ REMOVED |  |  | Assist your users with automatic completion & suggestions when filling their address during checkout | website_sale, google_address_autocomplete |
| `website_sale_collect_wishlist` | ❌ REMOVED |  |  | Bridge module between Click & Collect and Wishlist | website_sale_wishlist, website_sale_collect |
| `website_sale_comparison` | ❌ REMOVED |  |  | Allow shoppers to compare products based on their attributes | website_sale |
| `website_sale_comparison_wishlist` | ❌ REMOVED |  |  | Bridge module for Website sale comparison and wishlist | website_sale_comparison, website_sale_wishlist |
| `website_sale_mondialrelay` | ❌ REMOVED |  |  | Let's choose Point Relais® on your ecommerce | website_sale, delivery_mondialrelay |
| `website_sale_stock_wishlist` | ❌ REMOVED |  |  | Notify the user when a product is back in stock | website_sale_stock, website_sale_wishlist |
| `website_sale_wishlist` | ❌ REMOVED |  |  | Allow shoppers to enlist products | website_sale |
| `im_livechat` | CHANGED-MAJOR | 404/421 | ✅ | Chat with your website visitors | mail, digest, utm, phone_validation |
| `theme_default` | CHANGED | 2/55 |  | Default Theme | website |
| `website` | CHANGED-MAJOR | 1340/1809 | ✅ | Enterprise website builder | digest, web, html_editor, http_routing, portal, social_media, auth_signup, mail, google_recaptcha, utm, html_builder |
| `website_blog` | CHANGED-MAJOR | 177/165 |  | Publish blog posts, announces, news | website_mail, website_partner, html_builder |
| `website_cf_turnstile` | CHANGED-MAJOR | 57/64 |  | Cloudflare Turnstile | website |
| `website_crm` | CHANGED-MAJOR | 76/81 |  | Generate leads from a contact form | website, crm |
| `website_crm_livechat` | CHANGED-MAJOR | 54/58 |  | View livechat sessions for leads | website_crm, website_livechat, crm_livechat |
| `website_crm_partner_assign` | CHANGED-MAJOR | 97/110 |  | Publish your resellers/partners and forward leads to them | base_geolocalize, crm, account, website_partnership, website_partner, website_google_map, portal |
| `website_crm_sms` | CHANGED-MAJOR | 51/55 |  | Allows to send sms to website visitor that have lead | website_sms, crm |
| `website_customer` | CHANGED-MAJOR | 77/84 |  | Publish your customer references | website_crm_partner_assign, website_partner, website_google_map |
| `website_event_crm` | CHANGED-MAJOR | 51/58 |  | Website Events CRM | event_crm, website_event |
| `website_event_sale` | CHANGED-MAJOR | 88/95 |  | Sell event tickets online | website_event, event_sale, website_sale |
| `website_forum` | CHANGED-MAJOR | 136/155 |  | Manage a forum with FAQ and Q&A | auth_signup, website_mail, website_profile |
| `website_google_map` | CHANGED | 4/76 |  | Show your company address on Google Maps | base_geolocalize, website_partner |
| `website_hr_recruitment` | CHANGED-MAJOR | 89/115 | ✅ | Manage your online hiring process | hr_recruitment, website_mail |
| `website_hr_recruitment_livechat` | CHANGED-MAJOR | 52/52 |  | Chatbot for the HR Recruitment | website_hr_recruitment, im_livechat |
| `website_links` | CHANGED-MAJOR | 71/81 |  | Generate trackable & short URLs | website, link_tracker |
| `website_livechat` | CHANGED-MAJOR | 119/137 |  | Chat with your website visitors | website, im_livechat |
| `website_mail` | CHANGED-MAJOR | 66/72 |  | Website Module for Mail | website, mail |
| `website_mass_mailing` | CHANGED-MAJOR | 95/105 |  | Attract visitors to subscribe to mailing lists | website, mass_mailing, google_recaptcha |
| `website_mass_mailing_sms` | CHANGED-MAJOR | 53/59 |  | Attract visitors to subscribe to mailing lists | website_mass_mailing, mass_mailing_sms |
| `website_partner` | CHANGED-MAJOR | 67/67 |  | Partner module for website | website |
| `website_payment` | CHANGED-MAJOR | 92/85 |  | Payment integration with website | website, account_payment, portal |
| `website_profile` | CHANGED-MAJOR | 67/79 |  | Access the website profile of the users | html_editor, website_partner, gamification |
| `website_project` | CHANGED-MAJOR | 59/65 |  | Add a task suggestion form to your website | website, project |
| `website_sale` | CHANGED-MAJOR | 573/565 | ✅ | Sell your products online | website, sale, website_payment, website_mail, portal_rating, digest, delivery, html_builder |
| `website_sale_collect` | CHANGED-MAJOR | 106/110 |  | Click & Collect | base_geolocalize, payment_custom, website_sale_stock |
| `website_sale_gelato` | CHANGED-MAJOR | 60/61 |  | eCommerce/Gelato bridge | sale_gelato, website_sale |
| `website_sale_loyalty` | CHANGED-MAJOR | 103/102 |  | Use coupon, promotion, gift cards and loyalty programs in your eCommerce store | website_sale, website_links, sale_loyalty |
| `website_sale_mass_mailing` | CHANGED-MAJOR | 53/62 |  | Let new customers sign up for a newsletter during checkout | website_sale, website_mass_mailing, mass_mailing_sale |
| `website_sale_mrp` | CHANGED-MAJOR | 57/59 |  | Manage Kit product inventory & availability | website_sale_stock, sale_mrp |
| `website_sale_slides` | CHANGED-MAJOR | 70/88 |  | Sell your courses online | website_slides, website_sale |
| `website_sale_stock` | CHANGED-MAJOR | 122/123 |  | Manage product inventory & availability | website_sale, sale_stock, stock_delivery |
| `website_slides` | CHANGED-MAJOR | 218/299 | ✅ | Manage and publish an eLearning platform | portal_rating, website, website_mail, website_profile, digest |
| `website_slides_forum` | CHANGED-MAJOR | 65/68 |  | Allows to link forum on a course | website_slides, website_forum |
| `website_slides_survey` | CHANGED-MAJOR | 76/93 |  | Add certification capabilities to your courses | website_slides, survey |
| `website_sms` | CHANGED-MAJOR | 52/54 |  | Allows to send sms to website visitor | website, sms |
| `website_timesheet` | CHANGED-MAJOR | 52/53 |  | Allow hiding timesheet information in the portal | website, hr_timesheet |

## Marketing (39)

| Module | Status | Files changed | App | Summary | Depends |
|---|---|---|---|---|---|
| `marketing_card_event` | 🆕 NEW |  |  | Generate dynamic shareable cards for entities linked to events. | marketing_card, event |
| `website_mass_mailing_event` | 🆕 NEW |  |  | Add pre-filled snippets in mass_mailing with an event snapshot | mass_mailing, website_event |
| `digest` | CHANGED-MAJOR | 67/83 |  | KPI Digests | mail, portal, resource |
| `event` | CHANGED-MAJOR | 124/178 |  | Trainings, Conferences, Meetings, Exhibitions, Registrations | barcodes, base_setup, digest, mail, phone_validation, portal, utm |
| `event_booth` | CHANGED-MAJOR | 56/76 |  | Manage event booths | event |
| `event_booth_sale` | CHANGED-MAJOR | 64/78 |  | Manage event booths sale | event_booth, event_sale |
| `event_crm` | CHANGED-MAJOR | 64/74 |  | Event CRM | event, crm |
| `event_crm_sale` | CHANGED-MAJOR | 51/56 |  | Event CRM Sale | event_crm, event_sale |
| `event_product` | CHANGED-MAJOR | 55/66 |  | Events Product | event, product, account |
| `event_sale` | CHANGED-MAJOR | 88/104 |  | Events Sales | event_product, sale_management |
| `event_sms` | CHANGED-MAJOR | 58/62 |  | SMS on Events | event, sms |
| `link_tracker` | CHANGED-MAJOR | 76/82 |  | Link Tracker | utm, mail |
| `marketing_card` | CHANGED-MAJOR | 74/100 | ✅ | Generate dynamic shareable cards | link_tracker, mass_mailing, website, base_report_wkhtmltox |
| `mass_mailing` | CHANGED-MAJOR | 364/479 | ✅ | Design, send and track emails | contacts, mail, html_builder, utm, link_tracker, social_media, web_tour, digest |
| `mass_mailing_crm` | CHANGED-MAJOR | 59/60 |  | Add lead / opportunities UTM info on mass mailing | crm, mass_mailing |
| `mass_mailing_crm_sms` | CHANGED-MAJOR | 51/53 |  | Add lead / opportunities info on mass mailing sms | mass_mailing_crm, mass_mailing_sms |
| `mass_mailing_event` | CHANGED-MAJOR | 66/58 |  | Mass mailing on attendees | event, mass_mailing |
| `mass_mailing_event_sms` | CHANGED-MAJOR | 51/55 |  | Event Attendees SMS Marketing | event, mass_mailing, mass_mailing_event, mass_mailing_sms, sms |
| `mass_mailing_event_track` | CHANGED-MAJOR | 66/58 |  | Mass mailing on track speakers | website_event_track, mass_mailing |
| `mass_mailing_event_track_sms` | CHANGED-MAJOR | 51/53 |  | Track Speakers SMS Marketing | mass_mailing, mass_mailing_sms, sms, website_event_track |
| `mass_mailing_sale` | CHANGED-MAJOR | 59/63 |  | Add sale order UTM info on mass mailing | sale, mass_mailing |
| `mass_mailing_sale_sms` | CHANGED-MAJOR | 51/53 |  | Add sale order info on mass mailing sms | mass_mailing_sale, mass_mailing_sms |
| `mass_mailing_slides` | CHANGED-MAJOR | 53/54 |  | Mass mailing on course members | website_slides, mass_mailing |
| `mass_mailing_sms` | CHANGED-MAJOR | 89/99 | ✅ | Design, send and track SMS | portal, mass_mailing, sms |
| `mass_mailing_themes` | CHANGED-MAJOR | 140/132 |  | Design gorgeous mails | mass_mailing |
| `social_media` | CHANGED-MAJOR | 56/58 |  | Social media connectors for company settings. | base |
| `survey` | CHANGED-MAJOR | 165/206 | ✅ | Send your surveys or share them live. | auth_signup, http_routing, mail, web_tour, gamification, digest |
| `survey_crm` | CHANGED-MAJOR | 61/67 |  | Generate leads from surveys | survey, crm |
| `utm` | CHANGED-MAJOR | 80/98 |  | UTM Trackers | base, web |
| `website_event` | CHANGED-MAJOR | 120/166 | ✅ | Publish events, sell tickets | event, website, website_partner, website_mail, html_builder |
| `website_event_booth` | CHANGED-MAJOR | 62/67 |  | Events, display your booths on your website | website_event, event_booth |
| `website_event_booth_exhibitor` | CHANGED-MAJOR | 56/67 |  | Event Booths, automatically create a sponsor. | website_event_exhibitor, website_event_booth |
| `website_event_booth_sale` | CHANGED-MAJOR | 59/66 |  | Events, sell your booths online | event_booth_sale, website_event_booth, website_sale |
| `website_event_booth_sale_exhibitor` | CHANGED-MAJOR | 51/54 |  | Bridge module between website_event_booth_exhibitor and website_event_booth_sale. | website_event_exhibitor, website_event_booth_sale |
| `website_event_exhibitor` | CHANGED-MAJOR | 70/84 |  | Event: manage sponsors and exhibitors | website_event |
| `website_event_track` | CHANGED-MAJOR | 113/150 |  | Sponsors, Tracks, Agenda, Event News | website_event |
| `website_event_track_live` | CHANGED-MAJOR | 55/65 |  | Support live tracks: streaming, participation, youtube | website_event_track |
| `website_event_track_live_quiz` | CHANGED-MAJOR | 51/58 |  | Bridge module to support quiz features during "live" tracks. | website_event_track_live, website_event_track_quiz |
| `website_event_track_quiz` | CHANGED-MAJOR | 64/75 |  | Quizzes on tracks | website_profile, website_event_track |

## Human Resources (32)

| Module | Status | Files changed | App | Summary | Depends |
|---|---|---|---|---|---|
| `fleet_maintenance` | 🆕 NEW |  |  | Integrates Fleet and Maintenance | fleet, maintenance |
| `hr_address_extended` | 🆕 NEW |  |  | Centralize employee information | hr, base_address_extended |
| `hr_calendar_google` | 🆕 NEW |  |  | HR Calendar with Google Calendar | hr_calendar, google_calendar |
| `hr_holidays_homeworking` | ❌ REMOVED |  |  | Manage holidays with remote work | hr_holidays, hr_homeworking |
| `hr_homeworking` | ❌ REMOVED |  |  | Remote Work | hr |
| `hr_homeworking_calendar` | ❌ REMOVED |  |  | Remote Work with calendar | hr_homeworking, calendar |
| `hr_org_chart` | ❌ REMOVED |  |  | HR Org Chart | hr, web_hierarchy |
| `hr_work_entry_holidays` | ❌ REMOVED |  |  | Manage Time Off in Payslips | hr_holidays, hr_work_entry |
| `fleet` | CHANGED-MAJOR | 98/178 | ✅ | Manage your fleet and track car costs | base, mail |
| `gamification` | CHANGED-MAJOR | 89/123 |  | Gamification | mail |
| `hr` | CHANGED-MAJOR | 299/312 | ✅ | Centralize employee information | auth_signup, base_setup, digest, phone_validation, resource_mail, web_hierarchy |
| `hr_attendance` | CHANGED-MAJOR | 156/166 | ✅ | Track employee attendance | hr, hr_work_entry, barcodes, base_geolocalize |
| `hr_calendar` | CHANGED-MAJOR | 76/77 |  | Display Working Hours in Calendar | hr, calendar |
| `hr_expense` | CHANGED-MAJOR | 143/161 | ✅ | Submit, validate and reinvoice employee expenses | account, web_tour, hr |
| `hr_fleet` | CHANGED-MAJOR | 75/70 |  | Get history of driven cars by employees | hr, fleet |
| `hr_gamification` | CHANGED-MAJOR | 76/85 |  | HR Gamification | gamification, hr |
| `hr_holidays` | CHANGED-MAJOR | 303/319 | ✅ | Allocate time off and follow leave requests | hr_work_entry, hr_calendar, resource |
| `hr_holidays_attendance` | CHANGED-MAJOR | 90/83 |  | Attendance Holidays | hr_attendance, hr_holidays |
| `hr_livechat` | CHANGED-MAJOR | 52/54 |  | HR - Livechat | hr, im_livechat |
| `hr_maintenance` | CHANGED-MAJOR | 73/65 |  | Equipment, Assets, Internal Hardware, Allocation Tracking | hr, maintenance |
| `hr_presence` | CHANGED-MAJOR | 65/68 |  | Employee Presence Control | hr, hr_holidays, sms |
| `hr_recruitment` | CHANGED-MAJOR | 133/187 | ✅ | Track your recruitment pipeline | hr, calendar, utm, attachment_indexation, web_tour, digest |
| `hr_recruitment_skills` | CHANGED-MAJOR | 66/68 |  | Manage skills of your employees | hr_skills, hr_recruitment |
| `hr_recruitment_sms` | CHANGED-MAJOR | 51/54 |  | Mass mailing sms to job applicants | hr_recruitment, sms |
| `hr_recruitment_survey` | CHANGED-MAJOR | 85/80 |  | Surveys | survey, hr_recruitment |
| `hr_skills` | CHANGED-MAJOR | 102/139 | ✅ | Manage skills, knowledge and resume of your employees | hr |
| `hr_skills_slides` | CHANGED-MAJOR | 57/66 |  | Add completed courses to resume of your employees | hr_skills, website_slides |
| `hr_skills_survey` | CHANGED-MAJOR | 55/61 |  | Add certification to resume of your employees | hr_skills, survey |
| `hr_timesheet_attendance` | CHANGED-MAJOR | 71/72 |  | Timesheets/attendances reporting | hr_timesheet, hr_attendance |
| `hr_work_entry` | CHANGED-MAJOR | 110/97 |  | Manage work entries | hr |
| `lunch` | CHANGED-MAJOR | 103/154 | ✅ | Handle lunch orders of your employees | mail |
| `project_timesheet_holidays` | CHANGED-MAJOR | 67/71 |  | Schedule timesheet when on time off | hr_timesheet, hr_holidays |

## Services (17)

| Module | Status | Files changed | App | Summary | Depends |
|---|---|---|---|---|---|
| `portal_discuss` | 🆕 NEW |  |  | Portal Discuss | mail, portal |
| `hr_hourly_cost` | ❌ REMOVED |  |  | Employee Hourly Wage | hr |
| `hr_timesheet` | CHANGED-MAJOR | 128/163 |  | Track employee time on tasks | hr, analytic, project, uom |
| `portal_rating` | CHANGED-MAJOR | 68/91 |  | Portal Rating | portal, rating |
| `project` | CHANGED-MAJOR | 295/394 | ✅ | Manage tasks and collaborate on projects | analytic, base_setup, mail, portal_rating, resource, web, web_tour, digest |
| `project_hr_expense` | CHANGED-MAJOR | 57/58 |  | Project expenses | project_account, hr_expense |
| `project_hr_skills` | CHANGED-MAJOR | 53/58 |  | Project skills | project, hr_skills |
| `project_mail_plugin` | CHANGED-MAJOR | 60/57 |  | Integrate your inbox with projects | project, mail_plugin |
| `project_mrp` | CHANGED-MAJOR | 57/60 |  | Monitor MRP using project | mrp, project |
| `project_mrp_account` | CHANGED-MAJOR | 62/63 |  | Monitor MRP account using project | mrp_account, project_mrp, project_stock_account |
| `project_mrp_sale` | CHANGED | 5/55 |  | Technical Bridge | project_mrp, sale_mrp, sale_project |
| `project_purchase` | CHANGED-MAJOR | 60/65 |  | Monitor purchase in project | purchase, project_account |
| `project_purchase_stock` | CHANGED-MAJOR | 59/58 |  | Project - Purchase - Stock | project_purchase, project_stock |
| `project_sale_expense` | CHANGED-MAJOR | 60/58 |  | Project - Sale - Expense | sale_project, sale_expense, project_hr_expense |
| `project_sms` | CHANGED-MAJOR | 57/64 |  | Send text messages when project/task stage move | project, sms |
| `project_stock` | CHANGED-MAJOR | 51/56 |  | Link Stock pickings to Project | stock, project |
| `project_stock_account` | CHANGED-MAJOR | 57/59 |  | Handle analytics in Stock pickings with Project | stock_account, project_stock |

## Productivity (31)

| Module | Status | Files changed | App | Summary | Depends |
|---|---|---|---|---|---|
| `mail_tracking` | 🆕 NEW |  |  | Technical tracking of discussion and message-related data | mail |
| `mail_tracking_mass_mailing` | 🆕 NEW |  |  | Track source of messages by mass mailing | mail_tracking, mass_mailing |
| `mail_tracking_sms` | 🆕 NEW |  |  | Track source of messages by sms | mail_tracking, sms |
| `auth_totp` | CHANGED-MAJOR | 68/74 |  | Two-Factor Authentication (TOTP) | web |
| `auth_totp_mail` | CHANGED-MAJOR | 63/73 |  | 2FA Invite mail | auth_totp, mail |
| `board` | CHANGED-MAJOR | 78/92 |  | Build your own dashboards | spreadsheet_dashboard |
| `calendar` | CHANGED-MAJOR | 207/230 | ✅ | Schedule employees' meetings | base, mail |
| `calendar_sms` | CHANGED-MAJOR | 69/64 |  | Send text messages as event reminders | calendar, sms |
| `data_recycle` | CHANGED-MAJOR | 63/69 | ✅ | Find old records and archive/delete them | mail |
| `google_calendar` | CHANGED-MAJOR | 114/125 |  | Google Calendar | google_account, calendar |
| `mail` | CHANGED-MAJOR | 1277/1436 | ✅ | Chat, mail gateway and private channels | base, base_setup, bus, web_tour, html_editor |
| `mail_bot` | CHANGED-MAJOR | 58/65 |  | Add OdooBot in discussions | mail |
| `mail_bot_hr` | CHANGED | 2/52 |  | Bridge module between hr and mailbot. | mail_bot, hr |
| `microsoft_calendar` | CHANGED-MAJOR | 90/95 |  | Outlook Calendar | microsoft_account, calendar |
| `project_todo` | CHANGED-MAJOR | 90/112 | ✅ | Organize your work with memos and to-do lists | project |
| `rating` | CHANGED-MAJOR | 93/108 |  | Customer Rating | mail |
| `rpc` | CHANGED | 5/57 |  | RPC endpoints | base |
| `spreadsheet` | CHANGED-MAJOR | 216/257 |  | Spreadsheet | bus, web, portal |
| `spreadsheet_dashboard` | CHANGED-MAJOR | 117/132 |  | Spreadsheet | spreadsheet |
| `spreadsheet_dashboard_account` | CHANGED-MAJOR | 55/56 |  | Spreadsheet | spreadsheet_dashboard, spreadsheet_account |
| `spreadsheet_dashboard_event_sale` | CHANGED-MAJOR | 54/54 |  | Spreadsheet | spreadsheet_dashboard, event_sale |
| `spreadsheet_dashboard_hr_expense` | CHANGED-MAJOR | 54/54 |  | Spreadsheet | spreadsheet_dashboard, sale_expense |
| `spreadsheet_dashboard_hr_timesheet` | CHANGED-MAJOR | 54/54 |  | Spreadsheet | spreadsheet_dashboard, hr_timesheet |
| `spreadsheet_dashboard_im_livechat` | CHANGED-MAJOR | 56/57 |  | Spreadsheet | spreadsheet_dashboard, im_livechat |
| `spreadsheet_dashboard_pos_hr` | CHANGED-MAJOR | 54/54 |  | Spreadsheet | spreadsheet_dashboard, pos_hr |
| `spreadsheet_dashboard_pos_restaurant` | CHANGED-MAJOR | 54/54 |  | Spreadsheet | spreadsheet_dashboard, pos_hr, pos_restaurant |
| `spreadsheet_dashboard_sale` | CHANGED-MAJOR | 57/57 |  | Spreadsheet | spreadsheet_dashboard, sale |
| `spreadsheet_dashboard_sale_timesheet` | CHANGED-MAJOR | 54/54 |  | Spreadsheet | spreadsheet_dashboard, sale_timesheet |
| `spreadsheet_dashboard_stock_account` | CHANGED-MAJOR | 54/54 |  | Spreadsheet | spreadsheet_dashboard, stock_account |
| `spreadsheet_dashboard_website_sale` | CHANGED-MAJOR | 54/54 |  | Spreadsheet | spreadsheet_dashboard, website_sale |
| `spreadsheet_dashboard_website_sale_slides` | CHANGED-MAJOR | 54/54 |  | Spreadsheet | spreadsheet_dashboard, website_sale_slides |

## Technical (15)

| Module | Status | Files changed | App | Summary | Depends |
|---|---|---|---|---|---|
| `iot_webserial` | 🆕 NEW |  |  | Interface with serial devices directly via the browser using Web Serial. | web |
| `printer` | 🆕 NEW |  |  | Base module to manage external printers (e.g. ePOS, ZPL) | base |
| `auth_password_policy_portal` | CHANGED-MAJOR | 51/55 |  | Password Policy support for Signup | auth_password_policy, portal |
| `cloud_storage` | CHANGED-MAJOR | 68/70 |  | Store chatter attachments in the cloud | base_setup, mail |
| `cloud_storage_azure` | CHANGED-MAJOR | 56/62 |  | Store chatter attachments in the Azure cloud | cloud_storage |
| `cloud_storage_google` | CHANGED-MAJOR | 58/64 |  | Store chatter attachments in the Google cloud | cloud_storage |
| `cloud_storage_migration` | CHANGED-MAJOR | 57/62 |  | Migrate local attachments to cloud storage | cloud_storage |
| `html_builder` | CHANGED-MAJOR | 411/866 |  | Generic html builder | html_editor |
| `mail_group` | CHANGED-MAJOR | 66/88 |  | Manage your mailing lists | mail, portal |
| `pos_event` | CHANGED-MAJOR | 96/113 |  | Link module between Point of Sale and Event | point_of_sale, event_product |
| `pos_event_sale` | CHANGED-MAJOR | 60/61 |  | Link module between pos_sale and pos_event | pos_event, pos_sale, event_sale |
| `pos_online_payment` | CHANGED-MAJOR | 85/84 |  | Point of Sale online payment | point_of_sale, account_payment |
| `pos_repair` | CHANGED-MAJOR | 54/58 |  | Link module between Point of Sale and Repair | pos_stock, repair |
| `stock_fleet` | CHANGED-MAJOR | 64/68 |  | Stock Transport Management | stock, fleet |
| `website_mail_group` | CHANGED-MAJOR | 54/65 |  | Add a website snippet for the mail groups. | mail_group, website |

## Hidden (55)

| Module | Status | Files changed | App | Summary | Depends |
|---|---|---|---|---|---|
| `base_report_paper_muncher` | 🆕 NEW |  |  | Paper Muncher Engine | base_setup |
| `base_report_wkhtmltox` | 🆕 NEW |  |  | wkhtmltopdf rendering engine |  |
| `populate` | 🆕 NEW |  |  | Generate synthetic data for an Odoo database | base |
| `pos_sale_delivery` | 🆕 NEW |  |  | POS - Sales Delivery | pos_sale, stock_delivery |
| `iot_base` | ❌ REMOVED |  |  | IoT Base | web |
| `iot_box_image` | ❌ REMOVED |  |  | Build tools for the IoT Box image |  |
| `transifex` | ❌ REMOVED |  |  | Add a link to edit a translation in Transifex | base, web |
| `api_doc` | CHANGED-MAJOR | 33/88 |  | API Documentation | web |
| `attachment_indexation` | CHANGED-MAJOR | 54/56 |  | Attachments List and Document Indexation | web |
| `auth_ldap` | CHANGED-MAJOR | 75/78 |  | Authentication via LDAP | base, base_setup |
| `auth_oauth` | CHANGED-MAJOR | 78/80 |  | OAuth2 Authentication | base, web, base_setup, auth_signup |
| `auth_passkey` | CHANGED-MAJOR | 65/129 |  | Log in with a Passkey | base_setup, web |
| `auth_passkey_portal` | CHANGED-MAJOR | 56/58 |  | Passkeys for portal users | auth_passkey, portal |
| `auth_password_policy` | CHANGED-MAJOR | 59/64 |  | Implement basic password policy configuration & check | base_setup, web |
| `auth_password_policy_signup` | CHANGED-MAJOR | 53/57 |  | Password Policy support for Signup | auth_password_policy, auth_signup |
| `auth_signup` | CHANGED-MAJOR | 78/86 |  | Signup | base_setup, mail, web |
| `auth_timeout` | CHANGED-MAJOR | 64/62 |  | Ask for authentication after user inactivity | auth_totp, auth_totp_mail, auth_passkey, bus |
| `auth_totp_portal` | CHANGED-MAJOR | 58/64 |  | TOTPortal | portal, auth_totp |
| `base_import` | CHANGED-MAJOR | 92/103 |  | Base import | web |
| `base_import_module` | CHANGED-MAJOR | 82/85 |  | Base import module | web |
| `base_install_request` | CHANGED-MAJOR | 60/60 |  | Base - Module Install Request | mail |
| `base_setup` | CHANGED-MAJOR | 77/85 |  | Initial Setup Tools | base, web |
| `base_sparse_field` | CHANGED-MAJOR | 70/71 |  | Implementation of sparse fields. | base |
| `bus` | CHANGED-MAJOR | 155/141 |  | IM Bus | base, web |
| `certificate` | CHANGED-MAJOR | 61/66 |  | Manage certificate | base_setup |
| `google_account` | CHANGED-MAJOR | 71/55 |  | Google Users | base_setup |
| `google_address_autocomplete` | CHANGED-MAJOR | 57/72 |  | Assist with automatic completion & suggestions when filling address | web |
| `google_gmail` | CHANGED-MAJOR | 55/69 |  | Google Gmail | mail |
| `google_recaptcha` | CHANGED-MAJOR | 54/60 |  | Google reCAPTCHA integration | base_setup |
| `hr_skills_event` | CHANGED-MAJOR | 54/60 |  | Link training events to resume of your employees | hr_skills, event |
| `html_editor` | CHANGED-MAJOR | 510/636 |  | A Html Editor component and plugin system. | base, bus, web |
| `http_routing` | CHANGED-MAJOR | 58/63 |  | Web Routing | web |
| `iap` | CHANGED-MAJOR | 82/85 |  | Basic models and helpers to support In-App Purchase. | web, base_setup |
| `iap_crm` | CHANGED-MAJOR | 51/53 |  | Bridge between IAP and CRM | crm, iap_mail |
| `iap_mail` | CHANGED-MAJOR | 53/58 |  | Bridge between IAP and mail | iap, mail |
| `iot_drivers` | CHANGED-MAJOR | 93/79 |  | Connect the Web Client to Hardware Peripherals |  |
| `microsoft_account` | CHANGED-MAJOR | 54/57 |  | Microsoft Users | base_setup |
| `microsoft_outlook` | CHANGED-MAJOR | 56/68 |  | Microsoft Outlook | mail |
| `odoo/addons/base` | CHANGED-MAJOR | 385/660 |  | Base |  |
| `onboarding` | CHANGED-MAJOR | 56/70 |  | Onboarding Toolbox | web |
| `partner_autocomplete` | CHANGED-MAJOR | 79/82 |  | Auto-complete partner companies' data | iap_mail |
| `payment` | CHANGED-MAJOR | 140/338 |  | The payment engine used by payment provider modules. | onboarding, portal |
| `phone_validation` | CHANGED-MAJOR | 73/89 |  | Validate and format phone numbers | base, mail |
| `portal` | CHANGED-MAJOR | 122/142 |  | Customer Portal | auth_signup, base_address_extended, html_editor, http_routing, mail, web |
| `privacy_lookup` | CHANGED-MAJOR | 56/62 |  | Privacy | mail |
| `resource` | CHANGED-MAJOR | 114/130 |  | Resource | base, web |
| `resource_mail` | CHANGED-MAJOR | 66/70 |  | Resource Mail | resource, mail |
| `sale_project_stock_account` | CHANGED-MAJOR | 53/55 |  | Technical Bridge | sale_project, project_stock_account |
| `sms_twilio` | CHANGED-MAJOR | 64/77 |  | Send SMS messages using Twilio | sms |
| `snailmail` | CHANGED-MAJOR | 74/90 |  | Snail Mail | iap_mail, mail |
| `snailmail_account` | CHANGED-MAJOR | 57/66 |  | Snail Mail - Account | account, snailmail |
| `web` | CHANGED-MAJOR | 1605/2429 |  | Web | base |
| `web_hierarchy` | CHANGED-MAJOR | 65/72 |  | Web Hierarchy | web |
| `web_tour` | CHANGED-MAJOR | 85/96 |  | Tours | web |
| `web_unsplash` | CHANGED-MAJOR | 70/82 |  | Find free high-resolution images from Unsplash | base_setup, html_editor |

## Localization (248)

| Module | Status | Files changed | App | Summary | Depends |
|---|---|---|---|---|---|
| `l10n_be_pos` | 🆕 NEW |  |  | Link module between point_of_sale and l10n_be | point_of_sale, l10n_be, account |
| `l10n_eg_edi_pos` | 🆕 NEW |  |  | Submit POS receipts to the Egyptian Tax Authority | point_of_sale, l10n_eg_edi_eta |
| `l10n_es_website_sale` | 🆕 NEW |  |  | Spain - ECommerce | l10n_es, website_sale |
| `l10n_eu_account_vies` | 🆕 NEW |  |  | VAT VIES Validation | account |
| `l10n_fr_payment` | 🆕 NEW |  |  | Applies CAWL/Worldline branding rules for French companies. | l10n_fr, payment |
| `l10n_gr_edi_delivery_note` | 🆕 NEW |  |  | Transmit Greece myDATA EDI for Delivery Notes | l10n_gr_edi, stock, sale, sale_stock |
| `l10n_id_pos_self_order_qris` | 🆕 NEW |  |  | Accept QRIS QR code payments in a kiosk. | pos_self_order, l10n_id_pos |
| `l10n_in_boe` | 🆕 NEW |  |  | Indian - Bill Of Entry | l10n_in, stock_landed_costs |
| `l10n_kr_sale` | 🆕 NEW |  |  | Republic of Korea - Sales | sale, l10n_kr |
| `l10n_mk` | 🆕 NEW |  |  | North Macedonia - Accounting | account |
| `l10n_mm` | 🆕 NEW |  |  | Myanmar - Accounting | account_qr_code_emv, l10n_account_withholding_tax |
| `l10n_ph_invoice` | 🆕 NEW |  |  | Apply Philippine SC/PWD discount privileges on customer invoices and credit notes. | l10n_ph |
| `l10n_ph_sale` | 🆕 NEW |  |  | Apply Philippine SC/PWD discount privileges on quotations and sale orders. | l10n_ph_invoice, sale |
| `l10n_pk_edi` | 🆕 NEW |  |  | Electronic Invoicing for Pakistan FBR(v1.12) | account_debit_note, iap, l10n_pk, stock_delivery |
| `l10n_pk_edi_pos` | 🆕 NEW |  |  | Pakistan - Point of Sale | l10n_pk, pos_discount, iap, stock_delivery |
| `l10n_tw_edi_ecpay_sale` | 🆕 NEW |  |  | ECPay E-invoice bridge module for Sales | sale, l10n_tw_edi_ecpay |
| `l10n_vn_edi_viettel_stock` | 🆕 NEW |  |  | Delivery E-invoicing using SInvoice by Viettel | l10n_vn_edi_viettel, stock |
| `l10n_cn_city` | ❌ REMOVED |  |  | China - City Data | l10n_cn, base_address_extended |
| `l10n_dk_nemhandel` | ❌ REMOVED |  |  | This module is used to send/receive documents with Nemhandel | account_edi_proxy_client, account_edi_ubl_cii, l10n_dk |
| `l10n_dk_nemhandel_response` | ❌ REMOVED |  |  | This module is used to send/receive responses to documents received/sent with Nemhandel | l10n_dk_nemhandel |
| `l10n_dk_oioubl` | ❌ REMOVED |  |  | E-Invoicing, Offentlig Information Online Universal Business Language | account_edi_ubl_cii, l10n_dk |
| `l10n_ec_stock` | ❌ REMOVED |  |  | Ecuador - Stock | l10n_ec, stock |
| `l10n_fr_hr_work_entry_holidays` | ❌ REMOVED |  |  | Management of leaves for part-time workers in France | l10n_fr_hr_holidays, hr_work_entry_holidays |
| `l10n_hu_edi_receive` | ❌ REMOVED |  |  | Hungary - E-invoicing Receive Vendor Bills | l10n_hu_edi |
| `l10n_latam_base` | ❌ REMOVED |  |  | LATAM Identification Types | contacts, base_vat |
| `l10n_lk_invoice` | ❌ REMOVED |  |  | Sri Lanka tax invoice sequence format and report layout. | l10n_lk |
| `l10n_pl_bank_verification` | ❌ REMOVED |  |  | Poland - Accounting - Bank Account Verification | l10n_pl |
| `l10n_ro_cpv_code` | ❌ REMOVED |  |  | Romania - CPV Code | l10n_ro_edi |
| `l10n_ro_edi_stock_batch` | ❌ REMOVED |  |  | Romania - E-Transport Batch Pickings | l10n_ro_edi_stock, stock_picking_batch |
| `l10n_sa_withholding_tax` | ❌ REMOVED |  |  | Saudi Arabia - Withholding Tax | l10n_account_withholding_tax, l10n_sa |
| `l10n_tr_nilvera` | ❌ REMOVED |  |  | Türkiye - Nilvera | l10n_tr, account_edi_ubl_cii |
| `l10n_tr_nilvera_base_vat` | ❌ REMOVED |  |  | Türkiye - Nilvera/Base VAT | l10n_tr_nilvera, base_vat |
| `l10n_tr_nilvera_edispatch` | ❌ REMOVED |  |  | Türkiye - e-Irsaliye (e-Dispatch) | l10n_tr_nilvera, stock, stock_account |
| `l10n_tr_nilvera_einvoice` | ❌ REMOVED |  |  | Türkiye - Nilvera E-Invoice | l10n_tr_nilvera, account_edi_ubl_cii |
| `l10n_tr_nilvera_einvoice_extended` | ❌ REMOVED |  |  | Türkiye - Nilvera E-Invoice Extended | l10n_tr_nilvera_einvoice, contacts |
| `l10n_uy_pos` | ❌ REMOVED |  |  | Uruguayan - Point of Sale | l10n_uy, point_of_sale |
| `l10n_account_edi_ubl_cii_tests` | CHANGED-MAJOR | 16/53 |  | Testing the Import/Export invoices with UBL/CII | account_edi_ubl_cii, l10n_fr_account, l10n_be, l10n_de, l10n_nl, l10n_au |
| `l10n_account_withholding_tax` | CHANGED-MAJOR | 30/35 |  | Withholding Tax | account |
| `l10n_account_withholding_tax_pos` | CHANGED | 2/4 |  | Withholding Tax on Payment - PoS | l10n_account_withholding_tax, point_of_sale |
| `l10n_ae` | CHANGED-MAJOR | 11/17 |  | United Arab Emirates - Accounting | account, l10n_gcc_invoice |
| `l10n_ae_pos` | CHANGED | 6/9 |  | United Arab Emirates - Point of Sale | l10n_gcc_pos, l10n_ae |
| `l10n_anz_ubl_pint` | CHANGED | 3/9 |  | Australia & New Zealand - UBL PINT | account_edi_ubl_cii |
| `l10n_ar` | CHANGED-MAJOR | 59/90 |  | Argentina - Accounting | l10n_latam_invoice_document, account |
| `l10n_ar_pos` | CHANGED-MAJOR | 13/20 |  | Argentinean - Point of Sale with AR Doc | l10n_ar, point_of_sale |
| `l10n_ar_stock` | CHANGED-MAJOR | 15/19 |  | Argentinean - Stock | l10n_ar, stock_account |
| `l10n_ar_website_sale` | CHANGED-MAJOR | 10/13 |  | Argentinean eCommerce | website_sale, l10n_ar |
| `l10n_ar_withholding` | CHANGED-MAJOR | 40/33 |  | Argentina - Payment Withholdings | l10n_ar, l10n_latam_check, l10n_account_withholding_tax |
| `l10n_at` | CHANGED | 7/16 |  | Austrian Standardized Charts & Tax | account, account_edi_ubl_cii, l10n_din5008 |
| `l10n_au` | CHANGED-MAJOR | 27/29 |  | Australia - Accounting | account |
| `l10n_bd` | CHANGED-MAJOR | 15/15 |  | Bangladesh - Accounting | account, l10n_account_withholding_tax |
| `l10n_be` | CHANGED-MAJOR | 25/27 |  | Belgium - Accounting | account, account_edi_ubl_cii |
| `l10n_be_pos_restaurant` | CHANGED | 7/10 |  | Belgian POS Restaurant Localization | pos_restaurant, l10n_be |
| `l10n_be_pos_sale` | CHANGED | 7/12 |  | Link module between pos_sale and l10n_be | pos_sale, l10n_be |
| `l10n_bf` | CHANGED | 5/15 |  | Burkina Faso - Accounting | l10n_syscohada, account |
| `l10n_bg` | CHANGED | 7/12 |  | Bulgaria - Accounting | account |
| `l10n_bg_ledger` | CHANGED | 3/9 |  | Bulgaria - Report ledger | l10n_bg |
| `l10n_bh` | CHANGED-MAJOR | 10/13 |  | Bahrain - Accounting | account, l10n_gcc_invoice |
| `l10n_bj` | CHANGED | 5/15 |  | Benin - Accounting | l10n_syscohada, account |
| `l10n_bo` | CHANGED | 7/12 |  | Bolivia - Accounting | account |
| `l10n_br` | CHANGED-MAJOR | 33/50 |  | Brazilian - Accounting | account, account_qr_code_emv, l10n_latam_invoice_document |
| `l10n_br_sales` | CHANGED | 5/9 |  | Brazil - Sale | l10n_br, sale |
| `l10n_br_website_sale` | CHANGED | 6/5 |  | Brazil - Website Sale | l10n_br, website_sale |
| `l10n_ca` | CHANGED-MAJOR | 19/24 |  | Canada - Accounting | account |
| `l10n_cd` | CHANGED | 6/15 |  | Democratic Republic of the Congo - Accounting | l10n_syscohada, account |
| `l10n_cf` | CHANGED | 5/15 |  | Central African Republic - Accounting | l10n_syscohada, account |
| `l10n_cg` | CHANGED | 5/15 |  | Congo - Accounting | l10n_syscohada, account |
| `l10n_ch` | CHANGED-MAJOR | 27/57 |  | Switzerland - Accounting | account, account_edi_ubl_cii, l10n_din5008 |
| `l10n_ch_pos` | CHANGED | 7/11 |  | Swiss - Point of Sale | l10n_ch, point_of_sale |
| `l10n_ci` | CHANGED | 5/15 |  | Ivory Coast - Accounting | l10n_syscohada, account |
| `l10n_cl` | CHANGED-MAJOR | 28/51 |  | Chile - Accounting | contacts, l10n_latam_invoice_document, uom, account |
| `l10n_cm` | CHANGED | 6/15 |  | Cameroon - Accounting | l10n_syscohada, account |
| `l10n_cn` | CHANGED-MAJOR | 36/36 |  | China - Accounting | base, account |
| `l10n_co` | CHANGED-MAJOR | 16/16 |  | Colombia - Accounting | account_debit_note, account |
| `l10n_co_pos` | CHANGED | 8/14 |  | Colombian - Point of Sale | l10n_co, point_of_sale |
| `l10n_cr` | CHANGED | 4/10 |  | Costa Rica - Accounting | account |
| `l10n_cy` | CHANGED | 8/14 |  | Cyprus - Accounting | account, account_edi_ubl_cii |
| `l10n_cz` | CHANGED-MAJOR | 24/29 |  | Czech - Accounting | account, account_edi_ubl_cii |
| `l10n_de` | CHANGED-MAJOR | 18/35 |  | Germany - Accounting | l10n_din5008, account, account_edi_ubl_cii |
| `l10n_din5008` | CHANGED | 7/17 |  | DIN 5008 | account |
| `l10n_din5008_expense` | CHANGED | 5/7 |  | DIN 5008 - Expenses | l10n_din5008, hr_expense |
| `l10n_din5008_purchase` | CHANGED | 6/7 |  | DIN 5008 - Purchase | l10n_din5008, purchase |
| `l10n_din5008_repair` | CHANGED | 6/10 |  | DIN 5008 - Repair | l10n_din5008, repair |
| `l10n_din5008_sale` | CHANGED | 6/8 |  | DIN 5008 - Sale | l10n_din5008, sale |
| `l10n_din5008_stock` | CHANGED | 6/8 |  | DIN 5008 - Stock | l10n_din5008, stock |
| `l10n_dk` | CHANGED-MAJOR | 36/66 |  | Denmark - Accounting | account, account_edi_proxy_client, account_edi_ubl_cii |
| `l10n_dk_fik` | CHANGED | 4/8 |  | Use FIK Number as Payment reference | l10n_dk |
| `l10n_do` | CHANGED-MAJOR | 21/23 |  | Dominican Republic - Accounting | account, l10n_latam_invoice_document |
| `l10n_dz` | CHANGED | 7/13 |  | Algeria - Accounting | account |
| `l10n_ec` | CHANGED-MAJOR | 21/39 |  | Ecuadorian Accounting | base, account_debit_note, l10n_latam_invoice_document, account |
| `l10n_ec_sale` | CHANGED | 8/13 |  | Ecuador - Sale | l10n_ec, sale |
| `l10n_ee` | CHANGED | 9/18 |  | Estonia - Accounting | account, account_edi_ubl_cii |
| `l10n_eg` | CHANGED-MAJOR | 13/17 |  | Egypt - Accounting | account, l10n_account_withholding_tax |
| `l10n_eg_edi_eta` | CHANGED-MAJOR | 42/43 |  | Egypt Tax Authority Invoice Integration | l10n_eg |
| `l10n_es` | CHANGED-MAJOR | 62/52 |  | Spain - Accounting (PGCE 2008) | account, account_edi_ubl_cii |
| `l10n_es_edi_facturae` | CHANGED-MAJOR | 34/49 |  | Spain - Facturae EDI | certificate, l10n_es |
| `l10n_es_edi_sii` | CHANGED-MAJOR | 21/25 |  | Spain - SII EDI Suministro de Libros | certificate, l10n_es |
| `l10n_es_edi_tbai` | CHANGED-MAJOR | 31/60 |  | Spain - TicketBAI | l10n_es, certificate |
| `l10n_es_edi_tbai_pos` | CHANGED-MAJOR | 18/23 |  | Spain - Point of Sale + TicketBAI | l10n_es_edi_tbai, point_of_sale |
| `l10n_es_edi_verifactu` | CHANGED-MAJOR | 38/57 |  | Module for sending Spanish Veri*Factu XML to the AEAT | l10n_es, certificate |
| `l10n_es_edi_verifactu_pos` | CHANGED-MAJOR | 18/26 |  | Add Veri*Factu support to Point of Sale | l10n_es_edi_verifactu, point_of_sale |
| `l10n_es_pos` | CHANGED-MAJOR | 15/25 |  | Spanish localization for Point of Sale | point_of_sale, l10n_es |
| `l10n_et` | CHANGED | 4/11 |  | Ethiopia - Accounting | account |
| `l10n_eu_oss` | CHANGED-MAJOR | 26/34 |  | EU One Stop Shop (OSS) | account |
| `l10n_fi` | CHANGED-MAJOR | 12/19 |  | Finland - Accounting | account, account_edi_ubl_cii |
| `l10n_fi_sale` | CHANGED | 3/6 |  | Finland - Sale | l10n_fi, sale |
| `l10n_fr` | CHANGED | 7/10 |  | France - Localizations | base |
| `l10n_fr_account` | CHANGED-MAJOR | 36/39 |  | France - Accounting | account, account_edi_ubl_cii, l10n_fr |
| `l10n_fr_facturx_chorus_pro` | CHANGED | 8/16 |  | France - BIS3 integration for Chorus Pro | account, account_edi_ubl_cii, l10n_fr_account |
| `l10n_fr_hr_holidays` | CHANGED-MAJOR | 13/14 |  | Management of leaves for part-time workers in France | hr_holidays |
| `l10n_fr_pdp` | CHANGED-MAJOR | 58/77 |  | France - E-Invoicing (Approved Platform) | l10n_fr_account, account_peppol, iap |
| `l10n_fr_pdp_pos` | CHANGED | 6/9 |  | PDP Flux 10 e-reporting for POS | l10n_fr_pdp, point_of_sale |
| `l10n_fr_pos_cert` | CHANGED-MAJOR | 26/39 |  | France - VAT Anti-Fraud Certification for Point of Sale (CGI 286 I-3 bis) | l10n_fr_account, point_of_sale |
| `l10n_ga` | CHANGED | 5/15 |  | Gabon - Accounting | l10n_syscohada, account |
| `l10n_gcc_invoice` | CHANGED | 4/14 |  | Gulf Cooperation Council - Invoice | account |
| `l10n_gcc_invoice_stock_account` | CHANGED | 1/3 |  | Gulf Cooperation Council WMS Accounting | l10n_gcc_invoice, stock_account |
| `l10n_gcc_pos` | CHANGED-MAJOR | 11/15 |  | Gulf Cooperation Council - Point of Sale | point_of_sale, l10n_gcc_invoice |
| `l10n_ge` | CHANGED-MAJOR | 11/13 |  | Georgian accounting localization package | account |
| `l10n_gf` | CHANGED | 1/3 |  | Guyana - Accounting | l10n_fr_account, account |
| `l10n_gn` | CHANGED | 5/15 |  | Guinea - Accounting | l10n_syscohada, account |
| `l10n_gp` | CHANGED | 1/4 |  | Guadeloupe - Accounting | l10n_fr_account, account |
| `l10n_gq` | CHANGED | 7/17 |  | Guinea Equatorial - Accounting | l10n_syscohada, account |
| `l10n_gr` | CHANGED-MAJOR | 10/12 |  | Greece - Accounting | account, account_edi_ubl_cii |
| `l10n_gr_edi` | CHANGED-MAJOR | 26/40 |  | Connect to myDATA API implementation for Greece | account_edi_ubl_cii, l10n_gr |
| `l10n_gr_edi_e_invoo` | CHANGED | 6/15 |  | Greece - myDATA E-invoicing through e-invoo | account_edi_proxy_client, l10n_gr_edi |
| `l10n_gt` | CHANGED-MAJOR | 13/15 |  | Guatemala - Accounting | account |
| `l10n_gw` | CHANGED | 5/15 |  | Guinea-Bissau - Accounting | l10n_syscohada, account |
| `l10n_hk` | CHANGED-MAJOR | 11/16 |  | Hong Kong - Accounting | account_qr_code_emv, account |
| `l10n_hn` | CHANGED | 4/10 |  | Honduras - Accounting | base, account |
| `l10n_hr` | CHANGED | 7/13 |  | Croatia - Accounting (Euro) | account |
| `l10n_hr_edi` | CHANGED-MAJOR | 24/51 |  | Croatia - e-invoicing | l10n_hr, account_edi_ubl_cii |
| `l10n_hr_kuna` | CHANGED | 4/12 |  | Croatia - Accounting (Kuna) | account |
| `l10n_hu` | CHANGED-MAJOR | 12/15 |  | Hungary - Accounting | account |
| `l10n_hu_edi` | CHANGED-MAJOR | 50/96 |  | Hungary - E-invoicing | account_debit_note, l10n_hu |
| `l10n_id` | CHANGED-MAJOR | 20/28 |  | Indonesian - Accounting | account |
| `l10n_id_efaktur_coretax` | CHANGED-MAJOR | 21/33 |  | Indonesia E-faktur (Coretax) | l10n_id |
| `l10n_id_pos` | CHANGED | 8/14 |  | Indonesia - Point of Sale | l10n_id, point_of_sale |
| `l10n_ie` | CHANGED | 6/14 |  | Ireland - Accounting | account, account_edi_ubl_cii |
| `l10n_il` | CHANGED | 6/14 |  | Israel - Accounting | account |
| `l10n_in` | CHANGED-MAJOR | 69/87 |  | Indian - Accounting | account_tax_python, account_debit_note, account, l10n_account_withholding_tax, iap |
| `l10n_in_edi` | CHANGED-MAJOR | 14/25 |  | Indian - E-invoicing | l10n_in |
| `l10n_in_ewaybill` | CHANGED-MAJOR | 18/30 |  | Indian - E-waybill | l10n_in |
| `l10n_in_ewaybill_irn` | CHANGED | 4/10 |  | Indian - E-waybill thru IRN | l10n_in_ewaybill, l10n_in_edi |
| `l10n_in_ewaybill_stock` | CHANGED | 9/15 |  | Indian - E-waybill Stock | l10n_in_stock, l10n_in_ewaybill |
| `l10n_in_hr_holidays` | CHANGED-MAJOR | 17/18 |  | Leave Management of Indian Localization | hr_holidays |
| `l10n_in_pos` | CHANGED-MAJOR | 44/56 |  | Indian - Point of Sale | l10n_in, point_of_sale |
| `l10n_in_purchase_stock` | CHANGED | 4/8 |  | Get warehouse address if the bill is created from Purchase Order | l10n_in_stock, purchase_stock |
| `l10n_in_sale` | CHANGED | 9/14 |  | Indian - Sale Report(GST) | l10n_in, sale |
| `l10n_in_sale_stock` | CHANGED | 4/8 |  | Get warehouse address if the invoice is created from Sale Order | l10n_in_sale, l10n_in_stock, sale_stock |
| `l10n_in_stock` | CHANGED | 4/10 |  | Indian - Stock Report(GST) | l10n_in, stock, stock_account |
| `l10n_iq` | CHANGED | 8/10 |  | Iraq - Accounting | account |
| `l10n_it` | CHANGED-MAJOR | 15/34 |  | Italy - Accounting | account, account_edi_ubl_cii |
| `l10n_it_edi` | CHANGED-MAJOR | 68/118 |  | Italy - E-invoicing | l10n_it, account_edi_proxy_client, account_debit_note |
| `l10n_it_edi_doi` | CHANGED-MAJOR | 13/26 |  | Italy - Declaration of Intent | l10n_it_edi, sale |
| `l10n_it_edi_sale` | CHANGED | 4/9 |  | Italy - Sale E-invoicing | l10n_it_edi, sale |
| `l10n_it_stock_ddt` | CHANGED-MAJOR | 12/15 |  | Italy - Stock DDT | l10n_it_edi, stock_delivery, stock_account |
| `l10n_jo` | CHANGED-MAJOR | 10/13 |  | Jordan - Accounting | account |
| `l10n_jo_edi` | CHANGED-MAJOR | 15/33 |  | Electronic Invoicing for Jordan UBL 2.1 | account_edi_ubl_cii, l10n_jo |
| `l10n_jo_edi_pos` | CHANGED-MAJOR | 18/30 |  | Jordan Accounting EDI for POS | l10n_jo_edi, pos_edi_ubl |
| `l10n_jp` | CHANGED-MAJOR | 23/25 |  | Japan - Accounting | account |
| `l10n_jp_ubl_pint` | CHANGED | 4/11 |  | Japan - UBL PINT | account_edi_ubl_cii |
| `l10n_ke` | CHANGED-MAJOR | 10/22 |  | Kenya - Accounting | account |
| `l10n_ke_edi_tremol` | CHANGED-MAJOR | 10/24 |  | Kenya Tremol Device EDI Integration | l10n_ke |
| `l10n_kh` | CHANGED-MAJOR | 12/16 |  | Cambodia - Accounting | account_qr_code_emv, l10n_account_withholding_tax |
| `l10n_km` | CHANGED | 6/16 |  | Comoros - Accounting | l10n_syscohada, account |
| `l10n_kr` | CHANGED-MAJOR | 18/20 |  | Republic of Korea - Accounting | account |
| `l10n_kw` | CHANGED | 7/8 |  | Kuwait - Accounting | account, l10n_gcc_invoice |
| `l10n_kz` | CHANGED | 6/12 |  | Kazakhstan - Accounting | account |
| `l10n_latam_check` | CHANGED-MAJOR | 19/28 |  | Checks Management | account |
| `l10n_latam_invoice_document` | CHANGED-MAJOR | 12/26 |  | LATAM Document Types | account, account_debit_note |
| `l10n_lb_account` | CHANGED-MAJOR | 10/12 |  | Lebanon - Accounting | account |
| `l10n_lk` | CHANGED-MAJOR | 16/22 |  | Provides accounting localizations for Sri Lanka. | account, l10n_account_withholding_tax |
| `l10n_lt` | CHANGED | 7/16 |  | Lithuania - Accounting | account, account_edi_ubl_cii |
| `l10n_lu` | CHANGED | 9/21 |  | Luxembourg - Accounting | account, account_edi_ubl_cii |
| `l10n_lv` | CHANGED | 8/14 |  | Latvia - Accounting | account, account_edi_ubl_cii |
| `l10n_ma` | CHANGED-MAJOR | 20/19 |  | Morocco - Accounting | base, account |
| `l10n_mc` | CHANGED | 2/4 |  | Monaco - Accounting | l10n_fr_account, account |
| `l10n_ml` | CHANGED | 5/15 |  | Mali - Accounting | l10n_syscohada, account |
| `l10n_mn` | CHANGED | 6/13 |  | Mongolia - Accounting | account |
| `l10n_mq` | CHANGED | 1/4 |  | Martinique - Accounting | l10n_fr_account, account |
| `l10n_mr` | CHANGED-MAJOR | 10/13 |  | Mauritania - Accounting | account |
| `l10n_mt` | CHANGED | 4/12 |  | Malta - Accounting | account, account_edi_ubl_cii |
| `l10n_mt_pos` | CHANGED | 6/7 |  | Malta - Point of Sale | point_of_sale |
| `l10n_mu_account` | CHANGED | 9/15 |  | Mauritius - Accounting | account |
| `l10n_mx` | CHANGED-MAJOR | 20/31 |  | Mexico - Accounting | account |
| `l10n_my` | CHANGED-MAJOR | 14/20 |  | Malaysia - Accounting | account, account_tax_python |
| `l10n_my_edi` | CHANGED-MAJOR | 42/59 |  | E-invoicing using MyInvois | l10n_my, l10n_my_ubl_pint, account_edi_proxy_client |
| `l10n_my_edi_pos` | CHANGED-MAJOR | 21/26 |  | Consolidated E-invoicing using MyInvois | l10n_my_edi, point_of_sale |
| `l10n_my_ubl_pint` | CHANGED | 9/16 |  | Malaysia - UBL PINT | account_edi_ubl_cii |
| `l10n_mz` | CHANGED | 8/12 |  | Mozambique - Accounting | base, account |
| `l10n_ne` | CHANGED | 5/15 |  | Niger - Accounting | l10n_syscohada, account |
| `l10n_ng` | CHANGED | 4/10 |  | Nigeria - Accounting | account |
| `l10n_nl` | CHANGED-MAJOR | 10/24 |  | Netherlands - Accounting | account, account_edi_ubl_cii |
| `l10n_no` | CHANGED-MAJOR | 10/18 |  | Norway - Accounting | account, account_edi_ubl_cii |
| `l10n_nz` | CHANGED-MAJOR | 10/15 |  | New Zealand - Accounting | account |
| `l10n_om` | CHANGED | 8/12 |  | Oman - Accounting | account, l10n_gcc_invoice |
| `l10n_pa` | CHANGED-MAJOR | 26/30 |  | Panama - Accounting | account, base_address_extended, contacts, l10n_latam_invoice_document |
| `l10n_pe` | CHANGED-MAJOR | 31/39 |  | Peru - Accounting | l10n_latam_invoice_document, account_debit_note, account |
| `l10n_pe_pos` | CHANGED-MAJOR | 15/22 |  | Peruvian - Point of Sale with Pe Doc | l10n_pe, point_of_sale |
| `l10n_ph` | CHANGED-MAJOR | 37/34 |  | This is the module to manage the accounting chart for The Philippines. | account, l10n_account_withholding_tax |
| `l10n_pk` | CHANGED-MAJOR | 26/23 |  | Pakistan - Accounting | account, account_tax_python, l10n_account_withholding_tax, product |
| `l10n_pl` | CHANGED-MAJOR | 22/38 |  | Poland - Accounting | account, account_edi_ubl_cii |
| `l10n_pl_edi` | CHANGED | 11/40 |  | Support for FA(3) electronic invoices in Poland via KSeF | l10n_pl, certificate |
| `l10n_pl_edi_jst` | CHANGED | 2/12 |  | Support for Local Government Unit (LGU) in the FA(3) format | l10n_pl, l10n_pl_edi |
| `l10n_pt` | CHANGED | 8/17 |  | Portugal - Accounting | base, account, account_edi_ubl_cii |
| `l10n_qa` | CHANGED | 7/8 |  | Qatar - Accounting | account, l10n_gcc_invoice |
| `l10n_re` | CHANGED | 1/4 |  | Reunion - Accounting | l10n_fr_account, account |
| `l10n_ro` | CHANGED-MAJOR | 10/15 |  | Romania - Accounting | account, account_edi_ubl_cii |
| `l10n_ro_edi` | CHANGED-MAJOR | 26/43 |  | E-Invoice implementation for Romania | account_edi_ubl_cii, l10n_ro |
| `l10n_ro_edi_stock` | CHANGED-MAJOR | 14/29 |  | Romania - E-Transport | stock_delivery, l10n_ro_edi |
| `l10n_rs` | CHANGED | 9/16 |  | Serbia - Accounting | account |
| `l10n_rs_edi` | CHANGED | 9/21 |  | E-Invoice implementation for Serbia | account_edi_ubl_cii, l10n_rs |
| `l10n_rw` | CHANGED | 7/14 |  | Rwanda - Accounting | account |
| `l10n_sa` | CHANGED-MAJOR | 31/41 |  | Saudi Arabia - Accounting | l10n_gcc_invoice, account, account_debit_note, l10n_account_withholding_tax |
| `l10n_sa_edi` | CHANGED-MAJOR | 59/63 |  | E-Invoicing, Universal Business Language | account_edi_ubl_cii, l10n_sa, certificate |
| `l10n_sa_edi_pos` | CHANGED-MAJOR | 23/24 |  | ZATCA E-Invoicing, support for PoS | l10n_sa_pos, l10n_sa_edi |
| `l10n_sa_pos` | CHANGED-MAJOR | 16/21 |  | Saudi Arabia - Point of Sale | l10n_gcc_pos, l10n_sa |
| `l10n_se` | CHANGED-MAJOR | 10/27 |  | Sweden - Accounting | account, account_edi_ubl_cii |
| `l10n_sg` | CHANGED-MAJOR | 25/33 |  | Singapore - Accounting | account_qr_code_emv, account, account_edi_ubl_cii, account_peppol |
| `l10n_sg_ubl_pint` | CHANGED | 8/10 |  | Singapore - UBL PINT | l10n_sg |
| `l10n_si` | CHANGED-MAJOR | 10/20 |  | Slovenian - Accounting | account, account_edi_ubl_cii |
| `l10n_sk` | CHANGED-MAJOR | 18/18 |  | Slovak - Accounting | account |
| `l10n_sn` | CHANGED | 5/15 |  | Sénégal - Accounting | l10n_syscohada, account |
| `l10n_syscohada` | CHANGED | 6/12 |  | OHADA - Accounting | account |
| `l10n_td` | CHANGED | 6/16 |  | Tchad - Accounting | l10n_syscohada, account |
| `l10n_test_pos_qr_payment` | CHANGED | 4/6 |  | POS QR Tests | point_of_sale, account_qr_code_sepa, l10n_be, l10n_ch, l10n_hk, l10n_br |
| `l10n_tg` | CHANGED | 5/15 |  | Togo - Accounting | l10n_syscohada, account |
| `l10n_th` | CHANGED-MAJOR | 41/46 |  | Thailand - Accounting | account_qr_code_emv, account, l10n_account_withholding_tax |
| `l10n_tn` | CHANGED | 7/13 |  | Tunisia - Accounting | account |
| `l10n_tr` | CHANGED-MAJOR | 19/31 |  | Türkiye - Accounting | account, contacts |
| `l10n_tw` | CHANGED-MAJOR | 11/17 |  | Taiwan - Accounting | account |
| `l10n_tw_edi_ecpay` | CHANGED-MAJOR | 11/29 |  | E-invoicing using ECpay | l10n_tw |
| `l10n_tw_edi_ecpay_pos` | CHANGED-MAJOR | 18/31 |  | ECpay E-invoice bridge module for POS | point_of_sale, l10n_tw_edi_ecpay |
| `l10n_tw_edi_ecpay_website_sale` | CHANGED-MAJOR | 18/18 |  | ECpay E-invoice bridge module for Ecommerce | website_sale, l10n_tw_edi_ecpay_sale |
| `l10n_tz_account` | CHANGED | 6/13 |  | Tanzania - Accounting | account |
| `l10n_ua` | CHANGED | 6/11 |  | Ukraine - Accounting | account |
| `l10n_ug` | CHANGED | 6/12 |  | Uganda - Accounting | account |
| `l10n_uk` | CHANGED | 8/16 |  | United Kingdom - Accounting | account |
| `l10n_us` | CHANGED-MAJOR | 13/15 |  | United States - Localizations | base, base_address_extended |
| `l10n_us_account` | CHANGED-MAJOR | 23/23 |  | United States - Accounting | l10n_us, account, base_address_extended |
| `l10n_uy` | CHANGED-MAJOR | 24/33 |  | Uruguay - Accounting | account, l10n_latam_invoice_document |
| `l10n_uz` | CHANGED-MAJOR | 14/14 |  | Uzbekistan - Accounting | account |
| `l10n_ve` | CHANGED | 5/10 |  | Venezuela - Accounting | account |
| `l10n_vn` | CHANGED-MAJOR | 14/21 |  | Vietnam - Accounting | account_qr_code_emv, account |
| `l10n_vn_edi_viettel` | CHANGED-MAJOR | 26/25 |  | E-invoicing using SInvoice by Viettel | l10n_vn |
| `l10n_vn_edi_viettel_pos` | CHANGED-MAJOR | 13/27 |  | POS E-invoicing using SInvoice by Viettel | l10n_vn_edi_viettel, point_of_sale |
| `l10n_yt` | CHANGED | 1/4 |  | Mayotte - Accounting | l10n_fr_account, account |
| `l10n_za` | CHANGED | 4/10 |  | South Africa - Accounting | account |
| `l10n_zm_account` | CHANGED | 5/12 |  | Zambia - Accounting | account |

## Test (49)

| Module | Status | Files changed | App | Summary | Depends |
|---|---|---|---|---|---|
| `odoo/addons/test_base` | 🆕 NEW |  |  | Test ORM | base |
| `odoo/addons/test_l10n` | 🆕 NEW |  |  | Test Localization | base |
| `odoo/addons/test_tests` | 🆕 NEW |  |  | Test Tests | base, web |
| `odoo/addons/test_translation` | 🆕 NEW |  |  | Test Translation | base, web_tour |
| `odoo/addons/test_web` | 🆕 NEW |  |  | test_search_panel | web, test_base |
| `test_populate` | 🆕 NEW |  |  | Test module for Odoo's Populate | populate |
| `test_translation_mode` | 🆕 NEW |  |  | In-context and interactive translation mode to streamline the module translation process using Weblate | web |
| `test_utm` | 🆕 NEW |  |  | UTM Tests: tests specific to the UTM module | utm |
| `odoo/addons/test_access_rights` | ❌ REMOVED |  |  | test of access rights and rules |  |
| `odoo/addons/test_action_bindings` | ❌ REMOVED |  |  | Test Action Bindings |  |
| `odoo/addons/test_auth_custom` | ❌ REMOVED |  |  | Tests that custom auth works & is not impaired by CORS |  |
| `odoo/addons/test_convert` | ❌ REMOVED |  |  | test_convert |  |
| `odoo/addons/test_converter` | ❌ REMOVED |  |  | test-field-converter | base |
| `odoo/addons/test_inherits` | ❌ REMOVED |  |  | test-inherits | base |
| `odoo/addons/test_mimetypes` | ❌ REMOVED |  |  | test mimetypes-guessing |  |
| `odoo/addons/test_orm` | ❌ REMOVED |  |  | Test ORM | base, web, web_tour |
| `odoo/addons/test_read_group` | ❌ REMOVED |  |  | test of (formatted/web)_read_group | base, web |
| `odoo/addons/test_rpc` | ❌ REMOVED |  |  | Test RPC | web, rpc |
| `odoo/addons/test_search_panel` | ❌ REMOVED |  |  | test_search_panel | web |
| `odoo/addons/test_testing_utilities` | ❌ REMOVED |  |  | Test testing utilities | base, web |
| `odoo/addons/test_translation_import` | ❌ REMOVED |  |  | test-translation-import | base |
| `account_test` | CHANGED-MAJOR | 66/72 |  | Accounting Consistency Tests | account |
| `odoo/addons/test_assetsbundle` | CHANGED | 6/33 |  | test-assetsbundle | base |
| `odoo/addons/test_data_module` | UNCHANGED | 0/1 |  | test module to test data only modules |  |
| `odoo/addons/test_data_module_install` | CHANGED | 1/4 |  | test installation of data module | test_data_module |
| `odoo/addons/test_http` | CHANGED-MAJOR | 29/34 |  | Test HTTP | web, web_tour, mail, rpc |
| `odoo/addons/test_inherit` | CHANGED | 9/13 |  | test-inherit | base, test_base |
| `odoo/addons/test_inherit_depends` | CHANGED | 2/5 |  | test-inherit-depends | test_inherit, test_base |
| `odoo/addons/test_inherits_depends` | CHANGED | 2/5 |  | test-inherits-depends | test_base |
| `odoo/addons/test_lint` | CHANGED-MAJOR | 32/30 |  | Test Lint | base |
| `odoo/addons/test_main_flows` | CHANGED | 7/9 |  | Test Main Flow | web_tour, crm, sale_timesheet, purchase_stock, mrp, account |
| `odoo/addons/test_uninstall` | CHANGED | 3/4 |  | test-uninstall | base |
| `test_base_automation` | CHANGED | 7/10 |  | Base Automation Tests: Ensure Flow Robustness | base_automation |
| `test_crm_full` | CHANGED | 2/5 |  | Test Full Crm Flow | crm, crm_iap_enrich, crm_iap_mine, crm_sms, event_crm, sale_crm, website_crm, website_crm_iap_reveal, website_crm_partner_assign, website_crm_livechat |
| `test_discuss_full` | CHANGED-MAJOR | 13/15 |  | Test of Discuss with all possible overrides installed. | calendar, crm, crm_livechat, hr_attendance, hr_fleet, hr_holidays, im_livechat, mail, mail_bot, microsoft_calendar, project_todo, website_livechat, website_sale, website_slides |
| `test_event_full` | CHANGED-MAJOR | 14/18 |  | Test Full Event Flow | event, event_booth, event_crm, event_crm_sale, event_sale, event_sms, payment_demo, website_event_booth_sale_exhibitor, website_event_exhibitor, website_event_sale, website_event_track, website_event_track_live, website_event_track_quiz |
| `test_html_field_history` | CHANGED | 3/7 |  | Test - html_field_history | html_editor |
| `test_import_export` | CHANGED-MAJOR | 19/25 |  | Base Import & Export Tests: Ensure Flow Robustness | web, base_import, website, test_base |
| `test_mail` | CHANGED-MAJOR | 51/64 |  | Mail Tests: performances and tests specific to mail | mail, test_base, phone_validation, mail_tracking |
| `test_mail_full` | CHANGED-MAJOR | 25/36 |  | Mail Tests: performances and tests specific to mail with all sub-modules | mail, mail_bot, mail_tracking_mass_mailing, mass_mailing, mass_mailing_sms, phone_validation, portal, rating, sms, test_mail, test_mail_sms, test_mass_mailing |
| `test_mail_sms` | CHANGED-MAJOR | 15/19 |  | SMS Tests: performances and tests specific to SMS | mail, mail_tracking_sms, sms, sms_twilio, test_base |
| `test_mass_mailing` | CHANGED-MAJOR | 26/27 |  | Mass Mail Tests: feature and performance tests for mass mailing | mail_tracking_mass_mailing, mass_mailing, mass_mailing_sms, sms_twilio, test_mail, test_mail_sms |
| `test_resource` | CHANGED-MAJOR | 14/15 |  | Test - Resource | resource |
| `test_sale_product_configurators` | CHANGED-MAJOR | 16/18 |  | Test Suite for Sale Product Configurator | event_sale, sale_management, sale_product_matrix |
| `test_sale_purchase_edi_ubl` | CHANGED | 1/4 |  | Sale & Purchase Order EDI Tests: Ensure Flow Robustness | purchase_edi_ubl_bis3, sale_edi_ubl |
| `test_spreadsheet` | CHANGED | 4/8 |  | Spreadsheet Test, mainly to test the mixin behavior | spreadsheet |
| `test_website` | CHANGED-MAJOR | 52/64 |  | Website Test, mainly for module install/uninstall tests | web_unsplash, website, theme_default |
| `test_website_modules` | CHANGED | 6/8 |  | Website Modules Test | theme_default, website, website_blog, website_event_sale, website_slides, website_livechat, website_crm_iap_reveal, website_sale |
| `test_website_slides_full` | CHANGED | 3/7 |  | Test Full eLearning Flow | website_sale_slides, website_slides_forum, website_slides_survey |
