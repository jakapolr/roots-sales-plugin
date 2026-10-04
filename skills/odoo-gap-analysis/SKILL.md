---
name: odoo-gap-analysis
description: "Generate a structured GAP analysis comparing Odoo options (Enterprise, BEECY SaaS, and Community implementation) when the user asks which Odoo path to recommend for a client, or when preparing a proposal."
version: 1.1.0
source: roots-custom
phase: 2
---

# Odoo GAP Analysis — Enterprise vs BEECY SaaS vs Community Implementation

> **Custom Skill** — Built by Roots.Tech
> **Purpose:** Replace manual, inconsistent GAP analysis with a structured, repeatable output

> **Editions/hosting/BEECY definitions:** always follow [references/odoo-editions.md](../../references/odoo-editions.md).
> Three distinct paths — do NOT collapse to "Enterprise vs Community":
> - **Enterprise** — licensed, all apps, Studio/Payroll/advanced MFG, hosted options
> - **BEECY SaaS** — Community + Thai localization, hosted by Roots, **standard (no custom modules)**, subscription
> - **Community Implementation** — Roots custom project on Community (full customization, customer-owned)
> Pick which paths are realistic for the client *before* building the matrix (e.g. heavy custom needs rule out BEECY SaaS).

> **Odoo 20 CE feature boundary (code-verified):** for what Community actually has vs what is Enterprise-only in v20, follow [references/odoo20-ce/](../../references/odoo20-ce/) (STUDY-PAPER §1.2 CE-vs-EE + each area §5) or the `odoo20-ce-expert` skill — do **not** guess feature parity from memory. The Enterprise-only / Thai-localization lists below are a starting point; verify against the KB for the client's target version.
> For the **app-level list of Enterprise-only apps** (Studio, Payroll, Quality, PLM, Documents, Sign, Field Service, Helpdesk, Subscriptions, IoT, …), see [references/odoo20-ce/data/editions-ce-vs-ee.md](../../references/odoo20-ce/data/editions-ce-vs-ee.md) — official vendor matrix, tagged `[web]` (not code-verified); keep it separate from the `[code]` CE facts.

## Trigger
Use when:
- User asks "which version should we recommend for [client]?"
- User is preparing a proposal and needs feature comparison
- Client asks about difference between Enterprise and Community
- During discovery call prep for manufacturing/food/distribution clients

## Input Required
Ask the user for (or extract from context):
1. **Industry** — manufacturing, food & beverage, distribution, services?
2. **Key modules needed** — Manufacturing, Inventory, Accounting, HR, Sales, Purchase, CRM?
3. **Company size** — number of users, number of transactions/month?
4. **Budget signal** — THB range or explicit budget?
5. **Specific requirements** — any special features mentioned?

## GAP Analysis Framework

### Module Coverage Matrix

For each requested module, assess:

| Feature | Enterprise | Community (BEECY) | Gap Level | Impact |
|---|---|---|---|---|
| [feature] | ✅ Full | ✅ Full | None | — |
| [feature] | ✅ Full | ⚠️ Partial | Minor | Low |
| [feature] | ✅ Full | ❌ Not available | Major | High |
| [feature] | ✅ Full | 🔧 Custom needed | Critical | High |

**Gap Levels:**
- **None** — Both versions have full feature parity
- **Minor** — Small difference, workaround available
- **Major** — Significant gap, custom development or process change needed
- **Critical** — Core requirement missing, must use Enterprise or major custom build

### Manufacturing Module (most common for Roots clients)

Key features to assess:
- Work Orders / MO (Manufacturing Orders)
- Bill of Materials (multi-level BoM)
- Production Planning / MPS
- Quality Control
- Maintenance
- PLM (Product Lifecycle Management) — Enterprise only

### Thai Localization (BEECY advantage)

BEECY-specific features that Enterprise does NOT include out-of-box:
- Thai VAT / Withholding Tax (WHT) forms
- e-Tax Invoice (Revenue Department format)
- Thai Payroll (SSO, PND1, PND3, PND53)
- Thai address format (Tambon/Amphoe/Changwat)
- Thai bank transfer formats (KTB, SCB, Bangkok Bank)
- Thai language UI

> ⚠️ **v20 stock-CE reality check:** stock `l10n_th` in Odoo 20 CE does **not** ship e-Tax Invoice or Thai Payroll (PND1/3/53) — these are Roots/BEECY custom builds, not native CE. See [references/odoo20-ce/areas/10-localizations.md](../../references/odoo20-ce/areas/10-localizations.md) §8 for the exact native-vs-gap list, and count every non-native item as build effort in the GAP + manday estimate.

### Scoring Decision Matrix

```
SME trading/retail/service · standard process · no custom modules · งบจำกัด
→ BEECY SaaS (subscription, hosted by Roots)

Budget < THB 800K AND < 50 users AND ต้อง custom / โรงงาน flow ไม่ซับซ้อนมาก
→ Community Implementation (custom project on Community)

Budget THB 800K–2M AND 50–150 users AND manufacturing
→ Community Implementation + custom modules  OR  Enterprise (compare TCO)

Budget > THB 2M OR > 150 users OR Enterprise-only features (Studio, Payroll, advanced MFG/PLM)
→ Enterprise (เลือก hosting: Online ถ้าไม่ custom / Odoo.sh / on-premise)

Government project (e-GP)
→ มักเลือก Enterprise (licensing documentation ชัดเจนกว่าสำหรับยื่นประมูล)
```
> ⚠️ ห้ามเสนอ BEECY SaaS ถ้าลูกค้าต้อง custom modules — เป็น standard package เลือก Community implementation แทน (ดู [references/odoo-editions.md](../../references/odoo-editions.md))

## Output Format

```
## GAP Analysis — [Client Name]
**Industry:** | **Size:** | **Modules:** | **Budget:**

### Recommendation
**Recommended:** [Odoo Enterprise (Standard / Custom) / Community Implementation / BEECY SaaS] · **version:** 20 (default)
**Confidence:** High / Medium / Low
**Rationale:** [2-3 sentences]

> **Two axes — don't collapse them:** *Edition* = Community vs Enterprise (feature boundary — see `references/odoo20-ce/`). *Path* = EE licence / BEECY SaaS / Community Implementation (how Roots delivers). A client can want EE-level features but take the **Community Implementation** path via OCA/custom.
> **Edition-neutral needs:** requirements with no native module in *either* edition (e.g. weighbridge/scale integration, farmer/plot database, electricity-sales billing) are **build effort regardless of edition** — do not slot them as an edition decision.

### Feature Coverage

| Module | Feature | Enterprise | BEECY | Gap | Priority |
|---|---|---|---|---|---|

### Cost Comparison (Estimate)
| | Enterprise Path | BEECY Path |
|---|---|---|
| License | THB X/year | Free |
| Implementation | THB X | THB X |
| Customization | THB X | THB X |
| **Total Year 1** | **THB X** | **THB X** |
| **Total 3-Year** | **THB X** | **THB X** |

### Risks
- [Risk 1]
- [Risk 2]

### Next Steps
- [ ] Confirm budget with [decision maker]
- [ ] Demo [specific module] to validate
- [ ] Get IT infrastructure details
```

## Roots Notes
- Always present both options — let client choose with full information
- BEECY path is typically 30–50% cheaper total cost
- Enterprise path has stronger support SLA and Odoo partner backing
- For government e-GP bids: Enterprise license documentation is cleaner
