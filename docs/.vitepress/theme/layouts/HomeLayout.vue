<template>
  <DefaultTheme.Layout>
    <template #home-hero-after>
      <!-- Social Proof Bar -->
      <div class="vp-proof-bar">
        <span class="vp-proof-item">
          <svg class="vp-proof-dot" viewBox="0 0 8 8"><circle cx="4" cy="4" r="3.5" fill="#10B981"/></svg>
          v3.0.0 最新版
        </span>
        <span class="vp-proof-sep">·</span>
        <span class="vp-proof-item">
          <svg class="vp-proof-dot" viewBox="0 0 8 8"><circle cx="4" cy="4" r="3.5" fill="#0A84FF"/></svg>
          DeepSeek-V4 解说生成
        </span>
        <span class="vp-proof-sep">·</span>
        <span class="vp-proof-item">
          <svg class="vp-proof-dot" viewBox="0 0 8 8"><circle cx="4" cy="4" r="3.5" fill="#8B5CF6"/></svg>
          Qwen2.5-VL 语义拆条
        </span>
        <span class="vp-proof-sep">·</span>
        <span class="vp-proof-item">
          <svg class="vp-proof-dot" viewBox="0 0 8 8"><circle cx="4" cy="4" r="3.5" fill="#F59E0B"/></svg>
          &lt;¥1 / 视频
        </span>
        <span class="vp-proof-sep">·</span>
        <span class="vp-proof-item">
          <svg class="vp-proof-dot" viewBox="0 0 8 8"><circle cx="4" cy="4" r="3.5" fill="#EF4444"/></svg>
          MIT 开源
        </span>
      </div>
    </template>
  </DefaultTheme.Layout>
</template>

<script setup lang="ts">
import DefaultTheme from 'vitepress/theme'
</script>
