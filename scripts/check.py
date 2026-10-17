"""The checks every pull request must pass (run it locally: python scripts/check.py).

Standard library only. It checks that:
  - every JSON file parses;
  - the plugin version in plugin.json and marketplace.json is the same;
  - every skill has front matter with a name that matches its folder and a description;
  - relative links in the markdown files point at files that exist;
  - nothing looks like a TUNAI key (tmcp_ followed by a long token);
  - no em dash appears in text an assistant or a person reads.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", "node_modules"}
TEXT_SUFFIXES = {".md", ".json", ".toml", ".yml", ".yaml", ".snippet", ".example", ".py", ".txt"}
EM_DASH = "—"
KEY = re.compile(r"tmcp_[A-Za-z0-9_-]{20,}")
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
problems: list[str] = []


def files() -> list[Path]:
    return [p for p in ROOT.rglob("*") if p.is_file() and not (set(p.relative_to(ROOT).parts) & SKIP_DIRS)]


def rel(p: Path) -> str:
    return str(p.relative_to(ROOT)).replace("\\", "/")


def fail(p: Path, msg: str) -> None:
    problems.append(f"{rel(p)}: {msg}")


def load(p: Path):
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        fail(p, f"not valid JSON ({e})")
        return None


def check_json() -> None:
    for p in files():
        if p.suffix == ".json":
            load(p)


def check_versions() -> None:
    plugin_path = ROOT / "tunai-jobs" / ".claude-plugin" / "plugin.json"
    market_path = ROOT / ".claude-plugin" / "marketplace.json"
    if not plugin_path.exists() or not market_path.exists():
        return
    plugin, market = load(plugin_path), load(market_path)
    if not plugin or not market:
        return
    listed = {x.get("name"): x.get("version") for x in market.get("plugins", [])}
    if listed.get(plugin.get("name")) != plugin.get("version"):
        fail(market_path, f"version {listed.get(plugin.get('name'))!r} does not match plugin.json {plugin.get('version')!r}")
    if not re.fullmatch(r"\d+\.\d+\.\d+", str(plugin.get("version", ""))):
        fail(plugin_path, "version must be X.Y.Z")


def check_skills() -> None:
    for p in files():
        if p.name != "SKILL.md":
            continue
        text = p.read_text(encoding="utf-8")
        m = re.match(r"---\n(.*?)\n---\n", text, re.S)
        if not m:
            fail(p, "missing front matter")
            continue
        meta = dict(line.split(":", 1) for line in m.group(1).splitlines() if ":" in line)
        name, desc = meta.get("name", "").strip(), meta.get("description", "").strip()
        if name != p.parent.name:
            fail(p, f"name {name!r} must match its folder {p.parent.name!r}")
        if len(desc) < 20:
            fail(p, "description is missing or too short")


def check_links() -> None:
    for p in files():
        if p.suffix != ".md":
            continue
        for target in LINK.findall(p.read_text(encoding="utf-8")):
            if re.match(r"[a-z]+:", target) or target.startswith("#"):
                continue
            path = target.split("#", 1)[0]
            if path and not (p.parent / path).exists():
                fail(p, f"link to a file that does not exist: {target}")


def check_text() -> None:
    for p in files():
        if p.suffix not in TEXT_SUFFIXES and p.name not in {"CODEOWNERS", "LICENSE"}:
            continue
        if rel(p) == "scripts/check.py":
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
        if KEY.search(text):
            fail(p, "looks like a TUNAI key; remove it and revoke the key")
        if p.name != "LICENSE" and EM_DASH in text:
            fail(p, "contains an em dash")


def main() -> int:
    for check in (check_json, check_versions, check_skills, check_links, check_text):
        check()
    if problems:
        print("\n".join(problems))
        print(f"\n{len(problems)} problem(s)")
        return 1
    print("ok: json, versions, skills, links, keys, dashes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
