---
name: roots-bid-prep
description: "Prepare the document package for a Thai government procurement bid (e-GP). Trigger when the user has decided to bid on a TOR and asks to prepare bid documents, qualification matrix, or bid checklist. Phrases: 'เตรียมเอกสารประมูล', 'bid prep', 'ทำเอกสารยื่นซอง', 'เตรียมยื่นประมูล', or after roots-tor-analyzer returns a Go decision."
version: 1.0.0
source: roots-custom
phase: 2
---

# Bid Preparation — Thai Government Procurement (e-GP)

> **Custom Skill** — Built by Roots.Tech
> **For:** e-GP (gprocurement.go.th) bid submissions
> **Runs after:** roots-tor-analyzer returns a "Go" decision

## Trigger

Use when:
- User decided to bid and asks to prepare documents
- User says "เตรียมเอกสารประมูล", "bid prep", "ทำเอกสารยื่นซอง", "เตรียมยื่นประมูล"
- roots-tor-analyzer just returned a Go decision and user wants next steps

## Purpose

แปลง TOR requirements เป็น checklist เอกสารที่ต้องเตรียม + map qualification ของ Roots กับเงื่อนไข TOR — เพื่อให้ทีมยื่นซองได้ครบ ไม่ถูกตัดสิทธิ์เพราะเอกสารขาด

---

## Process

### Step 1 — Extract Bid Requirements

จาก TOR (หรือผลของ roots-tor-analyzer) ดึงข้อมูล:

**ข้อมูลการยื่น**
- เลขที่โครงการ e-GP
- วัน/เวลา ยื่นซอง
- วัน/เวลา เปิดซอง
- วิธีการจัดซื้อ (e-bidding / คัดเลือก / เฉพาะเจาะจง)
- ราคากลาง (ถ้าระบุ)

**เงื่อนไขผู้ยื่น (Qualifications)**
- ทุนจดทะเบียนขั้นต่ำ
- ประสบการณ์ผลงาน (จำนวนปี / มูลค่าโครงการ / ประเภทงาน)
- หนังสือรับรองผลงาน
- บุคลากรขั้นต่ำ (วุฒิ / จำนวน / ประสบการณ์)
- หลักประกันซอง (Bid Bond) — มูลค่า + รูปแบบ

### Step 2 — Qualification Matrix

สร้างตารางเทียบ TOR requirement กับ Roots:

```
## Qualification Matrix — [โครงการ]

| # | เงื่อนไข TOR | Roots มี? | หลักฐาน | สถานะ |
|---|---|---|---|---|
| 1 | ทุนจดทะเบียน ≥ X | ✅/❌ | หนังสือรับรองบริษัท | พร้อม/ขาด |
| 2 | ผลงาน ERP ≥ 3 โครงการ | ✅/❌ | หนังสือรับรองผลงาน | พร้อม/ขาด |
| 3 | บุคลากร PMP ≥ 1 คน | ✅/❌ | certificate + CV | พร้อม/ขาด |
```

**Flag ทันที** ถ้า Roots ไม่ผ่าน qualification ข้อใด → อาจถูกตัดสิทธิ์ ต้องแจ้ง Director

### Step 3 — Document Checklist

แยกเป็น 2 ซอง (ตามแบบ e-bidding มาตรฐาน):

**ซองที่ 1 — ข้อเสนอด้านคุณสมบัติและเทคนิค**
- [ ] หนังสือรับรองการจดทะเบียนนิติบุคคล (ไม่เกิน 6 เดือน)
- [ ] สำเนา ภ.พ.20
- [ ] งบการเงินย้อนหลัง [N] ปี
- [ ] หนังสือรับรองผลงาน + สำเนาสัญญา
- [ ] บัญชีรายชื่อบุคลากร + วุฒิ + CV
- [ ] หลักประกันซอง (Bid Bond)
- [ ] หนังสือมอบอำนาจ (ถ้ามี)
- [ ] เอกสารเทคนิค: solution architecture, implementation plan, timeline
- [ ] บัญชีเอกสารในซอง

**ซองที่ 2 — ข้อเสนอด้านราคา**
- [ ] ใบเสนอราคา (ตามแบบ TOR)
- [ ] รายละเอียดการคิดราคา (BOQ)
- [ ] บัญชีเอกสารในซอง

### Step 4 — Technical Proposal Outline

แนะนำให้เรียก se-orchestrator Mode E เพื่อเขียน technical section
จากนั้นให้ proposal-reviewer ตรวจก่อนยื่น

Technical proposal ควรมี:
1. ความเข้าใจโครงการและขอบเขตงาน
2. Solution architecture (Odoo modules + edition)
3. แผนการดำเนินงาน (Waterfall phases + Gantt)
4. ทีมงานและบทบาท
5. การถ่ายทอดความรู้และการอบรม
6. การรับประกันและบำรุงรักษา
7. ผลงานอ้างอิง

### Step 5 — Risk & Timeline Check

```
## Bid Submission Plan

**Deadline ยื่นซอง:** [date/time]
**เวลาที่เหลือ:** [N] วันทำการ

| งาน | ผู้รับผิดชอบ | กำหนดเสร็จ |
|---|---|---|
| ขอ Bid Bond จากธนาคาร | Finance | [date] |
| รวบรวมหนังสือรับรองผลงาน | AE | [date] |
| เขียน technical proposal | SE | [date] |
| ตรวจเอกสารครบ | Director | [date] |
| ยื่นซอง e-GP | [name] | [date] |

⚠️ Critical path: [งานที่ใช้เวลานานสุด — มักเป็น Bid Bond]
```

---

## Output Format

```
## Bid Preparation Package — [โครงการ]
**เลขที่ e-GP:** [number]
**Deadline:** [date/time] — เหลือ [N] วันทำการ

### Qualification Status
✅ ผ่าน [N] ข้อ | ❌ ไม่ผ่าน/ต้องตรวจสอบ [N] ข้อ
[ถ้ามีข้อไม่ผ่าน — ระบุชัดและแจ้งว่าเสี่ยงถูกตัดสิทธิ์]

### Document Checklist
ซองที่ 1: [N] รายการ — พร้อม [N] | ขาด [N]
ซองที่ 2: [N] รายการ — พร้อม [N] | ขาด [N]

### เอกสารที่ต้องเร่งจัดทำ
1. [item] — [ผู้รับผิดชอบ] — [deadline]

### Next Steps
1. [action]

### ความเสี่ยง
[risks ที่ต้องระวัง — Bid Bond timing, เอกสารขาด, qualification gap]
```

---

## Roots-Specific Notes

- **Bid Bond** มักใช้เวลา 3–5 วันทำการจากธนาคาร — เป็น critical path เสมอ
- หนังสือรับรองผลงาน — ขอจากลูกค้าเก่าล่วงหน้า อาจช้า
- งบการเงิน — ต้องเป็นฉบับที่ผู้สอบบัญชีรับรองแล้ว
- เอกสารทุกฉบับที่เป็นสำเนา ต้องลงนามรับรองสำเนาถูกต้อง
- ตรวจสอบว่าหนังสือรับรองบริษัท "ไม่เกิน 6 เดือน" เสมอ
- ถ้า qualification ไม่ผ่าน — อย่าฝืนยื่น เสียเวลาและ Bid Bond ฟรี แจ้ง Director ตัดสินใจ
- งานนี้ต้องผ่าน Director review ก่อนยื่นเสมอ — เป็นข้อบังคับ
