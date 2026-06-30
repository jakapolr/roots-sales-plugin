---
name: deck-builder
description: "Build an on-brand presentation/asset for Roots or BEECY by invoking Claude's design tools. Pick a mode — Interactive HTML (rendered inline) or pptx (openable in Google Slides) — and the skill applies the correct brand identity automatically. Trigger when the user says 'ทำ presentation', 'สร้าง deck', 'ทำสไลด์', 'make a deck', 'pitch deck', 'นำเสนอ', 'ทำ slide ลูกค้า', 'สร้าง one-pager', or wants to turn a proposal/dashboard/analysis into slides. Asks brand + mode + content if not given."
version: 1.0.0
source: roots-custom
---

# Deck Builder — On-Brand Presentation Generator

สร้าง presentation/asset ที่ตรง brand ของ Roots หรือ BEECY โดยเรียกเครื่องมือ design ของ Claude เลือกได้ 2 โหมด: **Interactive HTML** หรือ **pptx (เปิดใน Google Slides)**

## Source of truth
- **Brand (สี/ฟอนต์/logo/กฎ):** [references/brand-ci.md](../../references/brand-ci.md) — ใช้ค่าจากไฟล์นี้เท่านั้น ห้ามเดา
- **Company context:** CONTEXT.md (auto-loaded)

## ขั้นตอน

### 1. ถาม 3 อย่าง (ถ้า user ยังไม่ระบุ)
| ถาม | ตัวเลือก |
|---|---|
| **แบรนด์** | Roots (corporate/B2B/gov) หรือ BEECY (SME SaaS) |
| **โหมด** | Interactive HTML (ดูสด, interactive) หรือ pptx (แก้ต่อใน Google Slides) |
| **เนื้อหา** | จาก sales artifact ที่มีอยู่ หรือ user ป้อน outline |

### 2. ดึงเนื้อหา (content sources)
- **Sales artifacts ใน plugin:** ผลจาก `odoo-gap-analysis`, `roots-sales-dashboard`, `roots-manday-estimator`, proposal, MOM — ถ้า user อ้างถึง ให้ดึงมาเป็นโครง deck
- **User outline/brief:** รับ outline หรือหัวข้อจาก user ตรง ๆ
- ถ้าเนื้อหายังไม่พอ → ถาม audience + goal + key message ก่อน (เหมือน create-an-asset)

### 3. โหลด brand template
อ่าน references/brand-ci.md → ดึง palette + ฟอนต์ของแบรนด์ที่เลือก:
- **Roots:** primary `#2B3990`, accent `#FCC210`, teal `#0097A7`/`#4BB4C8`; fonts Prompt + Open Sans + Sarabun
- **BEECY:** primary `#FCC210`, honey/tan `#C2B59B`, ink `#414042`; web font Prompt
- **ห้ามใช้สี/ฟอนต์ของอีกแบรนด์ปนกัน**

### 4. Logo — กฎ contrast เข้มงวด (ห้ามให้ logo จมพื้น)

> **กฎเหล็กจาก brand guideline:** logo **ขาว** บนพื้น **เข้ม** · logo **เข้ม/สี** บนพื้น **อ่อน** · **ห้าม logo กลืนพื้นหลังเด็ดขาด**

**ก่อนวาง logo ทุกครั้ง — ตรวจ contrast:**
1. ดูสีพื้นที่จะวาง → เข้มหรืออ่อน
2. เลือก variant ให้ตรงข้าม: พื้นเข้ม (เช่น Roots navy `#2B3990`, BEECY ink `#414042`) → **logo เวอร์ชันขาว** · พื้นอ่อน/cream → **logo เวอร์ชันสี/เข้ม**
3. ถ้า **ไม่รู้ว่าไฟล์ไหนคือเวอร์ชันขาว** หรือดึง raster ไม่ได้ → อย่าเดา ให้ใช้ทางใดทางหนึ่ง:
   - ทำ **typographic wordmark** ในสีที่ contrast ชัด (เช่น "ROOTS" ขาวล้วนบน navy) — นับเป็น compliant
   - หรือวาง logo บน **plate สีขาว/อ่อน** เล็ก ๆ เพื่อรับประกัน contrast
