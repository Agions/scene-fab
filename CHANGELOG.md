# 更新日志

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [2.1.2] - 2026-06-22

> SceneFab v2.1.2 — 修复 #82 二级启动失败 + 发布链加固

### 🐛 Bug Fixes

- **fix(startup):** 修复 issue #82 — `scenefab.ui.config_manager` 中 `ConfigManager.get()` 对缺失 key 抛 AttributeError,改为返回 `None`/`default` 并记录 info 级别日志,应用启动不再因缺失 `user.json` 配置崩溃（PR #84 + 新增 `tests/test_issue82_regression.py` 198 行回归测试）

### 🔧 Maintenance

- **fix(ci):** `release-build.yml` 的 `publish-pypi` job 现在 depends on `create-release`,保证 4 平台 PyInstaller build + GitHub Release 页面全部成功后才推 PyPI（PR #85）

## [2.2.0] - 2026-06-22

> SceneFab v2.2.0 — 模型目录统一 + 架构精简 + 文档专业重设计

### 🚀 Features

- **模型目录单源真相** (`scenefab.services.ai.model_catalog`) — `ModelProfile` 冻结数据类 + `MODEL_CATALOG` 覆盖 10 个 Provider，`DEFAULT_MODELS` / `NARRATION_MODEL_STACK` / `settings_model_options()` 统一派生
- **端到端冒烟测试** (`tests/test_smoke_pipeline.py`) — 35 个测试覆盖 VisionService → ScriptGenerator → SubtitleTranslator → DirectVideoExporter 全流水线
- **VisionAnalysisResult dict 兼容** — 新增 `__getitem__` / `__contains__` / `get()` / `keys()` / `to_dict()` 方法，支持 `result["description"]` 风格访问

### 🔧 Refactoring

- **Provider 模型统一** — 所有 Provider（deepseek/qwen/claude/gemini/doubao/glm5/hunyuan/kimi/local）从 `model_catalog` 派生 `MODELS` 和 `DEFAULT_MODEL`，消除硬编码模型名
- **LLMManager 配置模型生效** — 新增 `_apply_configured_model()`，`LLMRequest(model="default")` 正确应用 YAML 配置的模型
- **导出层精简** — 删除 `video_exporter.py`（409 行），只保留 `DirectVideoExporter`
- **视觉链精简** — 删除 `gemini35_flash.py`（359 行）和 `QwenVLProvider` 死代码，只保留 Qwen3.7 / GPT-5 / Gemini 3.1 Pro
- **兼容层清理** — 删除 `ai_service_manager.py` / `service_manager.py` / `utils/config.py`（零消费者）
- **services/__init__.py 重构** — 直接从 canonical source 导入，移除 deprecated shim

### 🐛 Bug Fixes

- **ConfigManager 新增 get/set** — 修复 `ProjectManager` 调用 `.get("editor.recent_files")` 的 latent bug
- **VisionProvider 返回类型** — ABC 返回类型更新为 `dict[str, Any] | VisionAnalysisResult`，移除 `# type: ignore[override]`
- **Settings UI 模型名** — 更新为 deepseek-v4-pro / gpt-5 / gemini-3.1-pro / qwen3.7-max / claude-sonnet-4-6
- **Script Generator fallback** — `gpt-4` → `gpt-5`
- **SubtitleTranslator 导入路径** — `.subtitle_extractor` → `.subtitle_translator`
- **ErrorInfo.timestamp** — 改用 `time.time()` 替代 Qt 实例调用
- **Application.initialize()** — 改用 `enumerate()` 替代 `list.index()`
- **DirectVideoExporter._progress_callback** — 初始化为 `None`

### 📚 Documentation

- **README.md 重写** — 精简专业版（259→102 行），科技感深色主题
- **docs/index.md 重写** — 精简 Hero + 6 卡片特性 + 3 列文档地图
- **VitePress 主题更新** — 统一 cyan→violet 渐变配色方案
- **architecture.md** — 添加 4 个 Mermaid 图（架构/交互/流水线/数据流）
- **ai-models.md** — 更新模型对比表 + 角色推荐配置 + 组合矩阵
- **config.md** — 快速参考表 + 双文件结构文档 + 常见场景
- **features.md** — 产品特性矩阵（6 模块 × 状态标记）
- **quick-start.md** — 精简为 3 步（安装/配置/运行）
- **deprecations.md** — 添加 Gemini35FlashProvider 删除记录
- **ai-configuration.md** — Qwen VL → Qwen3.7 全面更新
- **导航栏修复** — 首页与其他导航项水平对齐

