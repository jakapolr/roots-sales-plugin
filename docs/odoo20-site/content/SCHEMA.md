# Bilingual content schema for the Odoo 20 internal site (Trinity Roots)

Audience: Trinity Roots (Odoo partner, Bangkok) internal team.
- FUNCTIONAL team = business consultants / implementers / pre-sales (care about features, workflows, configuration, customer impact, CE vs EE).
- TECHNICAL team = developers / DevOps (care about models, fields, APIs, renames, migration code, file paths).

Write valid JSON (UTF-8, no comments, no trailing commas) to the output path you are given. Every human-readable string is an object {"en": "...", "th": "..."}.

Thai style: natural professional Thai as used by Thai Odoo/ERP consultants. Keep Odoo technical identifiers (model names, field names, module names, file paths, menu names like "Invoicing") in English inside the Thai text. Do not transliterate code. Thai must be a faithful translation of the English — same facts, no additions.

Accuracy: ONLY use facts that appear in the source markdown file(s) you are given. Do not invent. Keep confidence caveats ("Medium confidence", "verify") where the source has them. Bodies: 1–3 sentences each, concise.

Area schema:
{
  "id": "<given id>",
  "title": {"en","th"},
  "tagline": {"en","th"},            // one sentence: what this area covers in Odoo 20 CE
  "apps": ["module", ...],            // main CE app modules of the area (from the report)
  "functional": [                     // 6-9 items, most impactful first
    {"title":{"en","th"}, "body":{"en","th"}, "impact":"high|medium|low", "kind":"new|changed|removed"}
  ],
  "technical": [                      // 6-9 items, most impactful first
    {"title":{"en","th"}, "body":{"en","th"}, "impact":"high|medium|low", "kind":"new|changed|removed", "refs":["addons/x/models/y.py", ...]}
  ],
  "gotchas": [                        // 5-8 upgrade 19->20 pitfalls
    {"text":{"en","th"}, "audience":"functional|technical"}
  ],
  "not_in_ce": [ {"en","th"} ],       // 0-6 things customers expect that are Enterprise-only / absent in CE
  "removed": [                        // removed/merged modules of this area (from section 5 of the report)
    {"module":"name", "successor":"name or null", "note":{"en","th"}}
  ]
}
