---
name: roots-evidence-matcher
description: "Match TOR requirements and scoring criteria to existing evidence in the Evidence_Library. Trigger when roots-compliance-matrix or roots-scoring-matrix has rows with 'Needs human review' in evidence_link, or when user says 'หาหลักฐาน', 'match evidence', 'หา reference project', 'fill evidence gaps'. Fills evidence_link fields so proposal claims are always backed by proof."
version: 1.0.0
source: roots-custom
phase: 3
---

# Evidence Matcher

> **Custom Skill** — Built by Roots.Tech
> **Reads:** Evidence_Library register, TOR_Requirements, Scoring_Matrix
> **Writes:** Updates `evidence_link` in TOR_Requirements and Scoring_Matrix
> **Purpose:** Replace "Needs human review" evidence gaps with real pointers from the
> reusable library — so every requirement and scored criterion has a proof link before
> drafting starts.

## Trigger

Use when:
- roots-compliance-matrix or roots-scoring-matrix output shows "Needs human review" in evidence columns
- User says "หาหลักฐาน", "match evidence", "หา reference project", "fill evidence"
- Preparing a proposal and need to populate evidence links

## Process

### Step 1 — Read the evidence needed
Read TOR_Requirements rows with `evidence_link = Needs human review`.
Read Scoring_Matrix rows with `evidence_link = Needs human review`.
Collect the requirement/criterion text, type, and industry context from the TOR.

### Step 2 — Read Evidence_Library
Load the full Evidence_Library register. Filter to `reusable = yes` only.
Note: `confidentiality = internal-only` or `NDA` items cannot be attached to bids —
they can only be referenced internally.

### Step 3 — Match by relevance
For each gap, rank Evidence_Library items by:
1. Industry match (same vertical = high priority)
2. Module overlap (matching Odoo modules)
3. Value match (project value ≥ TOR's minimum reference value requirement)
4. Year (recent = preferred, usually last 5 years for government)
5. Evidence type (reference_letter > case_study > certificate for qualification proofs)

Return top 1–3 matches per gap. If no match exists → keep "Needs human review" and flag
as a gap that needs a new evidence item to be added to the library.

### Step 4 — Update the registers
For each matched gap: update `evidence_link` in TOR_Requirements and Scoring_Matrix
with the `ev_id` and a short description (e.g. `EV-001: ERP โรงงานน้ำตาล (2024)`).
Write back to Drive or output the updated rows.

### Step 5 — Flag unmatched gaps
Any requirement/criterion still showing "Needs human review" after matching = a real gap.
These need either: (a) a new project reference obtained, (b) a certificate acquired, or
(c) the bid is weakened on this point. Flag each with recommended action.

## Output Format

```
## Evidence Matching — [tor_id]
**Gaps found:** [N]  |  **Matched:** [N]  |  **Still unmatched:** [N]

### Matched ✅
| req_id / crit_id | evidence_link | confidence | notes |
|---|---|---|---|
| REQ-004 | EV-001: ERP โรงงานน้ำตาล (2024) | high | same industry, value 2.8M > TOR min 1M |

### Still unmatched ❌ (action required)
| req_id / crit_id | gap description | recommended action |
|---|---|---|
| SC-003 | No IFRS reference project | add to Evidence_Library after closing current IFRS project |

### Evidence library gaps (items to add for future bids)
- [evidence type needed] — [industry/module] — add after [project name] closes
```

## Roots-Specific Notes
- Government minimum reference value is often THB 1M–3M per project — filter accordingly.
- หนังสือรับรองผลงาน from client is the gold standard reference — certificates alone rarely suffice for mandatory qualification items.
- Confidentiality: never attach internal-only evidence to a public bid. You can reference the project name without attaching.
- After each won project closes, prompt Sales to add it to Evidence_Library — this is how the library grows.
- Evidence_Library should be updated quarterly with new references.
