# TOR Response Factory — Register Framework

> **Convention for all Roots TOR data registers.**
> Generalizes the proven [meeting-registry.md](../meeting-registry.md) pattern to the
> ten master tables of the TOR Response Factory.

These registers are the **data backbone** of the TOR Response Factory. The plugin's
skills and agents are the *brain*; these markdown registers (hosted in Google Drive)
are the *memory*. Every TOR skill reads from and writes back to one or more registers.

---

## Where registers live

| Environment | Location |
|---|---|
| **Production** | Google Drive → `8. Sales and Marketing/TOR/registers/` |
| **Repo (this folder)** | Seed/templates — copied to Drive on first setup |

The repo copy is the **template and schema reference**. The live copy in Drive is the
one skills read/write through the Google Drive MCP (`~~cloud-storage`).

---

## The register convention (every register follows this)

1. **Header block** — file location, maintained-by, purpose.
2. **How to use** — who reads, who writes, dedup rule if any.
3. **Registry table** — the data, one row per record, append-only.
4. **Field reference** — every column defined with an example.
5. **Statistics block** — auto-updated by the owning skill on each write.

**Rules (apply to all registers):**
- Skills/agents maintain registers — humans add notes only in a `notes` column.
- Append-only. Never rewrite history; supersede with a new row + status change.
- IDs are sequential and human-readable (e.g. `TOR-2026-001`, `REQ-001`).
- Dates: `YYYY-MM-DD` in tables and filenames; `DD/MM/YYYY` only in display prose.
- Money in THB unless the buyer is MNC.
- **Never fabricate.** If a value is unknown, write `Needs human review` — never guess.
- Cross-link by ID across registers (a requirement row references its `tor_id`).

---

## The ten registers

| Register | Owning skill / agent | Purpose |
|---|---|---|
| [TOR_Opportunities](TOR_Opportunities.md) | `roots-tor-intake` | Pipeline of all TORs — buyer, deadline, owner, bid/no-bid status |
| [TOR_Requirements](TOR_Requirements.md) | `roots-compliance-matrix` | **Compliance matrix** — requirement→type→owner→evidence→status |
| [Scoring_Matrix](Scoring_Matrix.md) | `roots-scoring-matrix` | Evaluation criteria→response angle→evidence→slide→risk |
| [Company_Documents](Company_Documents.md) | `roots-doc-freshness` | Document freshness — issue/expiry, latest approved file |
| [CV_Master](CV_Master.md) | `roots-cv-builder` | Role-based CV data + approval status |
| [Evidence_Library](Evidence_Library.md) | `roots-evidence-matcher` | Reusable project references, certs, case studies |
| [LC_Bank_Facility](LC_Bank_Facility.md) | `roots-lc-check` | Facility limit, usage, remaining capacity, expiry |
| [Submission_Checklist](Submission_Checklist.md) | `roots-submission-packager` | Per-bid file checklist — signed/stamped/uploaded status |
| [Review_Log](Review_Log.md) | `tor-qa-reviewer` | QA issues — severity, owner, resolution, final approver |
| [Lessons_Learned](Lessons_Learned.md) | `roots-lessons-learned` | Win/loss reason, score, reusable improvement |

---

## Review gates (G0–G6)

Registers carry the bid through the gate sequence. The `tor-factory-orchestrator`
enforces the gates; the **critical gate is G2** — no proposal drafting before the
compliance + scoring matrices are complete.

| Gate | Timing | Owner | Pass criteria | Register touched |
|---|---|---|---|---|
| G0 Intake | Day received | Sales Lead | TOR registered, deadline known | TOR_Opportunities |
| G1 Bid/No-Bid | T-7 to T-14 | Executive | Fit, capacity, LC, profitability OK | TOR_Opportunities, LC_Bank_Facility |
| G2 Matrix Freeze | Before drafting | Sales + Tech | **All criteria captured & assigned** | TOR_Requirements, Scoring_Matrix |
| G3 Draft Review | Midpoint | Sales + Tech | Proposal covers all key criteria | Evidence_Library, CV_Master |
| G4 QA Review | T-2 | QA Owner | No high-severity issues open | Review_Log, Submission_Checklist |
| G5 Submission Lock | T-1 | Executive | Final folder approved & locked | Submission_Checklist |
| G6 Lessons Learned | After result | Sales Lead | Win/loss reason captured | Lessons_Learned |

---

## Adding a register row (pattern for skills)

1. Read the live register from Drive (`~~cloud-storage`).
2. If the register has a dedup key (e.g. `tor_id`), check for an existing row first.
3. Compute the next sequential ID.
4. Append the new row to the table.
5. Update the Statistics block (count, date range, last-updated).
6. Write the file back to Drive. If Drive is not connected, output the new row and
   ask the user to paste it into their local copy.
