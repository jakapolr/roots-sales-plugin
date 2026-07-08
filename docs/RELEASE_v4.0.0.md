# 🎯 Roots Sales Plugin v4.0.0 — Release Summary

> สำหรับทีม Roots.Tech — v4 คือ **Hunting Strategy layer**: เปลี่ยน plugin จาก *"ทำงานให้"* เป็น *"คิดกลยุทธ์การล่าให้"*

---

## มีอะไรใหม่

v4.0.0 เพิ่มชั้น **กลยุทธ์การขาย** — ทุกดีลถูก score → จัด tier → บอก next best action ตาม methodology จริง (ICP · scorecard v2 · killing zone · MEDDICC · service matrix)

| ประเภท | ชื่อ | ทำอะไร |
|---|---|---|
| skill | **`deal-strategy`** | วินิจฉัยดีลเดียว — score tier (scorecard v2) + MEDDICC + killing-zone gate → เขียน scoring + Next Best Action (CTA) ลง Odoo chatter |
| skill | **`deal-lessons`** | จับเหตุ Won/Lost (reason v2) → สร้าง lesson (ขยาย roots-lessons-learned → ทุกดีล) |
| agent | **`strategy-orchestrator`** | batch — poll ดีลที่ Odoo hook ตั้ง flag → route → write-back chatter → clear flag |
| references | `strategy-doctrine` · `customer-scorecard` · `deal-service-matrix` · `won-lost-cheatsheet` | doctrine (4 ทฤษฎี) · ICP+scorecard v2 · allocation+CTA+token · Won/Lost symmetric |

## ต้องตั้งค่าฝั่ง Odoo (Phase 0 — as-built แล้ว)

| item | สถานะ |
|---|---|
| 5 custom fields: `x_deal_tier` · `x_won_reason` · `x_gap_status` · `x_needs_strategy` · `x_needs_lesson` | ✅ |
| Lost Reason v2 (14 เหตุ root-cause) | ✅ |
| Automation Rules A/B/C (stage→Quoting/Proposing · Won · Lost → ตั้ง flag) | ✅ |

> รายละเอียด field/rule ทั้งหมด → [`odoo-spec-reason-taxonomy.md`](odoo-spec-reason-taxonomy.md)

## Loop (ทำงานยังไง)

```
Odoo: stage เปลี่ยน/Won/Lost  → Automation Rule ตั้ง flag อัตโนมัติ
   ↓
strategy-orchestrator: poll flag → deal-strategy/deal-lessons → เขียน chatter → clear flag
```
- **chatter = memory ร่วม** AI↔AE → รอบถัดไปอ่าน note เก่า + คำตอบ AE → เข้าใจต่อเนื่อง
- **token discipline:** process เฉพาะ flagged · tier-gate ความลึก (A ลึก → D ข้าม)

## ⚠️ ข้อจำกัด

- Skill/agent ที่แตะ Odoo = **Claude Code CLI เท่านั้น** (Cowork รอ Odoo MCP)
- Batch/loop = scheduled job (CLI) · realtime push = Phase 4

---

## 🔧 วิธีอัปเดต (ทำตามลำดับ!)

```bash
# 1. ดึง marketplace ล่าสุดก่อน (จำเป็น — ข้ามแล้วได้ version เก่าจาก cache)
claude plugin marketplace update roots-sales-plugin
# 2. อัปเดต plugin
claude plugin update sales@roots-sales-plugin
# 3. restart Claude Code
```
เช็ค: `claude plugin list` → `sales  4.0.0  enabled`

## วิธีใช้ (ตัวอย่าง)

```
"ดีลนี้ทำอะไรต่อ" / "score ดีล [ชื่อ]"   → deal-strategy (วินิจฉัยเดี่ยว + CTA)
"run strategy orchestrator" / "รันคิว AI" → strategy-orchestrator (batch)
```

## v5 (next) — Farming Strategy

recurring 16% → 50% (Hunter → Farmer) · ดู [`ROADMAP_v5_farmer-strategy.md`](ROADMAP_v5_farmer-strategy.md)
