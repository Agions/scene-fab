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
      text: 快速开始
      link: /guide/quick-start

features:
  - icon: 文
    title: 第一人称脚本
    details: 以"我"的视角组织动机、冲突和转折，用 Hook → 主体 → 钩子结构模板避免只复述画面。
  - icon: 标
    title: 内容标签体系
    details: 题材、爽点、人物关系、集数上下文和下集钩子全部结构化记录，支撑批量一致性。
  - icon: 声
    title: 配音字幕一体化
    details: 以配音时长和字幕安全区倒推脚本文字量，Edge-TTS / F5-TTS 双引擎支持。
  - icon: 屏
    title: 竖屏交付
    details: 默认 1080×1920 画布，预置抖音、TikTok、Shorts 和小红书竖屏规格。
  - icon: 质
    title: 质量门禁
    details: Hook、桥段、字数、字幕同步和发布参数均有可执行的验收点。
  - icon: 架
    title: 工程化流程
    details: DAG 并行引擎、事件驱动架构、审计日志和模型目录单源真相。
---

<script setup>
import { withBase } from 'vitepress'

const roleCards = [
  {
    label: '新用户',
    title: '安装与配置',
    text: '完成运行环境、API Key、基础命令和第一次启动检查。',
    link: '/guide/quick-start.html'
  },
  {
    label: '内容团队',
    title: '生产规范',
    text: '从素材来源到脚本、配音、字幕、导出和复盘的完整流程。',
    link: '/guide/first-person-narration-production.html'
  },
  {
    label: '架构审阅',
    title: '系统架构',
    text: '理解状态机、视频服务、AI 服务、导出服务和资源层职责。',
    link: '/guide/quick-start.html'
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
