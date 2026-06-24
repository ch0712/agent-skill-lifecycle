"""Skill matching — find relevant skills based on conversation context."""
import re
from pathlib import Path
from typing import List, Tuple, Optional
from . import parse_skill, Skill


def _tokenize(text: str) -> set:
    """Simple tokenization: lowercase, split on non-alphanumeric."""
    return set(re.findall(r"[a-zA-Z][a-zA-Z0-9_\-.]*", text.lower()))


def _trigger_match(trigger: str, context: str) -> float:
    """Check if trigger phrase appears in context. Returns match score."""
    if not trigger or not context:
        return 0.0
    trigger_lower = trigger.lower()
    context_lower = context.lower()

    # Exact phrase match
    trigger_phrases = [p.strip() for p in trigger_lower.split("|")]
    for phrase in trigger_phrases:
        if phrase in context_lower:
            return 1.0

    # Keyword overlap
    trigger_tokens = _tokenize(trigger_lower)
    context_tokens = _tokenize(context_lower)
    if trigger_tokens and context_tokens:
        overlap = len(trigger_tokens & context_tokens)
        if overlap > 0:
            return 0.5 * (overlap / len(trigger_tokens))

    return 0.0


def _tag_match(skill_tags: List[str], context: str) -> float:
    """Check tag overlap with context."""
    if not skill_tags or not context:
        return 0.0
    context_lower = context.lower()
    matches = sum(1 for tag in skill_tags if tag.lower() in context_lower)
    return matches / len(skill_tags) if skill_tags else 0.0


def _description_match(description: str, context: str) -> float:
    """Check keyword overlap between description and context."""
    if not description or not context:
        return 0.0
    desc_tokens = _tokenize(description)
    context_tokens = _tokenize(context)
    if not desc_tokens or not context_tokens:
        return 0.0
    overlap = len(desc_tokens & context_tokens)
    return overlap / len(desc_tokens) if desc_tokens else 0.0


def match_skills(context: str, skills_dir: str, top_k: int = 5) -> List[Tuple[Skill, float]]:
    """Find skills relevant to the given context."""
    skills_dir_path = Path(skills_dir)
    if not skills_dir_path.exists():
        return []

    scored: List[Tuple[Skill, float]] = []

    for skill_md in skills_dir_path.rglob("SKILL.md"):
        try:
            skill = parse_skill(str(skill_md))
        except (ValueError, FileNotFoundError):
            continue

        if skill.deprecated:
            continue

        trigger_score = _trigger_match(skill.trigger, context)
        tag_score = _tag_match(skill.tags, context)
        desc_score = _description_match(skill.description, context)

        # Weighted score: trigger most important, then tags, then description
        total = trigger_score * 0.6 + tag_score * 0.25 + desc_score * 0.15
        if total > 0:
            scored.append((skill, round(total, 3)))

    # Sort by score descending
    scored.sort(key=lambda x: -x[1])
    return scored[:top_k]
