/**
 * SceneFab VitePress Theme — Custom Components
 * 注册自定义 Vue 组件以供 markdown 使用
 */

import { h } from 'vue'
import type { Theme } from 'vitepress'
import DefaultTheme from 'vitepress/theme'

// Custom Layouts
import HomeLayout from './layouts/HomeLayout.vue'
import DocLayout   from './layouts/DocLayout.vue'

// Custom Components
import Badge from './components/Badge.vue'
import Card  from './components/Card.vue'
import CardGrid from './components/CardGrid.vue'
import Callout from './components/Callout.vue'
import { CodeGroup, CodeGroupItem } from './components/CodeGroup.vue'
import { Timeline, TimelineItem } from './components/Timeline.vue'
import { Step, Steps } from './components/Steps.vue'

// Styles (always import last)
import './style.css'

export default {
  extends: DefaultTheme,

  Layout: HomeLayout,

  enhanceApp({ app, router, siteData }) {
    // Register global components with common names
    app.component('Badge',          Badge)
    app.component('Card',           Card)
    app.component('CardGrid',        CardGrid)
    app.component('Callout',         Callout)
    app.component('CodeGroup',       CodeGroup)
    app.component('CodeGroupItem',   CodeGroupItem)
    app.component('Timeline',        Timeline)
    app.component('TimelineItem',   TimelineItem)
    app.component('Step',            Step)
    app.component('Steps',           Steps)
  },
} satisfies Theme
