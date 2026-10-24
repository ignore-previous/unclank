"""Static checks for the unclank skills. No model or network needed by default.

Checks:
- each SKILL.md has valid frontmatter and stays within its size budget;
- every cited tell ID exists and isn't dropped, retired or kept out of checklists;
- each checklist line's label and confidence match the research record;
- each skill covers every live tell in its domains (warning only);
- references/evidence.md is up to date with the research;
- each eval scaffold.sh is up to date with its fixture;
- each skill has a "Last reviewed" date;
- quotes are under 15 words;
- no private terms (personal names, project names, local paths) in shipped files;
- cited sources have a URL (warning; an error with --release);
- with --links, every cited source URL loads.

Private terms come from `.private-terms` (one per line, git-ignored) and the
UNCLANK_PRIVATE_TERMS environment variable (comma-separated), so the list itself
is never published.

Usage: python scripts/check.py [--links] [--release]
"""

from __future__ import annotations

import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

import build_scaffold
from build_evidence import SKILLS, cited_ids, evidence_path, render
from research import ROOT, Entry, Source, load

# Domains each skill is meant to cover in full. Tells from other domains may be
# cited too; they just aren't required.
COVERAGE = {
    "unclank-launch": ["D08-tech-defaults-visible"],
    "unclank-quiz": ["D09-educational-content"],
    "unclank-store": ["D10-audience-platform-reaction", "D06-game-design"],
}

MAX_LINES = 200
MAX_BYTES = 20_000
MAX_DESCRIPTION = 1024
NAME = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
CHECK_LINE = re.compile(
    r"^- \[(Avoid|Choose deliberately) · (strong|moderate|anecdotal)\] .*?\[(D\d{2}-\d{3})\]"
)
LABEL_TAG = re.compile(r"\[(Avoid|Choose deliberately|Not a tell)[^\]]*\]")
QUOTE = re.compile(r'"([^"\n]{3,}?)"|“([^”\n]{3,}?)”')
LAST_REVIEWED = re.compile(r"^Last reviewed: \d{1,2} [A-Z][a-z]{2} \d{4}\.", re.M)
LOCAL_PATH = re.compile(r"[A-Za-z]:[\\/]Users[\\/]|/home/[a-z]|~/\.claude")
EMAIL = re.compile(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+")
ALLOWED_EMAIL = re.compile(r"(@(example\.(com|org|invalid)|users\.noreply\.github\.com|anthropic\.com)|^security@ignoreprevious\.dev)$")
SHIPPED = ["skills", "research", "evals", "scripts", ".claude-plugin", ".cursor-plugin", ".github",
           "README.md", "CREDITS.md", "CHANGELOG.md", "SECURITY.md", "LICENSE"]
REPO_URL = "https://github.com/ignore-previous/unclank"


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, msg: str) -> None:
        self.errors.append(msg)

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)


def excluded(e: Entry) -> str | None:
    """Why a tell must not be cited in a checklist, or None if it may be."""
    if e.confidence == "dropped":
        return "dropped"
    if "Retired" in e.fields:
        return "retired"
    if "not in the checklist" in e.fields.get("Flag", ""):
        return "kept out of checklists by its Flag"
    return None


def frontmatter(text: str) -> dict[str, str] | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end < 0:
        return None
    fields: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fields[k.strip()] = v.strip()
    return fields


