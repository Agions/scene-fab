# 更新日志

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [2.1.0] - 2026-06-04

> SceneFab v2.1.0 — 架构升级：单源真相事件总线 + 类型化领域事件 + DI 现代化

### 🚀 Features

- **UnifiedEventBus 单源真相** (`scenefab.core.unified_event_bus`) — 取代 v1.x 两个并行 EventBus 实现。字符串事件 + DomainEvent 强类型事件统一入口；async/sync handler 混合；EventLog 内存重放；stats() 可观测
- **类型化领域事件** (`scenefab.core.event_types`) — 8 个预定义 `DomainEvent`（PipelineStarted/StepCompleted/Completed、TaskCreated/ProgressUpdated/StatusChanged、LLMTokenGenerated、FFmpegExecuted）+ 自定义扩展
- **UnifiedTask 状态机** (`scenefab.core.task_model`) — 合法状态转换图 + CancelToken + TaskSource + 状态变更自动发 DomainEvent
- **DIContainer v2.1** (`scenefab.core.di_container`) — v1.x API 兼容 + SCOPED 作用域 + 解析钩子 + `get_app_container()` 全局自动注入 event_bus
- **TaskStore 3 后端** (`scenefab.core.task_store`) — InMemory（+TTL）/ SQLite（持久化）/ Redis（可选）。FastAPI router 私货 `_tasks: dict` 替换为共享后端
- **EventStore 持久化** (`scenefab.core.event_store`) — 3 后端 + 按 event_name / correlation_id 查询 + `install_event_store_into_bus()` 自动双写
- **SettingsV2** (`scenefab.core.config_v2`) — pydantic-settings + 7 配置组（LLM/TTS/Pipeline/Storage/Security/API/App）+ env 自动映射 + JSON Schema 生成 + `reload()`
- **WebSocket Hub** (`scenefab.core.ws_hub`) — 从 UnifiedEventBus 订阅事件并实时推送到 WS 客户端，支持按 event_names 过滤 + 按 event_filter 字段过滤

### 🔧 Integrations

- `TaskManager.create_task / set_status / update_progress` 现在自动发布 `TaskCreated / TaskStatusChanged / TaskProgressUpdated` 事件（v1.x 行为完全保留）
- `PipelineEngine.run / _execute_step` 现在自动发布 `PipelineStarted / PipelineStepCompleted / PipelineCompleted` 事件（通过 `event_bus=` 注入）
- `scenefab.core.EventBus` 和 `scenefab.event_bus.EventBus` 委托到 `UnifiedEventBus.get_default()`，**v1.x 公开 API 完全兼容**

### 📚 Documentation

- **ADR-006** — v2.1 架构升级：单源真相 + 类型化事件 + DI 现代化

### 🧪 Tests

- `tests/test_arch_v21.py` — 43 个 v2.1 新增测试（UnifiedEventBus / V1XCompatibility / UnifiedTask / DIContainer / TaskStore / SettingsV2 / EventStore / WSHub / 集成）
- **76/76 全过**（33 v2.0 + 43 v2.1，**零回归**）

---

## [2.0.0] - 2026-06-04

> SceneFab v2.0.0 — 短剧解说特化与 DAG 并行流水线

### 🚀 Features

- **DAG 并行流水线引擎** (`scenefab.core.pipeline_engine`) — 拓扑排序 + parallel_group 并行执行，always_run 步骤支持。**短剧整季生产 25 集从 ~29min 降至 ~15min（↓48%）**
- **FFmpeg 安全封装** (`scenefab.core.ffmpeg_safe`) — 参数白名单（codec/preset/crf）+ 危险字符检测 + 路径黑名单 + 审计日志集成，**消除 90%+ 命令注入面**
- **操作审计日志** (`scenefab.core.audit`) — SQLite 持久化 + `track()` 上下文管理器，自动捕获 LLM/FFmpeg/流水线步骤
- **批量任务处理器** (`scenefab.core.batch_processor`) — 并行 worker + 自动重试 + 断点续传（SQLite checkpoint）
- **短剧解说特化** (`scenefab.core.short_drama`) — 4 风格（悬疑/甜宠/复仇/逆袭）+ 7 桥段识别（身份揭露/打脸/救场/背叛/心动/对峙/反转）+ 集数扫描（EP01 / 第01集 / E01）
- **多平台智能适配** (`scenefab.core.platform_adapter`) — 8 平台配置（抖音/B站/小红书/西瓜/YouTube/TikTok/快手/剪映）+ 智能裁剪 + 平台专属封面
- **统一 Worker 基类** (`scenefab.core.base_worker`) — PySide6/headless 双模式 + 取消/暂停/审计集成
- **LLM 流式输出 Worker** (`scenefab.core.streaming_llm_worker`) — 逐 token Signal 推送 + 句子边界检测

