---
name: roots-doc-freshness
description: "Check and update company/eligibility document freshness for a Thai government bid. Trigger when the user says 'ตรวจเอกสาร', 'document freshness', 'เอกสารบริษัทครบไหม', 'check company docs', or automatically after roots-tor-intake registers a new TOR to ensure required admin documents are valid before the submission deadline."
version: 1.0.0
source: roots-custom
phase: 3
---

# Document Freshness Check

> **Custom Skill** — Built by Roots.Tech
> **Reads/updates:** Company_Documents register (Google Drive → `8. Sales and Marketing/TOR Factory/registers/Company_Documents.md`)
> **Runs:** After G0 intake, before G2 matrix freeze, and on demand
> **Purpose:** Ensure no document is expired or missing at submission — a single expired
> document disqualifies the entire bid.

## Trigger

Use when:
- A new TOR is registered (roots-tor-intake completed)
- User says "ตรวจเอกสาร", "document freshness", "เอกสารบริษัทครบไหม", "check company docs"
- A TOR's mandatory-passfail requirements include company/eligibility documents

## Process

### Step 1 — Read Company_Documents register
From Google Drive (or user paste). Get all rows with their `issue_date`, `expiry_date`,
`review_freq`, and `latest_file`.

### Step 2 — Check TOR-specific requirements
If a `tor_id` is provided, cross-reference TOR_Requirements for rows with
`type = legal` or `type = mandatory-passfail` that reference company documents.
Note any documents the TOR requires that are NOT in the register → these are **missing**.

### Step 3 — Classify each document

Apply these rules (today = date of running the skill):

| Status | Condition |
|---|---|
| **valid** | Has `latest_file` AND (no expiry OR expiry > today + 30 days) |
| **expiring** | Expiry ≤ today + 30 days but > today |
| **expired** | Expiry ≤ today |
| **missing** | Document required by TOR but not in register, OR in register but no `latest_file` |

For หนังสือรับรองบริษัท specifically: must be ≤ 6 months old at submission deadline
(not today). If issue_date < submission_deadline − 6 months → classify as **expired**.

### Step 4 — Draft reminder actions
For each non-valid document:
- **expiring/expired:** Gmail draft to owner with "กรุณาต่ออายุ / ขอเอกสารใหม่ ภายใน [date]"
- **missing:** flag for Admin to obtain — list exactly which TOR requirement needs it
If `~~email` connected: draft the reminder. If not: output the message text.

### Step 5 — Copy valid files to TOR folder
For every `valid` document: note the Drive path for copying into
`TOR_[folder]/01_Admin_Documents/`. (The user or submission packager does the copy;
this skill outputs the list.)

### Step 6 — Update register statuses + write back
Update each row's `status` field. Write to Drive or output changed rows.

## Output Format

```
## Document Freshness Report — [tor_id or "Firm-wide"]
**Checked:** [date]  |  **TOR deadline:** [date or N/A]

| Document | Status | Expiry / Issue | Action |
|---|---|---|---|
| หนังสือรับรองบริษัท | ✅ valid | issued 2026-04-01 | copy to 01_Admin_Documents |
| งบการเงิน | ⚠️ expiring | expires 2026-06-15 | renew before [deadline] |
| หนังสือรับรองผลงาน (โครงการ A) | ❌ missing | — | request from client immediately |

### Summary
✅ valid [N] | ⚠️ expiring [N] | ❌ expired/missing [N]

### Actions required
1. [doc] — [owner] — [deadline] — [action]

### Bid eligibility
🟢 All required documents valid / 🟡 Expiring items — must renew before [date] / 🔴 Missing/expired — bid at risk
```

## Roots-Specific Notes
- หนังสือรับรองบริษัท: must be ≤ 6 months old at submission (not at time of check).
- สำเนาเอกสาร: must have "รับรองสำเนาถูกต้อง" signature — flag if the latest_file is unsigned.
- งบการเงิน: must be auditor-certified (ผู้สอบบัญชีรับรอง) — note in status.
- For a per-bid document (หนังสือมอบอำนาจ, Bid Bond): flag as missing for every new TOR that needs it.
- Cross-reference with roots-lc-check if the TOR requires financial capacity evidence.
