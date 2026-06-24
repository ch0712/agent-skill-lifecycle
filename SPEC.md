# SKILL.md 协议规范 v1.0

> 定义：一种框架无关的 Agent 技能文档格式，让 AI Agent 能自主创建、加载、更新、淘汰可复用的过程性知识。

---

## 1. 文件格式

每个技能是一个独立的 Markdown 文件（`*.md`），包含 **YAML frontmatter**（元数据）和 **Markdown body**（技能内容）。

### 最小示例

```markdown
---
name: my-skill
description: 一句话描述这个技能做什么
---

# 技能名称

## 正文内容
```

### 完整示例

参见 `examples/` 目录。

## 2. Frontmatter 字段

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| `name` | string | ✅ | 技能名称。唯一标识符，全小写+连字符 |
| `description` | string | ✅ | 一句话描述（用于 Agent 自动匹配） |
| `version` | string | | 语义化版本号，如 `1.2.0` |
| `author` | string | | 创建者标识 |
| `created_at` | date | | ISO 8601 日期 |
| `updated_at` | date | | 最后更新时间 |
| `tags` | list | | 标签列表，用于分类和搜索 |
| `category` | string | | 分类名（如 `devops`, `data-science`, `creative`）|
| `trigger` | string | | 技能激活条件（何时 Agent 应加载此技能）|
| `deprecated` | bool | | 设为 `true` 表示此技能已废弃 |
| `replaced_by` | string | | 废弃时指明替代技能名 |
| `requires` | list | | 依赖的其他技能名 |
| `platforms` | list | | 支持的平台（`linux`, `macos`, `windows`）|
| `dependencies` | list | | 需要的外部命令或库 |

### Frontmatter 示例

```yaml
---
name: debugging-python-tests
description: Python 测试失败时系统性排查流程 — 从 pytest 错误定位根因
version: 2.1.0
author: agent
created_at: 2026-01-15
updated_at: 2026-06-20
tags: [python, testing, debugging]
category: software-development
trigger: pytest 测试失败或出现 Traceback
---
```

## 3. Body 内容约定

Body 是 Markdown 正文，供 Agent 阅读和执行。建议结构：

### 标题

一级标题（`#`）应为技能名称，与 frontmatter `name` 一致或可读版本。

### 内容块

推荐使用以下结构（非强制）：

```markdown
# 技能名称

## 场景 / 触发条件

何时使用这个技能。

## 步骤

1. 第一步
2. 第二步
3. ...

## 要点 / 坑点 / 注意事项

- 已知的易错点
- 需要特别小心的地方

## 验证方法

如何确认技能执行成功。
```

### 代码块

代码块使用标准 Markdown 代码围栏，可指定语言。

````markdown
```bash
# Shell 命令
pytest tests/ -x -v --tb=short
```

```python
# Python 代码
def validate():
    pass
```
````

## 4. 引用文件

技能可以附带引用文件、模板、脚本。推荐目录结构：

```
skills/
├── my-skill/
│   ├── SKILL.md          # 主文件（必须有）
│   ├── references/        # 参考文档
│   │   ├── deep-dive.md
│   │   └── api-ref.md
│   ├── templates/         # 模板文件
│   │   └── config.yaml
│   └── scripts/           # 可执行脚本
│       └── validate.sh
└── another-skill/
    └── SKILL.md
```

引用文件通过路径引用，不嵌入 SKILL.md 本身。

## 5. 技能匹配规则

Agent 在以下情况下应考虑加载某个技能：

1. **会话启动时** — 根据 `tags`/`category` 匹配已知的当前项目、用户偏好
2. **触发关键词出现时** — 用户或工具输出包含 `trigger` 中的关键词
3. **Agent 主动发现** — 任务遇到瓶颈，Agent 搜索可用技能库
4. **按需加载** — 用户显式调用 `/load-skill name`

### 匹配优先级

| 优先级 | 条件 |
|--------|------|
| P0 | `trigger` 直接命中当前上下文 |
| P1 | `tags` 匹配当前任务类型 |
| P2 | `category` 匹配当前领域 |
| P3 | 最近使用过的技能 |
| P4 | 其他 |

## 6. 技能状态生命周期

```
[草稿] ─→ [活跃] ─→ [过时] ─→ [已归档]
  ↑          ↑          │
  └──────────┴──────────┘ (修改后重置为活跃)
```

| 状态 | 含义 | 行为 |
|------|------|------|
| **草稿** | 刚创建，未经验证 | Agent 谨慎使用 |
| **活跃** | 已验证可用 | 正常匹配和加载 |
| **过时** | 被更新的版本替代或发现不正确 | 不再主动匹配，需要时提示"可能过时" |
| **已归档** | 不再使用但保留历史 | 不被加载，仅用于追溯 |

状态通过 `version` 比较和 `deprecated` 标记来管理。

## 7. 与框架无关的设计

本协议**不绑定任何特定 Agent 框架**。任何框架可以通过以下方式集成：

- **解析器** — 用任意语言实现 frontmatter + body 的解析
- **匹配器** — 根据 trigger/tags/category 实现技能自动匹配
- **加载器** — 将技能内容注入 Agent 的上下文窗口
- **生命管理员** — 实现创建、更新、废弃、归档的自动管理

常见的集成方式：

```
┌─ 外部事件 ─────────────────────────────────────┐
│  Agent 完成任务 | 用户反馈 | 新文档 | 定期巡检  │
└──────────────────────┬─────────────────────────┘
                       ↓
┌─ 生命周期管道 ──────────────────────────────────┐
│  评估 → 决定(创建/更新/归档) → 执行 → 验证     │
└─────────────────────────────────────────────────┘
                       ↓
┌─ 技能存储 ─────────────────────────────────────┐
│  SKILL.md 文件目录（本地 FS / Git / S3 / ...） │
└─────────────────────────────────────────────────┘
                       ↓
┌─ 注入管道 ───────────────────────────────────┐
│  匹配 → 加载 → (可选)注入到 System Prompt    │
└──────────────────────────────────────────────┘
```

## 8. 版本兼容性

当前版本：**v1.0**。协议变更将遵循语义化版本：

- **major** — 破坏性格式变更（现有技能需修改）
- **minor** — 新增可选字段，向后兼容
- **patch** — 文档澄清，无结构变更
