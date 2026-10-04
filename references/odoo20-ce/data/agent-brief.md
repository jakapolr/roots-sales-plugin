# Shared brief for Odoo 20 CE study agents

Sources (read-only, already on disk, shallow clones):
- Odoo 20.0 CE: /home/user/odoo-src/odoo20   (branch 20.0, HEAD b100a87, 2026-10-03)
- Odoo 19.0 CE: /home/user/odoo-src/odoo19   (branch 19.0)
- Parsed manifests: /home/user/odoo-src/data/manifests_19.json, manifests_20.json (keys = module names; core test modules prefixed odoo/addons/)
- Module lists: /home/user/odoo-src/new_in_20.txt, removed_in_20.txt (addons/ dir only)
No git history is available (depth 1) — compare by diffing the two trees.

Method (be evidence-based; NO guessing):
1. For each module in your scope: read __manifest__.py (summary, description, depends, category, application) in v20.
2. Compare to v19: `diff -rq odoo19/addons/X odoo20/addons/X`, diff models/*.py for new/removed fields & models (grep `_name =`, `fields.`), new views/wizards/controllers, new static/src JS components, manifest depends changes.
3. For modules REMOVED in 20: find where the functionality went (grep in odoo20 for model names / field names / xml ids, check `upgrade`/ migrations hints, check which manifest now provides it). Say "merged into X" only with evidence; otherwise "removed, no successor found".
4. For NEW modules: explain purpose, key models, dependencies.
5. Optionally use WebSearch/WebFetch on odoo.com official sources (release notes "Odoo 20", odoo.com/documentation/20.0) to cross-check — but label web claims as [web] and code-verified claims as [code]. Code is the source of truth. If a feature is Enterprise-only (not in this repo), say so explicitly.
6. Cite file paths (relative to odoo20/ e.g. `addons/stock/models/stock_picking.py`) for each important claim.

Output: write ONE markdown file at the path given in your task. Structure:
  # <Area title> — Odoo 20 CE
  ## 1. Scope (modules covered, count)
  ## 2. Module catalogue (table: module | app? | summary | what it does in 1-2 lines | status vs 19: New / Changed / Unchanged-ish / Removed→successor)
  ## 3. Feature deep-dive (per major app: key business features & workflows, key models, configuration options; written for a functional ERP consultant/implementer)
  ## 4. What's new / changed vs Odoo 19 (bullet list, most impactful first, each with [code] evidence path; mark confidence High/Medium/Low)
  ## 5. Removed / merged modules (table with evidence)
  ## 6. Implementation notes, risks & migration gotchas (for an Odoo partner upgrading customers 19→20)
  ## 7. Open questions / things not verifiable from CE code
Be thorough but concise: aim 2,500–6,000 words. Do NOT write anything outside your output file. Do not modify the source trees. Finish with a short summary (<=200 words) as your final reply listing the top 5 v20 changes in your area.
