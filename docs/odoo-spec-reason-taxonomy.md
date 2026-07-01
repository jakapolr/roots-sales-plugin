# 🔧 Odoo Spec — Lost Reason v2 + Won Reason + Hook Flags

> สำหรับ **Senior Technical** — spec ฝั่ง Odoo ที่ต้องทำใน **Phase 0** (เป็น dependency ของ v4.0 deal-strategy ทั้งหมด)
> ทำได้ **no-code เกือบทั้งหมด** (Settings → Technical) — ไม่ต้อง custom module ยกเว้นฟิลด์ 4 ตัว

| | |
|---|---|
| **Scope** | `crm.lead`, `crm.lost.reason` |
| **Edition** | Odoo CE (Community) — ทุกอย่างในนี้ทำได้บน CE |
| **Roadmap** | [`ROADMAP_v4_deal-strategy.md`](ROADMAP_v4_deal-strategy.md) |
| **สร้างเมื่อ** | 2026-07-01 |

---

## 1) ปัญหาของ setup ปัจจุบัน

| ปัญหา | ผลกระทบ |
|---|---|
| **"No response"** ถูกใช้เป็นเหตุปิดแบบมักง่าย (~196 ดีล) | ไม่รู้เหตุจริง → เอามาทำ strategy ไม่ได้ |
| มี free-text ปนใน lost reason | วิเคราะห์เป็นกลุ่มไม่ได้ |
| **ไม่มี Won Reason** เลย | รู้แค่ว่าแพ้เพราะอะไร ไม่รู้ว่าชนะเพราะอะไร → หา pattern การชนะไม่ได้ |

> **Single change ที่ให้ผลมากสุด:** แบน "No response" เป็นเหตุปิด แล้วบังคับใส่เหตุจริง

---

## 2) Lost Reason v2 — 2-tier taxonomy

**Tier 1 = Category (root cause)** → **Tier 2 = เหตุเจาะจง (คือ record ใน `crm.lost.reason`)**

| Tier 1 (category) | Tier 2 reason (`crm.lost.reason`) | strategy ที่ปลดล็อก |
|---|---|---|
| **Qualification** | No budget confirmed | qualify budget เร็วขึ้น |
| | No compelling event / bad timing | เข้ม compelling event ก่อน invest |
| | Not ICP — disqualified | แก้ที่ marketing/targeting |
| **Champion** | Lost champion / went dark | multi-thread, test champion |
| | No economic-buyer access | หา EB ให้เจอก่อนเสนอราคา |
| **Competition** | Lost to competitor — capability | shape decision criteria ก่อน RFP |
| | Lost to competitor — price | สร้าง ROI/TCO |
| | Lost to incumbent / status quo | สร้าง cost-of-inaction |
| **Value / Price** | Price too high vs value | value selling, ไม่ลดราคาลูกเดียว |
| | ROI not established | ใส่ metric ที่วัดได้ |
| **Capability** | Odoo capability gap | qualify fit เร็ว, อย่า oversell |
| | Customer not ready (no capacity) | qualify implementation readiness |
| **Process / Internal** | Roots too slow to respond | SLA ตอบกลับ |
| | Follow-up dropped | post-quote discipline |
| | Quote error / scope mismatch | QA ก่อนส่ง quote |

### กฎเหล็ก
- ❌ **ลบ "No response" ออกจาก catalog** — ห้ามเป็นเหตุปิด
- ถ้าไม่รู้เหตุจริง → ต้องเลือก `Unqualified — reason unknown` **พร้อม note บังคับ** และ flag ให้ manager review (ไม่ใช่ terminal เงียบ ๆ)

### ทางเลือกการ implement 2-tier บน Odoo CE
| ทางเลือก | วิธี | ข้อดี/ข้อเสีย |
|---|---|---|
| **A (แนะนำ)** | ตั้งชื่อ `crm.lost.reason` แบบ `Category: Reason` (เช่น `Champion: Lost champion / went dark`) | no-code 100%, group-by ได้ด้วยชื่อ / อ่านยากขึ้นเล็กน้อย |
| **B** | เพิ่มฟิลด์ `x_lost_category` (selection) บน `crm.lead` แยกจาก reason | reporting สะอาดกว่า / ต้องเพิ่ม field + ให้ user เลือก 2 ช่อง |

---

## 3) Won Reason — ฟิลด์ใหม่ `x_won_reason`

Odoo ไม่มี native Won Reason → เพิ่มฟิลด์ selection บน `crm.lead`

| ค่า (value) | label |
|---|---|
| `champion_driven` | Champion drove it internally |
| `compelling_event` | Compelling event / deadline |
| `localization_fit` | Thai localization / vertical fit (BEECY) |
| `displaced_competitor` | Displaced a competitor |
| `price_tco` | Best price / TCO |
| `relationship_referral` | Relationship / referral |
| `fast_low_risk` | Fast, low-risk delivery |

**Field definition**
```
Model:      crm.lead
Name:       x_won_reason
Type:       Selection
Tracking:   True        (ให้ขึ้น chatter)
Required:   เมื่อ stage = Won (บังคับผ่าน view / Automation)
```

---

## 4) Migration mapping (เหตุเก่า → ใหม่)

