<div align="center">

<img src="assets/logo-horizontal.svg" alt="SceneFab" width="480"/>
<br/>

# SceneFab · AI 影视解说视频创作工具

> **上传一部短剧 → AI 自动完成 25 集整季批量生产 → 一键导出抖音/B站/小红书**
> 从「几天一条」变成「一天十条」，从「单平台发布」变成「一键多平台分发」。

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![PySide6](https://img.shields.io/badge/Qt-6.9+-41C845?style=for-the-badge&logo=qt&logoColor=white)](https://qt.io/)
[![Platform](https://img.shields.io/badge/Platform-Win%20%7C%20macOS%20%7C%20Linux-silver?style=for-the-badge)](https://github.com/Agions/scene-fab/releases)
[![Version](https://img.shields.io/badge/v2.0.0-10B981?style=for-the-badge)](https://github.com/Agions/scene-fab/releases/tag/v2.0.0)

[**在线文档**](https://agions.github.io/scene-fab/) · [**下载 v2.0.0**](https://github.com/Agions/scene-fab/releases/tag/v2.0.0) · [**报告问题**](https://github.com/Agions/scene-fab/issues/new) · [**功能建议**](https://github.com/Agions/scene-fab/discussions)

</div>

---

## 🎉 v2.0 重大更新 — 短剧解说业务特化

SceneFab v2.0 是一次面向**短剧解说**业务的重大升级，专注**批量生产**、**多平台分发**、**流水线性能**与**安全加固**。

### ⚡ 性能提升（vs v1.1.0）

| 指标 | v1.1.0 | v2.0.0 | 提升 |
|------|:---:|:---:|:---:|
| **10min 视频处理** | ~70s | **~40s** | **↓ 43%** |
| **短剧整季 25 集** | ~29min | **~15min** | **↓ 48%** |
| **LLM 首字延迟** | 20s | **< 2s** | **↓ 90%** |
| **FFmpeg 注入面** | 多处 | **0** | **↓ 100%** |

### 🚀 v2.0 八大核心能力

<table>
  <tr>
    <td align="center" width="25%">
      <h3>⚡ DAG 并行流水线</h3>
      <p><b>拓扑排序 + parallel_group</b><br/>解说生成/配音/封面 3 步并行，整季 25 集 15 分钟出</p>
    </td>
    <td align="center" width="25%">
      <h3>📺 短剧整季批量</h3>
      <p><b>25-50 集一键导入</b><br/>自动识别集数（EP01/第01集），断点续传，自动重试</p>
    </td>
    <td align="center" width="25%">
      <h3>🎬 8 平台智能适配</h3>
      <p><b>抖音/B站/小红书/西瓜/YouTube/TikTok/快手/剪映</b><br/>一键导出多版本，AI 智能裁剪 + 平台封面</p>
    </td>
    <td align="center" width="25%">
      <h3>🔒 FFmpeg 安全加固</h3>
      <p><b>参数白名单 + 注入防护</b><br/>消除 90%+ 命令注入面，审计日志全程记录</p>
    </td>
  </tr>
  <tr>
    <td align="center"><h3>📝 LLM 流式输出</h3>
      <p><b>逐 token UI 推送</b><br/>首字延迟 &lt; 2s，实时看到解说稿生成过程</p>
    </td>
    <td align="center"><h3>🎭 短剧 4 风格</h3>
      <p><b>悬疑/甜宠/复仇/逆袭</b><br/>7 桥段识别（打脸/救场/心动/反转…）</p>
    </td>
    <td align="center"><h3>📊 审计日志</h3>
      <p><b>SQLite 持久化</b><br/>所有 LLM/FFmpeg 调用可追溯</p>
    </td>
    <td align="center"><h3>🛠️ 统一 Worker 基类</h3>
      <p><b>PySide6/headless 双模式</b><br/>取消/暂停/错误传播统一封装</p>
    </td>
  </tr>
</table>

---

## 它是什么？

**SceneFab** 是为自媒体解说创作者打造的 **AI 影视解说视频一站式创作工具**。上传一部电影或短剧，AI 自动理解视频语义、按情节拆条、生成第一人称解说稿、合成情感化配音、对齐字幕、最终输出带解说的完整视频。

### 核心能力（继承自 v1.x）

<table>
  <tr>
    <td align="center" width="33%">
      <h3>🎬 AI 语义拆条</h3>
      <p><b>Qwen2.5-VL 视觉理解</b><br/>自动识别场景边界、人物动作、对话起止</p>
    </td>
    <td align="center" width="33%">
      <h3>🎭 情感峰值选段</h3>
      <p><b>视觉 × 音频双维评分</b><br/>优先挑选叙事高潮片段</p>
    </td>
    <td align="center" width="33%">
      <h3>✍️ AI 解说稿生成</h3>
      <p><b>DeepSeek-V4 · 7+ 风格</b><br/>第一人称视角，词级时间戳</p>
    </td>
  </tr>
  <tr>
    <td align="center"><h3>🎙️ 一键配音合成</h3>
      <p><b>Edge-TTS · F5-TTS</b><br/>50ms 精度字幕对齐，零样本音色克隆</p>
    </td>
    <td align="center"><h3>💻 命令行原生</h3>
      <p><b>pip install 即用</b><br/>完整 CLI + <code>SKILL.md</code> Agent 接入</p>
    </td>
    <td align="center"><h3>🔒 完全本地</h3>
      <p><b>视频文件永不上传</b><br/>全本地处理，素材隐私 100% 安全</p>
    </td>
  </tr>
</table>

## 快速开始

### 下载安装

| 平台 | 架构 | 文件 |
|------|------|------|
| **Windows** | x64 | [SceneFab-2.0.0-win-x64.exe](https://github.com/Agions/scene-fab/releases/tag/v2.0.0) |
| **macOS**   | Apple Silicon | [SceneFab-2.0.0-mac-arm64.dmg](https://github.com/Agions/scene-fab/releases/tag/v2.0.0) |
| **macOS**   | Intel | [SceneFab-2.0.0-mac-x64.dmg](https://github.com/Agions/scene-fab/releases/tag/v2.0.0) |
| **Linux**   | x64 | [SceneFab-2.0.0-linux-x64.AppImage](https://github.com/Agions/scene-fab/releases/tag/v2.0.0) |

> 📦 也可从 PyPI / 源码安装：

```bash
# PyPI（推荐用户）
pip install scenefab>=2.0.0

# 源码（推荐开发者）
git clone https://github.com/Agions/scene-fab.git
cd scene-fab
pip install -e .
```

### 运行

```bash
# 启动 GUI
scenefab gui

# 短剧整季批量生产（v2.0 新增）
scenefab batch /path/to/series/ --preset short_drama_suspense --parallel 2

# 多平台一键导出（v2.0 新增）
scenefab export master.mp4 --platforms douyin,bilibili,xiaohongshu

# 单视频解说创作
scenefab commentary create-movie ./movie.mp4 --style 纪录片 --output ./output/
```

### 配置 AI（只需一个 Key）

```bash
# DeepSeek（解说生成主力）
export DEEPSEEK_API_KEY="sk-..."

# 可选：Qwen2.5-VL（视觉理解）
export QWEN_API_KEY="sk-..."

# 不配置也能用：Edge-TTS 配音、字幕对齐、视频合成等基础功能全本地可用
```

## 架构

SceneFab v2.0 采用 **分层 + 模块化** 架构，8 个 v2.0 新核心模块（`scenefab.core.*`）与 v1.x 服务层无缝集成：

```
┌────────────────────────────────────────────────────────────────────┐
│                🎬 SceneFab v2.0 Architecture                        │
└────────────────────────────────────────────────────────────────────┘

   ┌──────────────────────────────────────────────────────────┐
   │            UI 层 (PySide6 6.9 + Design Tokens)            │
   │   HomePage · 5-Step Wizard · MonitorPanel · Worker       │
   │   ↓ Signal/Slot                                            │
   └──────────────────────────────────────────────────────────┘
                              │
                              ▼
   ┌──────────────────────────────────────────────────────────┐
   │       v2.0 核心引擎 (scenefab.core.*)                     │
   │                                                            │
   │  ┌─────────────────┐  ┌─────────────────┐  ┌────────────┐ │
   │  │ PipelineEngine  │  │ BatchProcessor  │  │ BaseWorker │ │
   │  │ (DAG 并行)      │  │ (批量+断点)      │  │ (统一基类) │ │
   │  └─────────────────┘  └─────────────────┘  └────────────┘ │
   │  ┌─────────────────┐  ┌─────────────────┐  ┌────────────┐ │
   │  │ SafeFFmpegCmd   │  │ AuditLogger     │  │ShortDrama  │ │
   │  │ (白名单+审计)    │  │ (SQLite 审计)    │  │ Narrator   │ │
   │  └─────────────────┘  └─────────────────┘  └────────────┘ │
   │  ┌─────────────────┐  ┌─────────────────┐                 │
   │  │PlatformAdapter  │  │ StreamingLLM    │                 │
   │  │ (8 平台适配)     │  │ Worker (流式)   │                 │
   │  └─────────────────┘  └─────────────────┘                 │
   └──────────────────────────────────────────────────────────┘
                              │
                              ▼
   ┌──────────────────────────────────────────────────────────┐
   │            v1.x Services (业务服务层)                     │
   │                                                            │
   │  services/ai/        LLM / Vision / TTS / ASR 适配器      │
   │  services/video/     FFmpeg / 帧提取 / 合成 / 缓存        │
   │  services/audio/     音频处理 / 字幕对齐                  │
   │  services/export/    MP4 / 剪映草稿 / 平台导出             │
   │  services/orchestration/  任务调度 / 项目管理             │
   └──────────────────────────────────────────────────────────┘
                              │
                              ▼
   ┌──────────────────────────────────────────────────────────┐
   │          Models + Utils + Plugins (数据+工具)             │
   │   models/ 枚举 + 领域模型 │ utils/ 工具函数                │
   │   interfaces/ 抽象接口    │ plugins/ 插件加载              │
   └──────────────────────────────────────────────────────────┘
```

更详细的架构文档请见 [在线文档 - 架构](https://agions.github.io/scene-fab/dev/architecture) 与 [ADR 决策记录](https://github.com/Agions/scene-fab/tree/main/docs/adr)。

## 技术栈

| 模块 | 模型 / 技术 | 说明 |
|------|------------|------|
| **v2.0 DAG 流水线** | ThreadPoolExecutor + 拓扑排序 | 短剧整季并行处理 ↓48% |
| **v2.0 审计日志** | SQLite 3 | LLM/FFmpeg 调用全程追溯 |
| **v2.0 FFmpeg 封装** | 参数白名单 + 危险字符检测 | 消除 90%+ 命令注入面 |
| 语义拆条 | **Qwen2.5-VL** | 视频帧逐帧理解，语义场景边界检测 |
| 解说生成 | **DeepSeek-V4** | 第一人称视角，7+ 预设风格 + 短剧 4 风格 |
| 情感评分 | 视觉 + 音频双维 | 画面信息密度 + 语调变化 |
| 配音合成 | **Edge-TTS** · **F5-TTS** | Edge 主流低延迟，F5 零样本音色克隆 |
| 字幕对齐 | TTS Word-level Timing | 精确到每个字的起止时间，50ms 精度 |
| 视频合成 | **FFmpeg** | H.264/H.265 编码，本地处理 |
| 多平台导出 | **v2.0 PlatformAdapter** | 8 平台 (抖音/B站/小红书/西瓜/YouTube/TikTok/快手/剪映) |
| UI 框架 | **PySide6 6.9** | Qt for Python，原生桌面体验 |
| 状态管理 | **PyQt Signal/Slot** | 跨组件解耦，事件驱动 |

## 短剧解说业务流

v2.0 为短剧（1-3 分钟/集，整季 25-50 集）业务做了深度优化：

```
┌─────────────────────────────────────────────────────────────┐
│        短剧整季批量生产 (v2.0 Short Drama Mode)              │
└─────────────────────────────────────────────────────────────┘

   INPUT:  /series/重生女王归来/
     ├── EP01.mp4  ─┐
     ├── EP02.mp4  ─┤
     ├── ...        ├─→ 自动识别集数 + 剧情连贯性分析
     └── EP25.mp4  ─┘
                              │
                              ▼
   ┌─────────────────────────────────────────────────────────┐
   │ Phase 1: 全局预分析（一次性，整季共享）                   │
   │   · 快速扫描 → 剧情时间线                                  │
   │   · 主角团识别 → 角色关系图谱                              │
   │   · 提取高光时刻 → 高潮索引                                │
   └─────────────────────────────────────────────────────────┘
                              │
                              ▼
   ┌─────────────────────────────────────────────────────────┐
   │ Phase 2: 并行批量处理（2-4 集并行）                       │
   │   Worker 1: EP01 → EP03 → EP05 ...                        │
   │   Worker 2: EP02 → EP04 → EP06 ...                        │
   │   每集：拆条→桥段识别→解说→配音→合成（v2.0 DAG 并行）    │
   └─────────────────────────────────────────────────────────┘
                              │
                              ▼
   ┌─────────────────────────────────────────────────────────┐
   │ Phase 3: 整季后处理 + 多平台分发                          │
   │   · 统一封面风格（视觉一致性）                             │
   │   · 整季剧情摘要                                          │
   │   · 一键导出 8 平台版本（v2.0 PlatformAdapter）            │
   └─────────────────────────────────────────────────────────┘
                              │
                              ▼
   OUTPUT:
     output/重生女王归来/
       ├── douyin/      # 抖音 9:16 竖屏
       ├── bilibili/    # B站 16:9 横屏
       ├── xiaohongshu/ # 小红书 3:4
       ├── xigua/       # 西瓜视频 16:9
       ├── youtube/     # YouTube 16:9
       └── jianying/    # 剪映草稿 (可二次编辑)
```

## 文档

| 文档 | 说明 |
|------|------|
| [快速开始](https://agions.github.io/scene-fab/guide/quick-start) | 5 分钟上手 |
| [功能详解](https://agions.github.io/scene-fab/features) | 全部功能说明 |
| [AI 工作流](https://agions.github.io/scene-fab/guide/ai-video-guide) | 5 步流水线详解 |
| [架构设计](https://agions.github.io/scene-fab/dev/architecture) | 模块划分 + 数据流 |
| [ADR 决策记录](https://github.com/Agions/scene-fab/tree/main/docs/adr) | 5 篇架构决策（v2.0） |
| [配置参考](https://agions.github.io/scene-fab/config) | 环境变量与配置文件 |
| [疑难排查](https://agions.github.io/scene-fab/guide/troubleshooting) | 常见问题 |

**在线文档：https://agions.github.io/scene-fab/**

## 路线图

### ✅ v2.0.0 (2026-06-04) — 当前版本

- [x] **DAG 并行流水线引擎**（拓扑排序 + parallel_group + always_run）
- [x] **FFmpeg 安全封装**（参数白名单 + 注入防护 + 审计集成）
- [x] **操作审计日志**（SQLite 持久化）
- [x] **批量任务处理器**（并行 + 断点续传 + 自动重试）
- [x] **短剧解说特化**（4 风格 + 7 桥段识别 + 整季批量）
- [x] **多平台智能适配**（8 平台 + 智能裁剪 + 平台封面）
- [x] **统一 Worker 基类**（PySide6/headless 双模式）
- [x] **LLM 流式输出**（逐 token 推送 + 句子边界检测）
- [x] **5 篇架构决策记录**（ADR-001 ~ 005）

### ✅ v1.1.0 (2026-06-02) — 8-Phase 架构重构

- [x] 8-Phase 架构重构（类型统一、兼容层清理、大文件拆分）
- [x] 启用 ruff `UP` (pyupgrade) 规则（1573 个 lint 错误清零）
- [x] 完全向后兼容 v1.0.x

### 🚧 进行中

- [ ] Web Dashboard（轻量级远程监控 + 任务管理）
- [ ] 插件市场（用户自定义 AI Provider / TTS 音色）
- [ ] 多语言 i18n（日 / 韩 / 英 / 西 4 语言界面）

### 🔮 未来规划

- [ ] 直播解说模式（实时视频流接入 + 低延迟 AI 解说）
- [ ] 智能字幕翻译（保留时序的多语言翻译）
- [ ] 云端协作（项目云存储 + 多人审稿）
- [ ] 移动端预览（iOS / Android 实时预览 App）

## 贡献

欢迎 PR / Issue / Discussion！请遵循以下流程：

1. **Fork** 本仓库
2. 创建 feature 分支（`git checkout -b feat/amazing-feature`）
3. 提交改动（[Conventional Commits](https://www.conventionalcommits.org/) 规范）：
   ```
   feat: 新功能
   fix:  bug 修复
   docs: 文档更新
   style: 格式调整（无逻辑变化）
   refactor: 重构（无新功能/无 bug 修复）
   perf: 性能优化
   test: 测试
   chore: 构建/工具链
   ```
4. 推送分支（`git push origin feat/amazing-feature`）
5. 创建 [Pull Request](https://github.com/Agions/scene-fab/pulls)

## 致谢

SceneFab 的诞生离不开以下开源项目：

- [PySide6](https://doc.qt.io/qtforpython-6/) — Qt for Python，桌面 UI 框架
- [Qwen2.5-VL](https://github.com/QwenLM/Qwen2.5-VL) — 阿里通义千问视觉语言模型
- [DeepSeek](https://www.deepseek.com/) — 高性价比中文 LLM
- [Edge-TTS](https://github.com/rany2/edge-tts) — 微软 Edge 文本转语音
- [F5-TTS](https://github.com/SWivid/F5-TTS) — 零样本语音克隆
- [FFmpeg](https://ffmpeg.org/) — 视频处理瑞士军刀
- [Ruff](https://github.com/astral-sh/ruff) — 极速 Python linter
- [orjson](https://github.com/ijl/orjson) — 高性能 JSON 序列化
- [pytest](https://docs.pytest.org/) — 测试框架

## 许可证

[MIT License](LICENSE) · Copyright © 2025-2026 [Agions](https://github.com/Agions)

---

<div align="center">

⭐ 如果 SceneFab 对你有帮助，请给一个 Star · 🐛 遇到问题请提交 [Issue](https://github.com/Agions/scene-fab/issues)

[🚀 立即下载 v2.0.0](https://github.com/Agions/scene-fab/releases/tag/v2.0.0) · [📖 阅读 ADR](https://github.com/Agions/scene-fab/tree/main/docs/adr) · [🤝 加入贡献](https://github.com/Agions/scene-fab/blob/main/CONTRIBUTING.md)

</div>
