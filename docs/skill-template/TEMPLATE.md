# ───────────────────────────────────────────────────────────────
# SKILL TEMPLATE — วิธีใช้
#
# 1. คัดลอกโฟลเดอร์นี้ไปไว้ใน  ../../skills/  (ไม่ใช่ docs/)
# 2. ตั้งชื่อโฟลเดอร์ใหม่ให้ตรงกับชื่อ skill เช่น  skills/my-new-skill/
# 3. เปลี่ยนชื่อไฟล์นี้จาก TEMPLATE.md เป็น  SKILL.md
#    (Claude Code scan เฉพาะไฟล์ชื่อ SKILL.md เท่านั้น)
# 4. แก้ทุกบรรทัดด้านล่างที่มี comment "# << แก้ตรงนี้"
# 5. สำคัญ: ค่า name ต้องตรงกับชื่อโฟลเดอร์ พอดีเป๊ะ
# ───────────────────────────────────────────────────────────────
---
name: skill-name                 # << แก้ตรงนี้ — ต้องตรงกับชื่อโฟลเดอร์ (ใช้ kebab-case, ห้ามเว้นวรรค)
description: "One sentence: when Claude should use this skill automatically. Be specific about triggers."   # << แก้ตรงนี้ — ระบุ trigger ให้ชัด ภาษาไทยหรืออังกฤษก็ได้
version: 1.0.0                   # << เริ่มที่ 1.0.0 เพิ่มเมื่อแก้ไขครั้งถัดไป
source: roots-custom             # << ปล่อยไว้ "roots-custom" สำหรับ skill ที่ Roots สร้างเอง
---

# Skill Title                    <!-- << แก้ตรงนี้ — ชื่อ skill แบบอ่านง่าย -->

## Purpose
What this skill helps the user accomplish.

## When to Use
- Trigger condition 1
- Trigger condition 2

## Process

### Step 1 — [Name]
Instructions for Claude...

### Step 2 — [Name]
Instructions for Claude...

## Output Format

```
## [Section Title]
[Content structure]
```

## Roots-Specific Notes
Any context from CONTEXT.md relevant to this skill.

## Examples

**Input:** "..."
**Output:** ...
