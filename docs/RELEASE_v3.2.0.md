# 📊 Roots Sales Plugin v3.2.0 — Release Summary

> สำหรับทีม Roots.Tech — อ่านเพื่อเข้าใจว่ามีอะไรใหม่ ติดตั้งยังไง และใช้งานยังไง

---

## มีอะไรใหม่

v3.2.0 ทำให้ plugin **เชื่อมต่อ Odoo CE ของบริษัทได้สด** — ดึงยอดขาย/pipeline จริงมาทำ dashboard โดยไม่ต้องกรอก Google Sheet มือ

| รุ่น | เพิ่มอะไร |
|---|---|
| v3.1.0 | เชื่อม Odoo CE — `odoorpc-cli`, `odoo-crm-sync`, `odoo-sales-report` |
| **v3.2.0** | **`roots-sales-dashboard`** — dashboard สด 3 mode |

### 3 โหมดของ dashboard

| Mode | ใครใช้ | ตอบคำถาม |
|---|---|---|
| `strategic` | ผู้บริหาร | ทั้งปีจะถึง target ไหม (YTD vs เป้า + trend รายเดือน) |
| `month` | Sales Manager | เดือนนี้ปิดเท่าไหร่ ดันดีลไหน |
| `intelligence` | AE / SE | ดีลไหนน่าสนใจ next action คืออะไร (รวม priority + research + activity) |

> ⚠️ **สำคัญ:** Odoo skills ทำงานบน **Claude Code CLI (terminal)** เท่านั้น — Cowork ยังดึงสดไม่ได้ (รอ Odoo MCP server ใน Phase 4)

---

## 🔧 วิธีติดตั้ง

### A. Update (คนที่มี plugin อยู่แล้ว)

⚠️ **ต้องทำตามลำดับนี้** — ถ้าข้ามขั้น 1 จะได้เวอร์ชันเก่าจาก cache (เป็นปัญหาที่เจอบ่อย)

```bash
# 1. ดึง marketplace ล่าสุดจาก GitHub ก่อน (จำเป็น!)
claude plugin marketplace update roots-sales-plugin

# 2. อัปเดต plugin — ต้องมี @roots-sales-plugin ต่อท้าย
claude plugin update sales@roots-sales-plugin

# 3. ปิด-เปิด Claude Code ใหม่ (จำเป็น — ต้อง restart ถึงจะมีผล)
```
เช็ค: `claude plugin list` → ต้องเห็น `sales  3.2.0  enabled`

> ❌ อย่ารัน `claude plugin update sales` เฉย ๆ (ไม่เจอ — ต้องมี `@roots-sales-plugin`)
> ❌ อย่าข้ามขั้น 1 — ไม่งั้น `update`/`install` จะดึงจาก cache เก่า ได้เวอร์ชันเดิม

### B. Fresh Install (คนใหม่)

```bash
claude plugin marketplace add jakapolr/roots-sales-plugin
claude plugin install sales@roots-sales-plugin
# ปิด-เปิด Claude Code ใหม่ เพื่อโหลด plugin
```

### C. ติดตั้ง odoorpc-cli (จำเป็นสำหรับ Odoo skills ทุกตัว)

#### 🍎 Mac
```bash
# วิธี 1 — Homebrew (แนะนำ)
brew tap biszx/tap https://github.com/biszx/homebrew-tap
brew install biszx/tap/odoorpc_cli

# วิธี 2 — pip
pip3 install odoorpc-cli
```

#### 🪟 Windows
```powershell
# วิธี 1 — pip (ต้องมี Python ก่อน)
pip install odoorpc-cli

# วิธี 2 — ดาวน์โหลด installer (.exe) จาก GitHub Releases ของ biszx/odoorpc-cli
#          → odoorpc_cli-X.Y.Z-setup.exe (ไม่ต้องมี Python)
```

#### เชื่อมต่อ Odoo (ทั้ง Mac / Windows ทำเหมือนกัน)
```bash
odoo auth login --host https://<odoo-ของบริษัท> --db <database> --username <email> --password <password>
odoo auth info    # ✅ ต้องเห็นชื่อ + บริษัทตัวเอง
```
> ตั้งค่าครั้งเดียว — credential เก็บในเครื่อง

