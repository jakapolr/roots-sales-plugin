# 🧭 Roadmap v4.0 — deal-strategy: the Strategy Layer

> สำหรับทีม Roots.Tech + Senior Technical — เอกสารวางแผน v4.0 ว่าจะทำอะไร ทำไม และองค์กรต้องปรับอะไรบ้าง

| | |
|---|---|
| **Target version** | v4.0.0 |
| **Depends on** | Phase 0 data spine (ดู [`odoo-spec-reason-taxonomy.md`](odoo-spec-reason-taxonomy.md)) |
| **สถานะ** | Planning — ยังไม่เริ่ม implement |
| **สร้างเมื่อ** | 2026-07-01 |

---

## 1) Purpose — ทำไมต้องมีชั้นนี้

v3.x ทั้งหมดคือ **Tools layer** — plugin "ทำงานให้" (research, estimate, deck, dashboard, TOR)
แต่ที่เราเสีย **฿609M** ไป *ไม่ใช่เพราะ tool ไม่ดี* — เพราะ **strategy หาย** (ไม่มี champion, ไม่มี compelling event, ดีลตายหลัง quote). Tool ที่ดีขึ้นไม่ได้แก้ deal ที่ไม่มี champion

> **Thesis v4.0:** ยกระดับจาก *"Information → Action"* เป็น *"Data → Diagnosis → Strategy → Discipline"*
>
> **เป้าหมายหนึ่งบรรทัด:** ให้ AE ทุกคนมี **judgment ระดับ Sales Director ติดตัวทุกดีล** — plugin เลิกเป็นแค่คนทำงาน กลายเป็น **deal coach** ที่เรียนรู้ว่าเราชนะ/แพ้เพราะอะไร แล้ววินิจฉัยดีลปัจจุบัน + สั่ง next play ได้

---

## 2) The shift — Tools → Strategy

```
        v3.x TOOLS layer                        v4.0 STRATEGY layer
  (research·estimate·deck·TOR)   ────────▶   (diagnose·prescribe·learn)
       "ทำงานให้"                              "ตัดสินใจว่าอะไรชนะดีล"
```

---

## 3) Architecture — the engine

```
                    THE ENGINE — 3-loop flywheel
   ┌───────────────┐     ┌─────────────────┐     ┌───────────────────┐
   │ Loop 1 · Learn│ ──▶ │ Loop 2 ·Diagnose│ ──▶ │ Loop 3 ·Synthesise│
   │ won/lost →    │     │ MEDDICC score,  │     │ lessons →         │
   │ lessons       │     │ next best action│     │ Roots Playbook    │
   └───────┬───────┘     └─────────────────┘     └─────────┬─────────┘
           ▲                                                │
           └────────── Playbook sharpens the diagnosis ◀────┘

   DATA SPINE (build first — no-code in Odoo)
   [ Lost Reason v2 ] [ Won Reason ] [ 2 hook flags ] [ Automation Rules ]
```

**Flywheel:** Playbook (Loop 3) กลายเป็น *เกณฑ์* ที่ Loop 2 ใช้วินิจฉัย → ยิ่งปิดดีลมาก ยิ่งฉลาดขึ้น

---

## 4) The 3 loops (รายละเอียด)

| Loop | Trigger | ทำอะไร | Output | ตรงกับคำที่วางไว้ |
|---|---|---|---|---|
| **1 · Learn** | Won / Lost | จับเหตุ (Won/Lost reason) + สร้าง lesson 1 ชิ้น | lessons register | "ทำ Lesson learn เก็บเป็น Knowledge" |
| **2 · Diagnose** | Stage → Quoting/Proposing | ให้คะแนน MEDDICC + สั่ง next best action เขียนกลับ Odoo chatter | deal health + next play | "Review situation → ทำ Strategy ต่อ" |
| **3 · Synthesise** | รายเดือน/ไตรมาส | กลั่น lessons ทั้งหมด → **Roots Playbook** | wisdom (living doc) | "Summarize build wisdom ทีหลัง" |

### Loop 1 — Learn (capture)
- ขยาย skill `roots-lessons-learned` ที่ **ปัจจุบันผูกกับ TOR bids (G6) เท่านั้น** → ให้ครอบ **ทุก `crm.lead`** ไม่ใช่แค่ประมูลราชการ
- ทุกดีลที่ Won/Lost → บันทึก 1 lesson พร้อม Won/Lost reason (จาก taxonomy ใหม่)

### Loop 2 — Diagnose (the new brain)
- skill ใหม่ `deal-strategy` — อ่านสถานการณ์ดีล (stage, activity, research fields, ประวัติ) แล้วให้ **MEDDICC-style scorecard**:
  - มี **M**etric / **E**conomic buyer / **D**ecision criteria / **C**hampion / **C**ompelling event ครบไหม
  - health = แดง/เหลือง/เขียว + **next best action** ที่เจาะจง
