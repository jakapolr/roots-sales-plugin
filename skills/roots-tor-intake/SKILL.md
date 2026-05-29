---
name: roots-tor-intake
description: "Register a new TOR opportunity: create the TOR_Opportunities entry, Drive folder tree, and Google Calendar deadline gates. Trigger when the user says 'เพิ่ม TOR ใหม่', 'intake TOR', 'รับ TOR ใหม่', 'register this TOR', 'มี TOR มาใหม่', or when a PDF TOR is shared before analysis. Runs before roots-tor-analyzer — this is G0."
version: 1.0.0
source: roots-custom
phase: 3
---

# TOR Intake — G0 Gate

> **Custom Skill** — Built by Roots.Tech
> **Maintains:** TOR_Opportunities register (Google Drive → `8. Sales and Marketing/TOR/registers/TOR_Opportunities.md`)
> **Gate:** G0 — must run before any other TOR skill
> **Runs before:** roots-tor-analyzer

## Why this exists

Every TOR needs a `tor_id` the moment it arrives. Without it, requirements matrices,
scoring matrices, and checklists have nothing to link to. This skill creates the
opportunity record, the Drive folder tree, and the Calendar deadline sequence in one pass
— within 2 hours of the TOR landing (the blueprint KPI).

## Trigger

Use when:
- User shares a new TOR PDF or announces one has arrived
- User says "เพิ่ม TOR ใหม่", "intake TOR", "รับ TOR ใหม่", "register this TOR"
- Any other TOR skill is called but no `tor_id` exists yet

## Input

Extract from the TOR (or ask if unclear):
- Agency / buyer (หน่วยงาน)
- Project name (ชื่อโครงการ)
- Budget ceiling (วงเงิน) in THB
- Submission deadline (วันยื่นซอง) — date + time
- Procurement method (e-Bidding / e-Auction / เฉพาะเจาะจง)
- e-GP project number (เลขที่ e-GP) if available
- Owner (Roots person accountable)

## Process

### Step 1 — Dedup check
Read TOR_Opportunities. If a row with the same `egp_no` + `buyer` already exists,
warn the user and confirm before creating a duplicate.

### Step 2 — Assign tor_id
Increment from the last `tor_id` in the register (e.g. TOR-2026-004 → TOR-2026-005).

### Step 3 — Create Drive folder tree
If `~~cloud-storage` (Google Drive) is connected, create:
```text
8. Sales and Marketing/TOR/TOR_[Buyer]_[Project]_[YYYYMMDD]/
  00_TOR_and_Addendum/
  01_Admin_Documents/
  02_Company_Profile/
  03_Technical_Proposal/
  04_Solution_Spec/
  05_Project_Plan_and_Methodology/
  06_Team_CV/
  07_Experience_and_Evidence/
  08_Financial_and_LC/
  09_Commercial_Proposal/
  10_Presentation_Deck/
  11_QA_Checklist/
  12_Final_eGP_Upload/
  13_Print_Pack/
  99_Working/
```
If not connected: output the folder list and ask user to create it manually.

### Step 4 — Create Calendar deadline gates
If `~~calendar` (Google Calendar) is connected, create events:
- G1 Bid/No-Bid meeting: submission_deadline − 14 days (or immediately if < 14 days)
- G2 Document/matrix freeze: submission_deadline − 10 days
- G3 Draft review: submission_deadline − 7 days
- G4 QA review: submission_deadline − 2 days
- G5 Submission lock: submission_deadline − 1 day
- G5 Submission: deadline day
Title format: `[tor_id] [Gate] — [Project short name]`
If not connected: output the dates and ask the user to create them.

### Step 5 — Append to TOR_Opportunities register
Add the new row with `gate = G0`, `bid_decision = TBD`, `status = active`.
Update Statistics. Write back to Drive or output for paste.

## Output Format

```
## TOR Intake — [Project]
**tor_id:** [TOR-YYYY-NNN]
**e-GP:** [number or TBD]
**Buyer:** [agency]
**Budget:** THB [amount]
**Deadline:** [date/time] — [N] วันทำการที่เหลือ
**Owner:** [name]

### Folder created ✅
Drive: 8. Sales and Marketing/TOR/[folder name]/

### Calendar gates set ✅
G1 Bid/No-Bid: [date]
G2 Matrix freeze: [date]
G3 Draft review: [date]
G4 QA: [date]
G5 Lock: [date]
G5 Submit: [deadline]

### Next step
→ Run `roots-tor-analyzer` on the TOR PDF → Go/No-Go (G1)
→ On GO: run `roots-compliance-matrix` + `roots-scoring-matrix` (G2)
```

## Roots-Specific Notes
- tor_id is the unique key linking all registers — create it before everything else.
- Government e-GP deadline is often exact time (e.g. 10:00 น.) — capture it.
- If deadline is < 7 days away, flag immediately: "เวลาน้อยมาก — escalate ถึง Director ก่อน"
- Calendar events should include the tor_id in the title for easy search.