---

## 📖 วิธีใช้งาน + ตัวอย่าง

### 1. คำสั่ง odoorpc พื้นฐาน

```bash
# ดู pipeline ที่ยัง active
odoo search read crm.lead \
  --domain '[["type","=","opportunity"],["active","=",true]]' \
  --fields name,stage_id,expected_revenue,probability --limit 10

# นับดีลทั้งหมด
odoo search count crm.lead --domain '[["type","=","opportunity"],["active","=",true]]'

# ดู sale orders ที่ยืนยันแล้วเดือนนี้
odoo search read sale.order \
  --domain '[["state","in",["sale","done"]],["date_order",">=","2026-06-01"]]' \
  --fields name,partner_id,amount_untaxed,invoice_status

# ดู field ทั้งหมดของ model (ใช้ตอน explore)
odoo model field crm.lead
```

### 2. ใช้ผ่าน Skills (พิมพ์ภาษาธรรมชาติ — ไม่ใช่ slash command)

> ⚠️ `roots-sales-dashboard` เป็น **skill** ไม่ใช่ command — **อย่าพิมพ์** `/sales:roots-sales-dashboard` (จะขึ้น "Unknown command")
> พิมพ์เป็นประโยคปกติ แล้ว Claude จะ trigger skill ให้เอง

| อยากได้ | พิมพ์ว่า (ตัวอย่าง) |
|---|---|
| Dashboard ทั้งปี | "ทำ sales dashboard เทียบเป้าทั้งปีให้หน่อย" |
| ปิดเดือนนี้ | "ดู dashboard ปิดเดือนนี้ จาก Odoo" |
| Next action ต่อดีล | "วิเคราะห์ดีลน่าสนใจ next action จาก Odoo" |
| Pipeline สด | "ดึง pipeline จาก Odoo แยกตาม salesperson" |
| รายงานยอดขาย | "สรุปยอดขายเดือนพฤษภาคมจาก Odoo" |
| ไม่รู้จะใช้ตัวไหน | "ช่วยแนะนำ" → sales-help จะ route ให้ |

> หมายเหตุ: `/sales:pipeline-review` และ `/sales:meeting-search` เป็น **command** (เรียกด้วย `/` ได้) — ส่วน dashboard และ Odoo skills อื่นเรียกด้วยประโยค

### 3. ตัวอย่างจริง — ปิดเดือน

```
You: /sales:roots-sales-dashboard month
Claude: [ดึง Odoo สด] → June: committed ฿0.55M, forecast ~฿2.0M,
        target ฿6.1M, เหลือ 16 วัน
        Plays: STMS ฿2M (ปิดได้), โชคพิพัฒน์ ฿0.5M (quick win)...
        [ปุ่ม Draft follow-up เชื่อมเข้า draft-outreach]
```

---

## 🧠 เบื้องหลัง dashboard (สำหรับคนที่อยากเข้าใจลึก)

- **Actuals แยกหมวด** = `sale.order.line` → `price_subtotal` (ก่อน VAT) group by product → map เป็น bucket
- **Monthly trend** = `sale.order` → `amount_untaxed` group by `date_order:month`
- **Pipeline** = `crm.lead` (expected_revenue × probability)
- **Intelligence** = หลอม `priority` + `business_research`/`financial_research` (agent เขียนไว้) + `activity_state` → next action
- **Reconcile แล้ว:** ตัวเลขตรงกับ Sales Performance sheet ระดับบาท (Jan 2026) — ถ้าต่างกัน dashboard จะ flag ให้ตรวจ
- **BEECY:** ตัดออก (ยอดมาจากระบบอื่น)

config อยู่ที่ `skills/roots-sales-dashboard/targets-2026.md` (เป้าหมาย) และ `product-map.md` (product → bucket)

---

## ✅ สรุปสถานะ

- **v3.2.0 · 32 skills** · validation ผ่าน
- repo: https://github.com/jakapolr/roots-sales-plugin

## 🔭 ถัดไป (roadmap)

| Phase | สิ่งที่จะทำ |
|---|---|
| 4 | Odoo MCP server (HTTP) → Cowork ดึงสดเองได้ · Fireflies · e-GP monitor |
