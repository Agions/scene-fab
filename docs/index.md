---
layout: home

title: SceneFab
titleTemplate: false

hero:
  name: SceneFab
  text: AI 影视解说创作工具
  tagline: 智能拆条 · AI 解说生成 · 一键配音合成
  image:
    src: /logo.png
    alt: SceneFab
  actions:
    - theme: brand
      text: 快速开始 →
      link: /guide/quick-start
    - theme: alt
      text: 查看功能
      link: /features
    - theme: alt
      text: GitHub ⭐
      link: https://github.com/Agions/scene-fab

features:
  - icon:
      src: /icons/multi-video.svg
    title: AI 智能语义拆条
    details: 基于 Qwen2.5-VL 理解视频语义，按情节/场景自动切分，无需手动打点
  - icon:
      src: /icons/monologue.svg
    title: 多风格解说生成
    details: DeepSeek-V4 生成情感丰富解说稿，7 种预设风格一键切换，支持角色设定
  - icon:
      src: /icons/emotion.svg
    title: 情感峰值选段
    details: 视觉+音频双维度情感评分，优先选取叙事高潮片段，打造爆款解说
  - icon:
      src: /icons/module.svg
    title: 智能配音合成
    details: Edge-TTS / F5-TTS 文字转语音，50ms 精度字幕对齐，支持音色克隆
  - icon:
      src: /icons/style.svg
    title: 7 种情感风格
    details: 治愈 · 悬疑 · 励志 · 怀旧 · 浪漫 · 幽默 · 纪录片 + 角色自定义
  - icon:
      src: /icons/export.svg
    title: 多格式导出
    details: H.264/H.265 MP4 直出，或原生剪映草稿 JSON，无缝继续精剪
---

<!-- ── Comparison ───────────────────────────────────────────── -->
## vs 传统视频剪辑软件

<div class="vp-compare">

| 项目 | 传统方式（剪映/PR） | SceneFab |
|------|------------------|---------|
| 打点切分 | 手动逐帧，耗时数小时 | **AI 语义理解，自动拆条** |
| 解说文案 | 人工观看撰写，30 分钟+ | **DeepSeek 生成，30 秒完成** |
| 配音制作 | 需配音演员或购买版权 | **TTS 免费合成，任意音色** |
| 制作时间 | 1–3 小时/条 | **5–15 分钟/条** |
| 技术门槛 | 需剪辑基础 | **上传视频，一键完成** |
| 导出格式 | 仅 MP4 | **MP4 + 剪映草稿 JSON** |

</div>

<!-- ── Why SceneFab ─────────────────────────────────────────── -->
## 为什么选择 SceneFab

<div class="vp-why-grid">

:::card ⚡ 5 分钟完成解说视频
从上传视频到导出成品，全流程 AI 自动化。语义拆条 + 自动写稿 + 配音合成，无需手动剪辑。
:::

:::card 💰 成本极低
DeepSeek-V4 成本约 ¥0.1 / 1M tokens。处理一部 2 小时电影解说，成本不足 **1 元钱**。
:::

:::card 🔒 视频永不上传云端
全部处理在本地完成。FFmpeg 本地合成，API 仅传输解说文字（不含画面），你的素材永远留在本机。
:::

:::card 🎭 7 种情感风格
治愈 · 悬疑 · 励志 · 怀旧 · 浪漫 · 幽默 · 纪录片。AI 根据内容自动匹配合适解说语气。
:::

</div>

<!-- ── 4-Step Workflow ─────────────────────────────────────── -->
## 4 步创作流程

<div class="vp-workflow">

:::step
**上传视频**
拖拽或选择文件夹，支持 mp4/mov/avi/webm，自动扫描
:::

→

:::step
**AI 语义拆条**
Qwen2.5-VL 逐帧理解，按情节/场景自动切分，智能选段
:::

→

:::step
**解说生成 + 配音**
DeepSeek-V4 生成文案，Edge-TTS/F5-TTS 合成配音
:::

→

:::step
**字幕对齐 + 导出**
TTS 词级时间戳精准对齐字幕，MP4 / 剪映草稿输出
:::

</div>

<!-- ── Core Workflow Diagram ────────────────────────────────── -->
## 核心工作流

