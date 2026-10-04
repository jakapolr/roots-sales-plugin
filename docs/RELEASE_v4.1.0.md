# 📘 Roots Sales Plugin v4.1.0 — Release Summary

> สำหรับทีม Roots.Tech — v4.1 คือ **Odoo 20 CE Knowledge layer**: ให้ทีม Sales/SE เข้าใจ Odoo 20 Community ว่ามีอะไรใหม่ · อะไรเปลี่ยนจาก 19 · อะไรอยู่/ไม่อยู่ใน CE — จากความรู้ที่ **ตรวจสอบกับโค้ดจริง** ไม่ใช่เดาจากความจำ

---

## มีอะไรใหม่

v4.1.0 เพิ่ม **คลังความรู้ Odoo 20 Community Edition** ที่ศึกษาจาก source จริง (`odoo/odoo` branch `20.0 @ b100a87` เทียบ `19.0`, 3 ต.ค. 2026) พร้อม skill, หน้าเว็บ และการต่อเข้ากับ skill เดิม

| ประเภท | ชื่อ | ทำอะไร |
|---|---|---|
| references | **`references/odoo20-ce/`** | KB ครบ — study paper, แคตตาล็อก 720 โมดูล + CSV, รายงาน 10 หมวด (framework/web/accounting/sales/supply/pos/website/hr/l10n), เจาะ `l10n_th` |
| skill | **`odoo20-ce-expert`** | ตอบคำถาม Odoo 20 CE — ฟีเจอร์ใหม่, การเปลี่ยน 19→20, EE-only, อัปเกรด/port, `l10n_th` · **ยึด reference ไม่ตอบจากความจำ** |
| site | **`docs/odoo20-site/`** | Field Guide site (EN/ไทย) — ฟีเจอร์ v20 รายหมวด + หน้า **CE vs EE** รวมสำหรับ Sales |
| wiring | `odoo-editions` · `odoo-gap-analysis` · `roots-manday-estimator` · `se-orchestrator` · `sales-help` | ต่อให้คำตอบที่อิงเวอร์ชันชี้มาที่ KB นี้ |

> 🔗 **เว็บ interactive (EN/ไทย):** [Odoo 20 Field Guide](https://claude.ai/artifact/LVT8ZS5yFVPn2ac9Mg5q1w) — อธิบาย Odoo 20 CE ทั้งหมด: overview + 10 หมวด · module explorer 720 โมดูล · playbook อัปเกรด 19→20 · หน้า CE vs EE · ดาวน์โหลด (study paper, CSV, AI learning pack)
> source: [`docs/odoo20-site/`](odoo20-site/) · *หน้า **CE vs EE** + charset fix ของ v4.1.0 จะปรากฏบน artifact เมื่อ **rebuild + republish** (ดูวิธีใน `docs/odoo20-site/README.md`)*

## หน้า "CE vs EE" (สำหรับ Sales)

หน้าเดียวที่รวมความต่าง Community vs Enterprise ไว้ใช้ตอนขาย/ประเมิน:
- **Strategic trade-offs (10)** — Need / CE 20 / ทางเลือกทั่วไป (Financial UI, Payroll, Quality/PLM/MPS, Studio, IoT, AI, ESG…)
- **ไม่มีใน Community (46)** — จับคู่ หมวด → ความสามารถที่เป็น EE-only/ไม่มีใน CE
- **ช่องว่างไทย l10n (16)** — Need / สถานะใน CE / สิ่งที่เราต้องทำ

## การ wire เข้า skill เดิม

- **`odoo-editions`** — คำถามเวอร์ชัน Odoo 20 → ชี้ไป `references/odoo20-ce/` + `odoo20-ce-expert`
- **`odoo-gap-analysis`** — เพิ่มเส้นแบ่ง CE-vs-EE v20 (code-verified) + เตือนว่า stock `l10n_th` 20 **ไม่มี** e-Tax/Payroll (เป็น custom/BEECY → นับเป็น build)
- **`roots-manday-estimator`** — ก่อนประเมินให้เช็ก KB: อะไร native ใน CE vs ต้อง custom/Enterprise + checklist port 19→20
- **`se-orchestrator`** — Odoo 18 → 18–20 + บล็อก Knowledge sources
- **`sales-help`** — route คำถาม "Odoo 20 / อัปเกรด / อยู่ใน CE ไหม" → `odoo20-ce-expert`

## ✅ ขอบเขต: CE อย่างเดียว

KB นี้ครอบคลุม **เฉพาะ Community Edition** — ฟีเจอร์ Enterprise ระบุได้เพียงว่า "ไม่มีใน CE" (เพราะ source EE ไม่ public)
> **Rooba / l10n_th v20** (localization ของ Roots) ยังไม่รวม — รอ Development migrate ขึ้น v20 เสร็จแล้วจะมา update กันอีกที

## 🔍 ความน่าเชื่อถือ

ก่อน merge ผ่านการ review 3 รอบ (consistency / site build / plugin wiring) + **spot-check กับ `odoo/odoo@20.0` ของจริง** — module add/remove, field renames, removed models, การย้าย `ir.model.access.csv → ir.access.csv` ตรงหมด · ของแถมจากการ review: fix `manifests.py`, แก้ charset bug (ไทย mojibake บน site), reconcile ตัวเลข, ลิงก์ llms.txt

## ⚠️ ข้อจำกัด

- Skill/agent ที่แตะ Odoo = **Claude Code CLI เท่านั้น** (Cowork รอ Odoo MCP) — ไม่เปลี่ยนจาก v4.0
- **Deploy Field Guide site** ต้องมี node/npm บนเครื่องจริง: `npm --prefix docs/odoo20-site/tools install` → `python3 docs/odoo20-site/build.py --pdf` → publish เป็น claude.ai artifact

---

## 🔧 วิธีอัปเดต (ทำตามลำดับ!)

```bash
# 1. ดึง marketplace ล่าสุดก่อน (จำเป็น — ข้ามแล้วได้ version เก่าจาก cache)
claude plugin marketplace update roots-sales-plugin
# 2. อัปเดต plugin
claude plugin update sales@roots-sales-plugin
# 3. restart Claude Code
```
เช็ค: `claude plugin list` → `sales  4.1.0  enabled`

## วิธีใช้ (ตัวอย่าง)

```
"Odoo 20 มีอะไรใหม่" / "อัปเกรด 19 เป็น 20 ต้องทำอะไร"   → odoo20-ce-expert
"ฟีเจอร์นี้อยู่ใน CE ไหม" / "port โมดูลนี้ 19→20"          → odoo20-ce-expert
"เทียบ CE vs EE ให้ลูกค้า"                                → odoo-gap-analysis (อิง KB v20)
เปิดหน้า Field Guide → แท็บ "CE vs EE" สำหรับตอนขาย
```

## v5 (next) — Farming Strategy

recurring 16% → 50% (Hunter → Farmer) · ดู [`ROADMAP_v5_farmer-strategy.md`](ROADMAP_v5_farmer-strategy.md)
