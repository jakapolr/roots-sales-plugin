# Register — TOR_Opportunities

> **Location:** Google Drive → `8. Sales and Marketing/TOR/registers/TOR_Opportunities.md`
> **Maintained by:** `roots-tor-intake` (create), `roots-tor-analyzer` (bid/no-bid), all skills (status)
> **Purpose:** Master pipeline of every TOR — the index every other register links to via `tor_id`.

## How to Use

- **Salesperson:** scan to see all live bids, deadlines, owners, and gate status.
- **Skills:** read to resolve a `tor_id`; `roots-tor-intake` appends new rows and checks
  for duplicates by `egp_no` + `buyer` before creating.

---

## Registry

| tor_id | egp_no | buyer | project | budget_thb | deadline | submission_channel | owner | bid_decision | gate | status | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| TOR-2026-001 | 64066 | กรมพัฒนาที่ดิน | ERP ระบบบริหารจัดการ | 3,500,000 | 2026-06-30 | e-Bidding | Pan | GO | G2 | active | sample row |

---

## Field Reference

| Field | Description | Example |
|---|---|---|
| `tor_id` | Sequential ID, `TOR-YYYY-NNN` | TOR-2026-001 |
| `egp_no` | e-GP project number | 64066 |
| `buyer` | Agency / company (Thai or English) | กรมพัฒนาที่ดิน |
| `project` | Project title | ERP ระบบบริหารจัดการ |
| `budget_thb` | Budget ceiling (วงเงิน) in THB | 3,500,000 |
| `deadline` | Submission deadline (วันยื่นซอง) `YYYY-MM-DD` | 2026-06-30 |
| `submission_channel` | e-Bidding / e-Auction / เฉพาะเจาะจง / hardcopy | e-Bidding |
| `owner` | Roots accountable person | Pan |
| `bid_decision` | GO / NO-GO / CONDITIONAL / TBD | GO |
| `gate` | Current gate G0–G6 | G2 |
| `status` | active / submitted / won / lost / withdrawn | active |
| `notes` | Optional human note | — |

---

## Statistics

> Auto-updated by `roots-tor-intake` on each append.

- Total TORs logged: 1
- Active bids: 1
- Date range: 2026-06-30 → 2026-06-30
- Last updated: 2026-05-29
