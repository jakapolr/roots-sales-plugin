---
name: roots-lc-check
description: "Check bank guarantee / LC facility availability for a Thai government bid and flag green/yellow/red eligibility. Trigger when the user says 'ตรวจ LC', 'check bid bond', 'LC เพียงพอไหม', 'หลักประกันซอง', 'bid guarantee', or when a TOR requires a bid bond (หลักประกันซอง) or financial capacity evidence."
version: 1.0.0
source: roots-custom
phase: 3
---

# LC / Bank Guarantee Check

> **Custom Skill** — Built by Roots.Tech
> **Reads/updates:** LC_Bank_Facility register (Google Drive → `8. Sales and Marketing/TOR/registers/LC_Bank_Facility.md`)
> **Gate:** G1 (bid eligibility) and G2 (before committing to bid)
> **Purpose:** Prevent the worst-case scenario: reaching the submission day and discovering
> the bank facility is insufficient or expired to issue the bid bond.

## Trigger

Use when:
- A TOR requires หลักประกันซอง (bid bond) or financial capacity evidence
- User says "ตรวจ LC", "check bid bond", "LC เพียงพอไหม", "หลักประกันซอง", "bid guarantee"
- roots-tor-intake or roots-tor-analyzer mentions a bid bond requirement

## Process

### Step 1 — Read TOR bid bond requirement
From TOR (or user input):
- Bid bond percentage (% of budget, typically 2–5%)
- Budget ceiling (วงเงิน)
- Bid bond form (bank guarantee letter / cashier's cheque / government bond)
- Required before: submission date (วันยื่นซอง)

Compute: **required_amount = budget × bid_bond_pct / 100**

### Step 2 — Read LC_Bank_Facility register
Get all facility rows. Compute actual remaining at bid submission:
- `remaining = facility_limit − used_amount`
  (used_amount includes all live bids already committed, not just this one)
- Check `expiry` vs submission deadline — facility must be valid at submission time.

### Step 3 — Apply eligibility logic

```
buffer = required_amount × 0.10  (10% safety margin)

🟢 green  : remaining ≥ required_amount + buffer
            AND facility expiry > submission deadline
🟡 yellow : required_amount ≤ remaining < required_amount + buffer
            (sufficient but thin margin)
            OR facility expires within 30 days of submission
🔴 red    : remaining < required_amount
            OR facility expired / expires before submission deadline
```

A 🟡 or 🔴 result must be **escalated to Executive before bid continues (G1)**.

### Step 4 — Update LC_Bank_Facility register
Update `used_amount` (add this bid's required amount if proceeding) and `eligibility`.
Write back to Drive or output for paste.

### Step 5 — Bid bond timeline reminder
Bank guarantee typically takes **3–5 business days**. Compute:
- Latest date to request: submission_deadline − 5 business days.
- If today > that date: 🔴 URGENT — contact bank immediately.
- Otherwise: draft Calendar reminder.

## Output Format

```
## LC / Bid Guarantee Check — [tor_id]
**TOR budget:** THB [budget]
**Bid bond required:** [%] = THB [required]
**Submission deadline:** [date]

### Facility status
| Bank | Limit | Used | Remaining | Expiry | Status |
|---|---|---|---|---|---|
| [bank] | THB [limit] | THB [used] | THB [remaining] | [date] | 🟢/🟡/🔴 |

**Overall eligibility: 🟢 GREEN / 🟡 YELLOW / 🔴 RED**

### Decision
🟢 Bid can proceed — sufficient guarantee capacity.
OR
🟡 Margin thin — recommend Executive approval before committing.
OR
🔴 Insufficient capacity — DO NOT proceed without Director decision.

### Timeline
Latest date to request bank guarantee: [date]
⚠️ Urgency level: [normal / urgent / critical]
```

## Roots-Specific Notes
- Bid bond (หลักประกันซอง) and performance bond (หลักประกันสัญญา) are separate — this skill covers the bid bond only. Performance bond is typically 5% of contract value and needed after winning.
- Some TORs accept cashier's cheque (แคชเชียร์เช็ค) — simpler and faster than bank guarantee if amount is small.
- If LC capacity is 🔴 red: do not quietly proceed. Flag to Director immediately. Submitting without valid bid bond = automatic disqualification.
- Update `used_amount` when a bid is submitted, and release it when the bid result is known (won → convert to performance bond, lost/withdrawn → release capacity).
