# Register — Review_Log

> **Location:** Google Drive → `8. Sales and Marketing/TOR Factory/registers/Review_Log.md`
> **Maintained by:** `tor-qa-reviewer` (also `proposal-reviewer`)
> **Purpose:** Track every QA issue raised on a bid — severity, owner, deadline, and
> resolution — so the **G4 gate rule holds: no final package while a high-severity issue
> is open and unwaived**.

## How to Use

- One section per `tor_id`.
- `tor-qa-reviewer` appends issues found during QA; owners update `resolved`.
- The `tor-factory-orchestrator` blocks G5 lock if any 🔴 row is unresolved & unwaived.

---

## Registry

| issue_id | tor_id | issue | severity | file | owner | deadline | resolved | final_approver |
|---|---|---|---|---|---|---|---|---|
| ISS-001 | TOR-2026-001 | REQ-002 (IFRS) has no evidence | 🔴 high | Technical_Proposal | SE | 2026-06-25 | no | — |
| ISS-002 | TOR-2026-001 | ชื่อโครงการไม่ตรงกันใน 2 จุด | 🟡 med | Cover | AE | 2026-06-26 | yes | AE |

---

## Field Reference

| Field | Description | Example |
|---|---|---|
| `issue_id` | Sequential per TOR, `ISS-NNN` | ISS-001 |
| `tor_id` | Parent TOR | TOR-2026-001 |
| `issue` | What's wrong (reference req_id/crit_id where relevant) | REQ-002 has no evidence |
| `severity` | 🔴 high / 🟡 medium / 🟢 low | 🔴 high |
| `file` | Affected document | Technical_Proposal |
| `owner` | Who must fix | SE |
| `deadline` | Fix-by date `YYYY-MM-DD` | 2026-06-25 |
| `resolved` | yes / no / waived | no |
| `final_approver` | Who signed off / waived | — |

---

## Gate rule

> **G4:** No bid proceeds to G5 lock while any `severity = 🔴 high` row has
> `resolved = no`. A 🔴 may be closed as `waived` only by Executive, recorded in
> `final_approver`.

---

## Statistics

> Auto-updated by `tor-qa-reviewer` on each write.

- Issues logged: 2
- Open 🔴 high: 1
- Resolved / waived: 1
- Last updated: 2026-05-29
