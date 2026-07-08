---
name: deal-strategy
description: "วินิจฉัยดีล Odoo — จัด tier (scorecard v2), ประเมิน MEDDICC health, ตรวจ killing-zone/graveyard gates แล้วเขียน scoring rationale + ONE Next Best Action กลับ chatter ของดีล. Trigger: 'diagnose deal', 'ดีลนี้ทำอะไรต่อ', 'วิเคราะห์ดีล [name]', 'score deal', 'next action for [deal]', หรือถูกเรียกโดย strategy-orchestrator (batch). CLI-only — แตะ Odoo ผ่าน odoorpc."
version: 1.0.0
source: roots-custom
phase: 4
---

# Deal Strategy — keystone skill (v4 Hunting)

> **Custom Skill** — Built by Roots.Tech
> **อ่านก่อนเสมอ:** [[strategy-doctrine]] · [[customer-scorecard]] · [[deal-service-matrix]] · [[won-lost-cheatsheet]]
> **CLI-only** — ใช้ `odoo` (odoorpc-cli) · Cowork ยังไม่รองรับ (รอ Odoo MCP)
> **Purpose:** เปลี่ยน "ให้ข้อมูล" เป็น "สั่งให้ทำ + เข้าใจต่อเนื่อง" — score + diagnose + CTA + loop

## Modes

- **Interactive** (ตอนนี้ใช้ได้) — user ถามถึงดีล 1 ตัว → แสดง diagnosis + CTA ใน chat และ/หรือ log ลง chatter
- **Batch** (Phase 4 — รอ orchestrator) — strategy-orchestrator ส่ง lead_id ที่มี event ใหม่ → diagnose → write-back chatter → clear flag

---

## Process

### Step 0 — Assemble context (4 ชั้น — §8.1 ของ deal-service-matrix)

> **สำคัญเรื่อง token (§9):** อ่าน research fields ยาว **ครั้งแรกครั้งเดียว** → distill เป็นสรุป 3 บรรทัดลง chatter · รอบถัดไปอ่าน**สรุป + note เก่า** ไม่ใช่ raw · ดึงเฉพาะ field ที่ใช้

```bash
# ชั้น Static — lead + custom fields
odoo search read crm.lead --domain '[["id","=",<ID>]]' \
  --fields "name,partner_id,stage_id,expected_revenue,probability,priority,\
date_deadline,activity_state,date_last_stage_update,x_deal_tier,\
business_research,financial_research,analysis_description,research_status,user_id" 2>/dev/null

# ชั้น Static — partner (industry, มหาชน?, DBD)
odoo search read res.partner --domain '[["id","=",<PID>]]' --fields "name,industry_id,is_company,comment" 2>/dev/null

# ชั้น History ⭐ — chatter = memory (อ่าน note เก่าของ AI + คำตอบ AE)
odoo search read mail.message --domain '[["model","=","crm.lead"],["res_id","=",<ID>]]' \
  --fields "date,author_id,subject,body" 2>/dev/null   # เอา 5–10 อันล่าสุดพอ

# ชั้น Related — quote/GAP line + ดีลอื่นของ partner
odoo search read sale.order.line --domain '[["order_id.partner_id","child_of",<PID>]]' --fields "order_id,name,price_subtotal" 2>/dev/null
```

**gap_status (interim — ยังไม่มี field):** อนุมานจาก — มี sale.order.line ชื่อ "GAP" ไหม + มี note "GAP" ใน chatter ไหม → `none/quoted/paid/done`

### Step 1 — Resolve tier
- มี `x_deal_tier` → ใช้เลย
- ไม่มี → คำนวณด้วย scorecard v2 (Step 2) แล้ว `odoo write crm.lead --ids <ID> --value '{"x_deal_tier":"A"}'`

### Step 2 — Scoring (scorecard v2 — [[customer-scorecard]])
ให้คะแนน 2 แกน 0–4 × น้ำหนัก → **ต้องผ่าน 2.5 ทั้ง 2 แกน** (ไม่เฉลี่ยรวม)

