# Brand CI — Roots & BEECY (Canonical Reference)

> **Single source of truth** สำหรับ visual identity ของ Roots และ BEECY
> ทุก skill/agent ที่สร้าง asset (deck, one-pager, HTML, pptx) ต้องอ้างไฟล์นี้ — ห้ามเดาสี/ฟอนต์เอง
> **Roots กับ BEECY เป็นคนละแบรนด์** — อย่าใช้ปนกัน เลือกตามว่าสื่อสารในนามไหน
> Sources: Roots CI deck + BEECY CI Guide Book (Nov 2024) + applied presentations · verified มิ.ย. 2026

---

## เลือกแบรนด์ไหน

| สถานการณ์ | ใช้แบรนด์ |
|---|---|
| Proposal/deck งาน implement, corporate, government, B2B enterprise | **Roots** |
| สื่อสารผลิตภัณฑ์ BEECY SaaS (SME, trading/retail/service) | **BEECY** |
| เอกสารบริษัท Trinity Roots | **Roots** |

---

# 1 · ROOTS

**Trinity Roots Co., Ltd.** · roots.tech · marketing@roots.tech
21Fl. Abdulrahim Place, 990 Rama IV Rd, Silom, Bang Rak, Bangkok 10500
**Tagline:** "Passion to Innovates"
**บุคลิก:** corporate, น่าเชื่อถือ, มืออาชีพ, นวัตกรรม

## สี (hex) — ใช้ตามนี้เท่านั้น

| บทบาท | ชื่อ | Hex | ใช้ตอนไหน |
|---|---|---|---|
| **Primary** | Dark Blue 1 | `#2B3990` | สีหลัก — header, แถบ, จุดเน้น |
| Secondary blue | — | `#515DAA` · `#6F85C2` · `#0F92D1` | รอง, gradient blue |
| Accent teal | — | `#0097A7` · `#4BB4C8` | ไฮไลต์, ไอคอน |
| **Accent yellow** | Dark Yellow 1 | `#FFCB1F` · `#FCC210` · `#F1C431` | เน้น, CTA, จุดสำคัญ |
| Light yellow | — | `#FFEB95` · `#FFDF83` · `#FEF4C8` | พื้นอ่อน, highlight |
| Dark neutral | Dark Grey 3 | `#58595B` · `#414042` | ตัวอักษรเข้ม |
| Mid/Light grey | — | `#808285` · `#A7A9AC` · `#E2E3F0` | เส้น, พื้นรอง |
| Warm neutral | — | `#C2B59B` (tan) · `#FCF2E7` (cream) | พื้นอุ่น |
| Base | White | `#FFFFFF` | พื้นหลัก |

**สีตัวอักษร (ใช้ 5 สีนี้):** Black · Dark Grey 3 `#58595B` · White · Dark Blue 1 `#2B3990` · Dark Yellow 1 `#FFCB1F`

**CSS variables (พร้อมใช้):**
```css
--roots-primary:#2B3990; --roots-blue-2:#515DAA; --roots-blue-3:#0F92D1;
--roots-teal:#0097A7; --roots-teal-2:#4BB4C8;
--roots-yellow:#FCC210; --roots-yellow-dark:#FFCB1F; --roots-yellow-light:#FFEB95;
--roots-ink:#414042; --roots-grey:#808285; --roots-cream:#FCF2E7; --roots-bg:#FFFFFF;
```

## ฟอนต์

| ใช้กับ | ฟอนต์ | หมายเหตุ |
|---|---|---|
| English | **Open Sans** | Google Font |
| Thai | **Prompt** | Google Font (heading/display) |
| English & Thai รวม | **Sarabun** | Google Font (body, doc) |

**Web/HTML stack:** `font-family:'Prompt','Open Sans','Sarabun',sans-serif;`
**Google Fonts import:** `Prompt:wght@300;400;500;600;700` + `Open Sans:wght@400;600;700` + `Sarabun:wght@400;500;600`

## ขนาดฟอนต์

| บริบท | H1 | H2 | Normal | Header/Footer |
|---|---|---|---|---|
| Subject (cover) | 60 | 22 | — | — |
| Presentation | 27–36 | 18–20 | 8–18 | — |
| Documentation | 18 | — | 12 | 8 |

## Logo (Drive: folder `1RsSIgHzfDSQ5CDTycE0_IfQGc68QJ1Hl`)
ใช้ได้ 4 สีเท่านั้น: **Original (สี) · White · Black · Grey**

> ⚠️ **ยังไม่ได้ label ว่าไฟล์ไหน = เวอร์ชันไหน** (read_file_content อ่าน PNG เป็นภาพไม่ได้) — จนกว่าจะ confirm:
> - พื้น**เข้ม** (navy/dark) → ต้องใช้เวอร์ชัน **White** · พื้น**อ่อน** → เวอร์ชัน **Original/สี**
> - ถ้าไม่แน่ใจไฟล์ → ใช้ **typographic wordmark** ("ROOTS" สี contrast ชัด) แทน อย่าเดาไฟล์แล้วเสี่ยง logo จมพื้น
> - วิธี label: download แต่ละไฟล์แล้วเปิดดู หรือให้ Roots ระบุว่าไฟล์ไหนคือ white/color/black/grey

| ไฟล์ | Drive file ID |
|---|---|
| LOGO roots-01.png … 05.png | `1XYmzCsOLUA5shwzW-WNgiwN__9vwrJcj` (01), `12LzFeaQTrMtVi2i4NEALWKskaiPrOPH7` (02), `1nciZ5rNHMsuqPrw0RzSiZkVYS1YKgw6b` (03), `15mVULT8UkkqFSzLEwYaMzVCgpKNYOkJD` (04), `18PWr5rpRRcVqPJoH0_Tyb6bDlElq-IlZ` (05) |
| Roots LG-S-01.png / 02.png | `1GibXDAt2_CGPWvWxAjZ1gK6lrmNEGnDu` / `11YFouIi71kWNBTbo1rEIG8l5KdscxugD` |

