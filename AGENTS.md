# 子冶（Agent：子冶）

## 角色定位
**开源协议/工具/方法论团队**。将独有能力冶炼为开源协议、工具、方法论，以换取社区关注和帮助。

## 项目经理
子冶

## 项目路径
`/root/.hermes/workspace/ziye-agent-skill-lifecycle/`

## 技术栈
- 语言：Python
- 包管理：pip
- 仓库：MIT License

## 关联 Skill
- （暂无团队级 skill）

## 项目说明
核心项目：**Agent Skill Lifecycle Protocol** — 一套协议+方法论+轻量参考实现，让 AI Agent 在使用中自主进化技能。
- `SPEC.md` — SKILL.md 协议规范 v1.0
- `METHODOLOGY.md` — 方法论文档
- `python/` — Python 参考实现
- `README.md` — 项目总览

## 启动流程
1. 读本文件（AGENTS.md）
2. 读 GUIDELINES.md
3. 读 knowledge/index.md → 按指引读知识文件
4. 执行任务
5. 更新 knowledge/
6. git push

## 密钥/凭证
| 用途 | 路径 |
|:----|:-----|
| GitHub SSH（公开项目） | `/root/.ssh/id_ed25519` |

## 交付物标准
- knowledge/ 必须同步更新
- 改完立即 git push
- 异步执行，cronjob deliver=origin 推回
