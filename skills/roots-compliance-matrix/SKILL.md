---
name: roots-compliance-matrix
description: "Decompose a Thai government/corporate TOR into a row-level compliance matrix (requirement → type → owner → evidence → status). Trigger after roots-tor-analyzer returns a GO decision, or when the user says 'ทำ compliance matrix', 'แตก requirement', 'requirement matrix', 'TOR checklist ละเอียด', or asks to map every TOR requirement before drafting a proposal. This is the G2 control gate — no proposal drafting until this matrix is complete."
version: 1.0.0
source: roots-custom
phase: 3
---

# Compliance Matrix — TOR Requirement Decomposition

> **Custom Skill** — Built by Roots.Tech
> **Maintains:** [TOR_Requirements register](../../registers/TOR_Requirements.md)
> **Runs after:** `roots-tor-analyzer` GO decision · **Runs before:** any proposal drafting
> **Gate:** G2 Matrix Freeze — the single most important control in the TOR Factory

## Why this exists

Bids are lost by missing **one mandatory item** or leaving **one scored criterion**
unanswered. This skill converts the entire TOR into a row-per-requirement matrix so every
requirement has an owner, an evidence pointer, and a response status — *before* anyone
writes a proposal. **Do not draft the proposal until this matrix is complete and frozen.**

## Trigger

Use when:
- `roots-tor-analyzer` just returned GO and the user wants to proceed
- User says "ทำ compliance matrix", "แตก requirement", "requirement matrix", "map TOR"
- User is about to draft a proposal for a TOR (intercept — build the matrix first)

## Input

- TOR text (from `roots-tor-analyzer` output, or OCR'd PDF, or pasted)
- The `tor_id` from [TOR_Opportunities](../../registers/TOR_Opportunities.md) (create via
  `roots-tor-intake` if it doesn't exist yet)

## Process

### Step 0 — Resolve the TOR
Find or confirm the `tor_id`. If none exists, ask the user to run `roots-tor-intake`
first (so the matrix links to a registered opportunity).

### Step 1 — Decompose the TOR section by section
Read the full TOR. Extract **every** discrete requirement as its own row. Do not merge
distinct requirements; do not drop any. Preserve the original wording closely enough that
the requirement is unambiguous (`requirement` column).

Cover all eight TOR layers:
1. Buyer context · 2. Scope & deliverables · 3. Eligibility/company documents ·
4. Technical compliance · 5. Project delivery · 6. Commercial conditions ·
7. Scoring/evaluation · 8. Submission packaging.

### Step 2 — Classify each requirement
For every row, set:
- **`type`** — one of: `mandatory-passfail`, `scored`, `commercial`, `legal`,
  `presentation`, `delivery`
- **`mandatory`** — `yes` if failing it disqualifies the bid, else `no`
- **`weight`** — the scoring weight if `type=scored`, else `—`
  (scored criteria are also expanded in detail by `roots-scoring-matrix`)

### Step 3 — Assign owner, evidence, risk
- **`owner`** — map to a Roots role (Admin / Finance / SE / Tech Lead / AE / PM) using the
  RACI in [registers/README.md](../../registers/README.md) and CONTEXT.md team.
- **`evidence_link`** — point to the register/anchor that proves compliance
  (e.g. `Company_Documents#affidavit`, `Evidence_Library`, `CV_Master`). If no evidence is
  known yet, write `Needs human review` — **never invent evidence**.
- **`risk`** — 🟢 OK / 🟡 WARN / 🔴 RISK. Mark 🔴 for any requirement Roots may fail
  (qualification gap, capability gap, missing document).
- **`response_status`** — start at `open`.

### Step 4 — Coverage & gate check
Compute coverage and surface blockers:
- Count mandatory requirements with no evidence or 🔴 risk → these block the bid.
- The matrix is **"frozen" (G2 pass)** only when every `mandatory-passfail` row has an
  owner and an evidence pointer (or an explicit `waived`), and no 🔴 is unresolved.
- Escalate 🔴 rows to Sales Lead + Tech Lead before drafting.

### Step 5 — Write the register
Append rows to [TOR_Requirements](../../registers/TOR_Requirements.md) using the
register-write pattern (read → dedup by `tor_id`+`req_id` → append → update Statistics →
write back to Drive). If Drive is not connected, output the table and ask the user to paste it.

## Output Format

```
## Compliance Matrix — [Project] (tor_id)
**Total requirements:** [N]  |  **Mandatory:** [N]  |  **Scored:** [N]

| req_id | section | requirement | type | mand. | weight | owner | evidence | status | risk |
|---|---|---|---|---|---|---|---|---|---|
| REQ-001 | ... | ... | legal | yes | — | Admin | Company_Documents#affidavit | open | 🟢 |

### 🔴 Blockers (must resolve before drafting)
1. [req_id] — [why it blocks] — owner: [who]

### Coverage
- Mandatory with evidence: [N]/[N]
- Scored criteria handed to roots-scoring-matrix: [N]
- **G2 Matrix Freeze:** PASS ✅ / NOT YET ❌ — [reason]

### Next step
→ Run `roots-scoring-matrix` for the [N] scored criteria
→ Run `roots-evidence-matcher` to fill "Needs human review" evidence
→ Drafting unlocks only after G2 PASS
```

## Roots-Specific Notes
- Never paraphrase a mandatory requirement so loosely that compliance becomes ambiguous.
- Government bids: every เอกสาร that must be signed/stamped is its own row (so the
  `roots-submission-packager` can track signature/stamp status later).
- If the TOR is unreadable in places (scanned/poor OCR), mark those rows `Needs human
  review` rather than guessing — flag the count clearly.
- This skill does not decide Go/No-Go — that's `roots-tor-analyzer`. It assumes GO.
- Cross-reference CONTEXT.md for Roots qualifications when setting `risk`.
