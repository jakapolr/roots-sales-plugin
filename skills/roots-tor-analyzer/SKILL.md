---
name: roots-tor-analyzer
description: "Analyze a TOR (Terms of Reference) PDF from Thai government procurement when the user uploads or pastes TOR content and asks about requirements, qualifications, or whether to bid. Feeds the compliance and scoring matrices and acts as the G1 gate before bid preparation begins."
version: 1.1.0
source: roots-custom
phase: 2
---

# TOR Analyzer — Thai Government Procurement

> **Custom Skill** — Built by Roots.Tech
> **For:** e-GP (gprocurement.go.th) TOR documents

## Trigger
Use when:
- User uploads a PDF TOR document
- User pastes TOR content and asks "should we bid on this?"
- User asks about TOR requirements, qualifications, or deadline
- User mentions กรม, กระทรวง, มหาวิทยาลัย, หน่วยงาน + ERP/IT system

## Input
- PDF or text of TOR document
- (Optional) Roots current qualifications for comparison

## Extraction Process

### Step 0 — OCR / Text Extraction

Use the PDF Tools MCP (`mcp__PDF_Tools_-_Fill__Sign__Merge__Split__Extract__read_pdf_content` or equivalent) to extract text from the TOR PDF before any analysis begins.

- If the PDF is text-searchable, extract the text directly.
- If the PDF is scanned (image-based), use OCR to obtain the text.
- For any section where the OCR output is unclear, ambiguous, or unreadable, mark it explicitly as **"Needs human review"** — never guess at or infer unreadable text.
- Proceed to Step 1 only after extraction is complete and all unclear sections are flagged.

### Step 1 — Basic Information
Extract:
- Project title (ชื่อโครงการ)
- Agency (หน่วยงาน)
- Budget ceiling (วงเงิน)
- Submission deadline (วันยื่นซอง)
- Opening date (วันเปิดซอง)
- Contract period (ระยะเวลาสัญญา)
- Procurement method (e-Bidding / e-Auction / วิธีเฉพาะเจาะจง)

### Step 2 — Technical Requirements
Extract all technical specifications:
- Software requirements (ERP modules, features)
- Hardware/infrastructure requirements
- Integration requirements
- Performance/SLA requirements
- Training requirements
- Warranty/support period

### Step 3 — Qualification Requirements
Extract mandatory qualifications:
- Company type (นิติบุคคล requirements)
- Years of experience (อายุบริษัท / ประสบการณ์)
- Past project references required (จำนวนโครงการ / มูลค่า)
- Financial statements (งบการเงิน — ยอดรายได้ขั้นต่ำ)
- Technical staff qualifications (CV requirements)
- Certifications required (ISO, CMMI, etc.)
- Partnership/licensing requirements (Odoo Partner?)

### Step 4 — Risk Flag Assessment

Rate each clause:
- 🟢 **OK** — Standard, Roots can comply
- 🟡 **WARN** — Possible issue, needs verification
- 🔴 **RISK** — Potential disqualifier or major concern

Common risk flags to check:
- Minimum revenue threshold too high
- Reference project minimum value > Roots' past projects
- Unrealistic timeline (< 6 months for full ERP)
- Penalty clauses > 10% of contract value
- Requirement for specific software brand (not Odoo)
- Requirement for server room / hardware (Roots is software-only)
- Mandatory Thai citizen staff percentage
- Bond/guarantee requirements

### Step 5 — Roots Fit Scoring

Score 1–10 on:
- **Technical fit** — Can Roots deliver the technical scope?
- **Qualification fit** — Does Roots meet all mandatory qualifications?
- **Competitive position** — Is this winnable against competitors?
- **Commercial fit** — Is the budget viable for the scope?

**Overall Go/No-Go threshold:** Average score ≥ 7 → Bid. Below 7 → No-go or discuss.

### Step 6 — Feed to Factory

After scoring, determine the bid decision and instruct the user on next steps:

**If `bid_decision = GO`:**
1. If `roots-tor-intake` has not yet been run for this `tor_id`, run it first to register the opportunity in the system.
2. Then run `roots-compliance-matrix` to generate the compliance requirements table.
3. Then run `roots-scoring-matrix` to generate the weighted scoring table.
4. The `tor-factory-orchestrator` will manage subsequent gates automatically — do not skip ahead.

**If `bid_decision = NO-GO`:**
- Document the reason in the TOR record.
- No further factory steps are required unless the decision is escalated and reversed.

**If `bid_decision = CONDITIONAL`:**
- Resolve the flagged conditions with the relevant owner before proceeding.
- Re-run this analyzer after conditions are resolved to confirm GO status.

## Output Format

```
## TOR Analysis — [Project Title]
**Agency:** | **Budget:** | **Deadline:** | **Method:**

### Go / No-Go Recommendation
**Decision: GO ✅ / NO-GO ❌ / CONDITIONAL ⚠️**
**Reason:** [1-2 sentences]

### Fit Scores
| Dimension | Score | Notes |
|---|---|---|
| Technical fit | /10 | |
| Qualification fit | /10 | |
| Competitive position | /10 | |
| Commercial fit | /10 | |
| **Overall** | **/10** | |

### Key Requirements
| Requirement | Details | Roots Status |
|---|---|---|
| [Req 1] | [Detail] | 🟢 OK / 🟡 WARN / 🔴 RISK |

### Qualification Checklist
| Qualification | Required | Roots Has | Status |
|---|---|---|---|
| Years in business | X years | 12 years | 🟢 |
| Min revenue | THB X | [check] | 🟡 |
| Reference projects | X projects > THB X | [verify] | ? |

### Risk Flags
🔴 **[Critical Issue]:** [Description]
🟡 **[Warning]:** [Description]

### Document Checklist (if bidding)
- [ ] หนังสือรับรองบริษัท (ไม่เกิน 6 เดือน)
- [ ] งบการเงิน 3 ปีล่าสุด
- [ ] บัญชีรายชื่อผู้ถือหุ้น
- [ ] Reference projects with client letters
- [ ] CV ของผู้รับผิดชอบโครงการ
- [ ] [Additional items from TOR]

### Next Actions
- [ ] [Action 1 by whom]
- [ ] [Action 2 by when]

### Factory Next Steps
<!-- Based on the Go/No-Go decision above -->

**If GO:**
- [ ] Run `roots-tor-intake` for tor_id [TOR_ID] (if not already done)
- [ ] Run `roots-compliance-matrix` — generates compliance requirements table
- [ ] Run `roots-scoring-matrix` — generates weighted scoring table
- Gate management continues via `tor-factory-orchestrator`

**If NO-GO:**
- [ ] Log decision and reason in TOR record — no further factory steps required

**If CONDITIONAL:**
- [ ] Resolve flagged conditions with owner: [list conditions]
- [ ] Re-run `roots-tor-analyzer` after resolution to confirm GO before proceeding
```

## Notes
- Always cross-reference with CONTEXT.md for Roots current qualifications
- If financial threshold unclear — flag for Director review before deciding
- Government projects: add 25% manday buffer in estimate
- e-GP method: e-Bidding = open competitive, วิธีเฉพาะเจาะจง = sole source (easier to win)