| เหตุเดิม | map ไป Tier 2 ใหม่ |
|---|---|
| No response (after quote) | Lost champion / went dark **หรือ** No compelling event *(ต้อง review รายดีล)* |
| No response (before quote) | Not ICP — disqualified **หรือ** No economic-buyer access |
| Too expensive | Price too high vs value |
| Chose competitor | Lost to competitor — capability / price *(ระบุ)* |
| No budget | No budget confirmed |
| (free-text อื่น ๆ) | review แล้ว map เข้ากลุ่มที่ใกล้สุด |

> ดีลเก่าที่ปิดแล้ว: map เท่าที่ทำได้ ส่วนดีลใหม่บังคับ taxonomy ใหม่ตั้งแต่ go-live

---

## 5) Hook flags — 2 ฟิลด์ boolean

| Field | Type | Default | Trigger ที่ set = true |
|---|---|---|---|
| `x_needs_strategy` | Boolean | false | stage เข้า Quoting/Proposing |
| `x_needs_lesson` | Boolean | false | Won หรือ Lost |

Tracking = True ทั้งคู่ ( debug ง่าย). Claude เป็นคนเขียนกลับเป็น false หลังประมวลผลเสร็จ

---

## 6) Automation Rules (no-code)

**Settings → Technical → Automation Rules** (`base_automation`) — ไม่ต้องเขียนโค้ด

### Rule A — Flag for AI strategy
```
Model:      crm.lead
Trigger:    On Update  →  ฟิลด์ stage_id
Before/domain:  stage_id in [Quoting, Proposing]  AND  x_needs_strategy = false
Action:     Update Record  →  x_needs_strategy = true
```

### Rule B — Flag for AI lesson (Lost)
```
Model:      crm.lead
Trigger:    On Update  →  active เปลี่ยนเป็น false   (ดีลถูก mark lost)
Action:     Update Record  →  x_needs_lesson = true
```

### Rule C — Flag for AI lesson (Won)
```
Model:      crm.lead
Trigger:    On Update  →  stage_id = Won (is_won = true)
Action:     Update Record  →  x_needs_lesson = true
```

---

## 7) Write-back contract (Claude → Odoo)

Claude poll ใช้ `odoorpc-cli` เขียนผลกลับผ่าน `message_post` (ลง chatter ของดีล)

### Strategy (Loop 2) — post ลง chatter
```
odoo call-method crm.lead --method message_post \
  --args '[[<lead_id>]]' \
  --kwargs '{"body": "<html diagnosis>", "subject": "AI Deal Strategy"}'
# แล้วเคลียร์ flag
odoo write crm.lead <lead_id> '{"x_needs_strategy": false}'
```

**รูปแบบ body (strategy):**
```
## 🧭 AI Deal Strategy — <date>
Health: 🟡 Yellow
MEDDICC gap: ไม่มี Champion, Compelling event ยังไม่ชัด
Next best action: นัด economic buyer ภายใน 5 วัน / ยืนยัน deadline โครงการ
Owner: <AE>  ·  Due: <date>
```

### Lesson (Loop 1) — เก็บ knowledge + เคลียร์ flag
```
# 1. append ลง lessons register (Drive / Obsidian)
# 2. (optional) message_post สรุป lesson ลง chatter
# 3. เคลียร์ flag
odoo write crm.lead <lead_id> '{"x_needs_lesson": false}'
```

---

## 8) Poll job contract (Claude)

Scheduled job (Claude Code scheduled task / cron) อ่านดีลที่ flag แล้ว route:

```
odoo search_read crm.lead \
  --domain "['|', ('x_needs_strategy','=',True), ('x_needs_lesson','=',True)]" \
  --fields "id,name,stage_id,x_needs_strategy,x_needs_lesson,lost_reason_id,x_won_reason" 2>/dev/null
```
- `x_needs_strategy` → รัน `deal-strategy` → write-back → clear
- `x_needs_lesson` → รัน `roots-lessons-learned` → capture reason → clear
- **Idempotent:** flag เป็นตัวกันประมวลผลซ้ำ (เคลียร์แล้วจะไม่ถูกหยิบอีก)

---

## 9) Definition of Done (acceptance)

- [ ] "No response" ถูกลบออกจาก `crm.lost.reason`
- [ ] Lost ทุกดีลมี category + reason ตาม taxonomy v2 (ถ้า unknown ต้องมี note)
- [ ] `x_won_reason` บังคับกรอกเมื่อ stage = Won
- [ ] 4 custom fields สร้างครบ (`x_won_reason`, `x_needs_strategy`, `x_needs_lesson`, และ `x_lost_category` ถ้าเลือกทางเลือก B)
- [ ] Automation Rule A/B/C ทำงาน: flag flip ถูกต้องเมื่อ stage change / won / lost
- [ ] Claude poll เขียนผลกลับ chatter ได้ และ **เคลียร์ flag** — ไม่มี double-post
- [ ] Field help text อธิบาย taxonomy ให้ user เลือกถูกหน้างาน

---

## 10) Rollout order (Phase 0)

```
1. สร้าง 4 custom fields
2. restructure crm.lost.reason (ลบ No response, ใส่ taxonomy v2) + help text
3. migrate เหตุเก่าเท่าที่ทำได้
4. เปิด Automation Rule A/B/C
5. ทดสอบ: เลื่อน stage / mark won / mark lost → เช็ค flag + chatter write-back
6. เปิดใช้จริง + สอนทีม (KT Track A)
```

> เสร็จ Phase 0 → plugin ฝั่ง v4.0 (Loop 1/2/3) ถึงจะมีข้อมูลพอทำงาน
