# 🌾 Roadmap v5 — Farmer Strategy (Recurring → Sustain)

> **⚠️ FOR FURTHER DISCUSSION** — เอกสารนี้เก็บ thesis + design ที่ตกผลึกจากการ brainstorm (ก.ค. 2026)
> **ยังต้องลง detail strategy เพิ่มเติมอีกหลายจุด** (ดู §8 open questions) ก่อน implement จริง
> **Scope:** v5 = การ **"เลี้ยงฐาน"** (Farming) — ต่อจาก v4 ที่เป็น Hunting → [[strategy-doctrine]]
> Draft: 2026-07 · pairs with [[deal-service-matrix]] · [[customer-scorecard]]

---

## 1) Thesis — Hunter → Farmer (recurring 16% → 50%)

Wisdom จากรุ่นพี่วงการ ERP (ex-IBM, ปัจจุบัน Oracle):

> *"องค์กร Professional Services แบบนี้ ต้อง maintain MA/recurring ให้ได้ **50% ของ revenue ทุกปี** ถึงจะถือว่า Sustain — โดยเน้น Support Services ที่ทำ Performance Review + upsell/cross-sell ลูกค้าในมืออย่างต่อเนื่อง"*

**ข้อมูลจริง Roots 2025:**
| | มูลค่า | % |
|---|---|---|
| Implementation (one-off) | ฿41M | 71% |
| MA | ฿6.75M | 11.7% |
| Cloud | ฿2.27M | 4% |
| **Recurring (MA+Cloud)** | **฿9M** | **16%** |
| Benchmark ความยั่งยืน | — | **50%** |

→ Roots = **"หมาล่าเนื้อ"** — ทุกต้นปีเริ่มที่ ~84% ว่าง ต้องล่า ฿48M ใหม่แค่เพื่อยืนกับที่ → sales หมดแรงตลอด ไม่ compound

> **Reframe:** Roots ต้องทำกับตัวเองแบบที่ทำกับโชคยืนยง — reposition จาก *project shop (ล่าเนื้อ)* → *recurring partner (เลี้ยงสวน)*

---

## 2) Mandate — Farmer เป็นเจ้าของตัวเลขเดียว

ไม่ใช่ "ดูแลลูกค้า" (คลุมเครือ) แต่ = **เจ้าของ NRR (Net Revenue Retention)**
เป้าตรง: **MA attach 50% → 90%** · **recurring 16% → เพิ่มทุกไตรมาส**

---

## 3) 4 motion ของการเลี้ยงสวน (วน loop รายปี)

Farmer รับช่วงตอน go-live แล้ววน loop (ไม่ใช่ปิดแล้วจบ):

| motion | ทำอะไร | ตัวชี้วัด |
|---|---|---|
| **1 · Adopt** | go-live health, 90 วันแรก (adoption = leading indicator ของ retention) | time-to-value, usage |
| **2 · Review (QBR)** | โชว์ ROI ตามรอบ + หา need ใหม่ (= "Performance Review" ของรุ่นพี่) | QBR coverage |
| **3 · Expand** | **GAP-back-in** (optimization/phase-2 GAP) = upsell/cross-sell | expansion revenue |
| **4 · Renew** | MA renewal เชิงรุก (ไม่ scramble ตอนหมดอายุ) | attach/renewal rate |
| **+ Advocate** | A ที่ healthy → reference/referral กลับ Hunter (ปิด wish-list gap) | referrals sourced |

> **Insight สำคัญ:** GAP ไม่ใช่แค่คัดเมล็ดใหม่ (hunting) — เป็น **เครื่องมือรดน้ำลูกค้าเดิม** ด้วย (farming)

---

## 4) Coverage model — คน 1 คนเลี้ยงทั้งสวนด้วย plugin leverage

ไม่ใช่ทุก account ได้ human-touch เท่ากัน (tier ตาม `x_deal_tier`):

| tier | ใครดูแล | motion |
|---|---|---|
| 🎃 A | Farmer (คน) high-touch | QBR รายไตรมาส · expansion roadmap · exec sponsor |
| 🌱 B | Farmer + plugin | check-in ครึ่งปี · plugin เตือน health |
| ⚙️ C/D | **plugin ล้วน** (tech-touch) | renewal alert อัตโนมัติ · self-serve · GAP-back-in prompt |

→ **plugin ทำงานหนัก** = Farmer 1 คนคุมทั้งฐานได้ (เหตุผลที่ Farmer function ต้องมาคู่ plugin ไม่ใช่จ้างทีม CS)

---

## 5) Staffing — staged (อย่าจ้างทีมก่อนพิสูจน์)

