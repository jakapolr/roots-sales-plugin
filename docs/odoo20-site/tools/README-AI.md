# How to use this pack with AI tools

| Tool | What to do |
|---|---|
| **Claude Project / ChatGPT Project / Gemini Gem** | Upload `odoo20-ce-knowledge-combined.md` and `module_catalog_19_vs_20.csv` as project knowledge. Instruction: "Answer from the Odoo 20 CE knowledge files; cite file paths and confidence; say when something is Enterprise-only." |
| **Claude Code / Codex / Copilot CLI** | Copy this folder into your repo (e.g. `docs/odoo20-ce-kb/`) and copy `skill/odoo20-ce-expert/` into `.claude/skills/` (or `.agents/skills/`). Also install Odoo's official `skills/` from the odoo repo. |
| **NotebookLM** | Add `STUDY-PAPER.md` and the 10 `areas/*.md` files as sources. |
| **RAG / vector DB** | Index `areas/*.md` split by `##` headings; keep the file name + heading as metadata. `llms.txt` is the index. |

Snapshot: Odoo 20.0 @ b100a87, 3 Oct 2026. Re-check against code before quoting to customers.
