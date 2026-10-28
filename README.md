# Creator Agent Skills

**给中文创作者的 AI Agent 技能包：公众号写稿、小红书笔记、封面标题、短视频脚本、每日新闻选题 — 5 个拿来就能用的 SKILL.md，兼容 Claude Code / Codex 等支持 Skills 的 Agent。**

**Agent skills for Chinese content creators: WeChat writing, Xiaohongshu notes, cover/title hooks, short-video scripts and daily news topic selection.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 为什么 / Why

Agent Skills 是现在 GitHub 上最热的品类，但绝大多数是给程序员的。创作者的活 — 写稿、起标题、做封面文案、写短视频脚本 — 同样是固定流程，同样值得被写成技能：把踩过的坑变成硬规则（不编事实、争议说法要归因、标题不许把传闻写成事实），Agent 每次都照着做，而不是每次看运气。

这 5 个技能都来自一个日更 7–8 篇的真实公众号生产流程，不是凭空编的模板。

## 技能清单 / Skills

| 技能 | 做什么 |
|---|---|
| `wechat-article-writer` | 从核实过的事实清单写公众号待审稿：固定分节、只用给定事实、来源小字 |
| `xiaohongshu-note` | 把内容改成小红书笔记包：标题组、正文、逐张卡片文案（3:4）、话题标签 |
| `cover-title-hook` | 标题和封面文案：把真实冲突推到最尖锐但诚实的形式，给封面断行版 |
| `short-video-script` | 30–90 秒短视频脚本：钩子、分段口播、屏幕字、封面文案 |
| `daily-news-brief` | 每日国际新闻选题：扫描、去重、按读者影响排序，输出带来源的事实点 |

## 安装 / Install

把 `skills/` 下你需要的技能文件夹复制到你的 Agent 技能目录，例如 Claude Code：

```bash
cp -r skills/wechat-article-writer ~/.claude/skills/
cp -r skills/cover-title-hook ~/.claude/skills/
```

其他支持 SKILL.md 规范的 Agent 同理。装好后直接对 Agent 说“用 wechat-article-writer 帮我把这组事实写成公众号稿”，它就会按技能里的流程和硬规则执行。

## 校验 / Validate

仓库自带校验器，贡献新技能前先跑：

```bash
python3 validate_skills.py
# 检查每个 SKILL.md 的 frontmatter、name 与文件夹一致性、描述长度和正文完整度
```

## 配套工具 / Companion tools

同系列的另外两个开源工具，正好和这些技能接上：

- [WeChat Creator Kit](https://github.com/Yangdingcheng/wechat-creator-kit) — 低成本公众号写稿流水线（程序版）
- [Social Card Forge](https://github.com/Yangdingcheng/social-card-forge) — 一份内容生成全平台尺寸卡片
- [SlideForge](https://github.com/Yangdingcheng/slideforge) — Markdown 一键转可编辑 PPT

## Contributing

欢迎 PR 新技能（其他平台、其他垂类都行）：一个文件夹 + 一个 SKILL.md，跑通 `validate_skills.py` 即可。规则要具体、能执行，别写空泛的“写得好一点”。

## License

MIT