- เขียนผลกลับเข้า **chatter ของดีลใน Odoo** (rep เห็นตรงที่ทำงาน)

### Loop 3 — Synthesise (wisdom)
- skill ใหม่ `playbook-synthesis` — รายเดือน/ไตรมาส กลั่น lessons ทั้งกอง → **`references/roots-playbook.md`**
- Playbook = "pattern ของการชนะ/แพ้" → ป้อนกลับเป็นเกณฑ์ให้ Loop 2 ใช้วินิจฉัย (ปิด flywheel)

---

## 5) สิ่งที่เพิ่มในตัว plugin

| ประเภท | ชื่อ | หน้าที่ | Loop |
|---|---|---|---|
| skill | `deal-strategy` | เครื่องวินิจฉัย + สั่ง play | 2 |
| skill | `roots-lessons-learned` (ขยาย) | จับ Won/Lost ทุกดีล → lesson | 1 |
| skill | `playbook-synthesis` | สร้าง wisdom (Playbook) | 3 |
| agent | `strategy-orchestrator` | รัน scheduled poll, route ดีลที่ flag | — |
| reference | `sales-methodology.md` | MEDDICC, champion, compelling event, post-quote discipline | — |
| reference | `reason-taxonomy.md` | Lost/Won taxonomy (source of truth ฝั่ง plugin) | — |
| reference | `roots-playbook.md` | living doc — output ของ Loop 3 | 3 |

---

## 6) How it runs — hook pattern (flag → poll → write-back)

Claude ไม่ใช่ server → ใช้ pattern **"event-driven ใน Odoo, pull-process โดย Claude":**

```
1. Odoo Automation Rule (no-code) ตั้ง flag
   - stage → Quoting/Proposing  → x_needs_strategy = true
   - Won / Lost                 → x_needs_lesson  = true
2. Claude scheduled job (odoorpc-cli)
   - อ่านดีลที่ flag = true
   - strategy → deal-strategy → message_post กลับ chatter
   - won/lost → lesson + capture reason → เก็บ knowledge
   - เขียน flag = false (เคลียร์ กันประมวลผลซ้ำ)
```

| | ตอนนี้ | Phase 4 |
|---|---|---|
| **กลไก** | flag → Claude poll → write-back | realtime push (webhook) |
| **ทำงานบน** | Claude Code CLI + scheduled job ✅ | Cowork-native ✅ |
| **ต้องมี** | Automation Rule + 2 custom field | **Odoo MCP server** |

> รายละเอียด field / Automation Rule / migration ทั้งหมด → [`odoo-spec-reason-taxonomy.md`](odoo-spec-reason-taxonomy.md)

---

## 7) Org change — 80% ของงานจริง (ส่วนที่ยากสุด)

Tech คือ 20% ที่ง่าย ที่เหลือคือเปลี่ยนพฤติกรรม:

| เปลี่ยน | จาก → เป็น | เจ้าของ |
|---|---|---|
| **Data discipline** | เลือก "No response" มักง่าย → บังคับ log เหตุจริง (required field) | Sales Manager |
| **Ritual ใหม่** | ไม่มี → weekly *deal strategy review* ใช้ AI diagnosis เป็น pre-read | Head of Sales |
| **ภาษากลาง** | ต่างคนต่างพูด → ทีมเข้าใจ compelling event / champion / economic buyer ตรงกัน | ทั้งทีม (ผ่าน KT) |
| **Post-quote SLA** | quote แล้วปล่อย → ทุก quote ต้องมี next step + mutual action plan ก่อนส่ง | AE |
| **Stage redesign** | "Follow-up 1/3/6M" (สุสาน ฿92M) → stage ที่บังคับมี next action | Sales Ops |
| **Playbook ownership** | — → มีคน curate wisdom (AI ≠ ความจริงอัตโนมัติ) | Head of Sales |

> **ประเด็นสำคัญ:** ถ้าทีมไม่มีภาษากลาง → diagnosis ของ AI จะกลายเป็น noise → นี่คือเหตุผลว่าทำไม **KT ต้องมาคู่กับ v4.0**

---

## 8) Knowledge Transfer + Learning Materials

KT มี 2 track — จุดขายคือ **สอน fundamental ด้วยข้อมูลจริงของ Roots เอง** (ไม่ใช่ทฤษฎี):

