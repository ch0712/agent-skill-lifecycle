"""CLI entry point for skill-protocol."""

import sys
import json
from . import parse_skill
from .validator import validate_skill, validate_all
from .lifecycle import LifecycleManager


def main():
    if len(sys.argv) < 2:
        print("Usage: skill-protocol <command> [args]")
        print()
        print("Commands:")
        print("  validate <path>     Validate a single SKILL.md file")
        print("  validate-all <dir>  Validate all SKILL.md files in a directory")
        print("  info <path>         Show skill metadata")
        print("  health <dir>        Run health check on all skills")
        print("  lifecycle <dir>     Show lifecycle actions")
        return

    cmd = sys.argv[1]

    if cmd == "validate" and len(sys.argv) >= 3:
        errors = validate_skill(sys.argv[2])
        if errors:
            for e in errors:
                print(f"  ⚠️  {e}")
            sys.exit(1)
        else:
            print("  ✅  Valid")

    elif cmd == "validate-all" and len(sys.argv) >= 3:
        results = validate_all(sys.argv[2])
        valid = sum(1 for r in results if r["valid"])
        total = len(results)
        print(f"  {valid}/{total} skills valid")
        for r in results:
            status = "✅" if r["valid"] else "⚠️"
            print(f"  {status}  {r['file']}")
            for e in r["errors"]:
                print(f"       {e}")

    elif cmd == "info" and len(sys.argv) >= 3:
        skill = parse_skill(sys.argv[2])
        info = {
            "name": skill.name,
            "description": skill.description,
            "version": skill.version,
            "tags": skill.tags,
            "category": skill.category,
            "trigger": skill.trigger,
            "deprecated": skill.deprecated,
        }
        print(json.dumps(info, ensure_ascii=False, indent=2))

    elif cmd == "health" and len(sys.argv) >= 3:
        mgr = LifecycleManager(sys.argv[2])
        reports = mgr.check_all()
        for r in reports:
            status_icon = {"active": "✅", "stale": "🟡", "deprecated": "⚠️", "archived": "🗄️"}
            icon = status_icon.get(r.status, "❓")
            print(f"  {icon}  {r.skill.name:30s} {r.health_score:>4}/10  [{r.status}]")
            for issue in r.issues[:3]:
                print(f"       {issue}")

    elif cmd == "lifecycle" and len(sys.argv) >= 3:
        mgr = LifecycleManager(sys.argv[2])
        actions = mgr.maintain()
        for a in actions:
            action_icon = {"keep": "✅", "mark_stale": "🟡", "deprecate": "⚠️", "archive": "🗄️"}
            icon = action_icon.get(a.action, "❓")
            print(f"  {icon}  {a.action:15s} {a.skill_name:30s} [{a.health_score}/10] {a.reason}")

    else:
        print(f"Unknown command: {cmd}")
        sys.exit(1)


if __name__ == "__main__":
    main()
