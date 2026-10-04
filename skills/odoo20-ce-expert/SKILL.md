---
name: odoo20-ce-expert
description: "Answer questions about Odoo 20 Community Edition: what each module does, what changed since Odoo 19, what is Enterprise-only, how to upgrade 19→20 and port custom modules, and what the Thai localization (l10n_th) covers. Trigger when the user mentions Odoo 20, 'v20', upgrading from 19, ir.access, Owl 3, offline mode, pos_stock, l10n_th / 50 ทวิ / ใบกำกับภาษี in Odoo 20, or asks 'Odoo 20 มีอะไรใหม่', 'อัปเกรด 19 เป็น 20', 'โมดูลนี้ใน 20 เปลี่ยนอะไร', 'CE 20 ทำได้ไหม'."
version: 1.0.0
source: roots-custom
---

# Odoo 20 CE Expert

ตอบคำถามเรื่อง Odoo 20 Community Edition (CE) ทั้งฝั่ง functional และ technical โดยยึดคลังความรู้ที่ศึกษาจากโค้ดจริง (odoo/odoo branch `20.0` @ `b100a87` เทียบกับ `19.0`, 3 ต.ค. 2026)

## Source of truth

อ่านจาก [references/odoo20-ce/](../../references/odoo20-ce/) เสมอ — **ห้ามตอบจากความจำ** ถ้าขัดกับ reference ให้ยึด reference

| คำถามเกี่ยวกับ | อ่านไฟล์ |
|---|---|
| ภาพรวม / 10 การเปลี่ยนแปลงหลัก / CE vs EE / แผนอัปเกรด / ความเสี่ยง | `STUDY-PAPER.md` (Part 0, 5, 6, 7) |
| สถานะโมดูล (NEW / REMOVED / CHANGED), dependencies | `01-module-catalog.md` หรือ `data/module_catalog_19_vs_20.csv` |
| Framework, ORM, `ir.access`, Python 3.12, HTTP, CLI | `areas/01-framework-core.md` |
| Web client, Owl 3, offline, report engines, spreadsheet, IoT | `areas/02-web-ui-technical.md` |
| Discuss, mail tracking, calendar, portal | `areas/03-communication-collab.md` |
| Accounting / Invoicing, payments, Peppol, taxes | `areas/04-accounting-finance.md` |
| Sales, CRM, product, pricelists, UoM, loyalty | `areas/05-sales-crm-product.md` |
| Inventory, purchase, MRP, repair, maintenance (รวมการผลิตแบบ process เช่น น้ำตาล/อาหาร) | `areas/06-supply-chain-mrp.md` |
| Point of Sale, restaurant, self-order | `areas/07-point-of-sale.md` |
| Website, eCommerce, events, marketing | `areas/08-website-ecommerce-marketing.md` |
| HR, project, timesheets (รวม ESG scan) | `areas/09-hr-project-services.md` |
| Localization: ไทย, ASEAN, ฮ่องกง, Thai gaps | `areas/10-localizations.md` (§3.1 Thailand, §8 gaps) |

ทุกรายงานรายหมวดมีโครงสร้างเดียวกัน: §2 แคตตาล็อก · §3 ฟีเจอร์ · **§4 สิ่งที่เปลี่ยนจาก 19** · §5 โมดูลที่ถูกลบ/รวม · **§6 ข้อควรระวังในการอัปเกรด** · §7 คำถามที่ยังตรวจสอบไม่ได้

## หลักการตอบ

1. **แยก CE กับ EE ให้ชัด** — คลังความรู้นี้ครอบคลุมเฉพาะ CE ถ้าฟีเจอร์ไม่อยู่ใน CE ให้ตอบว่า "ไม่มีใน CE" (เช่น AI agents, IoT Box, Accounting reports/reconciliation widget, Payroll, Quality, Subscriptions) ห้ามยืนยันว่า EE มีอะไรถ้า reference ไม่ได้ระบุ — ใช้ skill `odoo-editions` สำหรับคำถามเรื่อง edition/hosting/BEECY
2. **คงระดับความมั่นใจ** — ถ้า reference ระบุ Medium/Low confidence หรือ [web] ต้องบอกผู้ถามด้วย
3. **อ้างอิงหลักฐาน** — สำหรับทีม technical ให้ระบุ path ไฟล์ที่ reference อ้างไว้ (เช่น `addons/stock/models/stock_move.py`)
4. **แยกมุมมองตามผู้ถาม** — ทีม functional/presales: ฟีเจอร์ ขั้นตอนงาน ผลกระทบต่อลูกค้า · ทีม technical: model, field, API, การ rename, งาน port
5. **ถ้า reference ไม่ครอบคลุม** ให้บอกตรง ๆ และแนะนำตรวจโค้ดจริง: `git clone --depth 1 -b 20.0 https://github.com/odoo/odoo`

## Checklist การ port โมดูล 19 → 20 (สรุป)

- รัน `odoo-bin upgrade_code` ก่อน (มีสคริปต์ `19.4-00-ir-access`, `owl3-migration`, `19.3-00-account-groups`, `20.0-00-search-date-filters` ฯลฯ)
- Security: `ir.model.access.csv` + `ir.rule` → `security/ir.access.csv` (`id,name,model_id,group_id/id,operation,domain`) แล้วทดสอบทีละ role
- Rename: `product_uom`→`uom_id`, `holiday_status_id`→`work_entry_type_id`, `acc_number`→`account_number`, `expense_policy`→`reinvoice_policy`, `checked`→`review_state`
- Model ที่ถูกลบ: `account.group`, `res.bank`, `stock.scrap`, `hr.leave.type`, `hr.work.entry` (ใน CE)
- โมดูลที่ถูกลบใน `depends`: `base_vat`, `base_iban`, `stock_picking_batch`, `website_sale_wishlist`, `hr_org_chart`, `iot_base` ฯลฯ
- JS: Owl 3, ไม่มี jQuery/publicWidget, services→plugins, QUnit→Hoot
- Infra: Python ≥ 3.12, `http_interface` default เป็น `127.0.0.1`

รายละเอียดเต็มดู `STUDY-PAPER.md` Part 6 และ §6 ของรายงานแต่ละหมวด

## ลูกค้าไทย (l10n_th)

CE 20 ให้: VAT, ทะเบียนใบกำกับภาษี (`l10n_th.tax.invoice`, เลขไม่ขาดตอน), ภาษีหัก ณ ที่จ่ายตอนชำระเงิน, หนังสือรับรอง 50 ทวิ, PromptPay QR, รายงาน ภ.พ.30
**ไม่มีใน CE:** e-Tax Invoice & e-Receipt, รายงาน/ยื่น ภ.ง.ด.3/53 (ถูกลบใน 20), Payroll/ประกันสังคม, POS ใบกำกับภาษีอย่างย่อ — ดูตาราง 16 ข้อใน `areas/10-localizations.md` §8
**ข้อควรระวังการอัปเกรด:** `l10n_th` ไม่มี migration script ฐานข้อมูลเดิมจะยังใช้ภาษีชุด v19 ต้องวางแผน remap

## Internal site

เว็บภายใน (EN/TH) สำหรับทีม: https://claude.ai/artifact/LVT8ZS5yFVPn2ac9Mg5q1w — source อยู่ที่ `docs/odoo20-site/`