### 🧪 Tests

- **test_integration.py 重写** — 31 个测试全部修复（API 不匹配 → 正确使用 generate/content/ConfigManager）
- **test_model_catalog.py 扩展** — 3→35 个测试（ModelProfile / Catalog / DefaultModels / NarrationStack / ProviderModels / SettingsOptions）
- **test_vision_providers.py 更新** — QwenVLProvider → Qwen37FrameProvider
- **总计 695 passed, 1 skipped**

### 🗑️ Removed

- `src/scenefab/services/ai/providers/gemini35_flash.py` — 冗余 Provider
- `src/scenefab/services/export/video_exporter.py` — 旧导出器
- `src/scenefab/services/ai_service_manager.py` — 兼容层
- `src/scenefab/services/service_manager.py` — 兼容层
- `src/scenefab/utils/config.py` — 零消费者的 JSON 配置系统
- `tests/test_video_exporter.py` — 旧导出器测试
- `docs/deprecations.md` — 内部跟踪文档
- `docs/technical-audit-2026-06-17.md` — 内部审计文档
- `docs/icons/` — 与 public/icons 重复

### 📦 Resources

- **新应用图标** — `resources/app_icon.svg`（cyan→violet 渐变 + SF 标识）
- **特性图标更新** — `docs/public/icons/*.svg` 统一 #06b6d4 配色
- **Qt 样式表** — dark_theme.qss / light_theme.qss 已更新为 cyan 主色调

---
>>>>>>> 4b818e7 (refactor: v2.2.0 — model catalog unification, architecture cleanup, docs redesign)

## [2.1.1] - 2026-06-16

> SceneFab v2.1.1 — 解说生成状态机 + 架构基线清理

### 🚀 Features

- **解说生成状态机** (`scenefab.pipeline.narration_state_machine`) — 5 状态 + 评估循环（UNDERSTAND → STORYGRAPH → DRAFT → EVALUATE → HOOK_REWRITE），见 ADR 007
- **NarrationEvaluator** (`scenefab.pipeline.narration_evaluator`) — 5 维加权解说稿质量评估器

### 🔧 Maintenance

- 测试入口修复：`pytest` 无需 `PYTHONPATH=src` 或 editable install 即可运行（`pythonpath = ["src"]`）；默认关闭 `pytest-qt` 插件，非 UI 测试不再依赖 Qt binding
- 版本号单源真相：`pyproject.toml` / README 徽章 / UI 导航构建标签统一为 `2.1.1`（UI 标签改为从 `scenefab.utils.version` 动态读取）
- 死代码与生成物清理（UI 旧组件、`__pycache__` / `.pyc`）

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
  - Phase 6: 配置精简与依赖收敛
  - Phase 7+8: UI 枚举导出 + 最终验收
- **依赖审计** — 同步运行依赖，移除冗余工具，升级 PySide6 6.9.0 / pydantic 2.5.0

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

- **AI 视频解说生成** (Monologue Maker)：Qwen3.7 视频理解 + DeepSeek-V4 解说生成 + SenseVoice ASR + Edge-TTS/F5-TTS 配音
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

### 🛠 体验与交付

- **CLI 完整实现**：`commentary create-movie/create-drama`、`batch`、`project create/list/info/delete`、`plugin list` 等命令
- **核心服务稳定性提升**：SmartGrouper, FirstPersonExtractor, EmotionPeakDetector, SegmentSelector 等关键链路完成验证
- **动态版本管理**：`pyproject.toml` 使用 `dynamic = ["version"]`，版本号统一从 `scenefab.__version__` 读取

### 📝 文档

- README / shields 升级至 v1.0.0
- 专业文档站（VitePress）：快速开始、功能详解、AI 工作流、配置参考、疑难排查

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
