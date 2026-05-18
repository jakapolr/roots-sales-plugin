---
description: Search the meeting registry for past MOMs by client, date, type, or attendee
argument-hint: "<client name, date, or type:xxx>"
---

# /roots:meeting-search

ค้นหา meeting ที่ผ่านมาจาก registry และเข้าถึง MOM files ได้โดยตรง

## Usage

```
/roots:meeting-search [query]
```

## Query Examples

```bash
# ค้นหาตามชื่อลูกค้า
/roots:meeting-search Green Deli

# ค้นหาตามช่วงวันที่
/roots:meeting-search 2026-01

# ค้นหาตามประเภทการประชุม
/roots:meeting-search type:government-bid

# ค้นหาตามชื่อ Salesperson
/roots:meeting-search attendee:Fern

# ค้นหาหลายเงื่อนไข
/roots:meeting-search Green Deli type:proposal
```

## What Claude Will Do

1. Read `/Sales/meeting-registry.md` from Google Drive (if connected) or ask user to paste registry
2. Filter rows matching the query
3. Return a table of matching meetings with clickable Drive links
4. Offer to open any specific MOM for review

## Output Format

```
## ผลการค้นหา — "[query]"

พบ [N] การประชุมที่ตรงเงื่อนไข:

| ID | วันที่ | ลูกค้า | ประเภท | MOM |
|---|---|---|---|---|
| MTG-2026-001 | 2026-01-15 | Green Deli Foods | discovery | [เปิด MOM] |
| MTG-2026-005 | 2026-03-02 | Green Deli Foods | proposal | [เปิด MOM] |

ต้องการดู MOM ไหนครับ? พิมพ์ ID หรือคลิกลิงก์ด้านบน
```

## No Results

```
ไม่พบการประชุมที่ตรงกับ "[query]"

แนะนำ:
- ลองค้นหาด้วยชื่ออื่น (เช่น ภาษาไทย/อังกฤษ)
- ดู registry ทั้งหมด: /roots:meeting-search all
```
