# Won / Lost Reason Cheat-Sheet — Canonical Reference

> **1-page** สำหรับ AE/Sales — เลือกเหตุ Won/Lost ให้ถูก แล้วมันจะกลายเป็น strategy ได้
> Won ↔ Lost จับคู่ **แกนเดียวกัน** → เทียบได้ว่า *"อะไรทำให้ชนะ vs อะไรทำให้แพ้"*
> as-built 2026-07-07 · pairs with [[odoo-spec-reason-taxonomy]] · [[customer-scorecard]]

---

## กฎทองข้อเดียว

> **เลือกเหตุที่ตอบได้ว่า "คราวหน้าทำอะไรต่าง"** — "เงียบหาย" ไม่ใช่เหตุ, "เงียบเพราะไม่มี champion" คือเหตุ
> ❌ ห้ามใช้เหตุคลุมเครือ (No response / Plan changed ถูก archive แล้ว) — บังคับใส่ root cause จริง

---

## ตารางจับคู่ Won ↔ Lost (แกนเดียวกัน)

| แกน | 🏆 Won (`x_won_reason`) | 💔 Lost (`crm.lost.reason`) | สัญญาณกลยุทธ์ |
|---|---|---|---|
| **Champion** | Champion-driven | Champion: Went dark / lost champion · No economic-buyer access | multi-thread, ยึด champion + EB |
| **Compelling event** | Compelling event / deadline | Qualify: No compelling event / timing | qualify trigger ตั้งแต่ต้น |
| **Fit / Capability** | Superior fit / Thai localization | Fit: Odoo capability gap · Customer not ready | qualify fit + readiness |
| **Competition** | Displaced competitor | Compete: other ERP (SAP/Oracle) · cheaper Odoo · status quo | shape decision criteria ก่อน RFP |
| **Value / Price** | Best price / TCO | Value: Price vs perceived value | ROI/value selling ไม่ลดราคาลูกเดียว |
| **Relationship** | Relationship / referral | *(ใกล้ Champion: went dark)* | nurture advocate → referral |
| **Delivery / Speed** | Fast / low-risk delivery | Process: Roots slow / dropped · Quote error | speed-to-lead SLA · post-quote discipline |
| **Qualification** | *(ชนะ = qualify ผ่าน)* | Qualify: No budget · Not ICP / disqualified | qualify budget/ICP เร็ว |

---

## ทำไมต้อง symmetric

พอ log ทั้ง 2 ฝั่งบนแกนเดียวกัน → คำนวณได้ว่า **แกนไหน correlate กับชนะ vs แพ้**
- ถ้า "Champion-driven" = เหตุชนะอันดับ 1 และ "Went dark" = เหตุแพ้อันดับ 1 → **champion คือ leverage สูงสุด** → ทุ่มสอน multi-threading
- นี่คือวัตถุดิบของ Playbook (v4 Loop 3 synthesise) และ deal-strategy MEDDICC weighting

---

## วิธี log (culture)

1. **Lost:** เลือก 1 ใน 14 เหตุ v2 (จัดกลุ่ม Qualify/Champion/Compete/Value/Fit/Process) + note สั้น
2. **Won:** เลือก `x_won_reason` (บังคับเมื่อ stage = Won) + note ว่า *อะไรคือ tipping point*
3. ถ้าไม่รู้เหตุจริง → "Unknown - needs review" (ต้อง rare + flag ให้ manager)

---

## Odoo fields
- `lost_reason_id` → 14 เหตุ v2 (id 11–24) · เหตุเก่า archived (ประวัติยังอยู่)
- `x_won_reason` → 7 ค่า (สร้างผ่าน UI — ดู [[odoo-spec-reason-taxonomy]])

## Related
- [[odoo-spec-reason-taxonomy]] · [[customer-scorecard]] · [[strategy-doctrine]]
