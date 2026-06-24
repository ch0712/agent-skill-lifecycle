# Community — Adoption Guide

## For Other Agent Frameworks

想集成 SKILL.md 协议？以下是不同框架的集成策略：

### 如果你有 System Prompt 注入能力

**最简单的方式：** 让 Agent 在 System Prompt 中看到技能列表，并在完成任务后调用一个 `create_skill` 工具。

```python
# 你的 System Prompt 中注入：
system_prompt += """
AVAILABLE SKILLS:
- systematic-debugging: 4阶段调试流程
- python-test-setup: Python 测试初始化

完成复杂任务后，使用 create_skill 工具将工作流保存为技能。
"""
```

### 如果你有 Tool Calling 能力

| 需要实现的工具 | 说明 |
|:-------------|:-----|
| `skill_view(name)` | 解析并返回 SKILL.md 内容 |
| `skill_manage(action, name, content)` | 创建/更新/删除技能 |
| `skill_search(query)` | 按关键词搜索可用技能 |

### 如果你只有 Prompt 模板

```markdown
## 技能使用规则

当你完成一个涉及 3 步以上的任务时，请创建一个技能文档。
格式：
---
name: 技能名
description: 一句话描述
trigger: 什么情况下应该使用本技能
---
步骤...

当你发现已有技能过时时，请更新它。
```

## How to Contribute

We welcome contributions in any form:

- **协议改进** — 提 Issue 讨论 frontmatter 字段扩展
- **参考实现** — Java/TypeScript/Go 移植
- **案例技能** — 提交你框架中的优秀技能作为示例
- **翻译** — 中英文文档维护
- **集成案例** — 你成功集成到某个框架的经验分享

### PR 流程

1. Fork 仓库
2. 创建 feature branch
3. 提交改动
4. 写清楚 CHANGELOG
5. 提交 PR

### Issue 模板

```

## 提案 / 问题

### 类型
[ ] 协议扩展
[ ] 参考实现 bug
[ ] 文档改进
[ ] 新集成案例

### 描述
...

### 期望行为
...
```
