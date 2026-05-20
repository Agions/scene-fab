---
layout: home

title: Voxplore
titleTemplate: false

hero:
  name: Voxplore
  text: AI First-Person Video Narrator
  tagline: 批量上传视频 · AI 自动分组选段 · 一键生成电影感配音解说
  image:
    src: /logo.png
    alt: Voxplore
  actions:
    - theme: brand
      text: 快速开始 →
      link: /guide/quick-start
    - theme: alt
      text: 查看功能
      link: /features
    - theme: alt
      text: GitHub ⭐
      link: https://github.com/Agions/Voxplore

features:
  - icon:
      src: /icons/multi-video.svg
    title: 多视频智能合并
    details: 批量上传视频，AI 视觉+声纹混合分组，避免同一人重复生成解说
  - icon:
      src: /icons/monologue.svg
    title: 第一人称片段提取
    details: 逐帧分析画面，Qwen2.5-VL 判断"我"的视角，提取情感峰值高光片段
  - icon:
      src: /icons/emotion.svg
    title: 情感峰值驱动选段
    details: 叙事完整优先 + 情感峰值加权，悬疑铺垫 → 剧情高潮 → 情感共鸣
  - icon:
      src: /icons/module.svg
    title: 模块化成品输出
    details: 合并版完整叙事 + 高光片段单独发布，最大化内容分发效率
  - icon:
      src: /icons/style.svg
    title: 7 种情感风格
    details: 治愈/悬疑/励志/怀旧/浪漫/幽默/纪录片 + 角色设定自定义
  - icon:
      src: /icons/export.svg
    title: 多格式导出
    details: H.264/H.265 MP4 直出，或原生剪映草稿 JSON，无缝继续精剪
---

<!-- Hero Float Cards (slot-based, injected by HomeLayout) -->

<!-- ── Comparison ───────────────────────────────────────────── -->
## vs 传统视频解说

<div class="vp-compare">

| 项目 | 传统方式 | Voxplore |
|------|---------|---------|
| 制作时间 | 30–120 分钟 | **3–10 分钟** |
| 配音成本 | ¥50–500/分钟 | **< ¥0.01/视频** |
| 技术门槛 | 专业剪辑 + 配音 | **上传视频，一键完成** |
| 隐私安全 | 上传第三方平台 | **视频永不上传云端** |
| 字幕同步 | 手动对齐，耗时费眼 | **TTS word-level，50ms 精度** |
| 导出格式 | 仅 MP4 | **MP4 + 剪映草稿 JSON** |

</div>

<!-- ── Why Voxplore ─────────────────────────────────────────── -->
## 为什么选择 Voxplore

<div class="vp-why-grid">

:::card ⚡ 3 分钟完成解说
从上传视频到导出成品，全流程自动化。AI 自动分析、自动写稿、自动配音，无需手动剪辑。
:::

:::card 💰 不到一分钱一个视频
DeepSeek-V4 成本约 $0.1 / 1M tokens。处理一个 5 分钟视频成本不足 **1 分钱**。
:::

:::card 🔒 视频永不上传云端
全部处理在本地完成。FFmpeg 本地合成，API 仅传输文字（解说稿），你的视频永远留在本机。
:::

:::card 🎭 7 种情感风格
治愈 · 悬疑 · 励志 · 怀旧 · 浪漫 · 幽默 · 纪录片。AI 根据视频内容自动匹配最合适的解说语气。
:::

</div>

<!-- ── 4-Step Workflow ─────────────────────────────────────── -->
## 4 步创作流程

<div class="vp-workflow">

:::step
**上传视频**
文件夹选择 / Ctrl 多选，自动扫描 mp4/mov/avi/webm
:::

→

:::step
**场景理解**
Qwen2.5-VL 逐帧分析，提取"我"的主体视角高光片段
:::

→

:::step
**情感选段**
叙事完整优先 + 情感峰值驱动，悬疑铺垫 → 高潮 → 共鸣
:::

→

:::step
**解说 + 导出**
DeepSeek-V4 生成文案 + Edge-TTS 配音，MP4 / 剪映草稿输出
:::

</div>

<!-- ── Tech Stack ────────────────────────────────────────────── -->
## 技术栈

<div class="vp-arch-table">

| 模块 | 模型 / 技术 | 说明 |
|------|-----------|------|
| 分组 | **Qwen2.5-VL** + 声纹 | 视觉 0.7 + 音频 0.3 混合相似度 |
| 提取 | **Qwen2.5-VL** | 逐帧分析，主体视角判断，9–60 秒片段 |
| 情感 | 视觉 + 音频双维度 | 画面信息密度 + 语调变化，综合评分排序 |
| 解说 | **DeepSeek-V4** | 代入"我"视角，7 种预设风格 + 角色设定 |
| 配音 | **Edge-TTS** · **F5-TTS** | Edge 主流低延迟，F5 零样本音色克隆 |
| 导出 | **MP4** · **剪映草稿** | 合并版 + 高光片段双输出 |

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
  <div class="vp-start-title">配置 DeepSeek API</div>
  <div class="vp-start-desc">每月约 ¥7 足够，处理一个 5 分钟视频不足 1 分钱</div>
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
  <span class="vp-stat-val">v1.0.1</span>
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
  <span class="vp-stat-val">&lt;¥0.01</span>
  <span class="vp-stat-lbl">单视频成本</span>
</span>

</div>

<style>
/* Hero float cards injected via layout slot */
</style>