### 📚 Documentation

- **5 篇架构决策记录 (ADR)**
  - ADR-001: PySide6 vs Electron 桌面端 GUI 框架
  - ADR-002: 全量本地处理 vs 云端渲染
  - ADR-003: 事件驱动 + IoC 容器架构
  - ADR-004: DAG 并行 vs 串行流水线
  - ADR-005: F5-TTS 本地零样本 vs 云端 TTS

### 🧪 Testing

- **33 个 v2.0 核心模块测试** — 覆盖 BaseWorker / Audit / PipelineEngine (含循环依赖检测 + parallel timing) / SafeFFmpeg (注入/白名单/路径) / Batch (重试/断点) / ShortDrama (桥段/扫描) / Platform (裁剪/配置)
- **回归测试** — 416/416 通过，零 v2.0 引入回归

### 🔧 Internal

- **完全向后兼容 v1.x** — `EventBus` / `EventEmitter` / `ErrorInfo` / `event_bus` / `ApplicationState` 全部保留
- **代码组织** — `scenefab.core` 模块化拆分（8 个新模块 ~2,700 行）

### 📊 Performance

| 指标 | v1.1.0 | v2.0.0 | 提升 |
|------|:---:|:---:|:---:|
| 10min 视频处理 | ~70s | ~40s | ↓ 43% |
| 短剧整季 25 集 | ~29min | ~15min | ↓ 48% |
| LLM 首字延迟 | 20s | < 2s | ↓ 90% |
| FFmpeg 注入面 | 多处 | 0 | ↓ 100% |

---

## [1.1.0] - 2026-06-02

> SceneFab v1.1.0 — 大型架构重构与质量改进

### 🚀 Improvements

- **8-Phase 架构重构** — 消除重复类型定义、清理冗余兼容层、拆分大文件、统一枚举与命名
  - Phase 1: 合并 5 个重复类型定义 (EmotionType / ServiceStatus / ServiceHealth / AIServiceManager / ProjectMetadata)
  - Phase 2: 删除 6 个冗余兼容层 (engine / models / ai_services / config_manager / exporters / video)
  - Phase 3: 拆分 5 个 500+ 行 UI 大文件 (theme_optimizer / home_page / step_group / export_panel / export_monitor)
  - Phase 4: 删除 ~160 行死代码 (`run_mashup` / `run_monologue` / `_analyze_single_frame`)
  - Phase 5: 命名规范化 (`_signals.py` → `signals_bridge.py`, 10 个枚举集中到 `models/enums.py`)
  - Phase 6: 配置精简 (删除 `.flake8`/`.pylintrc`, ruff 统一为唯一 linter, pyright 取消 UI 排除)
  - Phase 7+8: UI 枚举导出 + 最终验收
- **启用 ruff `UP` (pyupgrade) 规则** — 自动修复 1573 个 UP 错误 (typing.Dict/List → dict/list, 旧语法糖)
- **依赖审计** — 同步 `requirements.txt` 与 `pyproject.toml`, 移除冗余工具 (googletrans / flake8 / isort), 升级 PySide6 6.9.0 / pydantic 2.5.0

### 🔧 Internal

- **CI 流水线**: PR Check 双 job (lint + test), merge-queue 友好
- **代码质量门禁**: ruff 0 errors, pytest 351 passed + 20 skipped

### 📦 Compatibility

- **完全向后兼容 v1.0.x** — 所有公共 API 与 import 路径保持不变
- **无破坏性变更** — 已发布的 v1.0.x 项目文件可直接打开

---

## [1.0.1] - 2026-05-31

> SceneFab v1.0.1 — 修复 GUI 启动问题

### 🐛 Bug Fixes

- **修复 GUI 启动报错** — 修正 `app.ui.components.containers.common_styles` 旧路径，重构为 `scenefab.ui.components.containers`
- **CI 修复** — release-build workflow 路径与构建参数对齐

---

## [1.0.0] - 2026-05-31

> SceneFab v1.0.0 — AI 影视解说视频创作工具首个 PyPI 发行版。
> 汇总了从初始化到 v4.x 的全部历史变更，作为 1.0.0 基线版本归档。

### 🚀 核心功能

- **AI 视频解说生成** (Monologue Maker)：Qwen2.5-VL 视频理解 + DeepSeek-V4 解说生成 + SenseVoice ASR + Edge-TTS/F5-TTS 配音
- **AI 视频混剪** (Mashup Maker)：智能分组 + 情绪峰值检测 + 视角映射
- **导出支持**：DirectVideoExporter (MP4/MOV/GIF) + JianyingExporter (剪映草稿)
- **导出预设**：B站 (1080P 60fps)、YouTube (4K 60fps)、Twitter、TikTok、微信

### 🎨 UI/UX

