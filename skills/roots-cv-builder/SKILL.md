---
name: roots-cv-builder
description: "Check CV freshness, request staff updates, and generate standardized tender CVs for Thai government/corporate bids. Trigger when the user says 'เตรียม CV ทีม', 'CV สำหรับประมูล', 'CV builder', 'ขอ CV ทีมงาน', or when a TOR requires team CVs with specific role qualifications."
version: 1.0.0
source: roots-custom
phase: 3
---

# CV Builder — Team Profile for Tender Submission

> **Custom Skill** — Built by Roots.Tech
> **Reads/updates:** CV_Master register (Google Drive → `8. Sales and Marketing/TOR Factory/registers/CV_Master.md`)
> **Purpose:** Ensure team CVs are always fresh, role-matched, and formatted to Thai
> government/corporate tender standards — so team scoring is never weakened by a
> stale or generic CV.

## Trigger

Use when:
- A TOR requires team CVs (almost all government bids do)
- User says "เตรียม CV ทีม", "CV สำหรับประมูล", "CV builder", "ขอ CV ทีมงาน"
- roots-scoring-matrix flags "team experience" as a scored criterion needing CV evidence

## Process

### Step 1 — Read TOR team requirements
From TOR_Requirements (or ask user), extract:
- Required roles (e.g. Project Manager, Solution Architect, Odoo Consultant)
- Minimum qualifications per role (degree, certification, years of experience)
- Any specific requirements (PMP, government project experience, Odoo certification)
- Number of required staff

### Step 2 — Read CV_Master
Check each role against available staff CVs. Evaluate:
- **`approval = approved`** AND **`last_updated` within 90 days** → ready to use
- **`last_updated` > 90 days** → stale → must request update
- **Role not in register** → gap → must identify candidate and collect fresh CV

### Step 3 — Draft update requests
For each stale or missing CV: draft a message to the staff member (via Gmail if connected)
with a standardized update form asking for:
  - Recent projects (client, role, module, year, outcomes)
  - Current role + experience years
  - Certifications (name, issuer, date, number)
  - Relevant modules: manufacturing / inventory / accounting / HR / other
  - Availability for this project

### Step 4 — Generate tender CV
Convert staff input into the standardized tender CV format. The format is designed for
Thai government evaluation panels (formal Thai, no English mixing unless role is technical):

```
## ประวัติบุคลากร

**ชื่อ-สกุล:** [name]
**ตำแหน่งในโครงการ:** [role for this bid]
**ประสบการณ์รวม:** [N] ปี

### คุณวุฒิ
[degree, field, institution, year]

### ใบรับรอง (Certifications)
- [cert name] — [issuer] — [date]

### ผลงานที่เกี่ยวข้อง
| โครงการ | หน่วยงาน | บทบาท | ระยะเวลา | มูลค่า (THB) |
|---|---|---|---|---|
| [project] | [client] | [role] | [period] | [value] |

### ทักษะที่เกี่ยวข้องกับโครงการนี้
[2–3 sentences directly matching TOR requirements — not generic]
```

### Step 5 — Team matrix
Create a summary table for the proposal's team section:

```
## Team Matrix — [tor_id]

| บทบาท | ชื่อ | ประสบการณ์ | Certification | สถานะ CV |
|---|---|---|---|---|
| Solution Architect | [name] | [N] ปี | Odoo v18 | ✅ ready |
| PM | [name] | [N] ปี | PMP | ⚠️ stale — update requested |
```

### Step 6 — Update CV_Master register
Update `last_updated`, `approval`, and `file` for refreshed CVs. Write back.

## Output Format

```
## CV Builder Report — [tor_id]
**Roles required:** [N]  |  **Ready:** [N]  |  **Stale/missing:** [N]

[Team Matrix table]

### Actions required
1. [staff] — [stale/missing] — update by [date] — [Gmail draft link or output]

### TOR qualification check
✅ All roles meet minimum qualifications / ❌ Gap: [role] — [requirement not met]
```

## Roots-Specific Notes
- Always tailor the "ทักษะที่เกี่ยวข้อง" section to THIS TOR's requirements — generic CVs score poorly.
- Government bids: authorized signature on CV page is sometimes required — note in checklist.
- If a required certification (e.g. PMP, ISO Lead Auditor) is missing, flag immediately — it's often a qualification disqualifier.
- Odoo certification: บริษัทที่เป็น Official Odoo Partner has a listing advantage — mention this.
- For a government bid using e-Bidding, CVs go into ซองที่ 1 (technical envelope).