- **Track A — Fundamentals ("why"):** สอน methodology (MEDDICC, champion, compelling event, post-quote discipline) ผ่าน case จริง เช่น *"ทำไมเราเสีย STMS ฿2M"*, *"฿609M หายไปไหน"*
- **Track B — The tool ("how"):** อ่าน AI diagnosis ยังไง, log เหตุยังไง, ritual ใหม่ทำยังไง

| # | ชิ้นงาน | รูปแบบ | ใช้ทำอะไร |
|---|---|---|---|
| 1 | **Roots Deal Strategy Playbook** | Interactive HTML (Claude Design) | สอน fundamental ผ่าน case จริง |
| 2 | **Field guide / cheat sheet** | 1-page การ์ด (พิมพ์ได้) | MEDDICC checklist + reason taxonomy ติดโต๊ะ |
| 3 | **"Anatomy of a lost deal"** | ชุด case study | ผ่า ฿609M / STMS ให้เห็นบทเรียน |
| 4 | **Manager's enablement kit** | เด็ค + สคริปต์ | สอนหัวหน้ารัน weekly strategy review |
| 5 | **Onboarding micro-course** | ชุดโมดูลสั้น interactive | พนักงานใหม่เข้าใจใน 1 ชม. |
| 6 | **Reason taxonomy poster / Odoo help text** | โปสเตอร์ + help text ในฟิลด์ | log เหตุถูกตั้งแต่หน้างาน |

ทุกชิ้นสร้าง on-brand ผ่าน `deck-builder` + `references/brand-ci.md`

---

## 9) Market tools ที่ใช้ facilitate v4

| Job-to-be-done | แนะนำ | เหตุผล |
|---|---|---|
| Knowledge base (lessons + Playbook) | **Obsidian** (เชื่อม MCP อยู่แล้ว) / Notion | เก็บ lesson แบบ linkable, Claude เขียน/อ่านได้ตรง |
| สร้าง learning deck | **Claude Design → deck-builder** (มีแล้ว) | on-brand อัตโนมัติ, export Google Slides |
| ส่ง course / async | Google Classroom / Loom | ทีมเรียนเองได้ |
| วัดความเข้าใจ | Google Forms quiz | เช็ค adoption ก่อน go-live |
| Host HTML materials | Netlify / internal wiki | แชร์ลิงก์เดียว |
| หน้างาน log เหตุ | **Odoo field help text + Automation Rules** | discipline ตั้งแต่ต้นทาง |

---

## 10) Rollout — เป็น phase (ลด risk ของ Big Change)

```
Phase 0  Data spine + KT Track A (fundamentals)     ← ทำ Odoo + สอนภาษากลางก่อน
Phase 1  Loop 1 Learn  (capture Won/Lost)           ← เริ่มสะสม knowledge
Phase 2  Loop 2 Diagnose (deal-strategy skill)      ← เริ่มให้ค่า diagnosis
Phase 3  Loop 3 Synthesise (Playbook) + hooks       ← flywheel ครบ
Phase 4  Realtime (Odoo MCP + webhook)              ← Cowork-native
```

KT แทรกทุก phase: Phase 0 = fundamentals · Phase 2 = อ่าน diagnosis · Phase 3 = manager ritual

---

## 11) Open decisions (ต้องเคาะก่อน implement)

1. **Lost Reason 2-tier ใน Odoo CE** — ใช้ flat catalog ตั้งชื่อแบบ `Category: Reason` หรือเพิ่มฟิลด์ `x_lost_category` แยก (ดู spec)
2. **Poll cadence** — รันทุกกี่นาที/ชม. (แนะนำเริ่มที่ทุก 1–2 ชม. ในเวลาทำงาน)
3. **ใครเป็นเจ้าของ Playbook** — Head of Sales curate หรือ committee
4. **Stage redesign** — retire "Follow-up 1/3/6M" ทันที หรือ freeze ไม่ให้ดีลใหม่เข้า

---

## Appendix — grounding data (ทำไม strategy layer ถึงคุ้ม)

จากการวิเคราะห์ Odoo จริง (`crm.lead` lost reasons):
- **฿609M lost** — ~80% ของมูลค่า = ไม่มี compelling event/champion (48%) + แพ้คู่แข่ง (32%)
- **96%** ของมูลค่าดีล "No response" (฿205M) ตาย **หลัง** ออก quote → post-quote collapse ไม่ใช่ ICP ผิด
- **฿92M** ค้างใน stage "Follow-up 1/3/6 month" = สุสานดีล
- **June 2026 close:** ฿2.876M = 47% ของเป้า ฿6.1M — STMS ฿2M เลื่อนไป July (post-quote discipline หาย)

> ทั้งหมดนี้เป็น **strategy failure ไม่ใช่ tool failure** — v4.0 ออกแบบมาแก้ตรงนี้
