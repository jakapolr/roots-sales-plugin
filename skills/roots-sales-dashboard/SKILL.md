---
name: roots-sales-dashboard
description: Live sales performance dashboard for Roots.Tech, pulling actuals and pipeline directly from Odoo CE via odoorpc-cli. Three modes — strategic (YTD vs annual target), month (month-end close tracker), and intelligence (per-opportunity next-action analysis fusing priority, agent research, and activity log). Triggered by 'sales dashboard', 'dashboard ยอดขาย', 'ดูยอดเทียบเป้า', 'close เดือนนี้', 'ปิดเดือน', 'next action ดีล', 'วิเคราะห์ opportunity'. Requires odoorpc-cli installed and authenticated. Runs on Claude Code CLI (needs shell).
metadata:
  version: 1.0.0
  category: custom
---

# Roots Sales Dashboard

Dashboard ยอดขายสดจาก Odoo CE — ดึง actuals + pipeline ตรงจาก Odoo แล้ว render เป็น visual dashboard ไม่ต้องพึ่ง Google Sheet ที่อัปเดตมือ

## ⚠️ ข้อจำกัดสภาพแวดล้อม (อ่านก่อน)

skill นี้ใช้ `odoorpc-cli` ซึ่งเป็น **คำสั่ง shell** — ทำงานได้เฉพาะที่มี Bash:
- ✅ **Claude Code CLI** (terminal) — ใช้ได้เต็มรูปแบบ
- ❌ **Cowork (web)** — ดึงสดไม่ได้ (ไม่มี shell) ส่วน render artifact ทำได้ถ้ามีข้อมูลป้อนให้

ถ้าทีมใช้ Cowork: รัน skill นี้บน Claude Code CLI ก่อน (Phase 4 = ทำ Odoo MCP server แล้ว Cowork จะดึงสดเองได้)

## Pre-requisite

```bash
pip install odoorpc-cli
odoo auth login --host https://<odoo-host> --db <database> --username <email> --password <password>
odoo auth info   # ยืนยันว่าเชื่อมต่อแล้ว
```

ดู [odoorpc-cli skill](../odoorpc-cli/SKILL.md) สำหรับ syntax คำสั่งเต็ม

## โหมดการใช้งาน

เรียกด้วย **ภาษาธรรมชาติ** (skill นี้ไม่ใช่ slash command) — ระบุ mode ด้วยคำว่า strategic / month / intelligence

| พิมพ์ว่า (ตัวอย่าง) | Mode | คนใช้ | ตอบคำถาม |
|---|---|---|---|
| "sales dashboard เทียบเป้าทั้งปี" | 1 · Strategic | CEO / ผู้บริหาร | ทั้งปีจะถึง target ไหม |
| "dashboard ปิดเดือนนี้" / "close เดือนนี้" | 2 · Month close | Sales Manager | เดือนนี้ปิดเท่าไหร่ ดันดีลไหน |
| "วิเคราะห์ดีล next action" | 3 · Intelligence | AE / SE | ดีลไหนน่าสนใจ next action คืออะไร |

ถ้า user ไม่ระบุ mode ชัด ให้ถามว่าต้องการ mode ไหน หรือ default = strategic
ทั้ง 3 mode ดึงข้อมูลด้วย query ชุดเดียวกัน (ด้านล่าง) ต่างกันที่การ render

---

## ขั้นตอนร่วม (ทุก mode)

1. ตรวจ `odoo auth info` — ถ้าไม่ login ให้แจ้ง user รัน `odoo auth login` เอง
2. อ่าน target จาก [targets-2026.md](targets-2026.md)
3. ดึงข้อมูลตาม mode
4. แปลง product → bucket ตาม [product-map.md](product-map.md)
5. คำนวณ (ดูแต่ละ mode) — Claude คำนวณใน-context ทั้งหมด ไม่เขียนกลับ Odoo
6. Render เป็น artifact ด้วย visualize/show_widget (ดู layout แต่ละ mode)

