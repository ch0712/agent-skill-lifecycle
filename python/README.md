# Skill Protocol — Python Reference Implementation

轻量 Python 包，实现 SKILL.md 的解析、验证、生命周期管理。

## 安装

```bash
pip install skill-protocol
```

## 使用

### 解析一个技能文件

```python
from skill_protocol import parse_skill

skill = parse_skill("path/to/skill.md")
print(skill.name)         # "systematic-debugging"
print(skill.description)  # "4阶段系统化调试流程..."
print(skill.tags)         # ["debugging", "systematic", "troubleshooting"]
print(skill.content)      # Markdown body（不含 frontmatter）
```

### 验证技能文件

```python
from skill_protocol import validate_skill

errors = validate_skill("path/to/skill.md")
if errors:
    for e in errors:
        print(f"⚠️  {e}")
else:
    print("✅ 技能格式正确")
```

### 技能匹配

```python
from skill_protocol import match_skills

# 从上下文中自动匹配技能
skills_dir = "/path/to/skills/"
context = "pytest 测试失败了，需要排查"
matches = match_skills(context, skills_dir)

for skill, score in matches:
    print(f"{skill.name}: {score:.2f}")
```

### 生命周期评估

```python
from skill_protocol import LifecycleManager

manager = LifecycleManager("/path/to/skills/")

# 检查所有技能状态
results = manager.check_all()
for r in results:
    print(f"{r.skill.name}: {r.status} (health: {r.health_score}/10)")

# 运行维护
actions = manager.maintain()
for a in actions:
    print(f"{a.action}: {a.skill_name} — {a.reason}")
```

## API 参考

### `parse_skill(path) -> Skill`
解析 SKILL.md 文件。返回 `Skill` 对象。

### `Skill` 对象属性

| 属性 | 类型 | 来源 |
|------|------|------|
| `name` | str | frontmatter |
| `description` | str | frontmatter |
| `version` | str | frontmatter (默认 "0.1.0") |
| `tags` | List[str] | frontmatter |
| `category` | str | frontmatter |
| `trigger` | str | frontmatter |
| `deprecated` | bool | frontmatter |
| `requires` | List[str] | frontmatter |
| `content` | str | markdown body |
| `path` | str | 文件路径 |
| `frontmatter_raw` | dict | 原始 frontmatter |

### `validate_skill(path) -> List[str]`
验证技能文件格式。返回错误列表（空 = 通过）。

检查项：
- 文件存在且可读
- frontmatter 是合法 YAML
- `name` 字段存在且合规
- `description` 字段存在且非空
- body 不为空

### `match_skills(context, skills_dir, top_k=5) -> List[Tuple[Skill, float]]`
基于上下文自动匹配技能。返回 `(技能, 匹配分数)` 元组列表。

匹配策略：
1. trigger 关键词命中 → 最高分
2. tags 交集 → 中等分  
3. description 关键词相似度 → 基础分

### `LifecycleManager(skills_dir)`

#### `check_all() -> List[HealthReport]`
评估所有技能的健康度和状态。

#### `maintain() -> List[LifecycleAction]`
自动执行生命周期维护（标记 stale/deprecated/archived）。
