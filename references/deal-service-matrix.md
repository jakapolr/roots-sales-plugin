# Deal Service Matrix & Allocation — Canonical Reference

> **Single source of truth** สำหรับ *"ดีลแต่ละ tier ควรได้ resource เท่าไหร่ และ next action คืออะไร"*
> ทุก skill/agent ที่แนะนำว่าจะทำอะไรกับดีลต่อ (`sales-help`, `deal-strategy`, `pipeline-review`) ต้องอ่านไฟล์นี้ — ห้ามคิดเกณฑ์เอง
> ออกแบบให้ **machine-consumable**: skill เอา `x_deal_tier` + `stage_id` ของดีล → lookup ตารางในนี้ → คืน next best action
> **Scope: v4 = Hunting** — ครอบ allocation "win-it" (ทุ่มปิด A) · การ "water/keep-it" หลังปิด → ย้ายไป [[ROADMAP_v5_farmer-strategy]]
> Draft: 2026-07 · pairs with [[customer-scorecard]] · [[strategy-doctrine]]

---

## 1) หลักการ — "ไม่ run democracy เน้น return"

Default ของทีมคือ **first-come-first-serve** (democracy โดยปริยาย) — เกิดเองเมื่อไม่มีระบบทับ ไฟล์นี้คือระบบที่ทับ

**ความไม่เท่าเทียม = fiduciary duty ไม่ใช่ความลำเอียง** — เพราะข้อมูลจริง:
- 1 ดีล A ≈ **12 ดีล C** (median deal size ต่างกัน 12.5×)
- **26% ของดีล = 64% ของรายได้** implementation เอกชน
- → ให้เวลาเท่ากันกับ A และ C = **malpractice ต่อบริษัท**

**"Water" มี 2 ครึ่ง** — **Win-it (ทุ่มปิด) = v4 · ไฟล์นี้** + Keep-it (over-deliver หลังปิด จนขยาย) = **v5 Farming** ([[ROADMAP_v5_farmer-strategy]]) ครึ่งหลังคือที่มาของ MA/Cloud/referral จริง

---

## 2) Tier definition (จาก scorecard v2 — 2 แกน)

ดีลได้ tier จาก 2 แกน (คะแนน 0–4, เส้นตัด 2.5) — รายละเอียดสูตรใน [[customer-scorecard]]

| tier | Value | Deliverability×Fit | ความหมาย | `x_deal_tier` |
|---|---|---|---|---|
| 🎃 A — Giant pumpkin | ≥2.5 | ≥2.5 | ทุ่มสุด | `A` |
| 🌱 B — Seedling | <2.5 | ≥2.5 | farm ให้โต | `B` |
| ⚠️ C — Trap | ≥2.5 | <2.5 | prize มีเงื่อนไข | `C` |
| 🥀 D — Weed | <2.5 | <2.5 | disqualify | `D` |

> **Trap (C) ไม่ใช่ "ทุ่มเพราะใหญ่"** — เดินต่อเฉพาะเมื่อ de-risk ได้ (standard-first scope / reprice risk / มี champion) มิฉะนั้นปฏิบัติเหมือน D

---

## 3) Service Matrix — tier ไหนได้อะไร

| dimension | 🎃 A | 🌱 B | ⚙️ C | 🥀 D |
|---|---|---|---|---|
| **Speed-to-lead** | < 1 ชม. | < 1 วัน | automation | self-serve |
| **ใครรับ** | AE เก่งสุด + SE + director sponsor | AE + SE ตามคิว | AE คนเดียว | ส่งต่อ/partner |
| **GAP** | fast-track, senior ลงเอง | ปกติ | เสนอ (ตัวคัด) | — |
| **Assets** | deck-builder on-brand เฉพาะดีล | template | template | — |
| **Cadence** | weekly + mutual action plan | รายปักษ์ | reactive | — |
| **หลังปิด (water)** → v5 | *(Farming — ดู [[ROADMAP_v5_farmer-strategy]])* | | | |

> B/C **ไม่ได้ "ไม่มีอะไร"** — ได้บริการ*แบบอื่น* (เบา, automated) — automation คือสิ่งที่ทำให้ under-serve C ได้โดยไม่ดรอปดีล

---

## 4) Stage × Tier → Next Best Action (ส่วนที่ skill ใช้)

Stage อ้างอิง `crm.stage` จริงใน Odoo — mapping ชื่อ stage → play

| Stage (crm.stage) | 🎃 A | 🌱 B | ⚙️ C / 🥀 D |
|---|---|---|---|
| **New** | contact <1ชม. · assign AE เก่ง+SE · ดึง DBD (1% sizing) · นัด discovery | contact <1วัน · qualify | automation nurture · qualify async |
| **Contacting** | multi-thread · หา economic buyer + champion · ผลักเข้า GAP | qualify มาตรฐาน · เสนอ GAP | template follow · เสนอ self-serve GAP |
| **Demo Pending** | demo เฉพาะด้วยข้อมูลลูกค้า · เชิญ director sponsor | demo มาตรฐาน | demo อัด/มาตรฐาน |
| **Proposing** | **ห้าม quote ก่อนถึง killing zone** — ยืนยัน GAP(paid) + EB + compelling event · senior ร่วม | GAP เสร็จก่อน · proposal มาตรฐาน | proposal มาตรฐาน · light |
| **Quoting** | แนบ mutual action plan · **นัด next step ก่อนส่ง** · present สด (ห้ามส่งเมลเฉย ๆ) · exec sponsor | นัด next step | ส่ง + automated follow |
| **Follow-up (1/3/6/12 month)** ⚰️ | **ห้ามนอนนิ่ง** — re-engage ด้วย value/compelling event ใหม่ หรือ re-diagnose · ถ้าตายจริง → mark **Lost + เหตุจริง** (ห้าม "No response") | re-engage 1 ครั้ง · ไม่ขยับ → Lost | automated nurture · ไม่มีสัญญาณ → Lost |
| **Won - in progress** → v5 | *(Farming/water: QBR · ขยาย MA/Cloud · case study · referral — ย้ายไป [[ROADMAP_v5_farmer-strategy]])* | | |

