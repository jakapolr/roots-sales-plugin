#!/usr/bin/env python3
"""
Validate the roots-sales-plugin structure.

Checks (each failure is collected and reported; exit 1 if any):
  1. Core JSON files parse cleanly (.claude-plugin/plugin.json, marketplace.json, .mcp.json)
  2. plugin.json has required keys (name, version) and a sane semver-ish version
  3. Every skills/<dir>/ contains a SKILL.md whose frontmatter `name` == <dir>
  4. Every agents/*.md has frontmatter with both `name` and `description`
  5. No SKILL.md frontmatter `name` collides with another

Frontmatter is parsed without PyYAML (simple, dependency-free) so CI needs no installs.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

errors: list[str] = []
checks_run = 0


def ok(msg: str) -> None:
    print(f"  \033[32m✓\033[0m {msg}")


def fail(msg: str) -> None:
    errors.append(msg)
    print(f"  \033[31m✗\033[0m {msg}")


def read_frontmatter(path: Path) -> dict[str, str] | None:
    """Return a dict of top-level scalar frontmatter keys, or None if no frontmatter."""
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not m:
        return None
    block = m.group(1)
    data: dict[str, str] = {}
    for line in block.splitlines():
        # only capture top-level "key: value" (no leading whitespace)
        km = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if km:
            key, val = km.group(1), km.group(2).strip()
            val = val.strip('"').strip("'")
            data[key] = val
    return data


def check_json_files() -> None:
    global checks_run
    print("\nJSON files:")
    json_files = [
        ROOT / ".claude-plugin" / "plugin.json",
        ROOT / ".claude-plugin" / "marketplace.json",
        ROOT / ".mcp.json",
    ]
    for jf in json_files:
        checks_run += 1
        rel = jf.relative_to(ROOT)
        if not jf.exists():
            fail(f"{rel} is missing")
            continue
        try:
            json.loads(jf.read_text(encoding="utf-8"))
            ok(f"{rel} is valid JSON")
        except json.JSONDecodeError as e:
            fail(f"{rel} is invalid JSON: {e}")


def check_plugin_manifest() -> None:
    global checks_run
    print("\nplugin.json manifest:")
    pj = ROOT / ".claude-plugin" / "plugin.json"
    if not pj.exists():
        return  # already reported by check_json_files
    try:
        data = json.loads(pj.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return
    for key in ("name", "version"):
        checks_run += 1
        if key in data and str(data[key]).strip():
            ok(f"plugin.json has '{key}' = {data[key]}")
        else:
            fail(f"plugin.json missing required key '{key}'")
    if "version" in data:
        checks_run += 1
        if re.match(r"^\d+\.\d+\.\d+", str(data["version"])):
            ok(f"plugin.json version looks like semver ({data['version']})")
        else:
            fail(f"plugin.json version '{data['version']}' is not semver-like")


def check_skills() -> None:
    global checks_run
    print("\nSkills (frontmatter name == folder):")
    skills_dir = ROOT / "skills"
    seen_names: dict[str, str] = {}
    if not skills_dir.is_dir():
        fail("skills/ directory is missing")
        return
    for sub in sorted(p for p in skills_dir.iterdir() if p.is_dir()):
        checks_run += 1
        skill_md = sub / "SKILL.md"
        if not skill_md.exists():
            fail(f"skills/{sub.name}/ has no SKILL.md")
            continue
        fm = read_frontmatter(skill_md)
        if fm is None:
            fail(f"skills/{sub.name}/SKILL.md has no frontmatter block")
            continue
        name = fm.get("name")
        if not name:
            fail(f"skills/{sub.name}/SKILL.md frontmatter missing 'name'")
            continue
        if name != sub.name:
            fail(f"skills/{sub.name}/SKILL.md name '{name}' != folder '{sub.name}'")
            continue
        if name in seen_names:
            fail(f"duplicate skill name '{name}' (also in {seen_names[name]})")
            continue
        seen_names[name] = sub.name
        ok(f"skills/{sub.name} ✓")


def check_agents() -> None:
    global checks_run
    print("\nAgents (frontmatter name + description):")
    agents_dir = ROOT / "agents"
    if not agents_dir.is_dir():
        fail("agents/ directory is missing")
        return
    for md in sorted(agents_dir.glob("*.md")):
        checks_run += 1
        fm = read_frontmatter(md)
        if fm is None:
            fail(f"agents/{md.name} has no frontmatter block")
            continue
        missing = [k for k in ("name", "description") if not fm.get(k)]
        if missing:
            fail(f"agents/{md.name} frontmatter missing: {', '.join(missing)}")
            continue
        ok(f"agents/{md.name} ✓ ({fm['name']})")


def main() -> int:
    print("Validating roots-sales-plugin…")
    check_json_files()
    check_plugin_manifest()
    check_skills()
    check_agents()

    print("\n" + "=" * 48)
    if errors:
        print(f"\033[31mFAILED\033[0m — {len(errors)} problem(s) across {checks_run} checks:")
        for e in errors:
            print(f"  • {e}")
        return 1
    print(f"\033[32mPASSED\033[0m — all {checks_run} checks green.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
