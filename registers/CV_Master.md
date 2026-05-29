# Register — CV_Master

> **Location:** Google Drive → `8. Sales and Marketing/TOR/registers/CV_Master.md`
> **Maintained by:** `roots-cv-builder`
> **Purpose:** Role-based CV data for tender team scoring. Tracks each staff member's
> latest CV, certifications, relevant projects, and approval status so team CVs are never
> assembled from scratch the night before submission.

## How to Use

- Single firm-wide register.
- `roots-cv-builder` checks `last_updated` freshness, requests updates when stale,
  and converts staff input into the standardized tender CV format.
- `roots-scoring-matrix` references this for the "team experience" criterion.

---

## Registry

| cv_id | staff | role | last_updated | certifications | relevant_projects | lang | approval | file |
|---|---|---|---|---|---|---|---|---|
| CV-001 | (sample) Somsak | Solution Architect | 2026-03-01 | PMP, Odoo v18 | 3 ERP ภาครัฐ | TH/EN | approved | drive://... |
| CV-002 | (sample) Nita | Odoo Consultant | 2025-11-15 | Odoo Functional | 5 manufacturing | TH | stale | drive://... |

---

## Field Reference

| Field | Description | Example |
|---|---|---|
| `cv_id` | Sequential ID, `CV-NNN` | CV-001 |
| `staff` | Staff name | Somsak |
| `role` | Tender role | Solution Architect |
| `last_updated` | Date CV last refreshed `YYYY-MM-DD` | 2026-03-01 |
| `certifications` | Relevant certs | PMP, Odoo v18 |
| `relevant_projects` | Project count/types relevant to bids | 3 ERP ภาครัฐ |
| `lang` | CV language versions available | TH/EN |
| `approval` | approved / pending / stale (>90 days) | approved |
| `file` | Drive link to latest CV | drive://... |

---

## Freshness rule

A CV is **stale** if `last_updated` > 90 days. `roots-cv-builder` flags stale CVs when a
TOR requires that role and prompts the staff member to refresh before submission.

---

## Statistics

> Auto-updated by `roots-cv-builder` on each write.

- Staff CVs tracked: 2
- approved 1 / pending 0 / stale 1
- % updated within 90 days: 50%
- Last updated: 2026-05-29
