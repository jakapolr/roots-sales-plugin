---
name: odoo-sales-report
description: Pull confirmed sale orders from Roots.Tech Odoo CE. Summarizes revenue by period, salesperson, or customer. Queries sale.order and sale.order.line models. Requires odoorpc-cli installed and authenticated.
metadata:
  version: 1.0.0
  category: custom
---

# Odoo Sales Report

ดึงข้อมูล Sale Orders ที่ยืนยันแล้วจาก Odoo CE ของ Roots.Tech เพื่อสรุปรายได้จริง แยกตาม period, salesperson, หรือ project type

## เมื่อไหร่ควรใช้

- สรุปรายได้รายเดือน/ไตรมาส
- ตรวจสอบ billing status ของ project ที่กำลัง implement
- เปรียบเทียบรายได้จริงกับ pipeline (Actual vs Forecast)
- เตรียมข้อมูลให้ management report

## Pre-requisite

```bash
pip install odoorpc-cli
odoo auth login --host https://<odoo-host> --db <database> --username <email> --password <password>
odoo auth info
```

---

## คำสั่ง

### 1. ดู fields ของ sale.order (ใช้ครั้งแรก)

```bash
odoo model field sale.order
```

### 2. ดึง sale orders ที่ confirm แล้ว รายเดือน

```bash
odoo search read sale.order \
  --domain '[["state","in",["sale","done"]],["date_order",">=","<YYYY-MM-01>"],["date_order","<=","<YYYY-MM-31>"]]' \
  --fields name,partner_id,user_id,state,amount_total,date_order,date_confirmation \
  --order 'date_order desc'
```

### 3. ดึง orders แยกตาม salesperson

```bash
odoo search read sale.order \
  --domain '[["state","in",["sale","done"]],["user_id.name","ilike","<ชื่อ>"]]' \
  --fields name,partner_id,amount_total,date_order,state \
  --order 'date_order desc'
```

### 4. สรุปรายได้ทั้งหมด (ยังไม่ยกเลิก)

```bash
odoo search read sale.order \
  --domain '[["state","in",["sale","done"]]]' \
  --fields name,partner_id,user_id,amount_total,date_order \
  --order 'date_order desc' \
  --limit 100
```

### 5. ดู order lines (รายละเอียด services/products)

```bash
odoo search read sale.order.line \
  --domain '[["order_id","=",<order_id>]]' \
  --fields product_id,name,product_uom_qty,price_unit,price_subtotal
```

### 6. ดึง orders ที่ยังค้างชำระ (invoicing)

```bash
odoo search read sale.order \
  --domain '[["state","=","sale"],["invoice_status","!=","invoiced"]]' \
  --fields name,partner_id,amount_total,invoice_status,date_order \
  --order 'date_order asc'
```

### 7. นับจำนวน orders รายเดือน

```bash
odoo search count sale.order \
  --domain '[["state","in",["sale","done"]],["date_order",">=","<YYYY-MM-01>"],["date_order","<=","<YYYY-MM-31>"]]'
```

---

## Output ที่ต้องการ

```
## Sales Report — [เดือน/ไตรมาส]

### Revenue Summary

| ตัวเลข | ค่า |
|---|---|
| Total Confirmed Revenue | X,XXX,XXX THB |
| Orders ทั้งหมด | N orders |
| Average Deal Size | XXX,XXX THB |

### By Salesperson

| Salesperson | Orders | Revenue (THB) | % of Total |
|---|---|---|---|
| ... | N | X,XXX,XXX | XX% |

### By Customer (Top 5)

| ลูกค้า | Orders | Revenue (THB) |
|---|---|---|
| ... | N | X,XXX,XXX |

### Orders ที่ต้อง Invoice

| Order | ลูกค้า | มูลค่า (THB) | Invoice Status | วันที่ Confirm |
|---|---|---|---|---|
| SO-XXXX | ... | ... | to invoice | ... |

### Comparison vs Pipeline

| ตัวเลข | ค่า |
|---|---|
| Confirmed Revenue (Actual) | X,XXX,XXX THB |
| Weighted Pipeline (Forecast) | X,XXX,XXX THB |
| Gap | X,XXX,XXX THB |
```

---

## Sale Order States

| state | ความหมาย |
|---|---|
| `draft` | Quotation (ยังไม่ confirm) |
| `sent` | Quotation ส่งให้ลูกค้าแล้ว |
| `sale` | Confirmed Sale Order |
| `done` | Locked (ปิดแล้ว) |
| `cancel` | Cancelled |

## Invoice Status

| invoice_status | ความหมาย |
|---|---|
| `nothing` | ไม่มีอะไรต้อง invoice |
| `to invoice` | รอ invoice |
| `invoiced` | Invoice แล้วทั้งหมด |

---

## Model Reference

| Field | Type | คำอธิบาย |
|---|---|---|
| `name` | char | เลข SO (SO-XXXX) |
| `partner_id` | many2one | ลูกค้า |
| `user_id` | many2one | Salesperson |
| `state` | selection | สถานะ order |
| `amount_total` | monetary | มูลค่ารวม (รวม VAT) |
| `amount_untaxed` | monetary | มูลค่าก่อน VAT |
| `date_order` | datetime | วันที่สร้าง/confirm |
| `date_confirmation` | datetime | วันที่ confirm จริง |
| `invoice_status` | selection | สถานะการ invoice |
| `note` | html | หมายเหตุ |

---

## การนำผลไปใช้ต่อ

- **Forecast:** ใช้ Actual Revenue เปรียบเทียบกับ weighted pipeline จาก `/sales:odoo-crm-sync`
- **Daily briefing:** เพิ่มข้อมูลใน `/sales:daily-briefing`
- **PM handoff:** ตรวจสอบ SO ที่ confirm แล้วก่อนส่งต่อให้ `/sales:pm-handoff`
- **Revenue tracking:** ดู invoice status เพื่อ follow up ฝ่ายบัญชี