---

# 2 · BEECY

**Tagline:** "stop busy start beecy" (พิมพ์เล็กเสมอ)
**บุคลิก (Brand Character):** Friendly · Innovative · Dependable — อบอุ่น เข้าถึงง่าย พลังบวก
**Mascot:** "น้องน้ำผึ้ง" (Nong Nam Phueng) — ใช้สื่อสาร character ของแบรนด์ (มีหลาย pose/emotion)

## Logo
- ประกอบด้วย 3 ส่วน: **Symbol "B"** + **Wordmark "BEECY"** (พิมพ์ใหญ่) + **tagline** (พิมพ์เล็ก)
- 3 เวอร์ชัน: **Primary · Secondary · B Symbol** (symbol ใช้เดี่ยวได้)
- **Clear space** = ความสูงของตัว B · **ขนาดเล็กสุด** 1 cm (print) / 32 px (screen)
- **กฎสี:** logo **ขาว** บนพื้นเข้ม/สีสด · logo **เทาเข้ม** บนพื้นอ่อน

**❌ ห้าม:** logo กลืนพื้นหลัง/ภาพ · ใส่ shadow/gradient/effect · ใช้ B เป็นตัวอักษรในคำ · เปลี่ยนสีบางส่วนของ wordmark · บิด/ยืดผิดสัดส่วน

Drive (folder `1DqyBwr36TlZf3EXWl2_Rdz6Yz5n2M_Yc`):
| ไฟล์ | ID |
|---|---|
| AW_BEECY Logo_Primary.png (+ _Grey `10B167C3b0ECpJKy85mVrxQNB9iJiMU-5`, _Black `1a0TGmcG9lnBk4bc3YjoLD6_WXXfpNmTu`) | `10EYMXrQZXv5apZ3EAl6VFk3nYuPZdc43` |
| BEECY_B Symbol.png (+ _Grey, _Black, _White) | `1Pg09L0sdwvoWP7IH_IE6wQLhFjfp40nL` |
| CI Guide Book (PDF) | `1u06un0d17KwGR7jY_AKV-T3R2LNHamCX` |

## สี (hex)

| บทบาท | Hex | หมายเหตุ |
|---|---|---|
| **Primary yellow** | `#FCC210` | สีหลักของแบรนด์ (RGB 252,194,16) |
| Yellow variants | `#F1C60B` · `#F7D852` · `#F9EE53` · `#FFCB1F` | |
| Light yellow | `#FFDF83` · `#FFEB95` | |
| Warm neutral | `#C2B59B` (tan) · `#E2DBCF` · `#FCF2E7` (cream) | |
| Dark | `#414042` (ink) · `#5B4A42` · `#997C34` | |
| Base | `#FFFFFF` | |
| Icon accents | `#DB5CFF` (ม่วง) · `#19CCE4` (ฟ้า) · `#EFEFEF` | สำหรับ module icons |

**CSS variables:**
```css
--beecy-primary:#FCC210; --beecy-yellow-2:#F7D852; --beecy-yellow-light:#FFDF83;
--beecy-tan:#C2B59B; --beecy-cream:#FCF2E7; --beecy-ink:#414042; --beecy-bg:#FFFFFF;
--beecy-icon-purple:#DB5CFF; --beecy-icon-cyan:#19CCE4;
```

## ฟอนต์

| ใช้กับ | ฟอนต์ | หมายเหตุ |
|---|---|---|
| Display/Subject | **FC-Subject-Rounded** | ฟอนต์เฉพาะ — ไม่ใช่ Google Font |
| Thai/body | **Sukhumvit Set** | ไม่ใช่ Google Font |
| **Website / HTML** | **Prompt** | ← ใช้ตัวนี้สำหรับงาน web/HTML deck |

> ⚠️ FC-Subject-Rounded / Sukhumvit Set ไม่ใช่ฟอนต์ฟรีบนเว็บ — **งาน HTML/web ให้ใช้ Prompt** (ตาม guide ระบุ "Typography for Website: Prompt")

---

## สรุปความต่าง Roots vs BEECY (สำหรับ AI ตัดสินใจเร็ว)

| | Roots | BEECY |
|---|---|---|
| สีนำ | Navy `#2B3990` | Yellow `#FCC210` |
| โทน | corporate, มืออาชีพ, B2B | friendly, อบอุ่น, SME |
| Tagline | Passion to Innovates | stop busy start beecy |
| ฟอนต์ heading | Prompt | FC-Subject-Rounded (web: Prompt) |
| Mascot | ไม่มี | น้องน้ำผึ้ง |
| ใช้กับ | implement, gov, enterprise | BEECY SaaS, SME |

## กฎสำหรับ asset generation (deck-builder ต้องทำตาม)
1. ระบุก่อนว่าทำในนาม **Roots** หรือ **BEECY** → ใช้ palette/ฟอนต์/logo ของแบรนด์นั้น **ไม่ปนกัน**
2. ใช้ hex จากไฟล์นี้เท่านั้น — ห้ามเดาสี
3. งาน web/HTML: Roots = Prompt/Open Sans · BEECY = Prompt
4. ใส่ logo เวอร์ชันให้ถูกพื้น (เข้ม→logo ขาว, อ่อน→logo เข้ม)
5. BEECY: เคารพกฎ clear space + ห้าม effect บน logo
