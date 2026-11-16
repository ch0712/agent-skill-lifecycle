# 当前状态

## 项目进度
- Agent Skill Lifecycle Protocol：早期阶段，概念验证中
- API 和协议仍在迭代
- 已有 Python 参考实现
- 开源后 4 个月（2026-06-24 建库）**零社区反馈**：0 Star / 0 Fork / 0 Issue / 0 PR

## 活跃分支
- main（远端默认，本地新克隆期曾记 master，实为 main）

## TODO
- [ ] 完善协议规范
- [ ] 更多框架集成示例
- [ ] 仓库可发现性补齐（见下「待补」）

---

## 社区巡检（2026-10-19，子冶周报）

| 指标 | 实测值 | 数据源 |
|:--|:--|:--|
| Stars | 0 | API `stargazers_count` |
| Watchers / Subscribers | 0 / 0 | API |
| Forks | 0 | API `forks_count` + `/forks` 空数组 |
| Open Issues | 0（历史累计 0 条） | `/issues?state=all` 返回 `[]` |
| Open PRs | 0（历史累计 0 条） | `/pulls?state=all` 返回 `[]` |
| Contributors | 仅 1 人（ch0712 本人以外 0 人） | `/contributors` |
| 最近一次 push | 2026-09-12T16:06:19Z（`a4fb741` chore(team): 补入团队文档） | API `pushed_at` |
| 本地 vs 远端 | 干净，`main...origin/main` 无分歧 | `git fetch` + `status -sb` |
| PyPI 发布 | **未发布**（`/pypi/agent-skill-lifecycle/json` → 404） | PyPI API |

### 本周（10-12 ~ 10-19）新增
- 0 Issue / 0 PR / 0 Star / 0 Fork / 0 commit。**完全静默。**

### 检索曝光实测（关键发现）
- 搜索 `"agent skill lifecycle" in:name,description,readme`：共 84 个结果，本仓库排第 **6**（可被检索到）。
- 但同名前缀竞争者已占位（`agentic-skills-lifecycle-engine`、`dsh-agent-skill-lifecycle`），赛道有同类。
- **仓库 `description` 为 null、`topics` 为空数组** → 在无关键词搜索、话题页（Topic）流量入口下等于不存在。

### 诊断结论
静默的根因**不是协议质量**，而是三个分发缺口：
1. **无 description / 无 topics** — GitHub 搜索权重与 Topic 聚合全部放弃；
2. **未发布到 PyPI** — `setup.py` 已就绪但包未上架，`pip install` 这条路是死的；
3. **仓库无任何对外分发动作**（无 Release / 无 tag / 无 announcement），开源即"埋在仓库里"。

### 待补（下次开工优先顺序）
- [ ] 补 `description`（一句话：Agent 在使用中自主进化技能的协议）+ 5 个 topics（agent-skills / llm-agents / skill-library / self-improving / hermes）
- [ ] 打 v1.0.0 tag + GitHub Release（让 `watch star fork` 有落点）
- [ ] PyPI 上架（确认包名可用 → twine upload）
- [ ] 写 1 篇对外可读的落地案例（用本机 Hermes 真实技能库做 example，比空协议有说服力）

---

## 社区巡检（2026-10-26，子冶周报 · 第 2 周）

| 指标 | 实测值 | 环比 10-19 |
|:--|:--|:--|
| Stars / Watchers | 0 / 0 | 持平 |
| Forks | 0 | 持平 |
| Issues（累计/开放） | 0 / 0 | 持平 |
| PRs（累计/开放） | 0 / 0 | 持平 |
| Tags / Releases | 0 / 0 | 持平（仍无落点） |
| PyPI | 404 未发布 | 持平 |
| 最近 commit | `489245b` 2026-10-19（上周巡检自身写入） | 本周 0 commit |
| description / topics | null / `[]` | **未修** |
| `pushed_at` | 2026-10-19T02:01:36Z | 7 天无变化 |

### 本周（10-19 ~ 10-26）新增
- 0 Issue / 0 PR / 0 Star / 0 Fork / 0 commit / 0 fork 事件。**连续第 2 周完全静默。**

