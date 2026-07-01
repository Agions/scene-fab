<div align="center">

<img src="assets/logo-horizontal.svg" alt="SceneFab" width="400"/>

<p><strong>AI 驱动的影视/短剧第一人称解说生产工具</strong></p>

<p>将素材理解、脚本生成、配音合成、字幕装配和平台导出串成标准化流程</p>

<br/>

[![Version](https://img.shields.io/badge/v2.4.0-06b6d4?style=flat-square&logo=git&logoColor=white)](https://github.com/Agions/scene-fab/releases)
[![Python](https://img.shields.io/badge/Python-3.10+-3b82f6?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![PySide6](https://img.shields.io/badge/PySide6-6.9+-3b82f6?style=flat-square&logo=qt&logoColor=white)](https://doc.qt.io/qtforpython/)
[![FFmpeg](https://img.shields.io/badge/FFmpeg-6.x-3b82f6?style=flat-square&logo=ffmpeg&logoColor=white)](https://ffmpeg.org/)
[![License](https://img.shields.io/badge/License-MIT-8b5cf6?style=flat-square)](LICENSE)
[![CI](https://img.shields.io/github/actions/workflow/status/Agions/scene-fab/pr-check.yml?branch=main&style=flat-square&color=22c55e&label=CI)](https://github.com/Agions/scene-fab/actions)
[![Docs](https://img.shields.io/github/actions/workflow/status/Agions/scene-fab/deploy-pages.yml?style=flat-square&color=3b82f6&label=Docs)](https://agions.github.io/scene-fab/)
[![Stars](https://img.shields.io/github/stars/Agions/scene-fab?style=flat-square&color=f59e0b)](https://github.com/Agions/scene-fab/stargazers)

<br/>

[快速开始](#快速开始) · [功能特性](#功能特性) · [架构概览](#架构概览) · [文档](#文档) · [贡献](#贡献)

</div>

---

## 目录

- [简介](#简介)
- [功能特性](#功能特性)
- [快速开始](#快速开始)
- [架构概览](#架构概览)
- [AI 模型支持](#ai-模型支持)
- [配置说明](#配置说明)
- [技术栈](#技术栈)
- [项目结构](#项目结构)
- [文档](#文档)
- [贡献](#贡献)
- [许可证](#许可证)

---

## 简介

SceneFab 是面向影视和短剧第一人称解说的生产工具。它将素材理解、脚本生成、配音合成、字幕装配和平台导出串成标准化流程，支持从单集创作到整季批量生产的完整链路。

系统围绕 DAG 并行流水线引擎构建，采用四层架构设计，支持 10 个 LLM 提供商和 8 个导出平台预设。

### 适用场景

| 场景 | 说明 |
|------|------|
| 短剧单集解说 | 30-90 秒竖屏稿，支持 Hook 生成和桥段检测 |
| 短剧整季批量 | 统一标签和关系设定，按集批量生成 |
| 电影/剧集片段解说 | 场景拆分 + 情绪峰值筛选 + 第一人称脚本 |
| 剪映继续精剪 | 导出剪映草稿，保留时间轴供二次处理 |

---

## 功能特性

### 视频理解

| 能力 | 说明 |
|------|------|
| 场景分析 | 自动识别场景切换、提取关键帧和画面摘要 |
| 人物识别 | 识别画面中的人物、推断角色关系 |
| 情绪峰值检测 | 检测冲突、反转、高潮等情绪节点 |
| 桥段检测 | 识别短剧常见桥段（打脸、逆袭、误会等） |
| StoryGraph 构建 | 构建剧情图谱，追踪人物和剧情线 |

### 解说生成

| 能力 | 说明 |
|------|------|
| 第一人称脚本 | Hook · 主体 · 反击 · 收束 · 钩子结构 |
| Hook 改写 | 自动生成多个 Hook 变体供选择 |
| 桥段模板 | 基于桥段标签自动匹配叙事模板 |
| 前情承接 | 连载模式下自动引用前集摘要 |
| 多模型复核 | 支持跨模型交叉审核脚本质量 |
| 字数约束 | 按平台和时长自动控制脚本字数 |

### 配音与字幕

| 能力 | 说明 |
|------|------|
| Edge-TTS 配音 | 多音色、语速/音调调节 |
| F5-TTS 音色克隆 | 基于参考音频克隆音色 |
| 时间戳对齐 | 配音音频自动生成字幕时间戳 |
| SRT/ASS 字幕 | 支持纯文本和完整样式两种格式 |
| 安全区控制 | 字幕自动避开平台互动栏和标题区 |

### 多平台导出

| 平台 | 画布 | 预设 |
|------|------|------|
| 抖音 | 9:16 | 1080×1920 |
| B站 | 16:9 | 1920×1080 |
| 小红书 | 9:16 | 1080×1920 |
| YouTube | 16:9 | 1920×1080 |
| TikTok | 9:16 | 1080×1920 |
| 快手 | 9:16 | 1080×1920 |
| 西瓜视频 | 16:9 | 1920×1080 |
| 微信视频号 | 9:16 | 1080×1920 |

### 批量处理

- 短剧整季批量生成
- 断点续传支持
- 并行 worker 处理
- 实时进度追踪

---

## 快速开始

### 安装

```bash
pip install scenefab
```

验证 FFmpeg：

```bash
ffmpeg -version
```

如果未安装 FFmpeg：

```bash
# macOS
brew install ffmpeg

# Ubuntu/Debian
sudo apt install ffmpeg

# Windows
# 从 https://ffmpeg.org/download.html 下载并添加到 PATH
```

### 配置

编辑 `config/llm.yaml`，填入至少一个 API Key：

```yaml
LLM:
  default_provider: "deepseek"

  deepseek:
    enabled: true
    api_key: "sk-your-deepseek-key"
    model: "deepseek-v4-pro"

  qwen:
    enabled: true
    api_key: "sk-your-qwen-key"
    model: "qwen3.7-max"
```

或使用环境变量：

```bash
export DEEPSEEK_API_KEY="sk-your-deepseek-key"
export QWEN_API_KEY="sk-your-qwen-key"
```

### 运行

```bash
# 启动 GUI
scenefab

# 查看版本
scenefab --version
```

详细安装说明请参阅 [安装指南](https://agions.github.io/scene-fab/guide/installation)。

---

## 架构概览

```text
┌─────────────────────────────────────────────────────────────┐
│                      UI 层 (PySide6)                        │
│         主窗口 · 页面 · 导航 · 主题 · 系统托盘               │
└──────────────────────────┬──────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────┐
│                    核心引擎层                                │
│    状态机 · DAG 并行流水线 · 批量处理器 · 任务模型            │
└──────────────────────────┬──────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────┐
│                   业务服务层                                 │
│  AI 服务 (LLM · Vision · TTS) · 视频服务 · 导出服务          │
└──────────────────────────┬──────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────┐
│                  基础设施层                                  │
│    事件总线 · DI 容器 · 审计日志 · 安全封装 · 配置管理        │
└─────────────────────────────────────────────────────────────┘
```

### 生产流水线

```text
视频输入
  → 场景理解 (SceneAnalyzer)
  → 剧情图谱 (StoryGraph)
  → 桥段识别 (TropeDetector)
  → 第一人称脚本 (ScriptGenerator)
  → 质量评估 (NarrationEvaluator)
  → Hook 改写 (HookRewriter)
  → 配音合成 (VoiceGenerator)
  → 字幕装配 (SubtitleAssembler)
  → 平台导出 (MultiPlatformExporter)
```

完整架构说明请参阅 [架构概览](https://agions.github.io/scene-fab/architecture)。

---

## AI 模型支持

SceneFab 支持 10 个 LLM 提供商：

| 提供商 | 推荐模型 | 用途 |
|--------|----------|------|
| DeepSeek | deepseek-v4-pro | 脚本生成（推荐） |
| Qwen (阿里云) | qwen3.7-max | 脚本生成 + 视觉理解 |
| OpenAI | gpt-5 | 脚本生成 |
| Claude (Anthropic) | claude-opus-4-6 | 脚本生成 |
| Gemini (Google) | gemini-3.1-pro | 视觉理解 |
| Kimi (月之暗面) | moonshot-v1-128k | 长文本处理 |
| GLM-5 (智谱) | glm-5-plus | 脚本生成 |
| 豆包 (字节) | doubao-pro-128k | 脚本生成 |
| 混元 (腾讯) | hunyuan-pro | 脚本生成 |
| 本地模型 (Ollama) | qwen3:32b | 离线部署 |

详细配置请参阅 [AI 模型参考](https://agions.github.io/scene-fab/ai-models)。

---

## 配置说明

SceneFab 使用两个配置文件：

### config/app_config.yaml

应用级配置（缓存、视频参数、TTS、LLM 提供商）：

```yaml
cache:
  enabled: true
  max_size: 100
  ttl: 3600

video:
  min_segment_duration: 9.0
  max_segment_duration: 60.0

tts:
  provider: "edge"
  voice: "zh-CN-XiaoxiaoNeural"
  rate: 1.0
```

### config/llm.yaml

LLM 专用配置（API Key、模型、参数）：

```yaml
LLM:
  default_provider: "deepseek"

  deepseek:
    enabled: true
    api_key: ${DEEPSEEK_API_KEY}
    model: "deepseek-v4-pro"
    max_tokens: 32768
    temperature: 0.7
```

支持环境变量替换（`${VAR_NAME}`），也可使用 `.env` 文件。

完整配置说明请参阅 [配置参考](https://agions.github.io/scene-fab/config)。

---

## 技术栈

| 组件 | 技术选型 | 用途 |
|------|----------|------|
| 桌面端 | PySide6 6.9+ | Qt 跨平台 GUI |
| 视频处理 | FFmpeg 6.x · OpenCV · MoviePy | 音视频分析与合成 |
| AI 推理 | OpenAI SDK · google-generativeai | LLM 和视觉模型调用 |
| 语音合成 | Edge-TTS · F5-TTS | 解说配音生成 |
| 场景检测 | PySceneDetect | 视频场景自动分割 |
| 数据验证 | Pydantic 2.5+ | 结构化数据校验 |
| 配置管理 | PyYAML · python-dotenv | YAML/环境变量配置 |
| 安全 | cryptography · keyring | API 密钥加密存储 |
| HTTP API | FastAPI · uvicorn | 可选 REST API 服务 |

---

## 项目结构

```text
scene-fab/
├── src/scenefab/              # 主包
│   ├── core/                  # 基础设施（事件总线 · DI · 审计 · 流水线引擎）
│   ├── models/                # 数据模型（项目 · 视频 · 叙述 · 媒体）
│   ├── services/              # 业务服务
│   │   ├── ai/                # AI 服务（LLM · 视觉 · TTS · 脚本生成）
│   │   ├── video/             # 视频服务（分析 · 处理 · 导出）
│   │   ├── export/            # 导出服务（剪映 · MP4 · 字幕）
│   │   └── video_tools/       # 视频工具（FFmpeg · 探测 · 硬件加速）
│   ├── pipeline/              # 生产流水线（状态机 · 步骤 · 评估）
│   ├── plugins/               # 插件系统（加载 · 注册 · 接口）
│   ├── api/                   # HTTP API（FastAPI 路由）
│   ├── ui/                    # 用户界面（PySide6 页面 · 主题）
│   └── utils/                 # 工具函数（安全 · 版本 · 日志）
├── tests/                     # 测试套件（755+ 测试）
├── docs/                      # VitePress 文档站
├── config/                    # 配置文件
├── resources/                 # 资源文件（图标 · 样式）
└── scripts/                   # 构建脚本
```

---

## 文档

| 文档 | 说明 |
|------|------|
| [快速开始](https://agions.github.io/scene-fab/guide/quick-start) | 3 步安装、配置和首次运行 |
| [安装指南](https://agions.github.io/scene-fab/guide/installation) | 各平台完整安装步骤 |
| [AI 配置](https://agions.github.io/scene-fab/guide/ai-configuration) | 多服务商配置详解 |
| [CLI 参考](https://agions.github.io/scene-fab/guide/cli-reference) | 命令行使用说明 |
| [Python API](https://agions.github.io/scene-fab/guide/python-api) | Python API 完整文档 |
| [生产规范](https://agions.github.io/scene-fab/guide/first-person-narration-production) | 第一人称解说完整生产流程 |
| [AI 工作流](https://agions.github.io/scene-fab/guide/ai-video-guide) | 从视频到成片的 AI 流程详解 |
| [导出发布](https://agions.github.io/scene-fab/guide/exporting) | 导出格式与平台预设 |
| [架构概览](https://agions.github.io/scene-fab/architecture) | 四层架构 · 状态机 · 数据流 |
| [AI 模型](https://agions.github.io/scene-fab/ai-models) | 模型选择与推荐配置 |
| [配置参考](https://agions.github.io/scene-fab/config) | 两文件配置结构详解 |
| [功能矩阵](https://agions.github.io/scene-fab/features) | 功能状态与适用场景 |
| [安全设计](https://agions.github.io/scene-fab/security) | 安全模型与最佳实践 |
| [疑难排查](https://agions.github.io/scene-fab/guide/troubleshooting) | 常见问题解决 |
| [常见问题](https://agions.github.io/scene-fab/faq) | FAQ |

---

## 贡献

欢迎贡献代码、报告问题或提出建议。

### 开发环境

```bash
# 克隆仓库
git clone https://github.com/Agions/scene-fab.git
cd scene-fab

# 安装开发依赖
pip install -e ".[dev]"

# 运行测试
make test

# 代码检查
make lint

# 格式化
make format
```

### 提交规范

- 使用 [Conventional Commits](https://www.conventionalcommits.org/) 格式
- 提交前运行 `make lint` 和 `make test`
- 新功能需要添加测试

### 问题反馈

- [Bug 报告](https://github.com/Agions/scene-fab/issues/new?template=bug_report.md)
- [功能建议](https://github.com/Agions/scene-fab/issues/new?template=feature_request.md)

---

## 许可证

[MIT License](LICENSE) © 2025-2026 [Agions](https://github.com/Agions)

---

<div align="center">

**[文档](https://agions.github.io/scene-fab/)** · **[更新日志](CHANGELOG.md)** · **[许可证](LICENSE)**

</div>
