# Register — LC_Bank_Facility

> **Location:** Google Drive → `8. Sales and Marketing/TOR Factory/registers/LC_Bank_Facility.md`
> **Maintained by:** `roots-lc-check`
> **Purpose:** Track bank guarantee / LC facility capacity so a bid is never blocked at
> the last minute by insufficient guarantee. `roots-lc-check` computes remaining capacity
> against a bid's required bid-bond and flags green / yellow / red.
> **Mode: BLOCK** — an insufficient/expired facility blocks the bid at G1 until Executive approval.

## How to Use

- Two levels: a **master facility** (your total bank credit line) and **individual LC
  instruments** (each bid bond / guarantee issued against it, tied to a project, with its
  own expiry and lifecycle).
- `roots-lc-check` reads a TOR's required guarantee amount/percentage and compares to
  remaining capacity, applying a safety buffer.
- A 🟡 or 🔴 result **blocks** the bid at G1 until Executive approval.
- **Lifecycle:** issued → tied to bid → [lost/expired] released, capacity returns; [won]
  converts to performance bond. Record the release so remaining capacity stays accurate.

---

## Registry — Facilities

| fac_id | bank | facility_limit | used_amount | remaining | expiry | conditions | eligibility |
|---|---|---|---|---|---|---|---|
| LC-001 | (sample) ธ.กรุงเทพ | 10,000,000 | 4,000,000 | 6,000,000 | 2026-12-31 | bid bond ≤ 5% | 🟢 |

## Registry — Instruments (individual LCs)

| inst_id | fac_id | tor_id | type | amount | issued_date | expiry | state |
|---|---|---|---|---|---|---|---|
| INST-001 | LC-001 | TOR-2026-001 | bid_bond | 175,000 | 2026-06-01 | 2026-09-30 | active |

---

## Field Reference — Facilities

| Field | Description | Example |
|---|---|---|
| `fac_id` | Sequential ID, `LC-NNN` | LC-001 |
| `bank` | Issuing bank | ธ.กรุงเทพ |
| `facility_limit` | Total facility (THB) | 10,000,000 |
| `used_amount` | Sum of active instruments (THB) | 4,000,000 |
| `remaining` | facility_limit − used_amount (THB) | 6,000,000 |
| `expiry` | Facility expiry `YYYY-MM-DD` | 2026-12-31 |
| `conditions` | Guarantee conditions / limits | bid bond ≤ 5% |
| `eligibility` | 🟢 sufficient / 🟡 low buffer / 🔴 insufficient or expired | 🟢 |

## Field Reference — Instruments

| Field | Description | Example |
|---|---|---|
| `inst_id` | Sequential ID, `INST-NNN` | INST-001 |
| `fac_id` | Parent facility | LC-001 |
| `tor_id` | Bid this instrument is tied to | TOR-2026-001 |
| `type` | bid_bond / performance_bond | bid_bond |
| `amount` | Value committed (THB) | 175,000 |
| `issued_date` | Date issued `YYYY-MM-DD` | 2026-06-01 |
| `expiry` | Instrument expiry `YYYY-MM-DD` | 2026-09-30 |
| `state` | active / released / converted / expired | active |

---

## Eligibility logic (applied by `roots-lc-check`)

```
required = bid bond amount (or % × budget)
buffer   = 10% of required (safety)
🟢 green  : remaining ≥ required + buffer  AND facility not near expiry
🟡 yellow : required ≤ remaining < required + buffer  → Executive approval (BLOCK until approved)
🔴 red    : remaining < required  OR facility expired/expiring before go-live → BLOCK
```

**Capacity release rule:** when a bid is lost/withdrawn or an instrument expires unused,
set `state = released` and recompute the facility's `used_amount` and `remaining`.

---

## Statistics

> Auto-updated by `roots-lc-check` on each write.

- Facilities tracked: 1
- Active instruments: 1
- Total remaining capacity: THB 6,000,000 (after active instruments)
- Facilities expiring < 90 days: 0
- Last updated: 2026-05-29