> **เกณฑ์การเงินที่ verify แล้ว:** ใช้ `price_subtotal` (ก่อน VAT) — ตรงกับ Sheet ของบริษัท 100% (reconcile Jan–Jun 2026 ทุกบาท ยกเว้น drift ที่ระบบจะ flag)
> **BEECY:** ตัดออกทุก mode — ยอด BEECY มาจากระบบอื่น ไม่อยู่ใน sale orders นี้

---

## Mode 1 — Strategic (YTD vs Target)

### Query A — Actuals แยกหมวด (YTD)

```bash
odoo call-method sale.order.line --method read_group --args '[[["order_id.state","in",["sale","done"]],["order_id.date_order",">=","<YEAR>-01-01"],["order_id.date_order","<=","<TODAY>"]],["price_subtotal"],["product_id"]]'
```
→ ได้ยอดรวมต่อ product → map เป็น bucket → รวมตาม bucket

### Query B — Monthly trend

```bash
odoo call-method sale.order --method read_group --args '[[["state","in",["sale","done"]],["date_order",">=","<YEAR>-01-01"],["date_order","<=","<TODAY>"]],["amount_untaxed"],["date_order:month"]]'
```
→ ยอด untaxed รายเดือน (= sum ของ price_subtotal ในเดือนนั้น)

### คำนวณ
- `% achieved` ต่อ bucket = actual ÷ target
- `gap` = annual target − YTD actual
- `required run-rate` = gap ÷ เดือนที่เหลือ
- `current run-rate` = YTD actual ÷ เดือนที่ผ่าน

### Render (artifact)
- KPI cards: YTD revenue · annual target · % achieved · gap
- Run-rate callout: required vs current ต่อเดือน
- Bar chart: monthly revenue (เดือนปัจจุบัน = สีอ่อน = partial)
- Progress bars ต่อ bucket — สี: เขียว ≥50% / เหลือง 20–50% / แดง <20%
- หมายเหตุ adjustments: Hardware, Special Discount

---

## Mode 2 — Month Close Tracker

### Query C — ยอดยืนยันเดือนนี้ (MTD)

```bash
odoo search read sale.order --domain '[["state","in",["sale","done"]],["date_order",">=","<MONTH>-01"],["date_order","<=","<MONTH-END>"]]' --fields name,partner_id,user_id,amount_untaxed,date_order,invoice_status
```

### Query D — ดีลที่ครบกำหนดภายในเดือนนี้ (รวมที่เลยกำหนด)

```bash
odoo search read crm.lead --domain '[["type","=","opportunity"],["active","=",true],["stage_id.is_won","=",false],["date_deadline","<=","<MONTH-END>"]] ' --fields name,partner_id,user_id,stage_id,expected_revenue,probability,date_deadline,activity_state,activity_date_deadline --order 'date_deadline asc'
```

### คำนวณ
- `committed` = Σ amount_untaxed ของ MTD orders
- `monthly target` = annual target ÷ 12
- `forecast close` = committed + Σ(expected_revenue × probability) ของดีลที่ปิดได้จริงในเดือน (prob ≥ ~30% และ stage ปลาย)
- `gap to target` = monthly target − forecast
- `days left` = วันสิ้นเดือน − วันนี้

### การจัดอันดับ "plays" (closeability)
เรียงดีลตาม **closeability score = expected_revenue × probability × urgency**
(urgency สูง = deadline ใกล้/เลย + stage ปลาย) — ไม่ใช่เรียงตามมูลค่าดิบ

### แยกออกเป็น 2 กลุ่ม
- **Plays (ดันได้):** ดีลที่มีมูลค่า + prob พอควร → แสดง action ต่อดีล
- **Decisions needed:** ดีลเลยกำหนดนาน / prob ~0 / `expected_revenue = 0` → ต้องตัดสินใจ archive/re-date/เติมข้อมูล