```
视频输入
   │
   ▼
┌──────────────────────────────┐
│   Step 1 · AI 语义拆条       │
│   Qwen2.5-VL 视觉理解        │
│   场景边界检测 · 语义聚类     │
└──────────────────────────────┘
   │
   ▼
┌──────────────────────────────┐
│   Step 2 · 情感峰值选段       │
│   视觉信息密度 + 音频语调     │
│   叙事完整优先 + 情感加权     │
└──────────────────────────────┘
   │
   ▼
┌──────────────────────────────┐
│   Step 3 · 解说稿生成         │
│   DeepSeek-V4 · 第一人称视角  │
│   7 种情感风格 · 多版本备选   │
└──────────────────────────────┘
   │
   ▼
┌──────────────────────────────┐
│   Step 4 · 配音合成           │
│   Edge-TTS / F5-TTS 音色克隆  │
│   50ms 精度字幕时间戳对齐     │
└──────────────────────────────┘
   │
   ▼
┌──────────────────────────────┐
│   Step 5 · 视频合成导出       │
│   FFmpeg H.264/H.265         │
│   MP4 直出 / 剪映草稿 JSON   │
└──────────────────────────────┘
```

<!-- ── Tech Stack ────────────────────────────────────────────── -->
## 技术栈

<div class="vp-arch-table">

| 模块 | 模型 / 技术 | 说明 |
|------|-----------|------|
| 语义拆条 | **Qwen2.5-VL** | 视频帧逐帧理解，语义场景边界检测 |
| 情感评分 | 视觉 + 音频双维 | 画面信息密度 + 语调变化，综合排序 |
| 解说生成 | **DeepSeek-V4** | 第一人称视角，7 种预设风格 + 角色设定 |
| 配音合成 | **Edge-TTS** · **F5-TTS** | Edge 主流低延迟，F5 零样本音色克隆 |
| 字幕对齐 | TTS Word-level Timing | 精确到每个字的起止时间，50ms 精度 |
| 视频合成 | **FFmpeg** | H.264/H.265 编码，本地处理 |
| 导出格式 | **MP4** · **剪映草稿** | 直出发布 / 继续精剪 |

</div>

<!-- ── Quick Start ──────────────────────────────────────────── -->
## 快速开始

<div class="vp-start-grid">

<a href="/guide/quick-start" class="vp-start-card">
  <div class="vp-start-icon">🚀</div>
  <div class="vp-start-title">5 分钟快速上手</div>
  <div class="vp-start-desc">下载安装包 / Homebrew / 源码运行，三种方式任选</div>
  <div class="vp-start-arrow">→</div>
</a>

<a href="/guide/ai-configuration" class="vp-start-card">
  <div class="vp-start-icon">🔑</div>
  <div class="vp-start-title">配置 AI API</div>
  <div class="vp-start-desc">DeepSeek + Qwen API，合计约 ¥10/月，处理一部电影不足 1 元</div>
  <div class="vp-start-arrow">→</div>
</a>

<a href="/features" class="vp-start-card">
  <div class="vp-start-icon">📖</div>
  <div class="vp-start-title">功能详解</div>
  <div class="vp-start-desc">情感风格、字幕样式、导出格式、硬件要求全解析</div>
  <div class="vp-start-arrow">→</div>
</a>

</div>

<!-- ── Stats ─────────────────────────────────────────────────── -->
<div class="vp-stats-row">

<span class="vp-stat">
  <span class="vp-stat-val">v3.0.0</span>
  <span class="vp-stat-lbl">最新版本</span>
</span>
<span class="vp-stat-sep">|</span>
<span class="vp-stat">
  <span class="vp-stat-val">MIT</span>
  <span class="vp-stat-lbl">开源协议</span>
</span>
<span class="vp-stat-sep">|</span>
<span class="vp-stat">
  <span class="vp-stat-val">Python 3.10+</span>
  <span class="vp-stat-lbl">跨平台</span>
</span>
<span class="vp-stat-sep">|</span>
<span class="vp-stat">
  <span class="vp-stat-val">PySide6</span>
  <span class="vp-stat-lbl">Qt 桌面端</span>
</span>
<span class="vp-stat-sep">|</span>
<span class="vp-stat">
  <span class="vp-stat-val">&lt;¥1</span>
  <span class="vp-stat-lbl">单部电影成本</span>
</span>

</div>

<style>
/* Hero float cards injected via layout slot */
</style>
