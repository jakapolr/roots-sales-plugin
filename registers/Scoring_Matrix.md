# Register — Scoring_Matrix

> **Location:** Google Drive → `8. Sales and Marketing/TOR Factory/registers/Scoring_Matrix.md`
> **Maintained by:** `roots-scoring-matrix`
> **Purpose:** Turn the TOR's **evaluation criteria** into a weighted response plan.
> Every scored criterion gets a response angle, required evidence, owner, and the deck
> slide that carries it. **The proposal deck must be generated from this register** so
> proposal and presentation never diverge. This is the register that defends against
> losing by a fraction of a point.

## How to Use

- One section per `tor_id`.
- `roots-scoring-matrix` extracts criteria + weights from the TOR evaluation section.
- `se-orchestrator` Mode E/F reads this to structure the proposal and deck.
- Sort by `weight` descending to see where points are won or lost.

---

## Registry

| crit_id | tor_id | criterion | max_score | weight_pct | pass_threshold | response_angle | evidence_link | slide | owner | reviewer | strength | risk |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SC-001 | TOR-2026-001 | ประสบการณ์ทีมงาน | 20 | 20% | — | 12 ปี + 3 ERP ภาครัฐ | CV_Master, Evidence_Library | 5 | SE | Tech Lead | strong | 🟢 |
| SC-002 | TOR-2026-001 | วิธีการดำเนินงาน | 30 | 30% | 18 | Waterfall + governance | methodology block | 4 | SE | Tech Lead | medium | 🟡 |

---

## Field Reference

| Field | Description | Example |
|---|---|---|
| `crit_id` | Sequential per TOR, `SC-NNN` | SC-001 |
| `tor_id` | Parent TOR | TOR-2026-001 |
| `criterion` | Evaluation criterion as written in the TOR | ประสบการณ์ทีมงาน |
| `max_score` | Maximum points for this criterion | 20 |
| `weight_pct` | Share of total score | 20% |
| `pass_threshold` | Minimum to pass (if any), else `—` | 18 |
| `response_angle` | How Roots should answer to maximize the score | 12 ปี + 3 ERP ภาครัฐ |
| `evidence_link` | Evidence backing the claim, or `Needs human review` | CV_Master |
| `slide` | Deck slide number that carries this criterion | 5 |
| `owner` | Who writes the response | SE |
| `reviewer` | Who validates | Tech Lead |
| `strength` | strong / medium / weak — Roots' position on this criterion | strong |
| `risk` | 🟢 / 🟡 / 🔴 — score-loss risk | 🟢 |

---

## Statistics

> Auto-updated by `roots-scoring-matrix` on each write.

- Criteria logged: 2
- Total weight covered: 50%
- Weak/medium criteria (score-loss risk): 1
- Last updated: 2026-05-29
