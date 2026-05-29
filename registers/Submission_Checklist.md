# Register — Submission_Checklist

> **Location:** Google Drive → `8. Sales and Marketing/TOR Factory/registers/Submission_Checklist.md`
> **Maintained by:** `roots-submission-packager`
> **Purpose:** Per-bid file-level checklist tracking the physical submission state of every
> required document — generated, signed, stamped, reviewed, uploaded, printed — so nothing
> is missing or unsigned at the deadline.

## How to Use

- One section per `tor_id`, mirroring the standard submission folder tree.
- `roots-submission-packager` generates rows from TOR_Requirements + the folder template.
- The bid cannot be **locked (G5)** until every required row is reviewed and (for e-GP)
  uploaded, or explicitly waived by Executive.

---

## Registry

| item_id | tor_id | folder | file | required_by_tor | generated | signed | stamped | reviewed | uploaded | printed |
|---|---|---|---|---|---|---|---|---|---|---|
| SUB-001 | TOR-2026-001 | 01_Admin_Documents | หนังสือรับรองบริษัท.pdf | yes | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ |
| SUB-002 | TOR-2026-001 | 06_Team_CV | CV_ทีมงาน.pdf | yes | ✅ | ⬜ | n/a | ⬜ | ⬜ | ⬜ |

---

## Field Reference

| Field | Description | Example |
|---|---|---|
| `item_id` | Sequential per TOR, `SUB-NNN` | SUB-001 |
| `tor_id` | Parent TOR | TOR-2026-001 |
| `folder` | Standard folder (see tree below) | 01_Admin_Documents |
| `file` | File name | หนังสือรับรองบริษัท.pdf |
| `required_by_tor` | yes / no (TOR-mandated vs supporting) | yes |
| `generated` | ✅ / ⬜ created |  |
| `signed` | ✅ / ⬜ / n/a signature applied |  |
| `stamped` | ✅ / ⬜ / n/a company seal applied |  |
| `reviewed` | ✅ / ⬜ passed QA |  |
| `uploaded` | ✅ / ⬜ uploaded to e-GP |  |
| `printed` | ✅ / ⬜ in print pack |  |

---

## Standard submission folder tree

```text
TOR_[Buyer]_[Project]_[YYYYMMDD]/
  00_TOR_and_Addendum/      05_Project_Plan_and_Methodology/   10_Presentation_Deck/
  01_Admin_Documents/       06_Team_CV/                        11_QA_Checklist/
  02_Company_Profile/       07_Experience_and_Evidence/        12_Final_eGP_Upload/
  03_Technical_Proposal/    08_Financial_and_LC/               13_Print_Pack/
  04_Solution_Spec/         09_Commercial_Proposal/            99_Working/
```

---

## Statistics

> Auto-updated by `roots-submission-packager` on each write.

- Items tracked: 2
- Required complete (reviewed): 1 / 2
- Ready to lock (G5): no
- Last updated: 2026-05-29
