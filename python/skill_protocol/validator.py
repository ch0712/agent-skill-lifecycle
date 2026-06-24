"""Skill file validation."""

from typing import List
from . import parse_skill, Skill

_REQUIRED = ["name", "description"]

_SKIP_DIRS = {".git", "__pycache__", "node_modules", ".venv", "venv"}


def validate_skill(path: str) -> List[str]:
    """Validate a single SKILL.md file. Returns list of error messages (empty = valid)."""
    errors: List[str] = []

    try:
        skill = parse_skill(path)
    except ValueError as e:
        return [str(e)]
    except FileNotFoundError:
        return [f"File not found: {path}"]

    for field in _REQUIRED:
        value = getattr(skill, field, "")
        if not value:
            errors.append(f"Missing required frontmatter field: '{field}'")

    if skill.name and not skill.name.replace("-", "").replace("_", "").isalnum():
        errors.append(
            f"Invalid skill name '{skill.name}': only alphanumeric, hyphens, and underscores allowed"
        )

    if skill.name and len(skill.name) > 64:
        errors.append(f"Skill name too long ({len(skill.name)} chars, max 64)")

    if not skill.content:
        errors.append("Skill body is empty (no Markdown content after frontmatter)")

    return errors


def validate_all(skills_dir: str) -> List[dict]:
    """Validate all SKILL.md files under a directory. Returns per-file results."""
    from pathlib import Path

    results = []
    base = Path(skills_dir)

    for skill_md in base.rglob("SKILL.md"):
        rel = skill_md.relative_to(base)
        parent = skill_md.parent.name
        if parent in _SKIP_DIRS:
            continue
        errors = validate_skill(str(skill_md))
        results.append({"file": str(rel), "valid": len(errors) == 0, "errors": errors})

    return results
