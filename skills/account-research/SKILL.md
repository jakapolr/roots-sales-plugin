---
name: account-research
description: "Automatically research a company or person when the user mentions a prospect, lead, or client they want to learn about before engaging."
version: 1.0.0
source: upstream — anthropics/knowledge-work-plugins/sales
---

# Account Research

> **Source:** Copied from [anthropics/knowledge-work-plugins/sales](https://github.com/anthropics/knowledge-work-plugins/tree/main/sales/skills/account-research)
> **Roots additions:** Thai company research sources, Odoo adoption signals, BOI-registered company lookup

## Purpose
Research a company or person — web search for company intel, key contacts, recent news, hiring signals, and financial health — to prepare for outreach or a call.

## Trigger
Use when the user mentions a prospect, client, or company they want to learn about, or when preparing for a call or meeting.

## Process

### Step 1 — Company Overview
Search for: company name + Thailand (or country), industry, size, founding year, ownership structure.
Check: DBD (Department of Business Development) registration if Thai company.

### Step 2 — Recent News & Signals
Search for: company news last 6 months, executive changes, expansion plans, funding, pain points mentioned in press.
Odoo adoption signal: look for job postings mentioning ERP, SAP, or system migration.

### Step 3 — Key Contacts
Identify: CEO, CFO, IT Director, Operations Director — the likely ERP decision makers.
Source: LinkedIn, company website, news articles.

### Step 4 — Competitive Context
What ERP/systems are they likely using now?
What pain points does their industry typically have?

### Step 5 — Roots Fit Assessment
Based on CONTEXT.md ICP criteria:
- Industry match (manufacturing, food, sugar?)
- Size match (50–500 employees?)
- Budget signal (project likely THB 500K+?)
- Relationship entry point available?

## Output Format

```
## [Company Name] — Account Brief
**Industry:** | **Size:** | **Location:**
**Current Systems:** (if known)
**Roots Fit Score:** /10

### Key Contacts
| Name | Role | LinkedIn |

### Recent Signals
- [Signal 1]
- [Signal 2]

### Recommended Approach
[How to open the conversation]

### Questions to Ask
1.
2.
3.
```

## Google Drive Integration
If ~~cloud-storage (Google Drive) is connected: save brief to `/Sales/Prospects/[CompanyName]/account-brief.md`
