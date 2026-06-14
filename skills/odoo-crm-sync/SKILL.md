---
name: odoo-crm-sync
description: Pull live CRM pipeline from Roots.Tech Odoo CE. Queries crm.lead for open opportunities, groups by stage/salesperson, and formats results for pipeline review or SE assignment. Requires odoorpc-cli installed and authenticated.
metadata:
  version: 1.0.0
  category: custom
---

# Odoo CRM Sync

ดึงข้อมูล CRM pipeline จาก Odoo CE ของ Roots.Tech แบบ real-time และจัดรูปแบบสำหรับ pipeline review, SE assignment, หรือส่งต่อให้ /forecast

## เมื่อไหร่ควรใช้

- ก่อนประชุม pipeline review
- เมื่อ SE ต้องการ deal list ปัจจุบันเพื่อ assign งาน
- เมื่อ Sales Manager ต้องการ snapshot แยกตาม stage
- เป็น data source ให้ /roots-manday-estimator หรือ /forecast

## Pre-requisite

```bash
# ติดตั้ง odoorpc-cli
pip install odoorpc-cli

# เชื่อมต่อ Odoo CE ของ Roots.Tech
odoo auth login --host https://<odoo-host> --db <database> --username <email> --password <password>

# ตรวจสอบ auth
odoo auth info
```

## ขั้นตอนการทำงาน

1. ตรวจสอบ auth และ connectivity
2. ดึง stage list (เรียงตาม sequence)
3. ดึง opportunities ทั้งหมดที่ active
4. จัดกลุ่มและคำนวณ weighted value
5. แสดงผลเป็น pipeline table พร้อม insights

---

## คำสั่ง

### 1. ตรวจสอบ auth

```bash
odoo auth info
```

### 2. ดู stages ที่มีในระบบ

```bash
odoo search read crm.stage \
  --fields name,sequence,is_won \
  --order 'sequence asc'
```

### 3. ดึง opportunities ทั้งหมดที่ active (ยังไม่ปิด)

```bash
odoo search read crm.lead \
  --domain '[["type","=","opportunity"],["active","=",true],["stage_id.is_won","=",false]]' \
  --fields name,partner_id,user_id,stage_id,expected_revenue,probability,date_deadline,description \
  --order 'stage_id asc, expected_revenue desc'
```

### 4. กรองตาม salesperson

```bash
odoo search read crm.lead \
  --domain '[["type","=","opportunity"],["active","=",true],["user_id.name","ilike","<ชื่อ>"]]' \
  --fields name,partner_id,stage_id,expected_revenue,probability,date_deadline \
  --order 'expected_revenue desc'
```

### 5. ดึง deals ที่ปิดชนะเดือนนี้

```bash
odoo search read crm.lead \
  --domain '[["type","=","opportunity"],["probability","=",100],["date_closed",">=","<YYYY-MM-01>"],["date_closed","<=","<YYYY-MM-31>"]]' \
  --fields name,partner_id,user_id,expected_revenue,date_closed \
  --order 'date_closed desc'
```

### 6. นับ deals แยกตาม stage

```bash
odoo search count crm.lead \
  --domain '[["type","=","opportunity"],["active","=",true],["stage_id.name","=","<stage_name>"]]'
```

### 7. ดู fields ทั้งหมดของ crm.lead (ใช้ครั้งแรกเพื่อ explore)

```bash
odoo model field crm.lead
```

---

## Output ที่ต้องการ

หลังได้ข้อมูล ให้จัดรูปแบบเป็น:

```
## Pipeline Snapshot — [วันที่]

### By Stage

| Stage | Deal | ลูกค้า | Salesperson | มูลค่า (THB) | Probability | Deadline | สถานะ |
|---|---|---|---|---|---|---|---|
| Qualification | ... | ... | ... | ... | ...% | ... | ⚠️ ใกล้ครบ |
| Proposal | ... | ... | ... | ... | ...% | ... | ✅ ปกติ |
| Won | ... | ... | ... | ... | 100% | — | 🎉 ปิดแล้ว |

### Summary

| ตัวเลข | ค่า |
|---|---|
| Total Pipeline | X,XXX,XXX THB |
| Weighted Pipeline | X,XXX,XXX THB |
| Deals ที่ต้องระวัง (deadline < 30 วัน, prob < 50%) | N deals |
| Deals ที่ต้อง SE support | N deals |
```

---

## Flags ที่ต้องระบุ

| Flag | เงื่อนไข |
|---|---|
| ⚠️ ใกล้ deadline | deadline < 30 วัน และ probability < 70% |
| 🔴 หยุดชะงัก | ไม่มี activity > 14 วัน (ดูจาก `activity_date_deadline`) |
| 🏗️ ต้องการ SE | stage = Proposal/Negotiation และยังไม่มี SE assigned |
| 💰 High Value | expected_revenue > 500,000 THB |

---

## Model Reference

| Field | Type | คำอธิบาย |
|---|---|---|
| `name` | char | ชื่อ opportunity/project |
| `partner_id` | many2one | ลูกค้า (res.partner) |
| `user_id` | many2one | Salesperson |
| `stage_id` | many2one | Stage ใน pipeline |
| `expected_revenue` | float | มูลค่าที่คาด (THB) |
| `probability` | float | ความน่าจะเป็นที่ปิดได้ (0-100) |
| `date_deadline` | date | วันกำหนดปิดดีล |
| `date_closed` | datetime | วันที่ปิดจริง (เฉพาะ Won deals) |
| `description` | html | รายละเอียดของดีล |
| `active` | bool | false = archived (won/lost) |

---

## การนำผลไปใช้ต่อ

- **Pipeline review:** ส่งผลให้ `/sales:pipeline-review` เพื่อวิเคราะห์เชิงกลยุทธ์
- **Forecast:** ใช้ weighted pipeline เป็น input ให้ `/sales:forecast`
- **SE assignment:** ส่ง deals ที่ต้องการ SE ให้ `se-orchestrator` agent
- **Manday estimation:** ส่ง deal ที่เข้า Proposal stage ให้ `/sales:roots-manday-estimator`
