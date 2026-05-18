# Meeting Registry — Roots.Tech Sales

> **File location:** Google Drive → `8. Sales and Marketing/Meetings/meeting-registry.md`
> **Maintained by:** MOM Writer agent (auto-updated after each MOM)
> **Purpose:** Central index of all processed meetings — enables deduplication, audit, and search

---

## How to Use This File

**Salesperson:** Use `/roots:meeting-search [client name]` or `/roots:meeting-search [date]` to find any past meeting.

**MOM Writer agent:** Read this file before processing any transcript. Match by `content_hash` to detect duplicates. Append new entry after creating MOM.

**Format:** Never edit entries manually. The agent maintains this file. Add notes in the `notes` column only.

---

## Registry

| id | date | client | meeting_type | attendees | mom_link | content_hash | processed_by | notes |
|---|---|---|---|---|---|---|---|---|
| MTG-2026-001 | 2026-01-15 | Green Deli Foods | discovery | ทีม Roots: Jack, Fern / ลูกค้า: คุณสมชาย CFO | [MOM_GreenDeli_20260115.md](https://drive.google.com/...) | a3f8c2d1 | mom-writer v1.0 | First contact meeting |
| MTG-2026-002 | 2026-02-03 | กรมพัฒนาที่ดิน | requirement | ทีม Roots: Pan, SE1 / ลูกค้า: อ.วิชัย IT | [MOM_LDD_20260203.md](https://drive.google.com/...) | b7e4a9f2 | mom-writer v1.0 | e-GP bid #64066 |

---

## Field Reference

| Field | Description | Example |
|---|---|---|
| `id` | Sequential ID, format MTG-YYYY-NNN | MTG-2026-001 |
| `date` | Meeting date YYYY-MM-DD | 2026-01-15 |
| `client` | Company name (Thai or English) | Green Deli Foods |
| `meeting_type` | discovery / requirement / proposal / review / follow-up / government-bid | discovery |
| `attendees` | Roots team: [names] / ลูกค้า: [names + roles] | ทีม Roots: Jack, Fern |
| `mom_link` | Google Drive direct link to MOM file | https://drive.google.com/... |
| `content_hash` | First 8 chars of SHA-256 hash of transcript — used for deduplication | a3f8c2d1 |
| `processed_by` | Agent version that created the MOM | mom-writer v1.0 |
| `notes` | Optional human notes | First contact |

---

## Statistics

> Auto-updated by agent on each append

- Total meetings logged: 2
- Clients covered: 2
- Date range: 2026-01-15 → 2026-02-03
- Last updated: 2026-02-03

---

## Search Examples

```
# Find all meetings with a client
/roots:meeting-search Green Deli

# Find by date range
/roots:meeting-search 2026-01 to 2026-03

# Find by meeting type
/roots:meeting-search type:government-bid

# Find by Roots team member
/roots:meeting-search attendee:Fern
```
