---
layout: home
title: SceneFab
titleTemplate: false

hero:
  name: SceneFab
  text: AI 影视解说创作工具
  tagline: 智能拆条 · AI 解说生成 · 一键配音合成
  image:
    src: /logo.svg
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
  - icon: 🎬
    title: AI 智能语义拆条
    details: 基于 Qwen2.5-VL 理解视频语义，按情节/场景自动切分，无需手动打点
  - icon: 🎙️
    title: 多风格解说生成
    details: DeepSeek-V4 生成情感丰富解说稿，7 种预设风格一键切换
  - icon: 🎭
    title: 情感峰值选段
    details: 视觉+音频双维度情感评分，优先选取叙事高潮片段
  - icon: 🔊
    title: 智能配音合成
    details: Edge-TTS / F5-TTS 文字转语音，50ms 精度字幕对齐
  - icon: 🎨
    title: 7 种情感风格
    details: 治愈 · 悬疑 · 励志 · 怀旧 · 浪漫 · 幽默 · 纪录片 + 角色自定义
  - icon: 📦
    title: 多格式导出
    details: H.264/H.265 MP4 直出，或原生剪映草稿 JSON，无缝继续精剪
---

<div class="vp-doc container">

<!-- COMPARISON TABLE -->
<div class="vp-section-header">
  <h2 class="vp-section-title">vs 传统视频剪辑软件</h2>
  <p class="vp-section-sub">从几天一条，到一天十条</p>
</div>

<div class="vp-compare">
  <div class="vp-compare-header">
    <div>项目</div>
    <div>传统方式（剪映/PR）</div>
    <div>SceneFab</div>
  </div>
  <div class="vp-compare-row">
    <div class="vp-compare-label">打点切分</div>
    <div>手动逐帧，耗时数小时</div>
    <div class="vp-compare-wins">AI 语义理解，自动拆条</div>
  </div>
  <div class="vp-compare-row">
    <div class="vp-compare-label">解说文案</div>
    <div>人工观看撰写，30 分钟+</div>
    <div class="vp-compare-wins">DeepSeek 生成，30 秒完成</div>
  </div>
  <div class="vp-compare-row">
    <div class="vp-compare-label">配音制作</div>
    <div>需配音演员或购买版权</div>
    <div class="vp-compare-wins">TTS 免费合成，任意音色</div>
  </div>
  <div class="vp-compare-row">
    <div class="vp-compare-label">制作时间</div>
    <div>1–3 小时/条</div>
    <div class="vp-compare-highlight">5–15 分钟/条</div>
  </div>
  <div class="vp-compare-row">
    <div class="vp-compare-label">导出格式</div>
    <div>仅 MP4</div>
    <div class="vp-compare-wins">MP4 + 剪映草稿 JSON</div>
  </div>
</div>

<!-- 4-STEP WORKFLOW -->
<div class="vp-section-header">
  <h2 class="vp-section-title">4 步创作流程</h2>
</div>

<div class="vp-workflow">
  <div class="vp-step">
    <div class="vp-step-num">1</div>
    <div class="vp-step-body">
      <div class="vp-step-title">上传视频</div>
      <div class="vp-step-desc">拖拽或选择文件夹，支持 mp4/mov/avi/webm</div>
    </div>
    <div class="vp-step-arrow">→</div>
  </div>
  <div class="vp-step">
    <div class="vp-step-num">2</div>
    <div class="vp-step-body">
      <div class="vp-step-title">AI 拆条</div>
      <div class="vp-step-desc">Qwen2.5-VL 逐帧理解，按情节/场景自动切分</div>
    </div>
    <div class="vp-step-arrow">→</div>
  </div>
  <div class="vp-step">
    <div class="vp-step-num">3</div>
    <div class="vp-step-body">
      <div class="vp-step-title">解说 + 配音</div>
      <div class="vp-step-desc">DeepSeek-V4 生成文案，Edge-TTS 合成配音</div>
    </div>
    <div class="vp-step-arrow">→</div>
  </div>
  <div class="vp-step">
    <div class="vp-step-num">4</div>
    <div class="vp-step-body">
      <div class="vp-step-title">导出</div>
      <div class="vp-step-desc">FFmpeg / 剪映草稿，MP4 / JSON 格式输出</div>
    </div>
  </div>
</div>

<!-- TECH STACK -->
<div class="vp-section-header">
  <h2 class="vp-section-title">技术栈</h2>
</div>

<div class="vp-arch-table">
  <div class="vp-arch-row vp-arch-header">
    <div>模块</div>
    <div>技术</div>
    <div>说明</div>
  </div>
  <div class="vp-arch-row">
    <div class="vp-arch-label">语义拆条</div>
    <div class="vp-arch-model">Qwen2.5-VL</div>
    <div>视频帧逐帧理解，语义场景边界检测</div>
  </div>
  <div class="vp-arch-row">
    <div class="vp-arch-label">解说生成</div>
    <div class="vp-arch-model">DeepSeek-V4</div>
    <div>第一人称视角，7 种预设风格</div>
  </div>
  <div class="vp-arch-row">
    <div class="vp-arch-label">配音合成</div>
    <div class="vp-arch-model">Edge-TTS / F5-TTS</div>
    <div>零样本音色克隆，50ms 字幕对齐</div>
  </div>
  <div class="vp-arch-row">
    <div class="vp-arch-label">视频合成</div>
    <div class="vp-arch-model">FFmpeg</div>
    <div>H.264/H.265 本地编码</div>
  </div>
  <div class="vp-arch-row">
    <div class="vp-arch-label">导出</div>
    <div class="vp-arch-model">MP4 · 剪映草稿</div>
    <div>直出发布 / 继续精剪</div>
  </div>
</div>

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