### 结论
静默不是本周新问题，而是**上周诊断未执行**的结果。10-19 已定位三个分发缺口
（无 description/topics、未发布 PyPI、无 tag/Release/任何对外分发动作），
本周复核这 4 个待补项**全部仍未动**。数字不会自己变，执行侧是唯一变量。

### 阻塞
- 无 GitHub PAT（`~/.hermes/.env` 中 `GITHUB_TOKEN` 处于注释态）→ traffic/views、
  popular/referrers 等需要 push 权限的流量接口无法读取，只能拿公开计数。
  补发 PAT 后可回答"到底有没有人来过"这一关键问题（0 反馈=没人来 vs 来了没转化）。

---

## 社区巡检（2026-11-02，子冶周报 · 第 3 周）

| 指标 | 实测值 | 环比 10-26 |
|:--|:--|:--|
| Stars / Watchers | 0 / 0 | 持平 |
| Forks | 0 | 持平 |
| Issues（累计/开放） | 0 / 0 | 持平 |
| PRs（累计/开放） | 0 / 0 | 持平 |
| Tags / Releases | 0 / 0 | 持平 |
| PyPI | `skill-protocol` / `agent-skill-lifecycle` / `agent-skill-lifecycle-protocol` 三个名字全部 404 | **名字仍可用，未被抢注** |
| Contributors | `[]`（空数组） | 持平 |
| 最近 push | 2026-10-26T02:00:52Z（上周周报自身 commit `9bb8faf`） | 本周 0 commit |
| description / topics | null / `[]` | **仍未修（第 3 周）** |
| GitHub 事件流 | 仅 2 条 PushEvent，均为自身巡检 | 无外部交互 |

### 本周（10-26 ~ 11-02）新增
- 0 Issue / 0 PR / 0 Star / 0 Fork / 0 commit / 0 clone（无 token，clone 数不可读）。**连续第 3 周完全静默。**

### 本周新发现：仓库自身功能存在 4 处「静默失败」（此前两周未检查到）
用本机直接跑参考实现复核，实测（命令与输出逐字记录）：

1. **CI 的 skill 校验步骤是空转门闸**
   `.github/workflows/ci.yml` 里 `validate_all('.')` → 实测 `validated 0 skills`，
   CI 打印「✅ All 0 skills valid」永远通过。
   根因：`validator.validate_all()` 只 `rglob("SKILL.md")`，而仓库唯一的示例是
   `examples/systematic-debugging.md`（非 SKILL.md 命名）→ 一个文件都没被校验。
2. **README 写的 `skill-protocol lifecycle check <dir>` 命令不存在**
   实测该命令 **exit=0 且零输出**。根因：`cli.py` 实现是 `lifecycle <dir>`，
   把字面量 `check` 当成目录名传进 `LifecycleManager('check')` → 扫不到任何文件，
   静默返回空列表，退出码仍是 0（典型 fail-silent）。
3. **`health <dir>` 对扁平 .md 目录零输出**
   实测 `health examples/` → 空输出。同理受 `_SKILL_FILENAME = "SKILL.md"` 限制，
   `lifecycle.py` 只认 SKILL.md。
4. **`setup.py` 的 `url` 指向 Gitee 私有仓**
   `url="https://gitee.com/xumijie/agent-skill-lifecycle"` — 若上 PyPI，
   主页链接会把用户导去 Gitee，而不是公开的 GitHub 仓。且缺 `long_description`
   （PyPI 页面会是空白描述）。

对照 `validate` 单文件：`validate examples/systematic-debugging.md` → `✅ Valid`，exit=0（这条是正常的）。

### 结论（第 3 周，判断变更）
前两周结论是「分发缺口 → 数字不会自己变」。本周补充一条更硬的判断：
**即使有人来，也会踩到 2 个静默失败命令（`lifecycle check` / `health`）而得不到任何反馈**。
即「0 反馈」不能全部归因于「没人来」，仓库自身的空转门闸 + 静默命令至少在
验证环节不成立。修复顺序应调到分发动作**之前**：先让 `npm/pip 装完能用`，
再谈发 tag / 上 PyPI / 写案例。

