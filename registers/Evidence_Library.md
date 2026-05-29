# Register — Evidence_Library

> **Location:** Google Drive → `8. Sales and Marketing/TOR Factory/registers/Evidence_Library.md`
> **Maintained by:** `roots-evidence-matcher`
> **Purpose:** Reusable library of proof — past project references, client letters,
> certificates, screenshots, case studies — so requirements and scoring criteria can be
> matched to existing evidence instead of recreating it each bid.

## How to Use

- Single firm-wide register, grows over time (every closed project adds rows).
- `roots-evidence-matcher` searches this to fill `evidence_link` in TOR_Requirements
  and Scoring_Matrix.
- `confidentiality` controls whether an item may be attached to a public bid.

---

## Registry

| ev_id | reference | client | industry | module | evidence_type | value_thb | year | confidentiality | reusable | file |
|---|---|---|---|---|---|---|---|---|---|---|
| EV-001 | (sample) ERP โรงงานน้ำตาล | (NDA) | sugar | Manufacturing, Inventory | reference_letter | 2,800,000 | 2024 | client-approved | yes | drive://... |
| EV-002 | (sample) Odoo อาหาร FEFO | Green Deli | food | Inventory, Quality | case_study | 1,200,000 | 2025 | internal-only | no | drive://... |

---

## Field Reference

| Field | Description | Example |
|---|---|---|
| `ev_id` | Sequential ID, `EV-NNN` | EV-001 |
| `reference` | Project / evidence title | ERP โรงงานน้ำตาล |
| `client` | Client name or `(NDA)` | (NDA) |
| `industry` | Vertical | sugar |
| `module` | Odoo modules involved | Manufacturing, Inventory |
| `evidence_type` | reference_letter / case_study / certificate / screenshot / contract | reference_letter |
| `value_thb` | Project value (for "min value" qualification checks) | 2,800,000 |
| `year` | Year delivered | 2024 |
| `confidentiality` | public / client-approved / internal-only / NDA | client-approved |
| `reusable` | yes / no — may be reused in a bid submission | yes |
| `file` | Drive link | drive://... |

---

## Statistics

> Auto-updated by `roots-evidence-matcher` on each write.

- Evidence items: 2
- Reusable for bids: 1
- Industries covered: sugar, food
- Last updated: 2026-05-29
