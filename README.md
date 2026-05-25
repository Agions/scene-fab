# SceneFab

**AI 影视解说创作工具 — 智能拆条 · AI 解说生成 · 一键配音合成**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python)](https://www.python.org/)
[![PySide6](https://img.shields.io/badge/Qt-6.5+-41C845?style=flat-square&logo=qt)](https://qt.io/)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-silver?style=flat-square)](https://github.com/Agions/scene-fab)
[![Releases](https://img.shields.io/badge/v3.0.0-10B981?style=flat-square)](https://github.com/Agions/scene-fab/releases)

---

## 定位

> **SceneFab** — 上传一部电影/短剧，AI 自动完成语义拆条、生成解说稿、合成配音，一键导出解说视频。
>
> 从「几天一条」变成「一天十条」。

| 成本 | 隐私 | 效率 |
|------|------|------|
| < ¥0.01/视频（DeepSeek-V4） | 视频永不上传云端，全本地 | 5-15 分钟/条 |

---

## 核心能力

| 能力 | 说明 |
|------|------|
| 🎬 **AI 语义拆条** | Qwen2.5-VL 理解视频语义，按情节/场景自动切分，无需手动打点 |
| 🎭 **情感峰值选段** | 视觉 + 音频双维评分，优先选取叙事高潮片段 |
| ✍️ **AI 解说稿生成** | DeepSeek-V4 生成情感丰富解说，7 种风格一键切换 |
| 🎙️ **一键配音合成** | Edge-TTS / F5-TTS，50ms 精度字幕对齐 |
| 📦 **多格式导出** | H.264/H.265 MP4 直出，或原生剪映草稿 JSON |
| 💻 **命令行原生** | pip 安装即用，支持 Agent 工作流接入（SKILL.md） |

---

## 5 步创作流程

```
上传视频（mp4/mov/avi/webm）
    │
    ▼
┌──────────────────────────────────────────┐
│  Step 1 · AI 语义拆条                      │
│  Qwen2.5-VL 视觉理解，场景边界检测          │
└──────────────────────────────────────────┘
    │
    ▼
┌──────────────────────────────────────────┐
│  Step 2 · 情感峰值选段                     │
│  视觉信息密度 × 0.6 + 音频语调 × 0.4       │
└──────────────────────────────────────────┘
    │
    ▼
┌──────────────────────────────────────────┐
│  Step 3 · 解说稿生成                       │
│  DeepSeek-V4 · 7 种情感风格               │
└──────────────────────────────────────────┘
    │
    ▼
┌──────────────────────────────────────────┐
│  Step 4 · 配音合成                         │
│  Edge-TTS / F5-TTS + 词级时间戳           │
└──────────────────────────────────────────┘
    │
    ▼
┌──────────────────────────────────────────┐
│  Step 5 · 视频合成导出                     │
│  FFmpeg H.264/H.265 · MP4 / 剪映草稿      │
└──────────────────────────────────────────┘
```

---

## 技术栈

| 模块 | 模型 / 技术 | 说明 |
|------|-----------|------|
| 语义拆条 | **Qwen2.5-VL** | 视频帧逐帧理解，语义场景边界检测 |
| 解说生成 | **DeepSeek-V4** | 第一人称视角，7 种预设风格 |
| 情感评分 | 视觉 + 音频双维 | 画面信息密度 + 语调变化，综合排序 |
| 配音合成 | **Edge-TTS** · **F5-TTS** | Edge 主流低延迟，F5 零样本音色克隆 |
| 字幕对齐 | TTS Word-level Timing | 精确到每个字的起止时间，50ms 精度 |
| 视频合成 | **FFmpeg** | H.264/H.265 编码，本地处理 |
| 导出格式 | **MP4** · **剪映草稿** | 直出发布 / 继续精剪 |

---

## 快速开始

### 安装

```bash
pip install scenefab
```

### 运行

```bash
# GUI 模式
scenefab gui

# 命令行模式
scenefab commentary create-movie ./movie.mp4 --style 纪录片 --output ./output/
```

### 配置 AI（只需一个 Key）

```bash
# DeepSeek（解说生成主力）
export DEEPSEEK_API_KEY="sk-..."

# 不配置时：Edge-TTS 配音等基础功能仍可正常使用
```

---

## 文档

| 文档 | 说明 |
|------|------|
| [快速开始](https://agions.github.io/scene-fab/guide/quick-start) | 5 分钟上手 |
| [功能详解](https://agions.github.io/scene-fab/features) | 全部功能说明 |
| [AI 工作流](https://agions.github.io/scene-fab/guide/ai-video-guide) | 5 步流水线详解 |
| [配置参考](https://agions.github.io/scene-fab/config) | 环境变量与配置文件 |
| [疑难排查](https://agions.github.io/scene-fab/guide/troubleshooting) | 常见问题 |

在线文档：**https://agions.github.io/scene-fab/**

---

## 许可证

[MIT License](LICENSE) · Copyright © 2025-2026 [Agions](https://github.com/Agions)

---

<div align="center">

⭐ 如果 SceneFab 对你有帮助，请给一个 Star

</div>
