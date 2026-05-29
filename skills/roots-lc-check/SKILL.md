---
name: roots-lc-check
description: "Check bank guarantee / LC facility availability for a Thai government bid and flag green/yellow/red eligibility. Trigger when the user says 'ตรวจ LC', 'check bid bond', 'LC เพียงพอไหม', 'หลักประกันซอง', 'bid guarantee', or when a TOR requires a bid bond (หลักประกันซอง) or financial capacity evidence."
version: 1.0.0
source: roots-custom
phase: 3
---

# LC / Bank Guarantee Check

> **Custom Skill** — Built by Roots.Tech
> **Reads/updates:** LC_Bank_Facility register (Google Drive → `8. Sales and Marketing/TOR Factory/registers/LC_Bank_Facility.md`)
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
The register has two levels: **facilities** (master credit lines) and **instruments**
(individual bid bonds / guarantees issued against a facility, each tied to a `tor_id`).

Compute actual remaining at bid submission:
- `used_amount = SUM(amount of instruments where state = active)` for that facility
- `remaining = facility_limit − used_amount`
- Check `expiry` vs submission deadline — facility must be valid at submission time.
- **First, reconcile stale instruments:** any instrument whose bid was lost/withdrawn, or
  that expired unused, should be `state = released` (capacity returns). Flag any that look
  stale so used_amount is not overstated.

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

**Mode: BLOCK.** A 🟡 or 🔴 result **blocks the bid at G1** — `tor-factory-orchestrator`
will not advance past G1 until Executive explicitly approves (🟡) or capacity is found
(🔴). Do not let preparation continue on a blocked bid without that approval.

### Step 4 — Update LC_Bank_Facility register
If the bid proceeds, add an **instrument** row (`type = bid_bond`, `amount = required`,
`tor_id`, `state = active`) and recompute the facility's `used_amount` and `remaining`.
When the result is known, `roots-lessons-learned` (G6) releases it: lost/withdrawn →
`state = released`; won → `state = converted` (to performance bond). Write back to Drive.

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
