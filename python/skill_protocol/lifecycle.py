"""Skill lifecycle management — creation, staleness detection, deprecation, archival."""

import os
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional, Tuple
from . import Skill, parse_skill


_SKILL_FILENAME = "SKILL.md"
_STALE_DAYS = 30
_DEPRECATED_DAYS = 15
_ARCHIVE_DIR = "_archived"


@dataclass
class HealthReport:
    """Health assessment for a single skill."""
    skill: Skill
    health_score: float  # 1-10
    status: str          # "active" | "stale" | "deprecated" | "archived"
    issues: List[str] = field(default_factory=list)
    last_used_days: Optional[int] = None


@dataclass
class LifecycleAction:
    """An action recommended by the lifecycle manager."""
    action: str          # "keep" | "mark_stale" | "deprecate" | "archive"
    skill_name: str
    reason: str
    health_score: float = 0.0


class LifecycleManager:
    """Manages the lifecycle of a skill directory."""

    def __init__(self, skills_dir: str, usage_log: Optional[str] = None):
        self.skills_dir = Path(skills_dir)
        self.usage_log_path = Path(usage_log) if usage_log else self.skills_dir / ".usage.json"

    def _list_skills(self) -> List[Skill]:
        """Recursively find all SKILL.md files."""
        skills = []
        archive_dir = self.skills_dir / _ARCHIVE_DIR
        for skill_md in self.skills_dir.rglob(_SKILL_FILENAME):
            parent = skill_md.parent
            if archive_dir in parent.parents:
                continue
            if parent.name.startswith("."):
                continue
            try:
                skills.append(parse_skill(str(skill_md)))
            except (ValueError, FileNotFoundError):
                continue
        return skills

    def _load_usage_data(self) -> dict:
        """Load usage tracking data."""
        if self.usage_log_path.exists():
            import json
            try:
                return json.loads(self.usage_log_path.read_text())
            except (json.JSONDecodeError, OSError):
                return {}
        return {}

    def _save_usage_data(self, data: dict):
        """Save usage tracking data."""
        import json
        self.usage_log_path.parent.mkdir(parents=True, exist_ok=True)
        self.usage_log_path.write_text(json.dumps(data, indent=2))

    def _compute_health(self, skill: Skill, usage: dict) -> HealthReport:
        """Compute health score for a single skill."""
        issues = []
        now = time.time()
        skill_usage = usage.get(skill.name, {})

        # Check trigger completeness
        has_trigger = bool(skill.trigger)
        if not has_trigger:
            issues.append("No trigger field — Agent cannot auto-match this skill")

        # Check tags
        has_tags = len(skill.tags) > 0
        if not has_tags:
            issues.append("No tags — poor discoverability")

        # Check recency
        days_since_update = None
        if skill.updated_at:
            try:
                from datetime import datetime
                updated = datetime.fromisoformat(skill.updated_at)
                days_since_update = (datetime.now() - updated).days
            except (ValueError, TypeError):
                pass

        # Check usage frequency
        last_used = skill_usage.get("last_used_at")
        last_used_days = None
        if last_used:
            last_used_days = (now - last_used) / 86400

        use_count = skill_usage.get("use_count", 0)

        # Scoring
        score = 10.0

        if not has_trigger:
            score -= 2.0
        if not has_tags:
            score -= 1.5
        if days_since_update and days_since_update > 60:
            score -= 1.5
            issues.append(f"Last updated {days_since_update} days ago")
        if skill.deprecated:
            score -= 3.0
        if use_count == 0:
            score -= 0.5  # New skill, not yet used

        # Determine status
        if last_used_days is not None and last_used_days > _STALE_DAYS:
            status = "stale"
        elif last_used_days is not None and last_used_days > _DEPRECATED_DAYS:
            status = "deprecated"
        elif skill.deprecated:
            status = "deprecated"
        else:
            status = "active"

        score = max(1.0, min(10.0, score))

        return HealthReport(
            skill=skill,
            health_score=round(score, 1),
            status=status,
            issues=issues,
            last_used_days=int(last_used_days) if last_used_days else None,
        )

    def check_all(self) -> List[HealthReport]:
        """Evaluate health of all skills in the directory."""
        skills = self._list_skills()
        usage = self._load_usage_data()
        return [self._compute_health(s, usage) for s in skills]

    def maintain(self) -> List[LifecycleAction]:
        """Run lifecycle maintenance. Returns recommended actions (does not execute them)."""
        reports = self.check_all()
        actions: List[LifecycleAction] = []

        for r in reports:
            if r.status == "deprecated" and r.last_used_days and r.last_used_days > _STALE_DAYS + _DEPRECATED_DAYS:
                actions.append(LifecycleAction(
                    action="archive",
                    skill_name=r.skill.name,
                    reason=f"Deprecated and unused for {r.last_used_days} days",
                    health_score=r.health_score,
                ))
            elif r.status == "stale":
                actions.append(LifecycleAction(
                    action="mark_stale",
                    skill_name=r.skill.name,
                    reason=f"Unused for {r.last_used_days} days",
                    health_score=r.health_score,
                ))
            elif r.health_score < 5:
                actions.append(LifecycleAction(
                    action="deprecate",
                    skill_name=r.skill.name,
                    reason=f"Health score {r.health_score}/10: {'; '.join(r.issues[:2])}",
                    health_score=r.health_score,
                ))
            else:
                actions.append(LifecycleAction(
                    action="keep",
                    skill_name=r.skill.name,
                    reason=f"Active (health: {r.health_score}/10)",
                    health_score=r.health_score,
                ))

        return actions

    def record_use(self, skill_name: str):
        """Record that a skill was used (called by Agent after loading a skill)."""
        usage = self._load_usage_data()
        now = time.time()
        if skill_name not in usage:
            usage[skill_name] = {"use_count": 0, "last_used_at": None}
        usage[skill_name]["use_count"] = usage[skill_name].get("use_count", 0) + 1
        usage[skill_name]["last_used_at"] = now
        self._save_usage_data(usage)
