# Register — LC_Bank_Facility

> **Location:** Google Drive → `8. Sales and Marketing/TOR/registers/LC_Bank_Facility.md`
> **Maintained by:** `roots-lc-check`
> **Purpose:** Track bank guarantee / LC facility capacity so a bid is never blocked at
> the last minute by insufficient guarantee. `roots-lc-check` computes remaining capacity
> against a bid's required bid-bond and flags green / yellow / red.

## How to Use

- One row per bank facility (firm-wide), plus per-bid allocations tracked in `notes`.
- `roots-lc-check` reads a TOR's required guarantee amount/percentage and compares to
  remaining capacity, applying a safety buffer.
- A 🟡 or 🔴 result requires Executive approval before the bid continues (G1).

---

## Registry

| fac_id | bank | facility_limit | used_amount | remaining | expiry | conditions | eligibility |
|---|---|---|---|---|---|---|---|
| LC-001 | (sample) ธ.กรุงเทพ | 10,000,000 | 4,000,000 | 6,000,000 | 2026-12-31 | bid bond ≤ 5% | 🟢 |

---

## Field Reference

| Field | Description | Example |
|---|---|---|
| `fac_id` | Sequential ID, `LC-NNN` | LC-001 |
| `bank` | Issuing bank | ธ.กรุงเทพ |
| `facility_limit` | Total facility (THB) | 10,000,000 |
| `used_amount` | Currently committed across live bids (THB) | 4,000,000 |
| `remaining` | facility_limit − used_amount (THB) | 6,000,000 |
| `expiry` | Facility expiry `YYYY-MM-DD` | 2026-12-31 |
| `conditions` | Guarantee conditions / limits | bid bond ≤ 5% |
| `eligibility` | 🟢 sufficient / 🟡 low buffer / 🔴 insufficient or expired | 🟢 |

---

## Eligibility logic (applied by `roots-lc-check`)

```
required = bid bond amount (or % × budget)
buffer   = 10% of required (safety)
🟢 green  : remaining ≥ required + buffer  AND facility not near expiry
🟡 yellow : required ≤ remaining < required + buffer  → Executive approval
🔴 red    : remaining < required  OR facility expired/expiring before go-live
```

---

## Statistics

> Auto-updated by `roots-lc-check` on each write.

- Facilities tracked: 1
- Total remaining capacity: THB 6,000,000
- Facilities expiring < 90 days: 0
- Last updated: 2026-05-29
