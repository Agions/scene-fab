<div align="center">

<img src="assets/logo-horizontal.svg" alt="SceneFab" width="480"/>

<br/>

**从一部电影到 25 集短剧解说，AI 全程陪你一气呵成。**

<br/>

[![Version](https://img.shields.io/badge/v2.2.0-FF6B35?style=flat-square&logo=git&logoColor=white)](https://github.com/Agions/scene-fab/releases)
[![License](https://img.shields.io/badge/License-MIT-22C55E?style=flat-square)](LICENSE)
[![Stars](https://img.shields.io/github/stars/Agions/scene-fab?style=flat-square&color=FACC15)](https://github.com/Agions/scene-fab/stargazers)
[![Forks](https://img.shields.io/github/forks/Agions/scene-fab?style=flat-square&color=8B5CF6)](https://github.com/Agions/scene-fab/network/members)
[![Issues](https://img.shields.io/github/issues/Agions/scene-fab?style=flat-square&color=EF4444)](https://github.com/Agions/scene-fab/issues)

[![CI](https://img.shields.io/github/actions/workflow/status/Agions/scene-fab/pr-check.yml?branch=feature/v21-arch&style=flat-square&color=22C55E&label=CI)](https://github.com/Agions/scene-fab/actions)
[![Release](https://img.shields.io/github/actions/workflow/status/Agions/scene-fab/release-build.yml?style=flat-square&color=22C55E&label=Release)](https://github.com/Agions/scene-fab/actions)
[![Deploy](https://img.shields.io/github/actions/workflow/status/Agions/scene-fab/deploy-pages.yml?style=flat-square&color=22C55E&label=Docs)](https://agions.github.io/scene-fab/)

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python&logoColor=white)
![Qt](https://img.shields.io/badge/PySide6-6.9+-41C845?style=flat-square&logo=qt&logoColor=white)
![FFmpeg](https://img.shields.io/badge/FFmpeg-6.x-007808?style=flat-square&logo=ffmpeg&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Win%20%7C%20macOS%20%7C%20Linux-0F0C29?style=flat-square)

[**在线文档**](https://agions.github.io/scene-fab/) · [**下载安装**](https://github.com/Agions/scene-fab/releases) · [**报告问题**](https://github.com/Agions/scene-fab/issues/new) · [**功能建议**](https://github.com/Agions/scene-fab/discussions)

</div>

---

## 📑 目录

- [它是什么？](#它是什么)
- [核心能力](#核心能力)
- [快速开始](#快速开始)
- [架构](#架构)
- [技术栈](#技术栈)
- [路线图](#路线图)
- [贡献](#贡献)
- [许可证](#许可证)

---

## 它是什么？

**SceneFab** 是为自媒体解说创作者打造的 **AI 影视解说视频一站式创作工具**。

上传一部电影或短剧 → AI 自动理解视频语义 → 按情节拆条 → 生成第一人称解说稿 → 合成情感化配音 → 对齐字幕 → 输出带解说的完整视频。

### 为什么选择 SceneFab

| 痛点 | SceneFab 解法 |
|------|--------------|
| 写一篇解说稿要 2-3 小时 | DeepSeek-V4 多 LLM 联合生成，7+ 风格，分钟级出稿 |
| 配音需要专业设备 | Edge-TTS / F5-TTS 双引擎，50+ 音色 + 零样本克隆 |
| 字幕对齐手动逐句调整 | TTS Word-level Timing，50ms 精度自动对齐 |
| 短剧整季 25 集一个个做 | DAG 并行流水线，整季 15 分钟批量出 |
| 多平台尺寸不同要反复剪 | 8 平台智能适配，一键导出抖音/B站/小红书 |
| 视频文件上传到云端不安全 | **完全本地处理**，素材隐私 100% 安全 |

> **目标用户**：影视解说自媒体人 · 短剧批量生产团队 · 混剪创作者 · AI 视频工具开发者

---

## 核心能力

<table>
  <tr>
    <th align="center" width="25%">🎬 AI 语义拆条</th>
    <th align="center" width="25%">✍️ 智能解说生成</th>
    <th align="center" width="25%">🎙️ 一键配音合成</th>
    <th align="center" width="25%">📺 8 平台适配</th>
  </tr>
  <tr>
    <td align="left" valign="top">
      <b>Qwen3.7 视觉理解</b><br/>
      自动识别场景边界、人物动作、对话起止<br/>
      情感峰值选段 · 视觉×音频双维评分
    </td>
    <td align="left" valign="top">
      <b>DeepSeek-V4 · 7+ 风格</b><br/>
      第一人称视角 · 词级时间戳<br/>
      短剧 4 风格（悬疑/甜宠/复仇/逆袭）
    </td>
    <td align="left" valign="top">
      <b>Edge-TTS · F5-TTS</b><br/>
      50ms 精度字幕对齐<br/>
      零样本音色克隆 · 情感化语音
    </td>
    <td align="left" valign="top">
      <b>抖音/B站/小红书/西瓜</b><br/>
      YouTube/TikTok/快手/剪映<br/>
      AI 智能裁剪 + 平台封面
    </td>
  </tr>
  <tr>
    <th align="center">⚡ DAG 并行流水线</th>
    <th align="center">📺 短剧整季批量</th>
    <th align="center">🔒 安全加固</th>
    <th align="center">📊 数据回流</th>
  </tr>
  <tr>
    <td align="left" valign="top">
      <b>拓扑排序 + parallel_group</b><br/>
      解说/配音/封面 3 步并行<br/>
      整季 25 集 15 分钟出
    </td>
    <td align="left" valign="top">
      <b>25-50 集一键导入</b><br/>
      自动识别集数 · 断点续传<br/>
      自动重试 · 进度实时反馈
    </td>
    <td align="left" valign="top">
      <b>FFmpeg 参数白名单</b><br/>
      消除 90%+ 命令注入面<br/>
      SQLite 审计日志全程记录
    </td>
    <td align="left" valign="top">
      <b>多平台效果追踪</b><br/>
      播放/点赞/评论/完播率<br/>
      智能优化建议 · 闭环迭代
    </td>
  </tr>
</table>

---

## 快速开始

### 下载安装

前往 [Releases](https://github.com/Agions/scene-fab/releases) 页面下载：

| 平台 | 架构 | 安装包 |
|------|------|--------|
| 🪟 Windows | x64 | `SceneFab-x.x.x-x64-setup.exe` |
| 🍎 macOS | Apple Silicon | `SceneFab-x.x.x-aarch64.dmg` |
| 🍎 macOS | Intel | `SceneFab-x.x.x-x64.dmg` |
| 🐧 Linux | x64 | `SceneFab-x.x.x-x64.AppImage` |

### 从源码安装

```bash
# 克隆仓库
git clone https://github.com/Agions/scene-fab.git
cd scene-fab

# 安装依赖
pip install -e .

# 启动 GUI
scenefab gui
```

### 配置 AI（只需一个 Key）

```bash
# DeepSeek（解说生成主力）
export DEEPSEEK_API_KEY="sk-..."

# 可选：Qwen3.7（视觉理解增强）
export QWEN_API_KEY="sk-..."

# 不配置也能用：Edge-TTS 配音、字幕对齐、视频合成等基础功能全本地可用
```

### 常用命令

```bash
# 单视频解说创作
scenefab commentary create-movie ./movie.mp4 --style 纪录片 --output ./output/

# 短剧整季批量生产
scenefab batch /path/to/series/ --preset short_drama_suspense --parallel 2

# 多平台一键导出
scenefab export master.mp4 --platforms douyin,bilibili,xiaohongshu
```

---

## 架构

```
┌──────────────────────────────────────────────────────────────────┐
│                    UI 层 (PySide6 6.9)                            │
│   HomePage · 5-Step Wizard · MonitorPanel · Worker               │
└──────────────────────────┬───────────────────────────────────────┘
                           │ Signal/Slot
                           ▼
┌──────────────────────────────────────────────────────────────────┐
│                v2.x 核心引擎 (scenefab.core.*)                    │
│  ┌─────────────┐ ┌─────────────┐ ┌────────────┐ ┌────────────┐  │
│  │PipelineEngine│ │BatchProcessor│ │ SafeFFmpeg │ │AuditLogger │  │
│  │ (DAG 并行)   │ │ (批量+断点)  │ │ (白名单)   │ │ (SQLite)   │  │
│  └─────────────┘ └─────────────┘ └────────────┘ └────────────┘  │
└──────────────────────────┬───────────────────────────────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────────────────────┐
│                   业务服务层 (services/)                           │
│  ai/          LLM · Vision · TTS · ASR 适配器                    │
│  video/       FFmpeg · 帧提取 · 合成 · 缓存                      │
│  emotion/     情绪弧线分析 · 节奏检测                             │
│  cover/       智能封面 · 元数据生成                               │
│  data_feedback/ 多平台数据回流 · 效果分析                         │
│  export/      MP4 · 剪映草稿 · 8 平台导出                        │
└──────────────────────────┬───────────────────────────────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────────────────────┐
│              Models + Utils + Plugins (数据+工具)                 │
│  models/ 领域模型 │ utils/ 工具函数 │ plugins/ 插件加载           │
└──────────────────────────────────────────────────────────────────┘
```

---

## 技术栈

| 层 | 技术 |
|---|---|
| **视觉理解** | [Qwen3.7](https://help.aliyun.com/zh/model-studio/) · [Gemini 3.5 Flash](https://ai.google.dev/) |
| **解说生成** | [DeepSeek-V4](https://www.deepseek.com/) · 多 LLM Fallback |
| **语音合成** | [Edge-TTS](https://github.com/rany2/edge-tts) · [F5-TTS](https://github.com/SWivid/F5-TTS) |
| **视频处理** | [FFmpeg](https://ffmpeg.org/) · [OpenCV](https://opencv.org/) |
| **UI 框架** | [PySide6](https://doc.qt.io/qtforpython/) · Qt Design Tokens |
| **数据存储** | SQLite 3 · 本地优先 |
| **代码质量** | [Ruff](https://github.com/astral-sh/ruff) · [pytest](https://docs.pytest.org/) · GitHub Actions CI |
| **AI Agent** | Hermes Agent · MCP Protocol |

---

## 路线图

### 已完成 ✅

- v2.2.0 — AI 模型升级（Qwen3.7 / Gemini 3.5 Flash / 新 TTS）· 数据回流 · 情绪分析 · 爆款预测
- v2.1.0 — 统一架构（EventBus + DI + 类型化事件）
- v2.0.0 — DAG 并行流水线 · FFmpeg 安全加固 · 短剧批量 · 8 平台适配
- v1.1.0 — 8-Phase 架构重构 · ruff UP 规则 · 完全向后兼容

### 进行中 🚧

- [ ] Web Dashboard（轻量级远程监控 + 任务管理）
- [ ] 插件市场（用户自定义 AI Provider / TTS 音色）
- [ ] 多语言 i18n（日 / 韩 / 英 / 西）

### 未来规划 🔮

- [ ] 智能字幕翻译（保留时序的多语言翻译）
- [ ] 云端协作（项目云存储 + 多人审稿）
- [ ] 移动端预览（iOS / Android 实时预览 App）

---

## 贡献

欢迎 PR / Issue / Discussion！

1. **Fork** 本仓库
2. 创建 feature 分支（`git checkout -b feat/amazing-feature`）
3. 提交改动（遵循 [Conventional Commits](https://www.conventionalcommits.org/)）
4. 推送分支并创建 [Pull Request](https://github.com/Agions/scene-fab/pulls)

| 类型 | 用途 | 示例 |
|------|------|------|
| `feat` | 新功能 | `feat(pipeline): commentary 5-step pipeline` |
| `fix` | Bug 修复 | `fix(ci): correct vision_providers import path` |
| `perf` | 性能优化 | `perf(emotion): parallel detection + audio cache` |
| `docs` | 文档更新 | `docs(readme): professional redesign` |

---

## 许可证

[MIT License](LICENSE) · Copyright © 2025-2026 [Agions](https://github.com/Agions)

---

<div align="center">

⭐ 如果 SceneFab 对你有帮助，请给一个 Star

[🚀 下载](https://github.com/Agions/scene-fab/releases) · [📖 文档](https://agions.github.io/scene-fab/) · [🐛 Issue](https://github.com/Agions/scene-fab/issues) · [🤝 贡献](https://github.com/Agions/scene-fab/blob/main/CONTRIBUTING.md)

</div>
