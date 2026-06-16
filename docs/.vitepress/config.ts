import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'SceneFab',
  description: 'SceneFab 第一人称影视/短剧解说生产文档，覆盖素材、脚本、配音、字幕、导出和发布复盘。',
  base: '/scene-fab/',
  lang: 'zh-CN',
  cleanUrls: false,
  ignoreDeadLinks: true,
  lastUpdated: true,

  head: [
    // Favicon
    ['link', { rel: 'icon', type: 'image/svg+xml', href: '/favicon.svg' }],
    ['link', { rel: 'alternate icon', type: 'image/png', href: '/logo.png' }],

    // SEO
    ['meta', { name: 'keywords',      content: '短剧解说,第一人称解说,影视解说,AI脚本,自动配音,AI字幕,竖屏导出,SceneFab' }],
    ['meta', { name: 'author',        content: 'Agions' }],
    ['meta', { name: 'robots',        content: 'index, follow' }],

    // Open Graph
    ['meta', { property: 'og:type',        content: 'website' }],
    ['meta', { property: 'og:title',       content: 'SceneFab 文档中心 — 第一人称影视解说生产流程' }],
    ['meta', { property: 'og:description', content: '面向短剧和影视解说团队的标准化生产文档：素材、脚本、配音、字幕、导出和发布复盘。' }],
    ['meta', { property: 'og:image',       content: 'https://agions.github.io/scene-fab/og-image.png' }],
    ['meta', { property: 'og:url',         content: 'https://agions.github.io/scene-fab/' }],
    ['meta', { property: 'og:site_name',   content: 'SceneFab' }],

    // Twitter / X
    ['meta', { name: 'twitter:card',        content: 'summary_large_image' }],
    ['meta', { name: 'twitter:title',       content: 'SceneFab 文档中心' }],
    ['meta', { name: 'twitter:description', content: '第一人称影视/短剧解说标准化生产流程。' }],
    ['meta', { name: 'twitter:image',       content: 'https://agions.github.io/scene-fab/og-image.png' }],

    // Theme
    ['meta', { name: 'theme-color', content: '#111210' }],
    ['meta', { name: 'color-scheme', content: 'dark' }],
  ],

  markdown: {
    lineNumbers: false,
    theme: {
      light: 'github-light',
      dark:  'github-dark',
    },
    container: {
      tipLabel: '💡 提示',
      warningLabel: '⚠️ 注意',
      dangerLabel: '🚨 危险',
      infoLabel: 'ℹ️ 信息',
      detailsLabel: '详情',
    },
  },

  themeConfig: {
    // ── Logo & Site Title ──────────────────────────────────
    logo:         '/logo.png',
    siteTitle:    'SceneFab',
    appearance:   'dark',

    // ── Last Updated ────────────────────────────────────────
    lastUpdated: {
      text: '最后更新',
      formatOptions: {
        dateStyle: 'medium',
        timeStyle: 'short',
      },
    },

    // ── Search ──────────────────────────────────────────────
    search: {
      provider: 'local',
      options: {
        placeholder: '搜索文档...',
        translations: {
          button: {
            buttonText:              '搜索',
            buttonAriaLabel:          '搜索文档',
          },
          modal: {
            noResultsText:     '未找到结果',
            resetButtonTitle:  '清除搜索',
            footerSectionText: {
              displayDetails: '按 ↑↓ 导航，Enter 选择',
            },
          },
        },
      },
    },

    // ── Navigation ──────────────────────────────────────────
    nav: [
      { text: '首页',          link: '/' },
      {
        text: '上手',
        items: [
          { text: '5 分钟上手',     link: '/guide/quick-start' },
          { text: '安装指南',        link: '/guide/installation' },
          { text: 'AI 配置',         link: '/guide/ai-configuration' },
          { text: '界面说明',        link: '/guide/interface' },
        ],
      },
      {
        text: '生产流程',
        items: [
          { text: '第一人称生产规范', link: '/guide/first-person-narration-production' },
          { text: 'AI 工作流',       link: '/guide/ai-video-guide' },
          { text: '导出发布',        link: '/guide/exporting' },
          { text: '功能边界',        link: '/features' },
        ],
      },
      {
        text: '参考',
        items: [
          { text: '架构概览',        link: '/architecture' },
          { text: 'AI 模型',         link: '/ai-models' },
          { text: '安全设计',        link: '/security' },
          { text: '配置参考',        link: '/config' },
        ],
      },
      {
        text: '帮助',
        items: [
          { text: '疑难排查',        link: '/guide/troubleshooting' },
          { text: 'FAQ',             link: '/faq' },
        ],
      },
    ],

    // ── Sidebar ────────────────────────────────────────────
    sidebar: {
      '/guide/': [
        {
          text: '上手',
          items: [
            { text: '5 分钟快速开始',    link: '/guide/quick-start' },
            { text: '安装指南',            link: '/guide/installation' },
            { text: 'AI 配置指南',         link: '/guide/ai-configuration' },
          ],
        },
        {
          text: '生产流程',
          items: [
            { text: '第一人称生产规范',    link: '/guide/first-person-narration-production' },
            { text: 'AI 工作流详解',      link: '/guide/ai-video-guide' },
            { text: '界面介绍',            link: '/guide/interface' },
            { text: '导出格式',            link: '/guide/exporting' },
          ],
        },
        {
          text: '疑难解答',
          items: [
            { text: '常见问题 FAQ',        link: '/faq' },
            { text: '疑难排查',            link: '/guide/troubleshooting' },
          ],
        },
      ],

      '/': [
        {
          text: '文档入口',
          items: [
            { text: '首页',              link: '/' },
            { text: '快速开始',          link: '/guide/quick-start' },
          ],
        },
        {
          text: '上手与配置',
          items: [
            { text: '5 分钟上手',        link: '/guide/quick-start' },
            { text: '完整安装',          link: '/guide/installation' },
            { text: '配置 API Key',      link: '/guide/ai-configuration' },
          ],
        },
        {
          text: '生产流程',
          items: [
            { text: '第一人称生产规范',    link: '/guide/first-person-narration-production' },
            { text: 'AI 工作流详解',      link: '/guide/ai-video-guide' },
            { text: '界面介绍',           link: '/guide/interface' },
            { text: '导出格式',           link: '/guide/exporting' },
          ],
        },
        {
          text: '参考',
          items: [
            { text: 'AI 模型',            link: '/ai-models' },
            { text: '架构概览',           link: '/architecture' },
            { text: '安全设计',           link: '/security' },
          ],
        },
        {
          text: '帮助',
          items: [
            { text: '常见问题',           link: '/faq' },
            { text: '疑难排查',           link: '/guide/troubleshooting' },
          ],
        },
      ],

      '/ai-models': [
        {
          text: 'AI 模型',
          items: [
            { text: 'AI 模型总览',         link: '/ai-models' },
          ],
        },
      ],
    },

    // ── Table of Contents ──────────────────────────────────
    outline: {
      level: [2, 3],
      label: '目录',
    },

    // ── Doc Footer (prev/next) ──────────────────────────────
    docFooter: {
      prev: '上一篇',
      next: '下一篇',
    },

    // ── Footer ──────────────────────────────────────────────
    footer: {
      message: 'SceneFab 文档中心 · 面向影视/短剧第一人称解说生产',
      copyright: 'Copyright © 2025-2026 Agions · 隐私优先 · 本地处理',
    },

    // ── Return to Top ────────────────────────────────────────
    returnToTopLabel: '返回顶部',
    sidebarMenuLabel: '菜单',

    // ── Not Found (404) ────────────────────────────────────
    notFound: {
      title: '页面未找到',
      quote: '你来到了一片空白的领域。',
      linkText: '返回首页',
    },
  },

  // ── Sitemap ────────────────────────────────────────────────
    sitemap: {
    hostname: 'https://agions.github.io/scene-fab/',
    lastmodDateOnly: true,
  },
})
