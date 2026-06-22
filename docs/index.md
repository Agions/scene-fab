---
layout: home
title: SceneFab 文档中心
titleTemplate: false

hero:
  name: SceneFab
  text: 第一人称影视解说生产文档
  tagline: 面向短剧和影视解说团队的标准化手册：素材采集、标签标注、脚本生成、配音字幕、竖屏导出和发布复盘集中在一套流程里。
  image:
    src: /logo.svg
    alt: SceneFab
  actions:
    - theme: brand
      text: 查看生产流程
      link: /guide/first-person-narration-production
    - theme: alt
      text: 5 分钟上手
      link: /guide/quick-start
    - theme: alt
      text: 导出参数
      link: /guide/exporting

features:
  - icon: 文
    title: 第一人称脚本
    details: 用“我”的视角组织动机、冲突和转折，避免只复述画面。
  - icon: 标
    title: 短剧内容标签
    details: 结构化记录题材、爽点、人物关系、集数上下文和下集钩子。
  - icon: 声
    title: 配音字幕一体化
    details: 以配音时长和字幕安全区倒推脚本文字量，减少后期返工。
  - icon: 屏
    title: 竖屏交付
    details: 默认面向 1080x1920，兼顾抖音、TikTok、Shorts、小红书和 B 站竖屏。
  - icon: 质
    title: 质量门禁
    details: Hook、桥段、关系一致性、字数、字幕同步和发布参数都有验收点。
  - icon: 架
    title: 工程化流程
    details: 文档、配置、导出预设和状态机实现保持同一套生产语言。
---

<script setup>
import { withBase } from 'vitepress'
</script>

<div class="vp-doc container">

<section class="sf-section">
  <div class="sf-section-head">
    <div>
      <div class="sf-section-kicker">DOCUMENT MAP</div>
      <h2 class="sf-section-title">按工作角色进入文档</h2>
    </div>
    <p class="sf-section-copy">新版文档把使用入口、生产规范、导出参数和架构参考分开，创作者不需要先读完整工程说明。</p>
  </div>

  <div class="sf-grid cols-3">
    <a class="sf-link-card" :href="withBase('/guide/quick-start.html')">
      <div class="sf-card-label">新用户</div>
      <div class="sf-card-title">安装、配置和验证</div>
      <p class="sf-card-text">完成运行环境、API Key、基础命令和第一次启动检查。</p>
    </a>
    <a class="sf-link-card" :href="withBase('/guide/first-person-narration-production.html')">
      <div class="sf-card-label">内容团队</div>
      <div class="sf-card-title">短剧解说生产规范</div>
      <p class="sf-card-text">从素材来源到脚本、配音、字幕、竖屏导出和复盘的完整流程。</p>
    </a>
    <a class="sf-link-card" :href="withBase('/guide/exporting.html')">
      <div class="sf-card-label">发布运营</div>
      <div class="sf-card-title">平台导出与发布参数</div>
      <p class="sf-card-text">按平台控制画布、码率、字幕安全区和剪映草稿交付。</p>
    </a>
    <a class="sf-link-card" :href="withBase('/guide/ai-configuration.html')">
      <div class="sf-card-label">配置负责人</div>
      <div class="sf-card-title">AI 服务配置</div>
      <p class="sf-card-text">管理解说生成、视觉理解、ASR 和 TTS 所需的服务参数。</p>
    </a>
    <a class="sf-link-card" :href="withBase('/guide/troubleshooting.html')">
      <div class="sf-card-label">排障</div>
      <div class="sf-card-title">常见问题处理</div>
      <p class="sf-card-text">定位安装、模型、视频处理、字幕同步和导出失败。</p>
    </a>
    <a class="sf-link-card" :href="withBase('/architecture.html')">
      <div class="sf-card-label">架构审阅</div>
      <div class="sf-card-title">系统架构概览</div>
      <p class="sf-card-text">理解状态机、视频服务、AI 服务、导出服务和资源层职责。</p>
    </a>
  </div>
</section>

<section class="sf-section">
  <div class="sf-section-head">
    <div>
      <div class="sf-section-kicker">WORKFLOW</div>
      <h2 class="sf-section-title">标准生产流</h2>
    </div>
    <p class="sf-section-copy">每一步都产出可复用的结构化信息，避免脚本、配音和导出阶段反复返工。</p>
  </div>

  <div class="sf-flow">
    <div class="sf-flow-row sf-flow-head">
      <div class="sf-flow-cell">阶段</div>
      <div class="sf-flow-cell">任务</div>
      <div class="sf-flow-cell">结构化输入</div>
      <div class="sf-flow-cell">交付物</div>
    </div>
    <div class="sf-flow-row">
      <div class="sf-flow-cell sf-step-no">01</div>
      <div class="sf-flow-cell">素材导入</div>
      <div class="sf-flow-cell">来源、授权、集数、平台方向、目标时长</div>
      <div class="sf-flow-cell">可追溯素材清单</div>
    </div>
    <div class="sf-flow-row">
      <div class="sf-flow-cell sf-step-no">02</div>
      <div class="sf-flow-cell">剧情标注</div>
      <div class="sf-flow-cell">题材、爽点、人物关系、关键秘密、前情摘要</div>
      <div class="sf-flow-cell">短剧内容模型</div>
    </div>
    <div class="sf-flow-row">
      <div class="sf-flow-cell sf-step-no">03</div>
      <div class="sf-flow-cell">场景理解</div>
      <div class="sf-flow-cell">场景摘要、桥段类型、冲突强度、视觉重点</div>
      <div class="sf-flow-cell">可生成脚本的剧情上下文</div>
    </div>
    <div class="sf-flow-row">
      <div class="sf-flow-cell sf-step-no">04</div>
      <div class="sf-flow-cell">脚本生成</div>
      <div class="sf-flow-cell">第一人称视角、平台字数、Hook、结尾钩子</div>
      <div class="sf-flow-cell">可配音解说稿</div>
    </div>
    <div class="sf-flow-row">
      <div class="sf-flow-cell sf-step-no">05</div>
      <div class="sf-flow-cell">配音字幕</div>
      <div class="sf-flow-cell">语速、音色、词级时间戳、字幕安全区</div>
      <div class="sf-flow-cell">音频、字幕和时间轴</div>
    </div>
    <div class="sf-flow-row">
      <div class="sf-flow-cell sf-step-no">06</div>
      <div class="sf-flow-cell">导出发布</div>
      <div class="sf-flow-cell">画布、码率、平台预设、封面和标题方向</div>
      <div class="sf-flow-cell">成片、草稿和复盘记录</div>
    </div>
  </div>
