# Odoo Editions, Hosting & BEECY — Canonical Reference

> **Single source of truth** สำหรับความแตกต่างของ Odoo editions / hosting / BEECY
> ทุก skill และ agent ที่พูดถึงเรื่องนี้ต้องอ้างอิงไฟล์นี้ — ห้ามเขียนเองให้ขัดกัน
> Verified: มิ.ย. 2026 · Odoo 18 · sources: odoo.com/page/editions, odoo.com/page/pricing, beecy.co

---

## หลักคิด: 3 แกนที่ต้องแยกออกจากกัน

ความสับสนเกือบทั้งหมดเกิดจากเอา "edition" "hosting" และ "ผลิตภัณฑ์ Roots" มาเทียบปนกัน ทั้งที่อยู่คนละแกน:

- **แกน A — EDITION** (license แบบไหน): Community หรือ Enterprise
- **แกน B — HOSTING** (รันที่ไหน): Self-hosted / Odoo.sh / Odoo Online
- **แกน C — PRODUCT ของ Roots**: BEECY SaaS หรือ Community Implementation (คนละอย่าง)

> "Odoo Online" **ไม่ใช่ edition** — เป็นวิธี host Enterprise แบบหนึ่ง
> "BEECY" **ไม่ใช่ Community เปล่า ๆ** — เป็นผลิตภัณฑ์ที่ Roots ห่อ Community ด้วย localization + บริการ

---

## แกน A — EDITION

| | Community (CE) | Enterprise (EE) |
|---|---|---|
| License | Open-source LGPLv3 — **ฟรี** | Licensed — จ่ายต่อ user/ปี |
| Apps | Subset | ครบทุก app |
| Enterprise-only features | ❌ | Studio, Mobile app, **Payroll**, AI/OCR (invoice, vendor bill), Spreadsheet/BI, **Field Service**, Knowledge, VoIP, Approvals, **Manufacturing ขั้นสูง** (Shopfloor, scheduling), PLM |
| Manufacturing พื้นฐาน (MO, BoM, MRP) | ✅ มี | ✅ มี |
| Hosting รวมให้ | ❌ ไม่ | ✅ รวม |
| Support / version upgrade | community | ✅ official |

> Community มี MRP พื้นฐาน (MO/BoM) แต่ **ฟีเจอร์โรงงานขั้นสูง** (Shopfloor, PLM, scheduling ขั้นสูง) เป็น Enterprise-only
> ⚠️ ขอบเขต feature ขยับได้ตามเวอร์ชัน — ตรวจ odoo.com/page/editions ของเวอร์ชันที่ใช้จริงเสมอ

---

## แกน B — HOSTING (เลือกได้ว่าจะรัน Odoo ที่ไหน)

| | custom module/code? | Edition ที่รองรับ | หมายเหตุ |
|---|---|---|---|
| **Odoo Online (SaaS)** | ❌ **ไม่ได้** (Studio เท่านั้น) | EE | odoo.com host ให้หมด · backup/security/monitoring รวม · ฟรี storage ~100GB |
| **Odoo.sh (PaaS)** | ✅ ได้ + dev/staging/prod + git | EE | Odoo จัดการ infra · ค่า hosting แยกจาก license |
| **On-premise / self-host** | ✅ ได้ | CE (ฟรี) หรือ EE | จัดการ server/infra เอง |

> **จุดที่ AI มักแนะนำผิด:** ลูกค้าที่ต้อง custom module เยอะ → **ห้ามไป Odoo Online** ต้องไป Odoo.sh / on-premise / หรือ BEECY/Community implementation

---

## แกน C — ผลิตภัณฑ์ของ Roots (มี 2 อย่าง — อย่าปนกัน!)

### C1 · BEECY SaaS — แพ็กเกจสำเร็จรูป (beecy.co)

