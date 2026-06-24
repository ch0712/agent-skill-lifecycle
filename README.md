# Agent Skill Lifecycle Protocol

**让 AI Agent 在使用中自主进化，而不是每次从零开始。**

> 当前 AI Agent 的能力增长方式：被动等待开发者更新 prompt / 微调模型。
> 
> Agent Skill Lifecycle 提出一种新的可能：**Agent 在执行任务的过程中，自动将成功模式、失败教训、工作流提炼为可复用的"技能"文档，并在未来场景中自动匹配、加载、更新、淘汰。**

## 核心洞察

| 当前 Agent 的做法 | Agent Skill Lifecycle 的做法 |
|:---|:---|
| 每次任务从零开始推理每一步 | 已有技能 → 直接应用，跳过重复推理 |
| 发现错误只在当前会话修正 | 发现错误 → 写入技能 → 永久免疫 |
| 学到的经验困在上下文中，会话结束即丢失 | 经验提炼为技能 → 跨会话持久化 |
| 技能文档靠人写，过时了也没人管 | 技能自动创建、自动验证、自动淘汰 |
| 所有 Agent 使用同样一套能力 | 每个 Agent 积累自己的专属过程知识库 |

## 生态位

这不是一个框架。这是一套**协议 + 方法论 + 轻量参考实现**，可以被任何 Agent 框架（Hermes、Claude Code、Codex、LangChain、AutoGPT、CrewAI 等）集成。

### 三大组成部分

1. **SKILL.md 协议规范** — 框架无关的技能文档格式（frontmatter + markdown body）
2. **Agent Skill Lifecycle 方法论** — 一套判断标准：何时创建、何时更新、何时归档
3. **轻量参考实现** — Python 包，提供解析、验证、生命周期管理的基础能力

## 快速开始

```bash
pip install skill-protocol

# 验证一个技能文件
skill-protocol validate path/to/skill.md

# 分析技能健康状况
skill-protocol health path/to/skills-dir/

# 运行生命周期检查
skill-protocol lifecycle check path/to/skills-dir/
```

## 项目状态

🚧 **早期阶段** — 概念验证中。API 和协议仍在迭代。

## 协议

MIT License
