# roots-sales-plugin

Sales productivity plugin for **Roots.Tech** — Thai Odoo ERP implementation firm.

Based on [Anthropic's official sales plugin](https://github.com/anthropics/knowledge-work-plugins/tree/main/sales), extended with:
- Odoo-specific skills (GAP analysis, Manday estimation, TOR analysis, bid prep)
- **Live Odoo CE integration** (CRM pipeline sync, sales order reports via odoorpc-cli)
- Thai market context and government procurement support
- Google Workspace connectors (Drive, Gmail, Calendar)
- PM skills for requirements and SRS documentation
- 6 sub-agents for SE work, MOM writing, proposal review, PM handoff, and TOR factory orchestration

## Install

```bash
# Add Roots plugin marketplace
claude plugin marketplace add jakapolr/roots-sales-plugin

# Install this plugin
claude plugin install sales@roots-sales-plugin
```

## Structure

```
roots-sales-plugin/
├── .claude-plugin/
│   ├── plugin.json              # Plugin manifest (name: sales, v3.2.0)
│   └── marketplace.json         # Marketplace registration
├── .mcp.json                    # Google Workspace connectors (3 active)
├── CONTEXT.md                   # Roots company context (auto-loaded)
├── CONNECTORS.md                # Tool stack documentation
├── README.md                    # This file
├── meeting-registry.md          # Central meeting index (template)
│
├── skills/                      # 32 skills
│   ├── [FROM UPSTREAM — anthropics/knowledge-work-plugins/sales]
│   │   ├── account-research/        # Company research
│   │   ├── call-prep/               # Meeting preparation
│   │   ├── call-summary/            # MOM from transcript
│   │   ├── competitive-intelligence/ # Competitor analysis
│   │   ├── create-an-asset/         # Sales materials
│   │   ├── daily-briefing/          # Morning summary
│   │   ├── draft-outreach/          # Email writing
│   │   ├── forecast/                # Pipeline forecast
│   │   └── pipeline-review/         # Deal review
│   │
│   ├── [FROM pm-skills — product-on-purpose/pm-skills]
│   │   ├── meeting-synthesize/       # Multi-meeting synthesis
│   │   ├── prd/                     # SRS / requirements doc
│   │   ├── user-stories/            # Task breakdown
│   │   ├── acceptance-criteria/     # Test cases
│   │   └── lean-canvas/             # Project fit analysis
│   │
│   ├── [CUSTOM — Roots-specific]
│   │   ├── sales-help/              # Navigator — routes user to right tool
│   │   ├── odoo-gap-analysis/       # Enterprise vs Community GAP
│   │   ├── roots-manday-estimator/  # Project cost estimation
│   │   ├── roots-tor-analyzer/      # Government TOR PDF analysis
│   │   └── roots-bid-prep/          # Bid qualification & documents
│   │
│   ├── [ODOO CRM INTEGRATION — v3.1.0 / v3.2.0]
│   │   ├── odoorpc-cli/             # Odoo JSON-RPC CLI wrapper (upstream: biszx/odoorpc-cli)
│   │   ├── odoo-crm-sync/           # Pull live CRM pipeline from Odoo CE (crm.lead)
│   │   ├── odoo-sales-report/       # Pull confirmed sale orders, revenue summary (sale.order)
│   │   └── roots-sales-dashboard/   # 3-mode live dashboard: strategic / month-close / intelligence
│   │
│   └── [TOR RESPONSE FACTORY — Phase 3 Custom]
│       ├── roots-tor-intake/         # Register a new TOR: Drive folder, calendar gates (G0)
│       ├── roots-compliance-matrix/  # Decompose TOR into row-level compliance matrix (G2)
│       ├── roots-scoring-matrix/     # Map evaluation criteria to weighted response strategy
│       ├── roots-evidence-matcher/   # Match TOR requirements to Evidence_Library entries
│       ├── roots-doc-freshness/      # Check company/eligibility document expiry dates
│       ├── roots-lc-check/           # Verify bank guarantee / LC facility availability
│       ├── roots-cv-builder/         # Generate standardized tender CVs for bid team
│       ├── roots-submission-packager/ # Assemble and lock the final submission package (G5)
│       └── roots-lessons-learned/    # Record win/loss result and lessons in register (G6)
│
├── agents/                      # 6 sub-agents
│   ├── se-orchestrator.md           # AI Sales Engineer (5 modes)
│   ├── mom-writer.md                # MOM + registry + follow-up email
│   ├── proposal-reviewer.md         # Quality gate before sending (read-only)
│   ├── pm-handoff.md                # Sales → PM/Delivery handoff
│   ├── tor-factory-orchestrator.md  # Orchestrates G0–G6 TOR pipeline across all factory skills
│   └── tor-qa-reviewer.md           # QA gate agent: checks compliance matrix & scoring coverage
│
├── registers/                   # 10 data registers (TOR Response Factory)
│   ├── TOR_Opportunities.md         # Master pipeline of every TOR — index all other registers link to
│   ├── TOR_Requirements.md          # Compliance matrix — every TOR requirement as a trackable row
│   ├── Scoring_Matrix.md            # Weighted scoring plan: criteria → response angle → evidence → owner
│   ├── Evidence_Library.md          # Reusable proof library: past projects, client letters, certificates
│   ├── Company_Documents.md         # Freshness control for company/eligibility documents
│   ├── LC_Bank_Facility.md          # Bank guarantee / LC facility capacity tracker
│   ├── CV_Master.md                 # Role-based CV data for tender team scoring
│   ├── Submission_Checklist.md      # Per-bid file checklist tracking physical submission state
│   ├── Review_Log.md                # QA issue tracker: severity, owner, deadline, resolution
│   └── Lessons_Learned.md           # Win/loss capture for every submitted bid (G6)
│
├── commands/                    # 2 slash commands
│   ├── pipeline-review.md           # /roots:pipeline-review
│   └── meeting-search.md            # /roots:meeting-search
│
└── docs/
    └── skill-template/          # Template for creating new custom skills
        ├── TEMPLATE.md              # Copy to skills/ and rename to SKILL.md
        └── README.md                # How to use the template
```

## Registers

Ten data registers live in `registers/` and serve as the shared state layer for the TOR Response Factory. Each register is owned by a specific skill and synced to Google Drive.

| Register | Purpose |
|---|---|
| `TOR_Opportunities.md` | Master pipeline of every TOR opportunity — the primary index all other registers link to via `tor_id` |
| `TOR_Requirements.md` | Compliance matrix — every TOR requirement as a row with owner, evidence link, and status |
| `Scoring_Matrix.md` | Weighted scoring plan mapping evaluation criteria to response angle, evidence, owner, and deck slide |
| `Evidence_Library.md` | Reusable proof library of past project references, client letters, awards, and certificates |
| `Company_Documents.md` | Freshness control for all company/eligibility documents so expired docs never block a submission |
| `LC_Bank_Facility.md` | Bank guarantee / LC facility capacity tracker ensuring a bid is never blocked at signing |
| `CV_Master.md` | Role-based CV data for tender team scoring, tracking staff qualifications per TOR role |
| `Submission_Checklist.md` | Per-bid file-level checklist tracking the physical submission state of every required document |
| `Review_Log.md` | QA issue tracker recording every review finding with severity, owner, deadline, and resolution |
| `Lessons_Learned.md` | Win/loss capture for every submitted bid (G6) to improve future scoring and strategy |

## Components

| Type | Count | Notes |
|---|---|---|
| Skills | 32 | 8 upstream + 5 pm-skills + 6 custom + 9 TOR factory + 4 Odoo CRM |
| Sub-agents | 6 | se-orchestrator, mom-writer, proposal-reviewer, pm-handoff, tor-factory-orchestrator, tor-qa-reviewer |
| Commands | 2 | /roots:pipeline-review, /roots:meeting-search |
| MCP connectors | 3 active | Google Drive, Gmail, Calendar |

## Phases

| Phase | Status | Scope |
|---|---|---|
| 1 | ✅ Ready | 19 skills, 4 agents, 2 commands, Google Workspace MCP, meeting registry |
| 2 | ✅ Ready | Odoo CE CRM integration — 4 skills (odoorpc-cli, odoo-crm-sync, odoo-sales-report, roots-sales-dashboard) via CLI connector |
| 3 | ✅ Ready | TOR Response Factory — 9 skills + 2 agents + 10 registers, G0–G6 gate-enforced pipeline |
| 4 | ⏳ Planned | Odoo MCP server (HTTP), Fireflies transcript connector, e-GP monitor |

## Updating

### When Anthropic releases a new upstream version
```bash
# Compare upstream skill against local copy
git diff upstream/main -- sales/skills/account-research/SKILL.md

# Copy updated skill if relevant
cp upstream/sales/skills/account-research/SKILL.md skills/account-research/SKILL.md

# Reload
/reload-plugins
```

### When adding a new skill
```bash
# Copy the template from docs/ into skills/
cp -r docs/skill-template skills/my-new-skill
mv skills/my-new-skill/TEMPLATE.md skills/my-new-skill/SKILL.md
# Edit SKILL.md — frontmatter 'name' must match the folder name
/reload-plugins
```

### When adding a new team member
```bash
# Share the GitHub repo, then they run:
claude plugin marketplace add jakapolr/roots-sales-plugin
claude plugin install sales@roots-sales-plugin
```

## Attribution

- Upstream sales skills: Apache 2.0 © Anthropic ([source](https://github.com/anthropics/knowledge-work-plugins))
- PM skills: Apache 2.0 © product-on-purpose ([source](https://github.com/product-on-purpose/pm-skills))
- Roots custom skills, agents, commands: Proprietary © Trinity Roots Co., Ltd.
