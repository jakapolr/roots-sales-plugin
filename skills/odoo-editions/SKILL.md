---
name: odoo-editions
description: "Authoritative explainer for the difference between Odoo Community, Odoo Enterprise, Odoo Online (and Odoo.sh/on-premise hosting), and Roots' two BEECY offerings (BEECY SaaS vs Community implementation). Trigger whenever the user or a client asks about Odoo versions/editions, which Odoo to use, Community vs Enterprise, Odoo Online vs self-hosted, licensing, hosting options, or what BEECY is and how it differs. Phrases: 'Community vs Enterprise', 'Odoo Online คืออะไร', 'BEECY ต่างจาก Odoo ยังไง', 'ใช้ version ไหนดี', 'custom ได้ไหม', 'edition ไหน', 'self-host vs cloud'."
version: 1.0.0
source: roots-custom
---

# Odoo Editions / Hosting / BEECY — Explainer

ตอบคำถามเรื่องความแตกต่างของ Odoo editions, hosting, และ BEECY ให้ **ถูกต้องและไม่สับสน** โดยยึดข้อมูลจาก reference เดียว

## Source of truth

อ่าน [references/odoo-editions.md](../../references/odoo-editions.md) เสมอก่อนตอบ — เป็นข้อมูลเดียวที่ verify แล้ว (official Odoo docs + beecy.co)
**ห้ามตอบจากความจำเอง** ถ้าขัดกับ reference ให้ยึด reference

## หลักการตอบ

1. **แยก 3 แกนให้ลูกค้าเห็นก่อน** — Edition (CE/EE) · Hosting (Online/Odoo.sh/on-premise) · ผลิตภัณฑ์ Roots (BEECY SaaS / Community implementation) เป็นคนละเรื่อง
2. **อย่าเทียบข้ามแกน** — "Online vs Community" ไม่ใช่การเทียบที่ถูก (Online = hosting, Community = edition)
3. **BEECY ระบุให้ชัดว่าตัวไหน** — BEECY SaaS (แพ็กเกจ standard, ไม่ custom) หรือ Community implementation (โปรเจกต์ custom ได้)
4. **เรื่อง custom code สำคัญสุด** — ถามลูกค้าว่าต้อง custom ไหม เพราะตัดสินทันที (Online/BEECY SaaS = ไม่ได้ · Odoo.sh/on-premise/Community impl = ได้)
5. **เวอร์ชัน** — ขอบเขต CE vs EE เปลี่ยนตามเวอร์ชัน ถ้าไม่ชัดให้บอกว่าต้องตรวจ official docs ของเวอร์ชันนั้น ไม่เดา

## เมื่อใช้ประกอบงานขาย/discovery

- ถามก่อน: งบ? จำนวน user? ต้อง custom ไหม? โรงงาน/ซับซ้อนแค่ไหน? งานราชการหรือไม่?
- แล้วใช้ Decision Guide ใน reference เพื่อแนะนำ
- ถ้าต้องเทียบ feature/cost เป็นเรื่องเป็นราว → ส่งต่อให้ skill `odoo-gap-analysis`

## รูปแบบคำตอบที่แนะนำ

```
[แยกแกนให้เห็น 1-2 บรรทัด]
[ตอบเฉพาะสิ่งที่ถาม โดยอ้าง reference]
[ถ้าเป็นการเลือกให้ลูกค้า → ถามเงื่อนไข แล้วชี้ตาม Decision Guide]
[ถ้า custom เกี่ยวข้อง → เตือนข้อจำกัด Online/BEECY SaaS]
```

## เชื่อมต่อ skill อื่น
- เทียบ feature/cost ละเอียด + เลือก path → `odoo-gap-analysis`
- ประเมินราคา implementation → `roots-manday-estimator`
- positioning vs คู่แข่ง → `competitive-intelligence`