</section>

<section class="sf-section">
  <div class="sf-section-head">
    <div>
      <div class="sf-section-kicker">SHORT DRAMA MODEL</div>
      <h2 class="sf-section-title">短剧解说必须结构化的内容</h2>
    </div>
    <p class="sf-section-copy">调研样本显示，短剧解说的成功要素集中在题材标签、关系冲突、反转爽点和连续钩子。</p>
  </div>

  <div class="sf-grid cols-2">
    <div class="sf-card">
      <div class="sf-card-title">高频标签</div>
      <div class="sf-tags">
        <span class="sf-tag">女性成长</span>
        <span class="sf-tag">都市爱情</span>
        <span class="sf-tag">打脸虐渣</span>
        <span class="sf-tag">穿越重生</span>
        <span class="sf-tag">马甲</span>
        <span class="sf-tag">家庭伦理</span>
        <span class="sf-tag">甜宠闪婚</span>
        <span class="sf-tag">战神归来</span>
      </div>
    </div>
    <div class="sf-card">
      <div class="sf-card-title">桥段优先级</div>
      <p class="sf-card-text">身份揭露、对峙冲突、打脸反转、救场、背叛、心动、结尾悬念。脚本生成和质量评估都应围绕这些桥段展开。</p>
    </div>
  </div>
</section>

<section class="sf-section">
  <div class="sf-section-head">
    <div>
      <div class="sf-section-kicker">QUALITY GATES</div>
      <h2 class="sf-section-title">上线前验收项</h2>
    </div>
    <p class="sf-section-copy">质量门禁不是后期检查表，而是贯穿脚本生成、配音和导出的生产约束。</p>
  </div>

  <div class="sf-grid cols-3">
    <div class="sf-check-card">
      <div class="sf-card-title">脚本</div>
      <div class="sf-check-list">
        <div class="sf-check-item"><span class="sf-check-dot"></span><span>前 3 秒出现冲突、身份、危险、目标或反转。</span></div>
        <div class="sf-check-item"><span class="sf-check-dot"></span><span>每 6-10 秒推进一次新信息。</span></div>
        <div class="sf-check-item"><span class="sf-check-dot"></span><span>结尾留下后果、悬念或下一集钩子。</span></div>
      </div>
    </div>
    <div class="sf-check-card">
      <div class="sf-card-title">音频字幕</div>
      <div class="sf-check-list">
        <div class="sf-check-item"><span class="sf-check-dot"></span><span>字幕不超过两行，移动端首屏可读。</span></div>
        <div class="sf-check-item"><span class="sf-check-dot"></span><span>字幕与配音偏差目标小于 50ms。</span></div>
        <div class="sf-check-item"><span class="sf-check-dot"></span><span>配音响度稳定，原声不压过解说。</span></div>
      </div>
    </div>
    <div class="sf-check-card">
      <div class="sf-card-title">发布</div>
      <div class="sf-check-list">
        <div class="sf-check-item"><span class="sf-check-dot"></span><span>默认竖屏画布 1080x1920。</span></div>
        <div class="sf-check-item"><span class="sf-check-dot"></span><span>字幕避开互动栏、标题栏和底部进度区。</span></div>
        <div class="sf-check-item"><span class="sf-check-dot"></span><span>成片、剪映草稿和复盘字段一并归档。</span></div>
      </div>
    </div>
  </div>
</section>

<section class="sf-section">
  <div class="sf-section-head">
    <div>
      <div class="sf-section-kicker">DELIVERY</div>
      <h2 class="sf-section-title">平台交付基线</h2>
    </div>
    <p class="sf-section-copy">先用统一基线减少返工，再按平台标题、封面和发布时间做运营侧差异化。</p>
  </div>

  <div class="sf-grid cols-3">
    <div class="sf-card sf-metric">
      <div class="sf-metric-value">1080x1920</div>
      <div class="sf-metric-label">短视频默认画布</div>
    </div>
    <div class="sf-card sf-metric">
      <div class="sf-metric-value">8-12 Mbps</div>
      <div class="sf-metric-label">竖屏推荐码率</div>
    </div>
    <div class="sf-card sf-metric">
      <div class="sf-metric-value">120-720 字</div>
      <div class="sf-metric-label">30-180 秒中文解说稿区间</div>
    </div>
  </div>
</section>

</div>