def check_skill(skill: str, entries: dict[str, Entry], sources: dict[str, Source],
                r: Report, release: bool) -> set[str]:
    path = SKILLS / skill / "SKILL.md"
    rel = path.relative_to(ROOT).as_posix()
    text = path.read_text(encoding="utf-8")

    fm = frontmatter(text)
    if fm is None:
        r.error(f"{rel}: missing or malformed frontmatter")
        fm = {}
    if fm.get("name") != skill:
        r.error(f"{rel}: frontmatter name {fm.get('name')!r} should be {skill!r}")
    if not NAME.match(skill) or len(skill) > 64:
        r.error(f"{rel}: skill name must be lowercase words joined by hyphens, 64 chars max")
    desc = fm.get("description", "")
    if not desc:
        r.error(f"{rel}: frontmatter has no description")
    elif len(desc) > MAX_DESCRIPTION:
        r.error(f"{rel}: description is {len(desc)} chars (max {MAX_DESCRIPTION})")

    lines = text.splitlines()
    if len(lines) > MAX_LINES:
        r.error(f"{rel}: {len(lines)} lines (budget {MAX_LINES})")
    if len(text.encode("utf-8")) > MAX_BYTES:
        r.error(f"{rel}: {len(text.encode('utf-8'))} bytes (budget {MAX_BYTES})")
    if not LAST_REVIEWED.search(text):
        r.error(f"{rel}: no 'Last reviewed: D Mon YYYY.' line")

    ids = cited_ids(path)
    for tid in ids:
        e = entries.get(tid)
        if e is None:
            r.error(f"{rel}: cites unknown tell {tid}")
            continue
        why = excluded(e)
        if why:
            r.error(f"{rel}: cites {tid}, which is {why}")

    for n, line in enumerate(lines, 1):
        m = CHECK_LINE.match(line)
        if m:
            label, conf, tid = m.groups()
            e = entries.get(tid)
            if e is None:
                continue
            if e.is_not_a_tell:
                r.error(f"{rel}:{n}: {tid} is a Not-a-tell but sits on a checklist line")
            elif (e.label, e.confidence) != (label, conf):
                r.error(f"{rel}:{n}: {tid} is tagged {label} · {conf}, "
                        f"research says {e.label} · {e.confidence}")
        elif line.startswith("- ") and LABEL_TAG.match(line[2:]):
            r.error(f"{rel}:{n}: checklist tag without a tell ID or in the wrong form")

    for domain in COVERAGE.get(skill, []):
        live = [e.id for e in entries.values()
                if e.domain == domain and not e.is_not_a_tell and not excluded(e)]
        missing = [t for t in live if t not in ids]
        if missing:
            r.warn(f"{rel}: doesn't cite these live {domain[:3]} tells: {', '.join(missing)}")
        nots = [e.id for e in entries.values() if e.domain == domain and e.is_not_a_tell]
        missing = [t for t in nots if t not in ids]
        if missing:
            r.warn(f"{rel}: doesn't cite these {domain[:3]} Not-a-tells: {', '.join(missing)}")

    ev = evidence_path(skill)
    try:
        _, want = render(skill, entries, sources)
    except SystemExit:
        want = None
    if want is not None:
        if not ev.exists():
            r.error(f"{ev.relative_to(ROOT).as_posix()}: missing; run scripts/build_evidence.py")
        elif ev.read_text(encoding="utf-8") != want:
            r.error(f"{ev.relative_to(ROOT).as_posix()}: out of date; run scripts/build_evidence.py")

    cited_sources: set[str] = set()
    for tid in ids:
        if tid in entries:
            cited_sources.update(entries[tid].source_ids)
    no_url = sorted(s for s in cited_sources if s in sources and not urls(sources[s]))
    if no_url:
        msg = f"{rel}: {len(no_url)} cited sources have no URL: {', '.join(no_url)}"
        (r.error if release else r.warn)(msg)
    unknown = sorted(s for s in cited_sources if s not in sources)
    if unknown:
        r.error(f"{rel}: cited tells point at unknown sources: {', '.join(unknown)}")
    return cited_sources


def shipped_files() -> list[Path]:
    files: list[Path] = []
    for name in SHIPPED:
        p = ROOT / name
        if p.is_file():
            files.append(p)
        elif p.is_dir():
            files += [f for f in p.rglob("*") if f.is_file() and "__pycache__" not in f.parts
                      and "results" not in f.relative_to(ROOT).parts[:2]]
    return files


def private_terms() -> list[str]:
    terms: list[str] = []
    f = ROOT / ".private-terms"
    if f.exists():
        terms += [t.strip() for t in f.read_text(encoding="utf-8").splitlines()
                  if t.strip() and not t.startswith("#")]
    terms += [t.strip() for t in os.environ.get("UNCLANK_PRIVATE_TERMS", "").split(",") if t.strip()]
    return terms