- **OKLCH 色彩系统**：感知均匀色彩空间，亮度和色度解耦
- **OutCubic 动效**：页面切换滑入动画 (220-280ms)
- **脉冲指示器**：活动步骤动画
- **专业布局**：玻璃态侧边栏 + 顶部工具栏 + 页面标题栏
- **设置页面组件化**：CF* 组件体系替代硬编码样式
- **Toast 通知系统**：info/success/warning/error 四种类型，自动消失

### ⚡ 性能优化

- **Whisper 本地模式**：faster-whisper medium 模型，GPU batch_size=8，CPU INT8 量化
- **LLM 磁盘缓存**：SQLite 持久化，TTL=24h，最大 500MB，LRU 淘汰
- **请求去重**：相同 prompt+model+temperature 只调用一次 API
- **并行处理**：视频帧提取、翻译、TTS 异步并行

### 🔒 安全

- **SecureExecutor**：所有 subprocess 调用统一经安全策略校验
- **PBKDF2**：HMAC 迭代次数 480,000 (OWASP 标准)
- **SecurityError 统一**：所有 ffmpeg/系统调用异常类型统一

### 📦 架构

- **Provider 插件化**：VisionProvider / LLMProvider / TTSProvider 协议 + ProviderRegistry 单例 + YAML 热加载
- **模块化拆分**：video services 分为 extraction/selection/grouping/tools/analyzers/loaders/cutters 多个子目录
- **依赖注入**：服务间解耦，提升可测试性
- **PySide6 迁移**：从 PyQt6 迁移至 PySide6 (LGPL)

### 🛠 开发体验

- **CLI 完整实现**：`commentary create-movie/create-drama`、`batch`、`project create/list/info/delete`、`plugin list` 等命令
- **TDD 测试覆盖**：核心服务单元测试（SmartGrouper, FirstPersonExtractor, EmotionPeakDetector, SegmentSelector）
- **CI/CD 优化**：pip → uv，ruff lint 统一配置，type-check / lint / test 分工明确
- **动态版本管理**：`pyproject.toml` 使用 `dynamic = ["version"]`，版本号统一从 `scenefab.__version__` 读取

### 📝 文档

- README / shields 升级至 v1.0.0
- 专业文档站（VitePress）：快速开始、功能详解、AI 工作流、配置参考、疑难排查
- CONTRIBUTING.md 贡献指南

### 🐛 Bug Fixes (历史累积)

- LLMManager 同步调用返回 None 问题修复
- Provider 健康检查超时 (5s) 修复
- FFmpegTool/SecureExecutor 异常类型错误 (CalledProcessError → SecurityError) 修复
- SecurityError 被静默吞噬问题修复
- Whisper 批处理 GPU 加速修复
- 无头环境 (offscreen) 兼容修复
- 缩略图缓存 LRU 逻辑修复
- 版本号显示错误修复
- 裸 `except:pass` 问题全面清理

### 📊 质量指标

- Tests：389+ passed, 20+ skipped, 0 failed
- Ruff Lint：All checks passed
- 死代码清理：删除 820+ 行冗余代码

---

## 历史版本 (归档)

以下为历史发布版本的原始条目，详情见 GitHub Releases。

| 版本 | 日期 | 说明 |
|------|------|------|
| v4.0.1 | 2026-05-08 | SecurityError 修复 + 死代码清理 |
| v4.0.0 | 2026-04-21 | Phase 1-4 全面重构 (TDD + Provider 插件化) |
| v3.10.0 | 2026-04-19 | UI 统一与组件化 |
| v3.9.1 | 2026-04-19 | LLM 磁盘缓存 + 性能优化 |
| v3.9.0 | 2026-04-14 | Whisper 本地化 + GPU 加速 |
| v3.8.0 | 2026-04-13 | UI 无障碍 + 减少动画偏好支持 |
| v3.7.0 | 2026-04-11 | 类型安全强化 + Pydantic v2 |
| v3.6.0 | 2026-04-10 | 创作向导重构 Phase 1 |
| v3.5.0 | 2026-04-09 | OKLCH + OutCubic 专业设计规范 |
| v3.4.1 | 2026-04-09 | UI 重构 Bug 修复 |
| v3.4.0 | 2026-04-09 | 场景检测性能改进 |
| v3.3.0 | 2026-04-08 | 品牌重命名 + 产品定位重构 |
| v3.2.0 | 2026-04-05 | FFmpeg 工具统一 + 缓存修复 |
| v3.1.1 | 2026-04-03 | PyQt6 → PySide6 迁移 |
| v3.1.0 | 2026-03-23 | AI 创作模式 (解说/混剪/独白) |
| v3.0.0 | 2026-03-08 | 基础 AI 功能 + 视频导出 |
| v2.0.0 | 2025-XX-XX | 项目初始化 + 基础 UI 框架 |
| v1.0.0 | 2024-XX-XX | 项目初始化 |