```
Value = size(1%)×0.45 + expansion×0.35 + strategic×0.20
Deliv = custom×0.25 + decision/champion×0.25 + feasibility×0.20 + competitive/event×0.15 + comms×0.15
```
- ระบุทุกเกณฑ์ว่า `[data]` (จาก Odoo) หรือ `[est]` (ประมาณจาก signal: priority/prob/activity/deadline)
- **แสดงการคิด** (evidence → คะแนน → contribution) — AE ต้องเรียนวิธีคิด ไม่ใช่แค่ผล

### Step 3 — MEDDICC scan → health (ให้คะแนนแต่ละตัว 0/1/2)

ให้คะแนน `2 = มีชัด · 1 = partial/คลุมเครือ · 0 = ไม่มี/ไม่รู้` · ระบุ `[data]` (จาก Odoo) หรือ `[ask]` (ต้องถาม AE)

| element | คำถาม | 2 (มีชัด) | 1 (partial) | 0 (ไม่มี) | source |
|---|---|---|---|---|---|
| **M** Metrics | ROI เป็นตัวเลข? | มีตัวเลข ROI/payback ที่ลูกค้ายอมรับ | มี pain เชิงปริมาณ แต่ยังไม่ผูกเงิน | ไม่มีตัวเลข | `[data]` financial_research / analysis_description |
| **E** Economic Buyer | ใครเซ็นงบ? | เข้าถึง/คุย EB แล้ว | รู้ว่าใคร แต่ยังไม่เข้าถึง | ไม่รู้ | `[ask]` |
| **D** Decision | เกณฑ์+ขั้นตอน? | รู้เกณฑ์ตัดสิน + process/timeline | รู้อย่างใดอย่างหนึ่ง | ไม่รู้ | `[ask]` |
| **I** Identify Pain | pain จริง? | ระบุ pain + ผลกระทบชัด | pain กว้าง ๆ | ไม่ชัด | `[data]` business_research |
| **C** Champion 🔴 | คนเชียร์ภายใน? | champion มีอิทธิพล + active push | มี contact เฉย ๆ ยังไม่ push | ไม่มี | `[ask]` |
| **C** Competition | แข่งกับใคร/do-nothing? | รู้คู่แข่ง + วิธีชนะ | รู้ว่าแข่ง แต่ไม่รู้วิธีชนะ | ไม่รู้ | `[ask]` + partner (มหาชน = SAP risk) |
| **CE** Compelling Event 🔴 | deadline บังคับ? | มีเหตุ + วันที่ชัด | มี date_deadline แต่ไม่ผูกเหตุ | ไม่มี | `[data]` date_deadline (proxy) |

**Health rollup:**
```
ถ้า Champion=0 OR Compelling Event=0  → 🔴 (hard rule — 48% ของ loss เป็นเพราะ 2 ตัวนี้)
มิฉะนั้น รวมคะแนน (เต็ม 14):  ≥11 → 🟢  ·  7–10 → 🟡  ·  <7 → 🔴
```

**map เข้า scorecard v2 (Step 2) + gates:**
- Champion + EB + Decision → เกณฑ์ **decision/champion (25%)**
- Competition + Compelling event → เกณฑ์ **competitive+event (15%)** + gate **killing-zone** (CE=0 → บล็อก quote)
- Metrics + Pain → informs feasibility (deliverability) + size/value

**element ที่ได้ 0/1 → กลายเป็น CTA "🎯 AE ยืนยัน" อัตโนมัติ** (เช่น UBE: E=?, Champion=? → ถามใน CTA)

### Step 4 — Gates (hard rules)
```
killing-zone: stage in [Proposing,Quoting] and gap != paid/done
   → private: BLOCK "ห้าม quote ก่อน paid-GAP"  |  gov: check pre-TOR
graveyard: stage in [Follow-up 1/3/6/12] and tier in [A,B] and activity in [none,overdue]
   → FLAG re-engage OR mark Lost + เหตุจริง (v2, ห้าม "No response")
stale: days_in_stage > threshold and activity == none  → FLAG next step
```

### Step 5 — Stage × Tier lookup + red flags
row `(stage, tier)` จาก [[deal-service-matrix]] §4 · ทับด้วย red flags §6 (affordability / public-listed / trap)

