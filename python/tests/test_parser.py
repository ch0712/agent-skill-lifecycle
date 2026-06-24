"""Tests for skill parser."""
import tempfile
import os
from skill_protocol import parse_skill


SAMPLE_SKILL = """---
name: test-skill
description: A test skill for unit testing
version: 1.0.0
tags: [test, debugging]
category: testing
trigger: "test failure"
---

# Test Skill

## Steps

1. Do something
2. Verify result
"""


def test_parse_valid_skill():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as f:
        f.write(SAMPLE_SKILL)
        path = f.name

    try:
        skill = parse_skill(path)
        assert skill.name == "test-skill"
        assert skill.description == "A test skill for unit testing"
        assert skill.version == "1.0.0"
        assert skill.tags == ["test", "debugging"]
        assert skill.category == "testing"
        assert skill.trigger == "test failure"
        assert "# Test Skill" in skill.content
    finally:
        os.unlink(path)


def test_parse_minimal_skill():
    content = """---
name: minimal
description: Minimal skill
---

# Minimal
"""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as f:
        f.write(content)
        path = f.name

    try:
        skill = parse_skill(path)
        assert skill.name == "minimal"
        assert skill.version == "0.1.0"  # default
        assert skill.tags == []
    finally:
        os.unlink(path)


def test_parse_no_frontmatter():
    content = "# Just a heading\n\nSome content"
    with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as f:
        f.write(content)
        path = f.name

    try:
        parse_skill(path)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass
    finally:
        os.unlink(path)
