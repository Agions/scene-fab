import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'SceneFab',
  description: 'AI 影视解说创作工具 — 智能拆条 · AI 解说生成 · 一键配音合成。Qwen2.5-VL + DeepSeek-V4 + Edge-TTS。',
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
    ['meta', { name: 'keywords',      content: 'AI影视解说,智能拆条,自动配音,AI字幕,视频剪辑,SceneFab,DeepSeek,Qwen,Edge-TTS,短视频创作' }],
    ['meta', { name: 'author',        content: 'Agions' }],
    ['meta', { name: 'robots',        content: 'index, follow' }],

    // Open Graph
    ['meta', { property: 'og:type',        content: 'website' }],
    ['meta', { property: 'og:title',       content: 'SceneFab — AI 影视解说创作工具' }],
    ['meta', { property: 'og:description', content: '智能拆条 · AI 解说生成 · 一键配音合成，让影视解说创作从几天一条变成一天十条' }],
    ['meta', { property: 'og:image',       content: 'https://agions.github.io/scene-fab/og-image.png' }],
    ['meta', { property: 'og:url',         content: 'https://agions.github.io/scene-fab/' }],
    ['meta', { property: 'og:site_name',   content: 'SceneFab' }],

    // Twitter / X
    ['meta', { name: 'twitter:card',        content: 'summary_large_image' }],
    ['meta', { name: 'twitter:title',       content: 'SceneFab — AI 影视解说创作工具' }],
    ['meta', { name: 'twitter:description', content: '智能拆条 · AI 解说生成 · 一键配音合成' }],
    ['meta', { name: 'twitter:image',       content: 'https://agions.github.io/scene-fab/og-image.png' }],

    // Theme
    ['meta', { name: 'theme-color', content: '#070B12' }],
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

    // ── Edit Link ──────────────────────────────────────────
    editLink: {
      pattern: 'https://github.com/Agions/scene-fab/edit/main/docs/:path',
      text: '在 GitHub 上编辑此页面',
    },

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
      { text: '功能介绍',      link: '/features' },
      {
        text: '快速开始',
        items: [
          { text: '5 分钟上手',     link: '/guide/quick-start' },
          { text: '完整安装指南',     link: '/guide/installation' },
          { text: '配置 API Key',    link: '/guide/ai-configuration' },
        ],
      },
      {
        text: '核心教程',
        items: [
          { text: 'AI 工作流详解',   link: '/guide/ai-video-guide' },
          { text: '第一人称生产规范', link: '/guide/first-person-narration-production' },
          { text: '导出格式',        link: '/guide/exporting' },
          { text: '界面介绍',        link: '/guide/interface' },
        ],
      },
      {
        text: '参考',
        items: [
          { text: 'AI 模型',         link: '/ai-models' },
          { text: '疑难排查',        link: '/guide/troubleshooting' },
          { text: '架构概览',        link: '/architecture' },
        ],
      },
      {
        text: '更多',
        items: [
          { text: '安全设计',        link: '/security' },
          { text: 'FAQ',             link: '/faq' },
          { text: '贡献指南',        link: '/contributing' },
        ],
      },
      {
        text: 'GitHub ⭐',
        link: 'https://github.com/Agions/scene-fab',
      },
    ],

    // ── Sidebar ────────────────────────────────────────────
    sidebar: {
      '/guide/': [
        {
          text: '快速入门',
          items: [
            { text: '5 分钟快速开始',    link: '/guide/quick-start' },
            { text: '完整安装指南',        link: '/guide/installation' },
            { text: '界面介绍',            link: '/guide/interface' },
          ],
        },
        {
          text: '核心教程',
          items: [
            { text: 'AI 工作流详解',      link: '/guide/ai-video-guide' },
            { text: '第一人称生产规范',    link: '/guide/first-person-narration-production' },
            { text: 'AI 配置指南',         link: '/guide/ai-configuration' },
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
          text: '入门',
          items: [
            { text: '首页',              link: '/' },
            { text: '快速开始',          link: '/guide/quick-start' },
            { text: '功能介绍',          link: '/features' },
          ],
        },
        {
          text: '快速开始',
          items: [
            { text: '5 分钟上手',        link: '/guide/quick-start' },
            { text: '完整安装',          link: '/guide/installation' },
            { text: '配置 API Key',      link: '/guide/ai-configuration' },
          ],
        },
        {
          text: '核心教程',
          items: [
            { text: 'AI 工作流详解',      link: '/guide/ai-video-guide' },
            { text: '第一人称生产规范',    link: '/guide/first-person-narration-production' },
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
          text: '社区',
          items: [
            { text: '常见问题',           link: '/faq' },
            { text: '贡献指南',           link: '/contributing' },
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

    // ── Social Links ────────────────────────────────────────
    socialLinks: [
      { icon: 'github',  link: 'https://github.com/Agions/scene-fab' },
      { icon: 'twitter', link: 'https://x.com/SceneFab' },
    ],

    // ── Footer ──────────────────────────────────────────────
    footer: {
      message: '基于 MIT License 开源 · Copyright © 2025-2026 Agions',
      copyright: 'SceneFab — AI 影视解说创作工具 · 隐私优先 · 本地处理',
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
