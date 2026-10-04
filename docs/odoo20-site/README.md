# Roots Odoo 20 Field Guide (internal site)

A bilingual (EN/TH) internal site for the Roots functional and technical teams, built from the Odoo 20 CE knowledge base in [`references/odoo20-ce/`](../../references/odoo20-ce/).

Published as a private claude.ai artifact: https://claude.ai/artifact/LVT8ZS5yFVPn2ac9Mg5q1w (share it from the page's Share menu).

## What it has
- Overview: headline numbers, the 10 most important changes, areas, bottom line.
- 10 area pages with a Functional / Technical / All lens: what changed vs 19, upgrade gotchas, not in CE, removed modules, modules, full report (each section translatable to Thai on demand via Claude).
- Module explorer for all 720 modules (657 in 20.0 + 63 removed).
- Upgrade 19→20 playbook, CE vs EE, risks.
- Downloads: study paper (PDF + MD), module catalogue, CSV, area reports, AI learning pack (ZIP built in the browser), combined knowledge file, llms.txt, Claude Code skill.

## Files
| Path | What |
|---|---|
| `index.src.html` | Page template (UI strings EN/TH, views, download and translation logic) |
| `content/*.json` | Curated bilingual content per area + overview (schema in `content/SCHEMA.md`) |
| `tools/` | `reports.mjs` (Markdown → per-section HTML), `pdf.mjs` (paper → PDF), `area.py` (module → area mapping), `manifests.py` + `catalog.py` (regenerate the catalogue from fresh Odoo clones; set `ODOO_SRC`) |
| `build.py` | Assembles `build/files/` (git-ignored) |

## Rebuild and republish
```bash
npm --prefix docs/odoo20-site/tools install
python3 docs/odoo20-site/build.py --pdf
```
Publish `build/files/index.html` to the same artifact URL with all other files in `build/files/` as supporting files and capabilities `{"downloads": true, "sample": {}}`.
