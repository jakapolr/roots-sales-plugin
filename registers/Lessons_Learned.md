# Register — Lessons_Learned

> **Location:** Google Drive → `8. Sales and Marketing/TOR Factory/registers/Lessons_Learned.md`
> **Maintained by:** `roots-lessons-learned`
> **Purpose:** Capture the win/loss reason and score for every submitted bid (G6) so
> insights feed forward into future bids. A 0.14% loss must never be repeated silently.

## How to Use

- One row per submitted TOR, added after the result is known.
- `roots-lessons-learned` reads the bid's registers + the official result and records
  what to reuse or change.
- Future bids: `roots-scoring-matrix` and `tor-qa-reviewer` consult recent rows for
  recurring weak criteria.

---

## Registry

| ll_id | tor_id | result | our_score | winning_score | gap | reason | reusable_improvement | next_action | owner |
|---|---|---|---|---|---|---|---|---|---|
| LL-001 | (sample) TOR-2025-014 | lost | 82.36 | 82.50 | 0.14 | weak on methodology slide | add governance detail to methodology block | update Evidence_Library methodology | Sales Lead |

---

## Field Reference

| Field | Description | Example |
|---|---|---|
| `ll_id` | Sequential ID, `LL-NNN` | LL-001 |
| `tor_id` | The submitted TOR | TOR-2025-014 |
| `result` | won / lost / disqualified / withdrawn | lost |
| `our_score` | Roots' evaluated score | 82.36 |
| `winning_score` | Winner's score (if known) | 82.50 |
| `gap` | Points difference | 0.14 |
| `reason` | Root cause of win/loss | weak on methodology slide |
| `reusable_improvement` | What to change in the library/process | add governance detail |
| `next_action` | Concrete follow-up | update methodology block |
| `owner` | Who owns the follow-up | Sales Lead |

---

## Statistics

> Auto-updated by `roots-lessons-learned` on each write.

- Bids recorded: 1 (sample)
- Win rate: — (sample only)
- Recurring weak themes: methodology
- Last updated: 2026-05-29
