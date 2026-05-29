---
name: roots-lessons-learned
description: "Record the win/loss result and lessons from a submitted bid in the Lessons_Learned register. Trigger after a bid result is known, when the user says 'บันทึก lessons learned', 'bid result', 'ผลประมูล', 'won/lost', 'G6 lessons', or when the user shares the procurement result announcement."
version: 1.0.0
source: roots-custom
phase: 3
---

# Lessons Learned — G6 Gate

> **Custom Skill** — Built by Roots.Tech
> **Maintains:** Lessons_Learned register (Google Drive → `8. Sales and Marketing/TOR Factory/registers/Lessons_Learned.md`)
> **Gate:** G6 — the final gate in the TOR factory cycle
> **Purpose:** Capture every bid result so insights compound forward. A 0.14% loss must
> be understood, not silently forgotten.

## Trigger

Use when:
- Bid result is announced (won / lost / disqualified)
- User says "บันทึก lessons learned", "bid result", "ผลประมูล", "G6 lessons"
- Periodic pipeline review: past bids without G6 entries flagged

## Process

### Step 1 — Gather result data
Ask for (or extract from shared announcement):
- `tor_id` of the submitted bid
- Result: won / lost / disqualified / withdrawn
- Roots' evaluated score (if published)
- Winner's score (if published, even approximate)
- Official announcement or evaluation sheet (if available)

### Step 2 — Diagnose the gap
If lost: for each scoring criterion in Scoring_Matrix, compare the response angle and
evidence used against the outcome. Identify likely weaknesses:
- Was a scored criterion underserved (low evidence, weak angle)?
- Was a mandatory item marginal?
- Were there QA issues in Review_Log that weren't fully resolved?
- Was the score gap in a specific section (methodology / team / technical / price)?

If won: identify what contributed most to the win (strongest evidence, highest-scoring sections).

### Step 3 — Identify reusable improvements
For each lesson: translate into a concrete action on a Roots system or library:
- "add methodology governance detail to Evidence_Library"
- "CV for [role] needs IFRS project added"
- "scoring-matrix: weight team experience criterion as strong only with government references"

### Step 4 — Assign next actions
Each improvement needs an owner and a deadline. Default owner: Sales Lead for process
items, Tech Lead for technical items.

### Step 5 — Update registers
- Append to Lessons_Learned register.
- Update TOR_Opportunities: set `status = won / lost / disqualified`, `gate = G6`.
- **Release LC capacity:** in LC_Bank_Facility, update this bid's instrument — lost/withdrawn → `state = released`, won → `state = converted` (to performance bond) — and recompute the facility's `used_amount` / `remaining`. This returns capacity for the next bid.
- Update Scoring_Matrix rows for any `strength` reclassifications.
- Write back to Drive or output for paste.

## Output Format

```
## G6 Lessons Learned — [tor_id]
**Project:** [project name]
**Result:** 🏆 WON / ❌ LOST ([gap] points) / 🚫 DISQUALIFIED

### Score summary
Our score: [N] | Winner: [N] | Gap: [N] points | Section with biggest gap: [section]

### Key lessons
| # | Lesson | Root cause | Improvement | Owner | By |
|---|---|---|---|---|---|
| 1 | [lesson] | [cause] | [what to change] | [who] | [date] |

### What worked well (carry forward)
- [strength 1]
- [strength 2]

### Register updates made
- TOR_Opportunities: status → [won/lost]
- Lessons_Learned: LL-[NNN] appended
- Scoring_Matrix: [any strength reclassifications]
```

## Roots-Specific Notes
- Even wins need a lessons-learned entry — document what worked so it's repeated intentionally.
- Score data from Thai government procurement is often published in the evaluation sheet (ผลการพิจารณา) — request it even if not proactively shared.
- If lost by < 1 point: always do a deep criteria-by-criteria review. This is recoverable with better evidence on one criterion.
- Feed recurring weak themes back into roots-scoring-matrix default `strength` assessments — so future bids start with calibrated expectations.
- G6 closes the loop: after G6, the tor_id is archived but its lessons flow forward into every future bid.
