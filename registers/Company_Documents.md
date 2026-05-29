# Register — Company_Documents

> **Location:** Google Drive → `8. Sales and Marketing/TOR Factory/registers/Company_Documents.md`
> **Maintained by:** `roots-doc-freshness`
> **Purpose:** Freshness control for all company/eligibility documents so an expired
> document never causes disqualification. `roots-doc-freshness` classifies each as
> valid / expiring / expired / missing and triggers reminders.

## How to Use

- Single firm-wide register (not per-TOR).
- `roots-doc-freshness` reads issue/expiry, computes status, and on a TOR it copies the
  latest valid file into that TOR's evidence folder.
- Referenced by `TOR_Requirements.evidence_link` (e.g. `Company_Documents#affidavit`).

---

## Registry

| doc_id | document | anchor | issue_date | expiry_date | review_freq | owner | latest_file | status |
|---|---|---|---|---|---|---|---|---|
| DOC-001 | หนังสือรับรองบริษัท | affidavit | 2026-04-01 | 2026-10-01 | monthly | Admin | drive://... | valid |
| DOC-002 | ภ.พ.20 | vat | 2019-05-10 | — | quarterly | Admin | drive://... | valid |
| DOC-003 | งบการเงิน (ปีล่าสุด) | financials | 2025-03-31 | — | per-bid | Finance | drive://... | valid |

---

## Field Reference

| Field | Description | Example |
|---|---|---|
| `doc_id` | Sequential ID, `DOC-NNN` | DOC-001 |
| `document` | Document name (Thai) | หนังสือรับรองบริษัท |
| `anchor` | Short key used by `evidence_link` references | affidavit |
| `issue_date` | Date issued `YYYY-MM-DD` | 2026-04-01 |
| `expiry_date` | Hard expiry, or `—` if none | 2026-10-01 |
| `review_freq` | monthly / quarterly / per-bid (freshness policy) | monthly |
| `owner` | Responsible person | Admin |
| `latest_file` | Drive link to latest approved file | drive://... |
| `status` | valid / expiring / expired / missing | valid |

---

## Freshness Policy (default)

| Document type | Review frequency |
|---|---|
| Company affidavit / certificate (หนังสือรับรอง) | monthly — must be ≤ 6 months old at submission |
| VAT / tax (ภ.พ.20) | quarterly or on change |
| Power of attorney (หนังสือมอบอำนาจ) | per bid |
| Authorized signatory evidence | monthly |
| Project references (หนังสือรับรองผลงาน) | quarterly |
| Product / partner certificates | quarterly |
| Financial / bank documents (งบการเงิน) | per bid |

---

## Statistics

> Auto-updated by `roots-doc-freshness` on each run.

- Documents tracked: 3
- valid 3 / expiring 0 / expired 0 / missing 0
- Next expiry: 2026-10-01 (affidavit)
- Last updated: 2026-05-29
