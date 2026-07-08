---
name: deal-lessons
description: "จับเหตุ Won/Lost ของดีล (จาก lost_reason_id v2 / x_won_reason) → สร้าง lesson 1 ชิ้น → เขียน chatter + append lessons register → เคลียร์ x_needs_lesson. Trigger: 'capture lesson [deal]', 'บันทึกบทเรียนดีล', หรือถูกเรียกโดย strategy-orchestrator เมื่อ x_needs_lesson=true. ขยาย roots-lessons-learned จาก TOR-only → ทุกดีล. CLI-only."
version: 1.0.0
source: roots-custom
phase: 4
---

# Deal Lessons — capture Won/Lost (v4 Loop 1)

> **Custom Skill** — Built by Roots.Tech
> **อ่านก่อน:** [[won-lost-cheatsheet]] · [[strategy-doctrine]] · [[odoo-spec-reason-taxonomy]]
> **CLI-only** · ขยาย `roots-lessons-learned` (เดิม TOR-only) → **ทุกดีล**
> **Purpose:** เปลี่ยนทุก win/loss เป็น knowledge ที่กลั่นเป็น wisdom (Playbook) ได้ทีหลัง

## Trigger
- strategy-orchestrator ส่งดีลที่ `x_needs_lesson=true` (Won/Lost hook)
- manual: "บันทึกบทเรียนดีล [name]"

## Process

### Step 1 — Read outcome + reason
```bash
odoo search read crm.lead --domain '[["id","=",<ID>]]' \
  --fields "name,partner_id,stage_id,active,expected_revenue,lost_reason_id,x_won_reason,x_deal_tier" 2>/dev/null
# lost = archived → เพิ่ม context {"active_test": false}
```
- **Lost** (`active=false`) → อ่าน `lost_reason_id` (v2, id 11–24)
- **Won** (`stage_id.is_won`) → อ่าน `x_won_reason`

### Step 2 — สร้าง lesson 1 บรรทัด (map แกน [[won-lost-cheatsheet]])
รูปแบบ: **"[Won/Lost] เพราะ <เหตุ> → ครั้งหน้า <สิ่งที่ทำต่าง>"**
- ผูกกับแกน: Champion / Compelling event / Compete / Value / Fit / Process
- ถ้าเหตุ = "Unknown - needs review" → flag ให้ manager (อย่าปล่อยผ่าน)

### Step 3 — เขียนกลับ + เก็บ knowledge
```bash
# post lesson ลง chatter
odoo call-method crm.lead --method message_post --args '[[<ID>]]' \
  --kwargs '{"body":"<html lesson>","subject":"AI Deal Lesson","subtype_xmlid":"mail.mt_note"}' 2>/dev/null
# clear flag
odoo write crm.lead --ids <ID> --value '{"x_needs_lesson": false}' 2>/dev/null
```
- (ภายหลัง) append ลง lessons register — ขยาย target ของ `roots-lessons-learned` จาก TOR register → all-deals register

### Step 4 — feed wisdom
lesson สะสม → `playbook-synthesis` (v4 Loop 3) กลั่นเป็น Roots Playbook รายเดือน/ไตรมาส
> ต้อง symmetric (Won ↔ Lost แกนเดียวกัน) เพื่อคำนวณว่า *แกนไหน correlate กับชนะ vs แพ้*

## Output format (lesson)
```
📌 AI Deal Lesson — [Won/Lost] · Tier <x>
เหตุ: <lost_reason v2 / x_won_reason>  (แกน: <Champion/Event/...>)
บทเรียน: <ครั้งหน้าทำอะไรต่าง>
มูลค่า: ฿<x>  ·  สำหรับ Playbook: <pattern ย่อ>
```

## Edge cases
| กรณี | ทำอะไร |
|---|---|
| ไม่มี reason (lost แต่ lost_reason_id ว่าง) | flag "reason ขาด" ให้ AE เติม (v2 ควร required) |
| reason = "Unknown - needs review" | escalate manager |
| Won แต่ x_won_reason ว่าง | ขอ AE เติม (บังคับ on Won) |

## Related
- [[won-lost-cheatsheet]] · [[strategy-orchestrator]] · [[deal-strategy]] · [[odoo-spec-reason-taxonomy]] · roots-lessons-learned