def check_text(r: Report) -> None:
    terms = private_terms()
    if not terms:
        r.warn("no private terms set (.private-terms or UNCLANK_PRIVATE_TERMS); name check skipped")
    term_res = [re.compile(r"\b" + re.escape(t) + r"\b", re.I) for t in terms]
    for path in shipped_files():
        if path.suffix.lower() not in {".md", ".py", ".json", ".yaml", ".yml", ".txt", ""}:
            continue
        rel = path.relative_to(ROOT).as_posix()
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for n, line in enumerate(text.splitlines(), 1):
            if path.suffix.lower() == ".md":
                for m in QUOTE.finditer(line):
                    q = m.group(1) or m.group(2)
                    if len(q.split()) >= 15:
                        r.error(f"{rel}:{n}: quote of {len(q.split())} words (keep under 15)")
            if LOCAL_PATH.search(line):
                r.error(f"{rel}:{n}: local file path")
            for m in EMAIL.finditer(line):
                if not ALLOWED_EMAIL.search(m.group(0)):
                    r.error(f"{rel}:{n}: email address {m.group(0)}")
            for t, tre in zip(terms, term_res):
                if tre.search(line):
                    r.error(f"{rel}:{n}: private term ({t[:1]}…)")


def check_plugin(r: Report) -> None:
    p = ROOT / ".claude-plugin" / "plugin.json"
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        r.error(f".claude-plugin/plugin.json: {exc}")
        return
    if data.get("name") != "unclank":
        r.error(".claude-plugin/plugin.json: name should be 'unclank'")
    if not re.match(r"^\d+\.\d+\.\d+$", str(data.get("version", ""))):
        r.error(".claude-plugin/plugin.json: version should be x.y.z")
    if data.get("repository") != REPO_URL:
        r.error(f".claude-plugin/plugin.json: repository should be {REPO_URL}")
    if not str(data.get("homepage", "")).startswith("https://"):
        r.error(".claude-plugin/plugin.json: homepage should be an https URL")
    cp = ROOT / ".cursor-plugin" / "plugin.json"
    try:
        cursor = json.loads(cp.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        r.error(f".cursor-plugin/plugin.json: {exc}")
        return
    for key in ("name", "version", "description", "homepage", "repository", "license"):
        if cursor.get(key) != data.get(key):
            r.error(f".cursor-plugin/plugin.json: {key} differs from .claude-plugin/plugin.json")


def urls(s: Source) -> list[str]:
    """A source's URL field can hold several URLs separated by ';'."""
    return [u for u in re.split(r"\s*;\s*|\s+", s.url) if u.startswith("http")]


def check_scaffolds(r: Report) -> None:
    for case_dir in build_scaffold.cases([]):
        dest = case_dir / "scaffold.sh"
        rel = dest.relative_to(ROOT).as_posix()
        if not dest.exists():
            r.error(f"{rel}: missing; run scripts/build_scaffold.py")
        elif dest.read_text(encoding="utf-8") != build_scaffold.render(case_dir):
            r.error(f"{rel}: out of date with its fixture; run scripts/build_scaffold.py")


def check_links(cited: set[str], sources: dict[str, Source], r: Report) -> None:
    for sid in sorted(cited):
        s = sources.get(sid)
        if not s:
            continue
        for url in urls(s):
            req = urllib.request.Request(url, headers={"User-Agent": "unclank-linkcheck/1.0"})
            try:
                with urllib.request.urlopen(req, timeout=20) as resp:
                    code = resp.status
            except urllib.error.HTTPError as exc:
                code = exc.code
            except (urllib.error.URLError, TimeoutError, OSError, ValueError) as exc:
                r.warn(f"{sid}: {url} did not load ({exc.__class__.__name__})")
                continue
            # Many sites refuse scripted requests; only a 404 or 410 means the page is gone.
            if code in (404, 410):
                r.error(f"{sid}: {url} returned {code}")
            elif code >= 400:
                r.warn(f"{sid}: {url} returned {code} (may block scripts; check by hand)")


def main(argv: list[str]) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    release = "--release" in argv
    entries, sources = load()
    r = Report()
    check_plugin(r)
    cited: set[str] = set()
    for path in sorted(SKILLS.glob("*/SKILL.md")):
        cited |= check_skill(path.parent.name, entries, sources, r, release)
    check_text(r)
    check_scaffolds(r)
    if "--links" in argv:
        check_links(cited, sources, r)
    for w in r.warnings:
        print(f"warning: {w}")
    for e in r.errors:
        print(f"error: {e}")
    print(f"{len(r.errors)} errors, {len(r.warnings)} warnings")
    return 1 if r.errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