4. ใส่ **clear space** รอบ logo (BEECY = เท่าความสูงตัว B) · ห้าม shadow/gradient/effect บน logo
5. ห้ามใช้สีตัวอักษร low-contrast กับพื้น (เช่น ฟ้าอ่อนบน navy — จม)

**การดึง raster logo (เมื่อรู้ variant):**
- Drive MCP `download_file_content` → ได้ base64 · HTML: `<img src="data:image/png;base64,...">` · pptx: เซฟ temp แล้ว insert ด้วย PowerPoint MCP
- Logo IDs/variants อยู่ใน [references/brand-ci.md](../../references/brand-ci.md)
- ดึงไม่ได้ → ทำต่อด้วย wordmark/เว้นช่อง + แจ้ง user (อย่าหยุดงาน)

> **Preview ใน chat (show_widget):** การ embed raster base64 inline กิน token มาก (~25K/ครั้ง) — สำหรับ preview ให้ใช้ typographic wordmark; ฝัง raster จริงเฉพาะตอน **export เป็นไฟล์** (.html/.pptx) ที่จ่าย cost ครั้งเดียว

### 5. Render ตามโหมด

**โหมด A — Interactive HTML**
- ใช้ `visualize` / show_widget
- ใส่ CSS variables ของแบรนด์ (ดู brand-ci.md), ฟอนต์ผ่าน Google Fonts (Prompt ฯลฯ)
- 1 ข้อความหลักต่อสไลด์ · visual > text · ใช้สี accent เน้นจุดสำคัญ
- เหมาะกับ: ส่ง link ดูสด, embed, demo

**โหมด B — pptx (Google Slides)**
- ใช้ PowerPoint MCP (`mcp__PowerPoint__By_Anthropic___*`): create_presentation → add_slide → ใส่ title/content/สี/logo
- ใช้สี hex ของแบรนด์กับ title bar / accent
- เสร็จแล้ว: เซฟ .pptx → (ถ้า user ต้องการ) อัปขึ้น Google Drive → เปิดด้วย Google Slides
- **ไม่มี native Google Slides MCP** — เส้นทางคือ .pptx → เปิดใน Slides (แก้ต่อได้)

### 6. โครงสไลด์มาตรฐาน (ปรับตามเนื้อหา)
1. Cover — title + แบรนด์ logo + tagline (Roots: "Passion to Innovates" / BEECY: "stop busy start beecy")
2. ปัญหา/บริบทลูกค้า
3. โซลูชัน (Odoo/BEECY ตาม fit — อ้าง references/odoo-editions.md ให้ถูก edition)
4. ขอบเขต/โมดูล + timeline
5. ราคา/manday (จาก roots-manday-estimator ถ้ามี)
6. ทำไมต้อง Roots (differentiators จาก CONTEXT.md)
7. Next steps + ช่องทางติดต่อ

## กฎสำคัญ
- แบรนด์เดียวต่อ 1 deck — Roots หรือ BEECY ไม่ปน
- สี/ฟอนต์จาก brand-ci.md เท่านั้น
- **Logo ต้อง contrast กับพื้นเสมอ — ห้ามจมพื้น** (ดูข้อ 4) ตรวจทุกครั้งก่อนวาง
- เลือก edition/ผลิตภัณฑ์ให้ถูกตาม [references/odoo-editions.md](../../references/odoo-editions.md) (อย่าสับ BEECY SaaS กับ Community implementation)
- ถ้า logo ดึงไม่ได้ → ทำต่อ เว้นช่องไว้ ไม่หยุดงาน

## เชื่อมต่อ skill อื่น
- เนื้อหา GAP → `odoo-gap-analysis`
- ตัวเลข pipeline/ยอด → `roots-sales-dashboard`
- ราคา/manday → `roots-manday-estimator`
- asset แบบ text-first (one-pager, battlecard) → `create-an-asset`
