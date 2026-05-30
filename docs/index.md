---
title: 首页
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
    details: DeepSeek-V4 生成情感丰富解说稿，7 种预设风格一键切换
  - icon:
      src: /icons/emotion.svg
    title: 情感峰值选段
    details: 视觉+音频双维度情感评分，优先选取叙事高潮片段
  - icon:
      src: /icons/module.svg
    title: 智能配音合成
    details: Edge-TTS / F5-TTS 文字转语音，50ms 精度字幕对齐
  - icon:
      src: /icons/style.svg
    title: 7 种情感风格
    details: 治愈 · 悬疑 · 励志 · 怀旧 · 浪漫 · 幽默 · 纪录片 + 角色自定义
  - icon:
      src: /icons/export.svg
    title: 多格式导出
    details: H.264/H.265 MP4 直出，或原生剪映草稿 JSON，无缝继续精剪
---

<div class="vp-doc container">

<!-- COMPARISON TABLE -->
<div class="vp-section-header">
  <h2 class="vp-section-title">vs 传统视频剪辑软件</h2>
  <p class="vp-section-sub">从几天一条，到一天十条</p>
</div>

| 项目 | 传统方式（剪映/PR） | SceneFab |
|------|------|--------|
| 打点切分 | 手动逐帧，耗时数小时 | AI 语义理解，自动拆条 |
| 解说文案 | 人工观看撰写，30 分钟+ | DeepSeek 生成，30 秒完成 |
| 配音制作 | 需配音演员或购买版权 | TTS 免费合成，任意音色 |
| 制作时间 | 1–3 小时/条 | **5–15 分钟/条** |
| 导出格式 | 仅 MP4 | MP4 + 剪映草稿 JSON |

<!-- 4-STEP WORKFLOW -->
<div class="vp-section-header">
  <h2 class="vp-section-title">4 步创作流程</h2>
</div>

| 步骤 | 操作 | 说明 |
|------|------|------|
| ① 上传 | 拖拽或选择文件夹 | 支持 mp4/mov/avi/webm |
| ② AI 拆条 | Qwen2.5-VL 逐帧理解 | 按情节/场景自动切分 |
| ③ 解说 + 配音 | DeepSeek-V4 + Edge-TTS | 生成文案，合成配音 |
| ④ 导出 | FFmpeg / 剪映草稿 | MP4 / JSON 格式输出 |

<!-- TECH STACK -->
<div class="vp-section-header">
  <h2 class="vp-section-title">技术栈</h2>
</div>

| 模块 | 技术 | 说明 |
|------|------|------|
| 语义拆条 | Qwen2.5-VL | 视频帧逐帧理解，语义场景边界检测 |
| 解说生成 | DeepSeek-V4 | 第一人称视角，7 种预设风格 |
| 配音合成 | Edge-TTS / F5-TTS | 零样本音色克隆，50ms 字幕对齐 |
| 视频合成 | FFmpeg | H.264/H.265 本地编码 |
| 导出 | MP4 · 剪映草稿 | 直出发布 / 继续精剪 |

<!-- STATS -->
<div class="vp-stats-row">
  <div class="vp-stat"><div class="vp-stat-val">v3.0.0</div><div class="vp-stat-lbl">最新版本</div></div>
  <div class="vp-stat-sep">|</div>
  <div class="vp-stat"><div class="vp-stat-val">&lt;¥1</div><div class="vp-stat-lbl">单部电影成本</div></div>
  <div class="vp-stat-sep">|</div>
  <div class="vp-stat"><div class="vp-stat-val">MIT</div><div class="vp-stat-lbl">开源协议</div></div>
  <div class="vp-stat-sep">|</div>
  <div class="vp-stat"><div class="vp-stat-val">Python 3.10+</div><div class="vp-stat-lbl">跨平台</div></div>
</div>

</div>