### Render (artifact)
- KPI cards: committed · forecast close · monthly target · gap
- Forecast bar 3 สี: committed | likely | gap
- "Plays for the next N days" — list เรียงตาม closeability + action chip ต่อแถว
- "Decisions needed" — ดีลค้าง/ไม่มีมูลค่า
- ปุ่ม sendPrompt → ต่อเข้า `draft-outreach` / `call-prep`

---

## Mode 3 — Opportunity Intelligence (Next Action)

ดึงสัญญาณ 4 ด้านต่อดีล แล้วสังเคราะห์เป็น next action

### Query E — ดีล priority สูง + research + activity

```bash
odoo search read crm.lead --domain '[["type","=","opportunity"],["active","=",true],["stage_id.is_won","=",false],["priority","in",["3","4","5"]]] ' --fields name,partner_id,user_id,stage_id,priority,probability,expected_revenue,date_deadline,research_status,activity_state,activity_summary,activity_date_deadline,date_last_stage_update --order 'priority desc'
```

### Query F — research ที่ agent เขียนไว้ (เฉพาะดีลที่เลือก)

```bash
odoo search read crm.lead --domain '[["id","in",[<ids>]]]' --fields name,business_research,financial_research,analysis_description,description
```
research/financial เป็น text/html — distill เป็น insight 1–2 บรรทัด (อย่า dump เต็ม)

### Signal fusion → classify next action

| สัญญาณ | field |
|---|---|
| ความตั้งใจทีม | `priority` (0 Zero → 5 Very High) |
| คุณภาพลูกค้า | `business_research` + `financial_research` |
| โมเมนตัม | `activity_state` (overdue/today/planned) + `date_last_stage_update` |
| ความเป็นจริง | `probability` + `stage_id` |

**กฎ classify:**
```
research ดี + prob สูง + activity ค้าง        → ACCELERATE  (ลูกค้าดี เราช้าเอง)
prob ดี + deadline เดือนนี้ + มี activity วาง  → CLOSE THIS MONTH
value สูง + prob ~0 + ค้างนาน               → ESCALATE OR KILL (อย่าถ่วง forecast)
research ขาด / expected_revenue = 0          → ENRICH FIRST (เติมข้อมูลก่อน)
```

### คัดเฉพาะเคสน่าสนใจ — "signal conflict"
แสดงเฉพาะดีลที่สัญญาณขัดแย้งกัน (จุดที่ต้องตัดสินใจ) ไม่แสดงทุกดีล:
- priority สูง แต่ prob ต่ำ
- research done แต่ activity overdue
- prob สูง + deadline ใกล้ แต่ไม่มี activity วางไว้

ดีลที่ขยับสม่ำเสมอตาม prob = ปกติ → ไม่ต้อง surface (ลด noise)

### Render (artifact)
- การ์ดต่อดีล: header (ชื่อ/มูลค่า/priority/owner) + recommendation badge
- signal chips: prob · research status · activity state · stale N days
- research insight 1–2 บรรทัด (distilled)
- → next action (specific, actionable)
- ปุ่ม sendPrompt → ต่อเข้า `draft-outreach` / `call-prep`

---

## หมายเหตุการ reconcile

ถ้ายอด Odoo ต่างจาก Sheet ของบริษัท ให้ flag ให้ user (ไม่ใช่ปกปิด) — เช่น order ถูก re-date/ยกเลิก/เปลี่ยน state หลัง Sheet อัปเดตล่าสุด นี่คือคุณค่าหลักของ dashboard สด: จับข้อมูลค้างที่ manual sheet พลาด

## การนำผลไปใช้ต่อ
- `/sales:forecast` — ใช้ weighted pipeline เป็น input
- `/sales:pipeline-review` — วิเคราะห์เชิงกลยุทธ์
- `se-orchestrator` — ส่งดีลที่ต้องการ SE
- `/sales:draft-outreach`, `/sales:call-prep` — ลงมือ follow-up จาก next action
