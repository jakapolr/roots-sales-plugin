---
description: Review your sales pipeline — deal health, prioritization, and next actions
argument-hint: "<optional: stage or rep filter>"
---

# /roots:pipeline-review

Review your sales pipeline — deal health, prioritization, and next actions.

## Usage

```
/roots:pipeline-review
```

Paste your current deals (from Odoo CRM or manual list), or describe your pipeline verbally.
If ~~crm (Odoo MCP) is connected, Claude will pull data automatically.

## What Claude will do

1. **Score each deal** by: stage, days since last activity, deal size, close probability
2. **Flag at-risk deals** — no activity >14 days, stuck in same stage >30 days
3. **Prioritize** — which deals to focus on this week
4. **Forecast** — weighted revenue this quarter
5. **Recommend next actions** — specific action for each top deal

## Output

```
## Pipeline Review — [Date]

### Summary
Active deals: X | Total pipeline: THB X | Weighted forecast: THB X

### Deal Scorecard
| Deal | Stage | Value | Days Active | Health | Priority | Next Action |
|---|---|---|---|---|---|---|

### At-Risk Deals
[Deals needing immediate attention]

### This Week's Focus (Top 3)
1. [Deal] — [Action] by [date]
2. [Deal] — [Action] by [date]
3. [Deal] — [Action] by [date]

### Forecast
Q[X] Committed: THB X
Q[X] Likely: THB X
Q[X] Upside: THB X
```
