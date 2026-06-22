<div align="center">

<img src="assets/logo-horizontal.svg" alt="SceneFab" width="420"/>

<br/>

### AI 影视解说视频一站式创作工具

<br/>

[![Version](https://img.shields.io/badge/v2.1.1-06b6d4?style=flat-square&logo=git&logoColor=white)](https://github.com/Agions/scene-fab/releases)
[![License](https://img.shields.io/badge/License-MIT-8b5cf6?style=flat-square)](LICENSE)
[![Stars](https://img.shields.io/github/stars/Agions/scene-fab?style=flat-square&color=f59e0b)](https://github.com/Agions/scene-fab/stargazers)
[![CI](https://img.shields.io/github/actions/workflow/status/Agions/scene-fab/pr-check.yml?branch=feature/v21-arch&style=flat-square&color=22c55e&label=CI)](https://github.com/Agions/scene-fab/actions)
[![Docs](https://img.shields.io/github/actions/workflow/status/Agions/scene-fab/deploy-pages.yml?style=flat-square&color=3b82f6&label=Docs)](https://agions.github.io/scene-fab/)

![Python](https://img.shields.io/badge/Python-3.10+-3b82f6?style=flat-square&logo=python&logoColor=white)
![PySide6](https://img.shields.io/badge/PySide6-6.9+-3b82f6?style=flat-square&logo=qt&logoColor=white)
![FFmpeg](https://img.shields.io/badge/FFmpeg-6.x-3b82f6?style=flat-square&logo=ffmpeg&logoColor=white)
![Platform](https://img.shields.io/badge/平台-Win%20%7C%20macOS%20%7C%20Linux-3b82f6?style=flat-square)

</div>

---

## 核心特性

<table>
  <tr>
    <td align="center" width="33%">
      <b>AI 智能理解</b><br/>
      视频语义拆解 · 场景识别 · 人物关系
    </td>
    <td align="center" width="33%">
      <b>解说生成</b><br/>
      多风格文案 · 多角色配音 · 字幕同步
    </td>
    <td align="center" width="33%">
      <b>一键导出</b><br/>
      8 平台预设 · 批量导出 · 硬件加速
    </td>
  </tr>
</table>

---

## 快速开始

**1. 安装**

```bash
pip install scenefab
# 或前往 Releases 下载安装包
```

**2. 配置**

```bash
export DEEPSEEK_API_KEY="sk-..."
# 可选：QWEN_API_KEY（视觉增强）
```

**3. 运行**

```bash
scenefab commentary create-movie ./movie.mp4 --style 纪录片 --output ./output/
scenefab batch /path/to/series/ --preset short_drama_suspense --parallel 2
scenefab export master.mp4 --platforms douyin,bilibili,xiaohongshu
```

---

## 架构

```
UI 层 (PySide6)  →  核心引擎 (DAG 并行 · 批量处理 · 安全审计)
       ↓                    ↓
业务服务层 (AI · 视频 · 导出)  →  数据层 (Models · Utils · Plugins)
```

---

## 文档

[快速开始](https://agions.github.io/scene-fab/guide/quickstart) · [AI 配置](https://agions.github.io/scene-fab/guide/ai-configuration) · [架构设计](https://agions.github.io/scene-fab/architecture) · [常见问题](https://agions.github.io/scene-fab/faq)

---

## 技术栈

![DeepSeek](https://img.shields.io/badge/DeepSeek-V4_Pro-06b6d4?style=flat-square)
![Qwen](https://img.shields.io/badge/Qwen-3.7-06b6d4?style=flat-square)
![Edge-TTS](https://img.shields.io/badge/Edge--TTS-06b6d4?style=flat-square)
![F5-TTS](https://img.shields.io/badge/F5--TTS-06b6d4?style=flat-square)
![FFmpeg](https://img.shields.io/badge/FFmpeg-6.x-06b6d4?style=flat-square)
![SQLite](https://img.shields.io/badge/SQLite-3-06b6d4?style=flat-square)

---

## 许可证

[MIT License](LICENSE) © 2025-2026 [Agions](https://github.com/Agions)
