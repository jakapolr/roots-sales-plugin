---
name: roots-submission-packager
description: "Generate the submission folder checklist, verify signed/stamped/uploaded status for every required document, and lock the final bid package. Trigger when the user says 'เตรียมซอง', 'pack submission', 'ทำ submission folder', 'สรุปเอกสารยื่น', 'G5 lock', or when the QA review is complete and the bid is approaching the deadline."
version: 1.0.0
source: roots-custom
phase: 3
---

# Submission Packager — G5 Gate

> **Custom Skill** — Built by Roots.Tech
> **Maintains:** Submission_Checklist register (Google Drive → `8. Sales and Marketing/TOR/registers/Submission_Checklist.md`)
> **Gate:** G5 Submission Lock — the bid folder cannot be locked without this checklist complete
> **Purpose:** Convert the TOR_Requirements and document registers into a concrete,
> file-level submission checklist so nothing is missing, unsigned, or unstamped at the deadline.

## Trigger

Use when:
- QA review (G4) is complete and bid is approaching submission
- User says "เตรียมซอง", "pack submission", "ทำ submission folder", "G5 lock"
- User wants to verify the submission folder is complete

## Process

### Step 1 — Read TOR_Requirements
Filter for `type = mandatory-passfail` and `type = legal` rows for the `tor_id`.
These become the required files in the checklist. Also read any scored items that require
evidence attachment.

### Step 2 — Generate the file list by folder
Map each requirement to the standard submission folder tree:

| Folder | Typical contents |
|---|---|
| 00_TOR_and_Addendum | Original TOR PDF, any addenda |
| 01_Admin_Documents | หนังสือรับรองบริษัท, ภ.พ.20, บัญชีผู้ถือหุ้น, หนังสือมอบอำนาจ, Bid Bond |
| 02_Company_Profile | Company overview, Odoo partnership letter |
| 03_Technical_Proposal | Technical proposal document |
| 04_Solution_Spec | Solution architecture, module spec |
| 05_Project_Plan_and_Methodology | Gantt chart, WBS, delivery plan |
| 06_Team_CV | CVs for all required roles |
| 07_Experience_and_Evidence | Reference letters, case studies, certificates |
| 08_Financial_and_LC | งบการเงิน, bank guarantee / Bid Bond letter |
| 09_Commercial_Proposal | Price form, BOQ (ซองที่ 2 for e-Bidding) |
| 10_Presentation_Deck | Slides if presentation required |
| 11_QA_Checklist | Completed QA checklist |
| 12_Final_eGP_Upload | Files in e-GP format for upload |
| 13_Print_Pack | Hard copy set (if required) |

### Step 3 — Build Submission_Checklist rows
For each file: create a `SUB-NNN` row with `generated / signed / stamped / reviewed / uploaded / printed` all starting at ⬜. Write the initial checklist to the register.

### Step 4 — Verify current status
Ask user (or read from Drive if connected) which items are:
- Generated (file exists in Drive folder)
- Signed (authorized signature applied)
- Stamped (company seal / ตรายาง บริษัท applied)
- Reviewed (QA passed — ref Review_Log)
- Uploaded to e-GP
- In print pack (if hard copy required)

Update each column. Output the current state.

### Step 5 — G5 lock check
The bid can be locked (G5 pass) only when:
- Every `required_by_tor = yes` row has `reviewed = ✅`
- Zero open 🔴 items in Review_Log for this tor_id
- Submission channel requirements met (uploaded for e-GP, printed for hard copy)

If all conditions met: output **"G5 LOCKED ✅ — Ready to submit"**
Otherwise: output exactly what is blocking the lock.

## Output Format

```
## Submission Package — [tor_id]
**Deadline:** [date/time] — [N] hours remaining
**Channel:** [e-Bidding / เฉพาะเจาะจง / hard copy]

### Checklist
| Folder | File | Req'd | Gen | Signed | Stamped | QA | Uploaded | Print |
|---|---|---|---|---|---|---|---|---|
| 01_Admin | หนังสือรับรองบริษัท | yes | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ |

### Summary
✅ Complete: [N] | ⬜ Pending: [N] | ❌ Missing: [N]

### G5 Lock status
🔒 LOCKED ✅ — Ready to submit
OR
⛔ NOT READY — [list exactly what is blocking]
```

## Roots-Specific Notes
- สำเนาเอกสาร: every photocopy must be signed "รับรองสำเนาถูกต้อง" + ตรายาง — this is a separate checklist item from the original.
- ซองที่ 1 (technical) and ซองที่ 2 (commercial) must be physically separate sealed envelopes for e-Bidding hard copy — the packager should create separate print packs.
- e-GP upload: file names must match the TOR's specified naming convention. Flag any mismatch.
- After submission: create an archive snapshot in `99_Working/archive_[YYYYMMDD]/` — never delete the submitted set.
