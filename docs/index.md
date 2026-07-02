---
layout: home
title: SceneFab 文档中心
titleTemplate: false

hero:
  name: SceneFab
  text: AI 影视解说，结构化生产
  tagline: 从素材理解到竖屏导出，用统一的状态机、质量门禁和标签体系驱动每一集产出。
  actions:
    - theme: brand
      text: 快速开始
      link: /guide/quick-start
    - theme: alt
      text: 查看功能
      link: /guide/first-person-narration-production
    - theme: alt
      text: GitHub ⭐
      link: https://github.com/Agions/scene-fab

features:
  - icon: /icons/multi-video.svg
    title: AI 智能语义拆条
    details: 基于 Qwen2.5-VL 理解视频语义，按情节/场景自动切分，无需手动打点。
  - icon: /icons/monologue.svg
    title: 多风格解说生成
    details: DeepSeek-V4 生成情感丰富解说稿，7 种预设风格一键切换。
  - icon: /icons/emotion.svg
    title: 情感峰值选段
    details: 视觉+音频双维度情感评分，优先选取叙事高潮片段。
  - icon: /icons/module.svg
    title: 智能配音合成
    details: Edge-TTS / F5-TTS 文字转语音，50ms 精度字幕对齐。
  - icon: /icons/style.svg
    title: 7 种情感风格
    details: 治愈 · 悬疑 · 励志 · 怀旧 · 浪漫 · 幽默 · 纪录片 + 角色自定义。
  - icon: /icons/export.svg
    title: 多格式导出
    details: H.264/H.265 MP4 直出，或原生剪映草稿 JSON，无缝继续精剪。
---

<script setup>
import { withBase } from 'vitepress'

const roleCards = [
  {
    label: '新用户',
    title: '安装与配置',
    text: '完成运行环境、API Key、基础命令和第一次启动检查。',
    link: '/guide/quick-start'
  },
  {
    label: '内容团队',
    title: '生产规范',
    text: '从素材来源到脚本、配音、字幕、导出和复盘的完整流程。',
    link: '/guide/first-person-narration-production'
  },
  {
    label: '架构审阅',
    title: '系统架构',
    text: '理解状态机、视频服务、AI 服务、导出服务和资源层职责。',
    link: '/guide/interface'
  }
]
</script>

<div class="vp-doc container">

<section class="sf-section">
  <div class="sf-section-head">
    <div>
      <div class="sf-section-kicker">文档地图</div>
      <h2 class="sf-section-title">按角色进入文档</h2>
    </div>
    <p class="sf-section-copy">新用户、内容团队和架构审阅者各有对应入口，无需通读全部内容。</p>
  </div>

  <div class="sf-grid cols-3">
    <a
      v-for="card in roleCards"
      :key="card.link"
      class="sf-link-card"
      :href="withBase(card.link)"
    >
      <div class="sf-card-label">{{ card.label }}</div>
      <div class="sf-card-title">{{ card.title }}</div>
      <p class="sf-card-text">{{ card.text }}</p>
    </a>
  </div>
</section>

</div>
