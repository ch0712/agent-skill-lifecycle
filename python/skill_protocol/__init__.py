"""Skill Protocol — core data model and parser frontmatter."""

import re
from dataclasses import dataclass, field
from typing import List, Optional, Dict


@dataclass
class Skill:
    """Represents a parsed SKILL.md file."""
    name: str
    description: str
    content: str
    path: str
    version: str = "0.1.0"
    author: str = ""
    created_at: str = ""
    updated_at: str = ""
    tags: List[str] = field(default_factory=list)
    category: str = ""
    trigger: str = ""
    deprecated: bool = False
    replaced_by: str = ""
    requires: List[str] = field(default_factory=list)
    platforms: List[str] = field(default_factory=list)
    frontmatter_raw: Dict = field(default_factory=dict)


_FRONTMATTER_RE = re.compile(
    r"^---\s*\n(?P<yaml>.*?)\n---\s*\n(?P<body>.*)",
    re.DOTALL,
)


def parse_skill(path: str) -> Skill:
    """Parse a SKILL.md file and return a Skill object."""
    with open(path, encoding="utf-8") as f:
        raw = f.read()

    m = _FRONTMATTER_RE.match(raw)
    if not m:
        raise ValueError(f"No valid frontmatter found in {path}")

    import yaml
    meta = yaml.safe_load(m.group("yaml"))
    if not isinstance(meta, dict):
        meta = {}

    body = m.group("body").strip()

    return Skill(
        name=meta.get("name", ""),
        description=meta.get("description", ""),
        content=body,
        path=path,
        version=meta.get("version", "0.1.0"),
        author=meta.get("author", ""),
        created_at=meta.get("created_at", ""),
        updated_at=meta.get("updated_at", ""),
        tags=meta.get("tags", []),
        category=meta.get("category", ""),
        trigger=meta.get("trigger", ""),
        deprecated=meta.get("deprecated", False),
        replaced_by=meta.get("replaced_by", ""),
        requires=meta.get("requires", []),
        platforms=meta.get("platforms", []),
        frontmatter_raw=meta,
    )