| หัวข้อ | รายละเอียด |
|---|---|
| คือ | Odoo **Community** + Thai localization + hosting + support → ขายเป็น subscription |
| Hosting | Cloud SaaS — Roots host ให้ · เข้าได้ทุกอุปกรณ์ |
| Customization | **standard package — ไม่รับ custom module** (คล้ายข้อจำกัดของ Odoo Online แต่อยู่บน Community) |
| Localization | VAT, หัก ณ ที่จ่าย (ภ.ง.ด.3/53), **e-Tax invoice**, **Thai payroll** (SSO, PND1) |
| Modules | Sales, POS, Purchase, Inventory, Accounting + **รองรับ Manufacturing** (MO/BoM) |
| ราคา | Easy Start 699 · Easy Pro 639 · Easy Plus 599 บาท/user/เดือน (5/10/20 users, รายปี) ≈ 3K–15K/account/เดือน |
| เหมาะกับ | Trading, Retail, Services + SME ที่อยากได้เร็ว/ถูก/ไม่ต้อง custom |

### C2 · Community Implementation — งานโปรเจกต์ (Roots implement เอง)

| หัวข้อ | รายละเอียด |
|---|---|
| คือ | Roots implement บน Odoo **Community** + BEECY localization modules + **custom development** |
| Hosting | ลูกค้า host เอง / cloud ที่เลือก (on-premise/self-host) |
| Customization | ✅ **custom ได้เต็มที่** — เพิ่ม module, แก้ flow, integrate ระบบอื่น |
| เหมาะกับ | งบจำกัดแต่ต้องการ custom เยอะ / โรงงานที่ flow ซับซ้อน / ไม่อยากจ่าย EE license |
| ต่างจาก BEECY SaaS | BEECY SaaS = แพ็กเกจ standard เช่าใช้; C2 = โปรเจกต์ custom เป็นเจ้าของเอง |

> ❗ ในเอกสารเก่าเขียน "Community = BEECY" หรือ "BEECY path" สำหรับลูกค้าโรงงาน — นั่นหมายถึง **C2 (Community implementation)** ไม่ใช่ C1 (BEECY SaaS) ต้องแยกให้ชัดเสมอ

---

## Decision Guide — แนะนำลูกค้าแบบไหน

```
SME trading/retail/service · อยากได้เร็ว · ไม่ต้อง custom · งบจำกัด
→ BEECY SaaS (C1)

งบจำกัด · ต้อง custom เยอะ / โรงงาน flow ซับซ้อน · อยากเป็นเจ้าของระบบ
→ Community Implementation (C2)

ต้องการ Enterprise features (Studio, Payroll ครบ, Field Service, MFG ขั้นสูง, PLM)
   หรือต้องการ official support/SLA · งบถึง
→ Odoo Enterprise
   └ host แบบไหน?
      • ไม่ต้อง custom code, อยากสบาย → Odoo Online
      • ต้อง custom code + อยากให้ Odoo จัดการ infra → Odoo.sh
      • ต้องคุม data/infra เอง → On-premise (EE)

งานราชการ (e-GP)
→ มักเลือก Enterprise — เอกสาร licensing ชัดเจนกว่าสำหรับยื่นประมูล
```

---

## กับดักที่ต้องเลี่ยง (ให้ AI ระวัง)

1. อย่าเทียบ "Online vs Enterprise vs Community" ตรง ๆ — Online คือ hosting, อีกสองตัวคือ edition (คนละแกน)
2. อย่าพูดว่า "BEECY = Community" ลอย ๆ — ระบุให้ชัดว่าเป็น BEECY SaaS (C1) หรือ Community implementation (C2)
3. อย่าบอกว่า Odoo Online custom module ได้ — **ไม่ได้**
4. อย่าบอกว่า BEECY SaaS custom module ได้ — เป็น standard package
5. ขอบเขต CE vs EE เปลี่ยนตามเวอร์ชัน — ถ้าไม่ชัด ให้ตรวจ official docs ของเวอร์ชันนั้น อย่าเดา

## Sources
- Odoo editions: https://www.odoo.com/page/editions
- Odoo hosting/pricing: https://www.odoo.com/page/pricing
- BEECY: https://beecy.co/ + Roots internal confirmation (มิ.ย. 2026)
