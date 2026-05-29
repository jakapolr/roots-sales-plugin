# CONTEXT.md — Roots Company Context

This file is loaded automatically by Claude for every session using this plugin.
It provides Roots-specific context so skills produce relevant, accurate output.

---

## Company

**Trinity Roots Co., Ltd. (Roots.Tech)**
- Location: Bangkok, Thailand
- Founded: 2013 (12 years operating)
- Size: 50–100 staff
- Core business: Odoo ERP implementation for Thai and Southeast Asian companies
- SaaS product: BEECY.co (Thai-localized Odoo)
- Website: roots.tech

---

## Ideal Customer Profile (ICP)

**Primary targets:**
- Thai manufacturing companies (food, sugar, industrial)
- Mid-market: 50–500 employees
- No ERP or replacing legacy system (SAP, Oracle, custom)
- Decision maker: CFO, CEO, IT Director, Operations Director
- Budget signal: THB 500K–5M project range

**Industry verticals (strongest):**
- Food & beverage manufacturing
- Sugar and agri-processing
- Distribution and logistics
- Professional services

**Geography:** Thailand primary, SEA secondary (Vietnam, Indonesia)

---

## Products & Services

| Offering | Description | Typical Price |
|---|---|---|
| Odoo Enterprise Implementation | Full ERP rollout, Waterfall | THB 500K–3M |
| Odoo Community + BEECY | Localized, cost-effective option | THB 300K–1.5M |
| BEECY SaaS Subscription | Monthly recurring, hosted | THB 3K–15K/month |
| Support & Maintenance | Post-go-live contract | THB 20K–80K/month |
| Government Procurement (e-GP) | ERP/IT system bids | THB 1M–10M+ |

---

## Rate Card (Internal Reference)

| Role | Daily Rate (THB) | Typical Allocation |
|---|---|---|
| Solution Architect / Senior SE | 6,000–8,000 | Discovery, GAP, architecture |
| Odoo Consultant / SE | 4,000–6,000 | Configuration, training |
| Project Manager | 5,000–7,000 | Planning, client coordination |
| Developer | 4,500–6,500 | Custom module dev |
| QA / Tester | 3,000–4,000 | UAT, test execution |

**Blended average for estimates:** THB 5,000/day
**Margin target:** 35–45% gross

---

## Sales Team

| Role | Name | Responsibility |
|---|---|---|
| Sales Director / CSO | Jack | Strategy, key accounts, deals >THB 2M |
| Sales Team Lead / Revenue Lead | Fern | Pipeline management, AE coaching |
| Growth Lead | Pan | New business, outbound |
| BEECY Growth Lead | Neung | SaaS pipeline |
| AI Ops Coordinator | Petch | Tools, automation, plugin support |

---

## Competitive Positioning

**vs. SAP / Oracle:** Roots wins on cost (10–20x cheaper), implementation speed (3–6 months vs 12–24), and Thai support
**vs. local custom dev:** Roots wins on reliability, upgrade path, and total cost of ownership
**vs. other Odoo partners:** Roots wins on BEECY localization, manufacturing expertise, and 12-year track record

**Key differentiators:**
- Only Odoo partner with dedicated Thai manufacturing vertical
- BEECY handles Thai-specific: VAT/WHT, e-Tax invoice, Thai payroll, Thai address format
- Sugar/food industry domain expertise (founder family background)
- BNV climate-tech network for ESG-adjacent manufacturing clients

---

## Communication Style

**Email tone:** Professional but approachable. Thai clients expect relationship-first communication. Lead with value, not features.
**Language:** Thai for SME clients, English for MNC / international clients, mix for bilingual contacts.
**Follow-up cadence:** 3 business days after proposal, 1 week if no response, 2 weeks final.

---

## Odoo Version

Current deployment: **Odoo 18** (Enterprise and Community)
BEECY: Based on Odoo 18 Community with Thai localization modules
Previous projects: Odoo 14, 16, 17 — migration experience available

---

## Notes for Skills

- When estimating Manday, default to blended rate of THB 5,000/day
- GAP Analysis should always show both Odoo Enterprise AND Community options (BEECY = Community path)
- For government bids (e-GP): formal Thai language required, reference past government project experience
- All proposals in THB unless client is MNC (then USD or SGD)
- SRS format: follow Roots Waterfall template (phases: Analysis → Design → Build → Test → Go-live → Support)

---

## TOR Response Factory

**Register location (Google Drive):** `8. Sales and Marketing/TOR/registers/`

Ten registers maintain the data backbone for all government bids:
TOR_Opportunities · TOR_Requirements · Scoring_Matrix · Company_Documents ·
CV_Master · Evidence_Library · LC_Bank_Facility · Submission_Checklist · Review_Log · Lessons_Learned

**Gate sequence:** G0 Intake → G1 Bid/No-Bid → G2 Matrix Freeze → G3 Draft → G4 QA → G5 Lock → G6 Lessons

**Critical rule (factory discipline):**
Do not draft the proposal until both the compliance matrix AND scoring matrix are complete
and frozen (G2 PASS). This is the single rule that prevents losing on a missed mandatory
item or uncovered scoring criterion.

**Never fabricate:** If a requirement is unreadable or evidence is unknown, mark it
"Needs human review" — never guess or invent. This applies to all TOR factory skills.

**KPI targets:**
- TOR intake to first summary: < 2 hours
- Compliance matrix before drafting: 100% of TORs
- Company documents valid at submission: 95%+
- Team CVs updated within 90 days: 90%+
- High-severity QA issues before lock: zero
