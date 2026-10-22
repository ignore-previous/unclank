"""Parse the research domain files into tells, not-a-tells and sources.

The domain files in research/domains/ are the canonical record. Each tell is a
heading ("### D08-001 Title" or "#### D08-010 Title") followed by "- Key: value"
lines. Sources are "S-D08-001 | title | url | date | type | via | status" lines.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOMAINS = ROOT / "research" / "domains"

HEADING = re.compile(r"^#{3,4} (D\d{2}-N?\d{2,3}) (.+)$")
FIELD = re.compile(r"^- ([A-Za-z][A-Za-z /-]*?): (.*)$")
SOURCE = re.compile(r"^(S-D\d{2}-\d{3}) \| (.*)$")


@dataclass
class Entry:
    id: str
    title: str
    domain: str
    fields: dict[str, str] = field(default_factory=dict)

    @property
    def is_not_a_tell(self) -> bool:
        return "-N" in self.id

    @property
    def label(self) -> str:
        if self.is_not_a_tell:
            return "Not a tell"
        return self.fields.get("Label", "").split(" (")[0].strip()

    @property
    def confidence(self) -> str:
        return self.fields.get("Confidence", "").split(" ")[0].strip()

    @property
    def source_ids(self) -> list[str]:
        return re.findall(r"S-D\d{2}-\d{3}", self.fields.get("Sources", ""))


@dataclass
class Source:
    id: str
    title: str
    url: str
    date: str
    kind: str
    via: str
    status: str


def load() -> tuple[dict[str, Entry], dict[str, Source]]:
    entries: dict[str, Entry] = {}
    sources: dict[str, Source] = {}
    for path in sorted(DOMAINS.glob("D*.md")):
        domain = path.stem
        current: Entry | None = None
        last_key: str | None = None
        for line in path.read_text(encoding="utf-8").splitlines():
            m = HEADING.match(line)
            if m:
                current = Entry(m.group(1), m.group(2).strip(), domain)
                entries[current.id] = current
                last_key = None
                continue
            if line.startswith("#"):
                current = None
                continue
            m = SOURCE.match(line)
            if m:
                parts = [p.strip() for p in m.group(2).split("|")]
                parts += [""] * (6 - len(parts))
                sources[m.group(1)] = Source(m.group(1), *parts[:6])
                continue
            if current is None:
                continue
            m = FIELD.match(line)
            if m:
                key: str = m.group(1)
                current.fields[key] = m.group(2).strip()
                last_key = key
            elif last_key and line.startswith("  ") and line.strip():
                current.fields[last_key] += " " + line.strip()
    return entries, sources