### 待办（优先级重排，第 3 版）
- [ ] P0 修 `validate_all` / `LifecycleManager` 的扫描口径（接受 `.md` 或把示例改名为 `SKILL.md`），并让 CI 在「0 个 skill 被校验」时 fail
- [ ] P0 修 CLI：`lifecycle check <dir>` 按 README 实现，未知子命令必须非 0 退出
- [ ] P1 补 `description` + 5 个 topics（此前 3 周未动）
- [ ] P1 `setup.py`：url 改 GitHub、补 `long_description`（读 README）
- [ ] P2 打 v1.0.0 tag + Release；PyPI 上架（名字已验证可用）
- [ ] P2 用本机 Hermes 真实技能库写 1 篇落地案例

### 阻塞（未变）
- 无 GitHub PAT（`~/.hermes/.env` 的 `GITHUB_TOKEN` 仍注释）→ `/traffic/views` 401，
  无法区分「没人来」vs「来了没转化」。这是回答「0 反馈根因」的唯一硬数据，建议补 PAT。

---

## 社区巡检（2026-11-09，子冶周报 · 第 4 周）

| 指标 | 实测值 | 环比 11-02 |
|:--|:--|:--|
| Stars / Watchers | 0 / 0 | 持平 |
| Forks | 0（`/forks` 空数组） | 持平 |
| Issues（累计/开放） | 0 / 0 | 持平 |
| PRs（累计/开放） | 0 / 0 | 持平 |
| Tags / Releases | 0 / 0 | 持平 |
| Contributors | `[]`（空数组） | 持平 |
| PyPI | `agent-skill-lifecycle` / `skill-protocol` / `agent-skill-lifecycle-protocol` 均 404 | 名字仍可用 |
| 最近 push | 2026-11-02T02:04:25Z（上周周报自身 commit `ae17fe7`） | 本周 0 commit |
| description / topics | null / `[]` | **仍未修（第 4 周）** |
| GitHub 事件流 | 共 3 条，全部是本账号自身 PushEvent（10-19 / 10-26 / 11-02） | 无外部交互 |
| CI | 5 次 run 全部 `success`，含 3 次纯文档 commit | 门闸从未拦下任何东西 |

### 本周（11-02 ~ 11-09）新增
- 0 Issue / 0 PR / 0 Star / 0 Fork / 0 commit / 0 外部事件。**连续第 4 周完全静默。**

### 本周复核：上周 4 处静默失败 **全部未修**，并补齐 1 条根因证据
用本机参考实现逐条重跑（`PYTHONPATH=python`，命令与输出逐字记录）：

1. `validate_all('.')` → `validated: 0`，exit=0。CI 打印「✅ All 0 skills valid」永远绿。
   根因确认：`validator.py:48` `base.rglob("SKILL.md")`，而仓库唯一示例是
   `examples/systematic-debugging.md`（不含 SKILL.md 命名）。
2. `lifecycle check examples/` → **零输出，exit=0**。根因确认：`cli.py:67` 把 `sys.argv[2]`
   当目录，字面量 `check` 被当作目录名 → 0 个技能 → 空列表 → 静默成功。
3. `lifecycle examples/`（文档所称的正确实现）→ **同样零输出，exit=0**。
   → 说明不只是 `check` 字面量问题，`_SKILL_FILENAME = "SKILL.md"`（`lifecycle.py:11`）
   这个扫描口径才是主因，两个入口一起死。
4. `health examples/` → 零输出，exit=0（同因）。
5. `setup.py:9` `url` 仍指向 `gitee.com/xumijie/agent-skill-lifecycle`（私有仓），
   且仍无 `long_description`（上 PyPI 会渲染空白描述页）。

### 本周新增发现
- **`--help` 不可用**：`skill-protocol --help` → `Unknown command: --help`，exit=1。
  只有裸执行才打印 usage。开源工具第一条命令就撞墙。
- **对照组证明核心算法没问题**：把示例复制成规范命名的 `demo/SKILL.md` 后，
  `validate-all` → `1/1 skills valid`、`health` → `9.5/10 [active]`、`lifecycle` → `keep`，全绿。
  → 缺陷 100% 在扫描口径与命令契约，不在协议/打分逻辑。修复面很小。
- CI 5 次 run 全 success（含 3 次纯文档 commit）→ 印证「空转门闸」：门闸从未有拦截能力。