**กฎ Follow-up graveyard:** stage นี้คือ *holding pen ไม่ใช่กลยุทธ์* — ดีล A/B **ห้าม**ค้างแบบ passive (นี่คือ ฿92M ที่ตายไป) · skill ที่เจอ A/B ใน stage นี้ + `activity_state` ว่าง → ต้อง flag ทันที

**กฎ Trap (C):** ก่อนลง resource ต้องผ่าน 1 ใน — (ก) scope standard-first, (ข) reprice สะท้อน delivery risk, (ค) ได้ champion ยืนยัน · ไม่ผ่าน = ปฏิบัติเหมือน D

---

## 5) Allocation Ritual (weekly — manager-owned)

Resource allocation เป็น **portfolio decision เหนือ AE รายคน** — ไม่ใช่ reflex ของ AE (ไม่งั้นกลับไป first-come)

```
INPUT   ทุกดีล open พร้อม x_deal_tier + stage + activity_state + days-in-stage
STEP 1  list A-deals ทั้งหมด → จัดสรร SE-time / director-time / AE เก่งสุด ให้ก่อน
STEP 2  A/B ที่ค้าง Follow-up + ไม่มี activity → บังคับ next action หรือ mark Lost
STEP 3  Trap (C) → ตัดสิน de-risk หรือ drop
STEP 4  ตรวจ over-concentration: A ไม่ควรมาจากลูกค้าเดียว >X% (ต้องเป็น patch หลายลูก)
OUTPUT  ดีล A ทุกตัวมีเจ้าของ resource ชัด + next action + SLA
CADENCE รายสัปดาห์ · owner: Sales Manager / Head of Sales
```

---

## 6) Red flags / overrides (ตัดเกรดทันที ไม่ว่าคะแนนเท่าไหร่)

- **Affordability fail** — predicted cost > กำไรทั้งปีลูกค้า (จาก DBD P&L) → cap ที่ C
- **Public-listed + localization ไม่ใช่ตัวตัดสิน** → cap winnability (มักแพ้ SAP/brand-safety)
- **Over-concentration** — "water winners" ≠ "ทิ้งที่เหลือ" ต้องมี patch หลายลูก + engine เลี้ยง B → A
- **Wrong-tier amplification** — ทุ่ม resource บน tier ที่จัดผิด = ขยายหายนะ (บ้านโป่ง) → allocation ไม่เท่ากัน = scorecard ยิ่งต้องแม่น

---

## 7) How skills consume this (contract)

skill ที่จะสร้างต่อ (เช่น `deal-strategy`, หรือให้ `sales-help` เรียก) ใช้ interface นี้:

```
INPUT (จาก crm.lead)
  x_deal_tier        A | B | C | D        (จาก scorecard v2; ถ้าไม่มี → คำนวณ/ขอ)
  stage_id.name      ชื่อ stage            (map เข้าตาราง §4)
  activity_state     overdue|today|planned|none
  x_gap_status       none|quoted|paid|waived|done   (ถ้ามี — Phase 0 spec)
  days_in_stage      จาก date_last_stage_update
  amount / expected_revenue

OUTPUT
  service_level      ระดับบริการ (§3)
  next_best_action   ข้อความ action (§4 lookup ตาม tier×stage)
  owner_role         ใครควรรับ (§3)
  sla                กรอบเวลา
  flags[]            เช่น "A ค้าง Follow-up ไม่มี activity" | "Trap ยังไม่ de-risk"
```

**หลักการ lookup:** `(tier, stage)` → row ใน §4 · ทับด้วย red flags §6 · เติม service_level จาก §3

---

## 8) Roadmap note

- ไฟล์นี้เตรียมแปลงเป็น skill เสริมใน plugin (v4.0 Loop 2 — `deal-strategy`)
- ต้องมีก่อน: `x_deal_tier` + `x_gap_status` ใน Odoo (ดู [[odoo-spec-reason-taxonomy]] / Phase 0) และ scorecard v2 ([[customer-scorecard]])
- ทำงานร่วม doctrine 4 ทฤษฎี ([[strategy-doctrine]]) — Pumpkin governs **private funnel เท่านั้น** (ไม่ใช่ราชการ/TOR)
- **v4/v5 split:** ไฟล์นี้ = allocation "win-it" (v4 Hunting) · การเลี้ยง/water หลังปิด (QBR, expansion, referral) = [[ROADMAP_v5_farmer-strategy]]
