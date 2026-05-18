# CONNECTORS.md — Roots-Sales-Plugin

Plugin files use `~~category` as a placeholder for tools in that category.
Roots uses Google Workspace as the primary tool stack.

## Active Connectors (Phase 1)

| Connector | Category | Used for | Status |
|---|---|---|---|
| Google Drive | `~~cloud-storage` | Proposal docs, SRS, MOM, TOR files | ✅ Active |
| Gmail | `~~email` | Outreach, follow-ups, proposal sends | ✅ Active |
| Google Calendar | `~~calendar` | Call prep, scheduling context | ✅ Active |

## Planned Connectors (Phase 2)

| Connector | Category | Used for | Status |
|---|---|---|---|
| Odoo CRM MCP | `~~crm` | Deal stage, contact history, pipeline | 🔧 Build on Hetzner |
| Fireflies / Otter | `~~transcripts` | Auto call recording → call-summary | ⏳ When team adopts |

## Placeholder Reference

When you see these in skill files, here is what they map to:

- `~~crm` → Odoo CRM (Phase 2) or manual paste from Odoo
- `~~email` → Gmail
- `~~calendar` → Google Calendar
- `~~cloud-storage` → Google Drive
- `~~transcripts` → Fireflies (Phase 2) or paste transcript manually
- `~~chat` → Line / Google Chat (no MCP yet — paste manually)

## Adding a New Connector

1. Find the MCP URL from the provider or Anthropic Directory
2. Add it to `.mcp.json` under `mcpServers`
3. Update this file with the new entry
4. Run `/reload-plugins` in Claude Code
5. Update relevant SKILL.md files to reference `~~new-category`

---

## Phase 2 Connectors (ยังไม่เปิดใช้งาน)

Server เหล่านี้ถอดออกจาก .mcp.json ชั่วคราว เพราะยังไม่มี URL — เพิ่มกลับเมื่อพร้อม:

| Server | สถานะ | URL ที่จะใช้ |
|---|---|---|
| `odoo-crm` | Phase 2 — รอ build บน Hetzner VPS | (Roots Odoo CRM MCP — deal stage, contact history) |
| `fireflies` | Phase 2 — รอทีมเลือก call recording tool | (Fireflies / Otter.ai transcript) |
| `hubspot` | Optional — เปิดเฉพาะถ้าทีมใช้ HubSpot | https://mcp.hubspot.com/anthropic |

วิธีเพิ่มกลับ: แก้ `.mcp.json` เพิ่ม block ใน `mcpServers` พร้อม `url` จริง แล้ว commit