### 已备好可落地补丁（**未提交，待批准**）
`/root/.hermes/workspace/ziye-drafts/2026-11-09-silent-failure-fix.patch`（174 行，4 文件）：
1. `examples/systematic-debugging.md` → `examples/systematic-debugging/SKILL.md`（让示例符合协议扫描口径）
2. `cli.py`：支持 `-h/--help/help`；`lifecycle [check] <dir>` 兼容 README 写法；
   未知命令打印 usage 并 exit 1；`validate-all/health/lifecycle` 扫到 0 个技能时 **fail loud（exit 2）**；
   `validate-all` 有非法技能时 exit 1（原来恒 0）
3. `ci.yml`：`validate_all` 返回 0 个文件时 exit 1（门闸不再空转）
4. `setup.py`：url 改 GitHub、补 `long_description`（读 README）+ `project_urls`

验证：临时副本 `/root/zy_draft` 内全部 README 命令实跑通过
（`--help` exit 0 / `validate-all` 1/1 / `health examples/` 9.5分 / `lifecycle check examples/` keep）；
`git apply --check` 对真实仓库通过，仓库工作区未被改动。

### 待办（第 4 版）
- [ ] **P0 应用上述补丁**（一条命令：`git apply` → 跑命令回归 → commit → push）
- [ ] P1 补 `description` + 5 个 topics（连续 4 周未动，是零成本流量入口）
- [ ] P2 打 v1.0.0 tag + Release；PyPI 上架（`skill-protocol` 名字仍可用）
- [ ] P2 用本机 Hermes 真实技能库写 1 篇落地案例

### 阻塞（未变）
- 无 GitHub PAT（`~/.hermes/.env:371` `GITHUB_TOKEN` 仍注释）→ `/traffic/views`、`/traffic/clones`
  401，无法区分「没人来」vs「来了没转化」。这也是判断「静默根因」的唯一硬数据。

---

## 社区巡检（2026-11-16，子冶周报 · 第 5 周）

| 指标 | 实测值 | 环比 11-09 |
|:--|:--|:--|
| Stars / Watchers | 0 / 0 | 持平 |
| Forks | 0（`/forks` 空数组） | 持平 |
| Issues（累计/开放） | 0 / 0 | 持平 |
| PRs（累计/开放） | 0 / 0 | 持平 |
| Tags / Releases | 0 / 0 | 持平 |
| Contributors | `[]` | 持平 |
| PyPI（`skill-protocol` / `agent-skill-lifecycle`） | 均 **404** | 名字仍可用，仍无包 |
| 最近 push | 2026-11-09T02:02:36Z（上周周报自身 commit `0d25a43`） | 本周 0 commit |
| description / topics | null / `[]` | **仍未修（第 5 周）** |
| GitHub 事件流 | 4 条，全部本账号 PushEvent（10-19 / 10-26 / 11-02 / 11-09） | 外部交互 0 |
| CI | 6 次 run 全 `success`（含 4 次纯文档 commit） | 门闸仍无拦截能力 |

### 本周（11-09 ~ 11-16）新增
- 0 Issue / 0 PR / 0 Star / 0 Fork / 0 commit / 0 外部事件。**连续第 5 周完全静默。**

### 本周新维度：赛道基准法（前 4 周从未做）— 一次性证伪「没人来」
用 GitHub Search API 按同义查询抓同赛道对手（`sort=stars`，实跑记录）：

| 查询 | total_count | Top 对手（★ / 描述要点） | 我们是否进前 10 |
|:--|--:|:--|:--|
| `skill lifecycle agent` | 656 | **FrancyJGLisboa/agent-skills-platform 2416★**（266 fork / 9 issue「govern their lifecycle: evidence, discovery, updates, rollback, quarantine, 17-platform distribution」）、MemTensor/skills-vote 309★（"Lifecycle Governance of Agent Skills from Collection… to Evolution"）、smixs/skill-conductor 212★、hqhq1025/skill-optimizer 193★、microsoft/SkillLens 184★ | **否** |
| `"SKILL.md" agent` | 3065 | microsoft/SkillOpt 19091★、bergside/awesome-design-skills 3669★、Illyism/seo-skills 1261★、EverMind-AI/SkillCorpus 704★ | **否** |
| `self-improving agent skills` | 361 | withkynam/vibecode-pro-max-kit 1172★、Kulaxyz/self-learning-skills 972★、pskoett/self-improving-agent 792★（116 fork / 20 条真实用户 issue） | **否** |