### Step 6 — Output: scoring log + CTA (§8.3)
CTA ต้องมี 3 อย่าง: **🎯 ONE action** (+owner+SLA) · **🔀 fork** · **↩️ reply path**

---

## Output — write กลับ chatter (as-built commands)

```bash
# scoring log (Log note ภายใน — ไม่สแปม follower)
odoo call-method crm.lead --method message_post \
  --args '[[<ID>]]' \
  --kwargs '{"body":"<html scoring>","subject":"AI Deal Scoring","subtype_xmlid":"mail.mt_note"}' 2>/dev/null

# CTA (โพสต์แยกหรือรวม)
odoo call-method crm.lead --method message_post \
  --args '[[<ID>]]' \
  --kwargs '{"body":"<html CTA>","subject":"Next Best Action","subtype_xmlid":"mail.mt_note"}' 2>/dev/null

# batch: เคลียร์ flag (เมื่อมี x_needs_strategy)
# odoo write crm.lead --ids <ID> --value '{"x_needs_strategy": false}' 2>/dev/null
```

**Log format (ย่อ):**
```
🎯 AI Deal Scoring — Tier <A/B/C/D> · confidence <H/M/L>
Value <n> (breakdown + evidence) · Deliverability <n> ([data]/[est])
Health <🔴🟡🟢> · MEDDICC gap: <...>
🎯 Next action: <1 อย่าง> · owner <..> · SLA <..>
🔀 Fork: ถ้า X → .. · ถ้า Y → ..
↩️ ตอบใน chatter → AI re-diagnose
```

---

## Decision priority (เมื่อมีหลาย flag → เลือก CTA เดียว)
```
1. killing-zone BLOCK   (override ทุกอย่าง)
2. graveyard/stale      (ดีลกำลังตาย)
3. MEDDICC gap หลัก     (champion/compelling event)
4. stage×tier base play
```
→ คืน **next best action เดียว** ไม่ใช่ list

---

## Continuity (loop — §8.4)
- chatter = memory: อ่าน note เก่าของ AI + คำตอบ AE → เข้าใจ evolution
- AE ตอบใน chatter → (batch) flag → รอบใหม่อ่าน context รวมคำตอบนั้น → re-diagnose + CTA ถัดไป
- **distill research ครั้งเดียว** เก็บสรุปใน chatter → รอบถัดไปไม่อ่าน raw (กัน token บวม)

## Token / cost discipline (§9)
| tier | depth | model | cadence |
|---|---|---|---|
| A | deep | Sonnet/Opus | ทุก event |
| B | เบา | Sonnet | event สำคัญ |
| C | template | Haiku | รายสัปดาห์ |
| D | ข้าม (ไม่ auto) | — | — |
- event-driven ไม่ full-sweep · cache refs · query เฉพาะ field ที่ใช้

---

## Edge cases
| กรณี | ทำอะไร |
|---|---|
| `x_deal_tier` ว่าง | คำนวณ (Step 2) + confidence flag |
| gap ไม่มี field | อนุมานจาก SO "GAP" line + chatter note |
| Trap (C) | ไม่สั่ง "ทุ่มปิด" — สั่ง de-risk (standard-first/reprice/champion) |
| gov deal | ข้าม Pumpkin/GAP → pre-TOR + TOR-factory context (ไม่ tier) |
| won/lost แล้ว | ไม่ diagnose — ส่งต่อ deal-lessons (จับเหตุ v2) |

## CLI cautions (validated)
- domain = JSON double-quote · fields = comma-string · ต่อท้าย `2>/dev/null` ตัด WARNING
- **สร้าง field ผ่าน RPC ไม่ได้** (registry reload timeout) → ทำ UI · แต่ write/message_post/create-record ได้ปกติ
- Lost Reason v2 = `crm.lost.reason` id 11–24 · `x_deal_tier` = Selection A/B/C/D

## Related
- [[deal-service-matrix]] (§4 play · §6 red flags · §8 context/CTA · §9 token) · [[customer-scorecard]] · [[strategy-doctrine]] · [[won-lost-cheatsheet]] · [[odoo-spec-reason-taxonomy]]