| Phase | ทำอะไร | ต้นทุน |
|---|---|---|
| **1 (เริ่ม)** | ให้ "หมวก Farmer" กับ senior 1 คน (SE/PM lead) part-time โฟกัส **5 forgotten pumpkin ฿28M** | ~ศูนย์ |
| **2** | motion พิสูจน์ ROI → **จ้าง AM/CSM คนแรก** | 1 hire |
| **3** | scale — tiered coverage เต็ม + plugin automation + KPI scoreboard | ตาม growth |

---

## 6) KPI + comp — ต้องแยกจาก Hunter (สำคัญมาก)

| | Hunter | **Farmer** |
|---|---|---|
| วัด | new logo bookings, win rate | **NRR · GRR · attach rate · expansion revenue** |
| comp | ค่าคอมดีลใหม่ | ค่าคอม**การต่อ + ขยาย** |

**กับดัก:** อย่า comp Farmer ด้วย new logo (จะทิ้งสวนไปล่า) · อย่าให้ Hunter รับผิดชอบ renewal (จะทิ้ง renewal ไปล่า) → แยก incentive เด็ดขาด

---

## 7) Handoff-2 (ที่ขาดวันนี้)

```
Hunter (ปิด) → pm-handoff [agent มีแล้ว] → Delivery (implement)
                                              ↓ ตอน go-live
                                        Farmer รับช่วง  ← ถือ expansion roadmap จาก GAP
```
> Roots มี `pm-handoff` (sales→delivery) แล้ว · **ที่ขาด = handoff-2 (delivery→Farmer) ตอน go-live** = จุดที่วันนี้ลูกค้าหลุดมือ (50% unwatered)

---

## 8) Pilot — เริ่มที่ "forgotten giant pumpkin" ฿28M

ลูกค้าที่เรา WON implementation แต่ **ไม่มี MA/Cloud เลย** (unwatered) — flagship + health:

| ลูกค้า | sector | implement | เครื่องมือรดน้ำ |
|---|---|---|---|
| วังน้ำเย็น | dairy | ฿10.0M | GAP-back-in → MA/expansion |
| จุฬารัตน์ | hospital | ฿7.3M | GAP-back-in |
| ยันฮี | hospital | ฿5.7M | GAP-back-in |
| ไทยอินโนฟู้ด | food | ฿3.0M | GAP-back-in |
| มาม่า | food | ฿1.85M | GAP-back-in (ยังไม่เคยทำ GAP) |

> เป้า pilot: แปลง unwatered → MA/expansion ให้เห็นตัวเลขใน 1–2 ไตรมาส **ก่อนจ้าง** · หมายเหตุ: MA attach ปัจจุบัน = 50% · unwatered ≥฿1M รวม ฿76M (ตัด gov/failed แล้วเหลือ flagship ~฿28M)

---

## 9) Plugin v5 features ที่ต้องมี

- `x_health_score` + **unwatered-pumpkin flag** (won impl, ไม่มี MA ใน X วัน)
- **QBR prep skill** — ดึง usage/ROI สรุปให้ Farmer อัตโนมัติ
- **GAP-back-in trigger** — เตือนจังหวะขยาย
- **renewal tracker** — MA ใกล้หมด → alert
- **handoff-2 agent** (delivery → Farmer)

---

## 10) ⚠️ Open questions — FOR FURTHER DISCUSSION

ต้องลง detail strategy เพิ่มก่อน implement:
1. **เป้า recurring จริงของ Roots** — 50% คือ mature-state; ราชการ/bid เป็น one-off structurally → private base ต้องแบกสูงกว่า · staged 16%→30%→50% ใช้กรอบเวลาเท่าไหร่?
2. **Health cluster ใช้ soil เดิมซ้ำแค่ไหน** — hospital ต้อง custom เฉพาะ (HIS/pharmacy) หรือไม่ → กระทบว่า niche #2 คือ "พืชที่ 2 ในนาเดิม" หรือ "นาใหม่ต้องเตรียมดิน"
3. **Comp model ของ Farmer** — สูตร NRR-based ที่แฟร์กับทีมเล็ก
4. **ใครถือหมวก Farmer คนแรก** (Phase 1) — SE lead / PM lead / hire?
5. **MA pricing / packaging** — tiered support levels? SLA?
6. **นิยาม health score** — usage + tickets + engagement + days-since-contact ถ่วงยังไง
7. **การเชื่อมโยง advocate → wish-list** — reference program เป็นระบบ

---

## Related
- [[strategy-doctrine]] — v4 Hunting doctrine (ล่าก่อนเลี้ยง)
- [[deal-service-matrix]] — allocation (win-it) · after-win/water = ย้ายมา v5 นี้
- [[customer-scorecard]] — ICP + scorecard v2
