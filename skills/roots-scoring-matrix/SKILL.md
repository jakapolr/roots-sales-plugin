---
name: roots-scoring-matrix
description: "Turn a TOR's evaluation/scoring criteria into a weighted response strategy — each criterion mapped to a response angle, required evidence, owner, and deck slide. Trigger when the user says 'ทำ scoring matrix', 'วิเคราะห์เกณฑ์ให้คะแนน', 'scoring criteria', 'criteria optimizer', 'จะได้คะแนนเต็มยังไง', or after roots-compliance-matrix has separated out the scored criteria. This is the skill that defends against losing by a fraction of a point."
version: 1.0.0
source: roots-custom
phase: 3
---

# Scoring Matrix — Criteria Optimizer

> **Custom Skill** — Built by Roots.Tech
> **Maintains:** [Scoring_Matrix register](../../registers/Scoring_Matrix.md)
> **Runs after:** `roots-compliance-matrix` (which flags the scored criteria)
> **Feeds:** `se-orchestrator` Mode E (proposal) and Mode F (deck)

## Why this exists

Roots lost a bid by **0.14%**. Compliance gets you qualified; **scoring** decides who wins.
This skill decomposes the TOR's evaluation section into a weighted plan: for each scored
criterion, what the evaluator wants, the strongest response angle, the evidence that backs
it, who writes it, and which deck slide carries it. The proposal **and** the presentation
deck are both generated from this one register, so they can never diverge.

## Trigger

Use when:
- `roots-compliance-matrix` has identified `type=scored` requirements
- User says "ทำ scoring matrix", "วิเคราะห์เกณฑ์ให้คะแนน", "criteria optimizer",
  "จะได้คะแนนเต็มยังไง", "scoring strategy"
- A performance-based / weighted-evaluation TOR (Pattern C) is being prepared

## Input

- The TOR evaluation/scoring section (เกณฑ์การพิจารณา / เกณฑ์ให้คะแนน)
- `tor_id` and the scored rows from
  [TOR_Requirements](../../registers/TOR_Requirements.md)
- Roots capability context (CONTEXT.md, Evidence_Library, CV_Master)

## Process

### Step 1 — Extract every scored criterion
From the TOR evaluation section, pull each criterion with its `max_score`, `weight_pct`,
and any `pass_threshold`. Weights must sum to 100% (or the TOR's stated total) — if they
don't, flag the discrepancy as `Needs human review`. Do not invent criteria.

### Step 2 — For each criterion, build the response plan
- **`response_angle`** — the strongest, *evidence-backed* answer to what the evaluator
  wants. Do not claim a capability Roots cannot prove.
- **`evidence_link`** — the proof (Evidence_Library / CV_Master / Company_Documents). If
  none exists yet, `Needs human review` and flag it as a gap.
- **`strength`** — `strong` / `medium` / `weak`: Roots' honest position on this criterion.
- **`owner`** / **`reviewer`** — who drafts and who validates.
- **`slide`** — the deck slide number that will carry this criterion (deck is built from
  this column).
- **`risk`** — 🟢 / 🟡 / 🔴 score-loss risk.

### Step 3 — Weighted prioritization
Rank criteria by `weight_pct × (1 − strength_factor)` to find where the most points are at
risk (high weight + weak/medium strength). These get the most proposal effort and the
strongest evidence. Surface this ranking explicitly — it tells the team where to invest.

### Step 4 — Score projection
Estimate Roots' likely score: for each criterion, `max_score × expected_capture%` based on
strength (strong ≈ 90%+, medium ≈ 70%, weak ≈ 50% — adjust with judgment). Sum to a
projected total. Compare against any known pass threshold and, if available, recent
[Lessons_Learned](../../registers/Lessons_Learned.md) winning scores. This is an estimate,
labeled as such — never present it as a guaranteed score.

### Step 5 — Write the register
Append to [Scoring_Matrix](../../registers/Scoring_Matrix.md) using the register-write
pattern. Update Statistics. Write back to Drive (or output for paste).

## Output Format

```
## Scoring Matrix — [Project] (tor_id)
**Total points:** [N]  |  **Criteria:** [N]  |  **Projected capture:** ~[N]% (estimate)

| crit_id | criterion | max | weight | angle | evidence | strength | slide | risk |
|---|---|---|---|---|---|---|---|---|
| SC-001 | ประสบการณ์ทีม | 20 | 20% | 12y + 3 ERP รัฐ | CV_Master | strong | 5 | 🟢 |

### Where points are most at risk (invest here)
1. [crit_id] — weight [%], strength [weak/medium] — [what to strengthen]

### Evidence gaps (run roots-evidence-matcher)
- [crit_id] — needs: [evidence type]

### Projected score (estimate, not a guarantee)
~[N] / [total]  —  [above/below] known pass threshold of [X]

### Next step
→ se-orchestrator Mode E uses this to structure the proposal
→ se-orchestrator Mode F builds the deck from the `slide` column
```

## Roots-Specific Notes
- **Honesty rule:** strength and projected score must reflect real, provable capability.
  Overstating a weak criterion is how bids are lost on the technical interview, not won.
- Deck and proposal both derive from this register — keep `slide` numbers consistent with
  the deck `se-orchestrator` Mode F produces.
- For government Pattern-C TORs, the methodology and team-experience criteria are usually
  the highest-weight, most-contested points — give them the strongest evidence.
- Feed recurring `weak` themes back to `roots-lessons-learned` after the result.
