---
name: roots-manday-estimator
description: "Estimate Mandays and project cost in THB when the user asks for a project estimate, implementation cost, or proposal pricing for an Odoo project."
version: 1.0.0
source: roots-custom
phase: 2
---

# Roots Manday Estimator

> **Custom Skill** — Built by Roots.Tech
> **Rate card and complexity model based on Roots historical projects**

## Trigger
Use when:
- User asks "how many mandays for [scope]?"
- User is preparing a proposal and needs cost estimate
- User asks "what should we quote for [client]?"

## Input Required
1. **Modules** — which Odoo modules? (Manufacturing, Inventory, Accounting, HR, Sales, Purchase, CRM, Website)
2. **Users** — number of concurrent users
3. **Customization level** — standard config / moderate custom / heavy custom
4. **Data migration** — yes/no, how many records?
5. **Training** — number of staff, sessions needed
6. **Timeline pressure** — normal (3–6 months) / fast (< 3 months)?

## Complexity Scoring

### Per-Module Base Mandays

| Module | Simple Config | Moderate Custom | Heavy Custom |
|---|---|---|---|
| Sales / CRM | 5 | 10 | 18 |
| Purchase | 4 | 8 | 14 |
| Inventory | 6 | 12 | 20 |
| Accounting | 8 | 15 | 25 |
| Manufacturing (MO + BoM) | 10 | 20 | 35 |
| Manufacturing + MPS | 15 | 28 | 45 |
| HR + Payroll (Thai) | 8 | 14 | 22 |
| Website / eCommerce | 6 | 12 | 20 |
| BEECY Thai Localization | 3 | 6 | 10 |

### Add-On Factors

| Factor | Add Mandays |
|---|---|
| Data migration < 10K records | +5 |
| Data migration 10K–100K records | +10 |
| Data migration > 100K records | +20 |
| Integration (per external system) | +8–15 |
| Training (per 10 staff) | +3 |
| Project Management | +15% of total |
| UAT support | +10% of total |
| Timeline pressure (< 3 months) | +20% of total |

### Complexity Classifier

**Simple Config:** Standard module with minimal field customization, no custom workflows
**Moderate Custom:** 3–5 custom reports, 2–3 custom workflows, some field additions
**Heavy Custom:** Major workflow changes, complex approval chains, external integrations, industry-specific logic

## Calculation

```
Base Mandays = SUM(module base mandays × complexity multiplier)
Add-ons = migration + integrations + training + PM + UAT
Timeline adjustment = if fast, ×1.2
Total Mandays = Base + Add-ons × Timeline adjustment

Cost = Total Mandays × THB 5,000 (blended rate)
Sell price = Cost ÷ (1 - margin%)
  → Standard margin: 40%
  → Competitive bid: 35%
  → Premium/complex: 45%
```

## Output Format

```
## Manday Estimate — [Client Name / Project]

### Scope Summary
Modules: | Users: | Complexity: | Timeline:

### Manday Breakdown
| Component | Mandays | Notes |
|---|---|---|
| [Module 1] | X | Moderate custom |
| [Module 2] | X | Standard config |
| Data Migration | X | ~50K records |
| PM | X | 15% of base |
| UAT Support | X | 10% of base |
| **TOTAL** | **X** | |

### Cost
| | Conservative | Target | Stretch |
|---|---|---|---|
| Mandays | X | X | X |
| Cost (40% margin) | THB X | THB X | THB X |
| Suggested Quote | **THB X** | **THB X** | **THB X** |

### Timeline
Estimated duration: X months (X sprints of 2 weeks)

### Assumptions
- [Assumption 1]
- [Assumption 2]

### Risks to Estimate
- [Risk that could increase mandays]
```

## Roots Notes
- Always show 3 scenarios: Conservative / Target / Stretch
- Round to nearest THB 50,000 on final quote
- For e-GP government bids: add 25% buffer — government projects always run over
- BEECY path typically 20–30% less mandays than Enterprise (less complex localization work)