对手侧的真实需求信号（不是 star 泡影）：`agent-skills-platform` 266 fork + 9 条 issue（含 "--without-semantic-recon …"、
"CONTRIBUTING mandates conventional commits; the last 20 commits on main don't use it" 这类**真实使用者才会提的细节缺陷**）；
`self-improving-agent` 116 fork + 20 条 issue（版本元数据不一致、升级覆盖本地补丁等）。
→ 该赛道**有真实用户、有维护问答**，`topic:agent-skills` 这类入口对手全部填满（10~19 个 topics），我们 `[]`。

### 判断翻转（第 5 周）
前 4 周的结论一直留着一条退路：「也许赛道本来没人要」。
本周**证伪该退路**：赛道热、有 fork、有真实 issue，而我们 656 个结果里进不了前 10。
「0 反馈」的归因锁定为**纯自身原因**，且是双因叠加：

1. **不可见**：`description=null`、`topics=[]`、0 tag / 0 release、0 外部反向链接 → GitHub 站内搜索与 Topic 聚合两个入口直接出局（对手 10~19 个 topics）。
2. **不可用**（第 5 周实测仍全部成立，第 3 周发现至今 3 周未修）：
   - `skill-protocol --help` → `Unknown command: --help`，**exit=1**
   - `lifecycle check examples/` → **零输出，exit=0**
   - `health examples/` → **零输出，exit=0**
   - `validate_all('.')` → `validated 0`，**exit=0**（CI 打印「✅ All 0 skills valid」）
   - README 第一行 `pip install skill-protocol` → PyPI **404**（包从未上架）

### 差异化诚实判定（本周必须回答，否则不配再发第 6 份报告）
- **代码层不成立**：本仓可发布代码 486 行（`cli.py` 81 / `lifecycle.py` 195 / `matcher.py` 86 / `validator.py` 56 / `__init__.py` 68），
  而定位几乎重合的 `agent-skills-platform`（2025-10 建库、MIT、Python、2416★）已把
  「匹配 → 更新 → 回滚 → 隔离 → 多平台分发」整块做完。我们这层**没有对手做不到的东西**。
- **文档层成立**：`SPEC.md` 207 行（协议字段与语义）+ `METHODOLOGY.md` 221 行（何时创建/更新/归档的判据）是唯一独有的部分，
  且与 `skill:open-source-readiness-assessment` §3 的判断一致——**价值在判据，不在代码量**。
→ 本仓的正解形态是 **A 层方法论仓**（协议 + 判据 + 一份与对手的差异表），不是 B 层工具链仓。

### 待办（第 5 版，重排）
- [ ] **P0 要一个判决，不要第六条建议**：「保代码层」还是「降为 A 层方法论仓」。连着 5 周、5 版待办同一件事未决，本身已是结论。
- [ ] P0（保代码层时唯一动作，约 0.5 天）：应用 `2026-11-09-silent-failure-fix.patch`（1 条 `git apply` + 回归）→ 补 description + 5 个 topics（对齐对手：`agent-skills` / `ai-agents` / `claude-code` / `codex` / `skill-library`）→ 打 v1.0.0 + Release → PyPI 上架 `skill-protocol`（名字仍 404 可用）。
- [ ] P1 巡检频率改**月度**：连续 5 周 0 外部事件，周频产出只剩自己的 commit（`pushed_at` 一直被自己的周报刷新）。
- [ ] P2（转 A 层时）：README 首段必须写「与 agent-skills-platform / skills-vote / skill-conductor 的差异表」，写不出差异就没有存在理由。

### 阻塞（未变，第 5 周）
- 无 GitHub PAT（`~/.hermes/.env` `GITHUB_TOKEN` 仍注释）→ `/traffic/views`、`/traffic/clones` 401。
  这是区分「没人来」vs「来了没转化」的唯一硬数据；本周已用赛道基准法绕开该盲区（对手有流量证明需求存在），但仍无法量化自己。
