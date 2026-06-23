<div align="center">

<img src="assets/logo-horizontal.svg" alt="SceneFab" width="420"/>

<br/>

### AI 影视解说视频一站式创作工具

<br/>

[![Version](https://img.shields.io/badge/v2.1.2-06b6d4?style=flat-square&logo=git&logoColor=white)](https://github.com/Agions/scene-fab/releases)
[![License](https://img.shields.io/badge/License-MIT-8b5cf6?style=flat-square)](LICENSE)
[![Stars](https://img.shields.io/github/stars/Agions/scene-fab?style=flat-square&color=f59e0b)](https://github.com/Agions/scene-fab/stargazers)
[![CI](https://img.shields.io/github/actions/workflow/status/Agions/scene-fab/pr-check.yml?branch=main&style=flat-square&color=22c55e&label=CI)](https://github.com/Agions/scene-fab/actions)
[![Docs](https://img.shields.io/github/actions/workflow/status/Agions/scene-fab/deploy-pages.yml?style=flat-square&color=3b82f6&label=Docs)](https://agions.github.io/scene-fab/)

![Python](https://img.shields.io/badge/Python-3.10+-3b82f6?style=flat-square&logo=python&logoColor=white)
![PySide6](https://img.shields.io/badge/PySide6-6.9+-3b82f6?style=flat-square&logo=qt&logoColor=white)
![FFmpeg](https://img.shields.io/badge/FFmpeg-6.x-3b82f6?style=flat-square&logo=ffmpeg&logoColor=white)
![Platform](https://img.shields.io/badge/平台-Win%20%7C%20macOS%20%7C%20Linux-3b82f6?style=flat-square)

</div>

---

## 项目简介

SceneFab 是面向影视和短剧第一人称解说的生产工具，将素材理解、脚本生成、配音合成、字幕装配和平台导出串成标准化流程。系统围绕 DAG 并行流水线引擎构建，支持从单集创作到整季批量生产的完整链路。

## 核心特性

| 能力 | 说明 |
|------|------|
| **视频语义理解** | 场景分析 · 人物识别 · 情绪峰值检测 · 桥段检测 · StoryGraph 构建 |
| **第一人称脚本** | Hook · 主体 · 反击 · 收束 · 钩子结构；多模型复核 · 字数约束 · 前情承接 |
| **配音字幕一体化** | Edge-TTS / F5-TTS 配音 · 时间戳对齐 · 字幕安全区控制 |
| **多平台导出** | 抖音 / B站 / 小红书 / YouTube / TikTok 等 8 平台预设 · 竖屏 / 横屏 |
| **批量生产** | 短剧整季批量处理 · 断点续传 · 并行 worker · 进度追踪 |
| **安全审计** | FFmpeg 安全封装 · 操作审计日志 · API 密钥加密存储 |

---

## 快速开始

```bash
# 1. 安装
pip install scenefab

# 2. 配置 API Key（至少一个）
export DEEPSEEK_API_KEY="sk-..."

# 3. 运行
scenefab
```

详细安装和配置说明请参阅[快速开始指南](https://agions.github.io/scene-fab/guide/quick-start)。

---

## 架构概览

```text
UI 层 (PySide6)  →  核心引擎 (状态机 · DAG 并行 · 批量处理)
       ↓                    ↓
业务服务层 (AI · 视频 · 导出)  →  基础设施层 (事件总线 · DI · 审计 · 配置)
```

完整架构说明请参阅[架构概览](https://agions.github.io/scene-fab/architecture)。

---

## 文档

| 文档 | 说明 |
|------|------|
| [快速开始](https://agions.github.io/scene-fab/guide/quick-start) | 3 步安装、配置和首次运行 |
| [生产规范](https://agions.github.io/scene-fab/guide/first-person-narration-production) | 第一人称解说完整生产流程 |
| [架构概览](https://agions.github.io/scene-fab/architecture) | 四层架构 · 状态机 · 数据流 |
| [AI 模型](https://agions.github.io/scene-fab/ai-models) | 模型选择与推荐配置 |
| [配置参考](https://agions.github.io/scene-fab/config) | 两文件配置结构详解 |
| [常见问题](https://agions.github.io/scene-fab/faq) | 安装、配置与使用问题解答 |

---

## 技术栈

| 组件 | 技术选型 |
|------|----------|
| 桌面端 | PySide6 6.9+ |
| 视频处理 | FFmpeg 6.x · OpenCV · MoviePy |
| AI 推理 | DeepSeek V4 · Qwen3.7 · GPT-5 · Claude · Gemini |
| 语音合成 | Edge-TTS · F5-TTS |
| 数据验证 | Pydantic 2.5+ |
| 配置管理 | PyYAML · python-dotenv |
| 安全 | cryptography · keyring |

---

## 许可证

[MIT License](LICENSE) © 2025-2026 [Agions](https://github.com/Agions)
