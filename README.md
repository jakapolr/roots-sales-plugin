# roots-sales-plugin

Sales productivity plugin for **Roots.Tech** — Thai Odoo ERP implementation firm.

Based on [Anthropic's official sales plugin](https://github.com/anthropics/knowledge-work-plugins/tree/main/sales), extended with:
- Odoo-specific skills (GAP analysis, Manday estimation, TOR analysis, bid prep)
- Thai market context and government procurement support
- Google Workspace connectors (Drive, Gmail, Calendar)
- PM skills for requirements and SRS documentation
- 4 sub-agents for SE work, MOM writing, proposal review, and PM handoff

## Install

```bash
# Add Roots plugin marketplace
claude plugin marketplace add roots-tech/roots-sales-plugin

# Install this plugin
claude plugin install sales@roots-sales-plugin
```

## Structure

```
roots-sales-plugin/
├── .claude-plugin/
│   ├── plugin.json              # Plugin manifest (name: sales, v1.5.0)
│   └── marketplace.json         # Marketplace registration
├── .mcp.json                    # Google Workspace connectors (3 active)
├── CONTEXT.md                   # Roots company context (auto-loaded)
├── CONNECTORS.md                # Tool stack documentation
├── README.md                    # This file
├── meeting-registry.md          # Central meeting index (template)
│
├── skills/                      # 19 skills
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
│   └── [CUSTOM — Roots-specific]
│       ├── sales-help/              # Navigator — routes user to right tool
│       ├── odoo-gap-analysis/       # Enterprise vs Community GAP
│       ├── roots-manday-estimator/  # Project cost estimation
│       ├── roots-tor-analyzer/      # Government TOR PDF analysis
│       └── roots-bid-prep/          # Bid qualification & documents
│
├── agents/                      # 4 sub-agents
│   ├── se-orchestrator.md           # AI Sales Engineer (5 modes)
│   ├── mom-writer.md                # MOM + registry + follow-up email
│   ├── proposal-reviewer.md         # Quality gate before sending (read-only)
│   └── pm-handoff.md                # Sales → PM/Delivery handoff
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

## Components

| Type | Count | Notes |
|---|---|---|
| Skills | 19 | 8 upstream + 5 pm-skills + 6 custom |
| Sub-agents | 4 | se-orchestrator, mom-writer, proposal-reviewer, pm-handoff |
| Commands | 2 | /roots:pipeline-review, /roots:meeting-search |
| MCP connectors | 3 active | Google Drive, Gmail, Calendar |

## Phases

| Phase | Status | Scope |
|---|---|---|
| 1 | ✅ Ready | All 19 skills, 4 agents, 2 commands, Google Workspace MCP, meeting registry |
| 2 | 🔧 Planned | Odoo CRM MCP, Fireflies transcript connector |
| 3 | ⏳ Planned | e-GP monitor, BEECY localization skill, team marketplace rollout |

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
claude plugin marketplace add roots-tech/roots-sales-plugin
claude plugin install sales@roots-sales-plugin
```

## Attribution

- Upstream sales skills: Apache 2.0 © Anthropic ([source](https://github.com/anthropics/knowledge-work-plugins))
- PM skills: Apache 2.0 © product-on-purpose ([source](https://github.com/product-on-purpose/pm-skills))
- Roots custom skills, agents, commands: Proprietary © Trinity Roots Co., Ltd.
