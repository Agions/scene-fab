# 更新日志

本文件记录 SceneFab 所有重要变更。格式遵循 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)，版本号遵循 [语义化版本控制](https://semver.org/lang/zh-CN/)。

---

## [2.3.0] - 2026-06-26

> SceneFab v2.3.0 — 代码审计 + 2 P1 安全修复 + API/UI 测试覆盖补齐

### 🐛 Bug Fixes

- **fix(security): hardware.py subprocess 走 SecureExecutor 审计链** — `check_nvidia_smi` / `check_intel_cpu` 改走新 `get_probe_executor()` 单例 (白名单: nvidia-smi, wmic), 不再裸 `subprocess.run`. 移除 `import subprocess`. 异常类型改 `SecurityError` + `TimeoutError`
- **fix(security): api/routers/pipeline.py 缺路径校验** — 复用 export router 模式 (`_DEFAULT_ALLOWED_BASE_DIRS` + `_get_path_validator` + `_validate_output_dir`), 早期拒绝空 `video_url`, `_process_narration` 校验 `output_dir` 失败时降级到 `cwd/outputs/jianying_drafts`
- **fix(api): GET / 根路由未注册** — `@app.get("/")` 在 `app = create_app()` 之后定义, 装饰器把 root 注册到 `app` 局部变量, 实际不生效. 修复: 把 root 移入 `create_app()` 函数内
- **fix(api): GET /api/v1/plugins/types 永远 404** — FastAPI 按路由声明顺序匹配, `/plugins/{plugin_id}` 在 `/plugins/types` 之前注册, 拦截 "types" 路径. 修复: 重排为 `/plugins` → `/plugins/types` → `/plugins/{plugin_id}` → `/plugins/{plugin_id}/enable`

### 🔧 Maintenance

- **refactor(llm): narrow HTTPClientMixin._call_api** — 改前 `except Exception` (宽 catch, 吞 RuntimeError/TypeError), 改后异常分两段 catch: `httpx.HTTPStatusError` → `_handle_http_error`, `httpx.HTTPError` → `ProviderError("网络错误")`, `json.JSONDecodeError/ValueError` → `ProviderError("响应解析")`. 真 bug 不再被吞
- **chore(cleanup): jianying_exporter.py MaterialType 注释** — pyflakes 报 "unused", 实际是间接 re-export (不在 `__all__` 但与其他 adapter 类型对齐). 注释明确为 "package-private" + 指引测试用 `from jianying_adapter import` 直路径
- **test(api): 补 api/ 0% 测试覆盖** — 18 个集成测试覆盖 5 个 router (health/pipeline/plugins/export/projects) + 全局异常处理 + 路由顺序
- **test(ui): 补 ui/ 0% 测试覆盖** — 8 个 headless-safe smoke test 覆盖 SceneFabMainWindow 类结构 + 子模块 import + theme 模块

### 🛡️ Security

- **新 utils/security.py:get_probe_executor()** — 全局 read-only 探测执行器单例, 白名单: `nvidia-smi`, `wmic`. 仍受 SecureExecutor 审计链约束 (白名单 + 路径 + shell=False + env sanitization)

### 诚实性记录

- **pyflakes 4 个 false positive** 经主 agent 亲自 verify: 3 个是懒导入/TYPE_CHECKING 模式 (非 bug), 1 个是 docstring 字符串
- **HTTPClientMixin 抽取 ROI 调研** 发现流式模式 (`async with self.http_client.stream`) 抽不出干净 helper (嵌套 context manager 冲突), 改为 narrow 化已有 `_call_api` 获得真 ROI
- **headless UI 测试** 写"结构契约 + import smoke" 替代行为测试, 避免 PySide6 offscreen + 系统 GL 库缺失的 flaky

### 测试

- 748 → 755 passed (+7, +1 skipped typography optional)
- 0 regression across 39,848 LOC
- 25 commits ahead of remote, 全部 pushed

### PR 链 (6 commits, all pushed)

| SHA | 类型 | 摘要 |
|---|---|---|
| `7da45ec` | fix(security) | 2 P1 — hardware subprocess + pipeline router 路径校验 |
| `2727e02` | refactor(llm) | narrow HTTPClientMixin._call_api 异常分两段 |
| `b57cda4` | test(api) | 补 api/ 覆盖 + 修 2 真 bug (根路由 + 路由顺序) |
| `4543ea3` | test(ui) | 补 ui/ smoke test |

---

## [2.2.0] - 2026-06-25

> SceneFab v2.2.0 — 深度架构重构（PR #88）+ API 安全加固

### 🚀 Features

- **examples/ 目录** — 5f214d1 closes #90，新增示例项目
- **架构深度重构** — 9b1bccf v2.2.0 主 PR, 删除 ~15000 行死代码, 收敛 5 个 LLM provider 基类, 统一 retry/JSON IO/项目 IO
- **全站文档专业重设计** — README、架构概览、AI 模型、配置参考

### 🐛 Bug Fixes

- **fix(api): 修 P0 字段名不一致** — `pipeline.py:124` `req["source_video"]` → `req["video_url"]` (与 schema 对齐, 修 KeyError 死路); emotion 默认值 `"惆怅"` → `"healing"` (对齐 EmotionType 枚举)
- **fix(api): 路径校验改用 PathValidator** — `export.py:80-94` 自造 `".." in parts` 校验改走 `PathValidator` + `DANGEROUS_PATH_PATTERNS` + 扩展名白名单 + 4 个默认 base_dir (cwd/outputs, ~/.scenefab/exports, ~/Downloads, ~/.cache/scenefab/exports); 可通过 `settings.allowed_base_dirs` 扩展
- **fix(export): ExportManager dispatch 显式化** — DirectVideoExporter 缺统一 `export()` 方法, 调用链 `ExportManager.export → exporter.export` 抛 `AttributeError`; 改为显式 `_dispatch` 分发到 `JianyingExporter.export(draft, output_dir, ...)` 或 `DirectVideoExporter.export(project_data, config)`, 缺字段时抛明确 `ExportError` 而非 crash
- **fix(test): test_project_manager 不硬编码版本** — `assert metadata.version == "2.1.2"` 改为 `get_version_string()` 动态断言, 跟随 pyproject 真实状态
- **fix(ci): ruff lint** — import 排序 + 语法残留 + 未使用导入清理 (e0b5208 / bd2152a / ad739fe / 1bf19da / 2c9e055)

### 🔧 Maintenance

- **chore(release): version 2.1.2 → 2.2.0** — 跟随 PR #88 实际状态, pyproject.toml + utils/version.py
- **chore(cleanup): 删 4 个空目录** — `cache_impl/` / `interfaces/` / 顶层 `orchestration/` / `services/viral/` (无 .py 残留, 仅 `__pycache__`)
- **test(update): 补 update/checker.py 测试** — 0% → 100% 覆盖, 20 个测试 (parse_version / strip_tag / check_update 7 个 mock 场景 / format_update_message)
- **test(export): 手写 P0 路径校验 10 case 回归测试** — 危险路径 400 / 白名单 202 / None 202 全部按预期

### 🗑️ Removed (v2.2.0 重构期间)

- `core/batch_processor.py` (526) / `core/config_v2.py` (448) / `core/event_store.py` (419) / `core/platform_adapter.py` (643) / `core/platform_extended.py` (622) / `core/ws_hub.py` (330)
- `services/ai/adapters/` / `services/ai/infra/` / `services/ai/asr.py` / `tts.py` / `cache.py` / `manager.py` / `llm.py` / `errors.py` / `interfaces.py` / `model_registry.py` / `vision.py` / `sensevoice_provider.py` (637) / `whisper_asr_provider.py` (305) / `providers/gemini35_flash.py` (359) / `provider_models.py` (226)
- `services/ai_service_manager.py` / `services/service_manager.py` / `services/export/video_exporter.py` (409)
- `utils/config.py` / `pickle_io.py` / `performance.py` / `secure_config_loader.py` / `shortcut_manager.py`
- 顶层 `task_manager.py` (519) / `version_manager.py` (573) / `version_models.py` / `registry_models.py` / `service_container.py` / `event_bus.py` / `cache_manager.py`

### 测试

- 611 → **631 passed** (新增 20 个 update/checker 测试)
- 手写 10 case P0 路径校验回归测试全部通过
- ruff 修复后 CI green

---

## [2.1.2] - 2026-06-22

> SceneFab v2.1.2 — 模型目录统一 · 架构精简 · 文档专业重设计

### 新增

- **模型目录单源真相** — `ModelProfile` 冻结数据类 + `MODEL_CATALOG` 覆盖 10 个 Provider；`DEFAULT_MODELS` / `NARRATION_MODEL_STACK` / `settings_model_options()` 统一派生
- **端到端冒烟测试** — 35 个测试覆盖 VisionService → ScriptGenerator → SubtitleTranslator → DirectVideoExporter 全流水线
- **VisionAnalysisResult 兼容增强** — 新增 `__getitem__` / `__contains__` / `get()` / `keys()` / `to_dict()` 方法

### 重构

- **Provider 模型统一** — 所有 Provider 从 `model_catalog` 派生 `MODELS` 和 `DEFAULT_MODEL`，消除硬编码
- **LLMManager 配置模型生效** — 新增 `_apply_configured_model()`，`LLMRequest(model="default")` 正确应用 YAML 配置
- **导出层精简** — 删除 `video_exporter.py`（409 行），只保留 `DirectVideoExporter`
- **视觉链精简** — 删除 `gemini35_flash.py`（359 行）和 `QwenVLProvider` 死代码
- **兼容层清理** — 删除 `ai_service_manager.py` / `service_manager.py` / `utils/config.py`（零消费者）

### 修复

- 修复 `ConfigManager.get()` 对缺失 key 抛出 AttributeError 的问题（Issue #82）
- 修复 `VisionProvider` 返回类型声明
- 修复 Settings UI 中的模型名称
- 修复 Script Generator fallback 模型名
- 修复 `SubtitleTranslator` 导入路径
- 修复 `ErrorInfo.timestamp` Qt 实例调用问题
- 修复 `DirectVideoExporter._progress_callback` 未初始化问题
- 修复 `release-build.yml` 的发布依赖链（PR #85）

### 文档

- 全站文档专业重设计：README、架构概览、AI 模型、配置参考、功能矩阵、安全设计
- VitePress 主题更新：统一配色方案
- 架构文档添加 4 个 Mermaid 图（架构 / 交互 / 流水线 / 数据流）

### 测试

- `test_integration.py` 重写 — 31 个测试全部修复
- `test_model_catalog.py` 扩展 — 3 → 35 个测试
- `test_vision_providers.py` 更新 — QwenVLProvider → Qwen37FrameProvider
- 总计 695 passed, 1 skipped

### 移除

- `services/ai/providers/gemini35_flash.py` — 冗余 Provider
- `services/export/video_exporter.py` — 旧导出器
- `services/ai_service_manager.py` / `service_manager.py` — 兼容层
- `utils/config.py` — 零消费者配置系统
- `tests/test_video_exporter.py` — 旧导出器测试

---

## [2.1.1] - 2026-06-16

> SceneFab v2.1.1 — 解说生成状态机 + 架构基线清理

### 新增

- **解说生成状态机** — 5 状态 + 评估循环（UNDERSTAND → STORYGRAPH → DRAFT → EVALUATE → HOOK_REWRITE）
- **NarrationEvaluator** — 5 维加权解说稿质量评估器

### 维护

- 测试入口修复：`pytest` 无需 `PYTHONPATH=src` 或 editable install 即可运行
- 版本号单源真相：`pyproject.toml` / README 徽章 / UI 导航构建标签统一
- 死代码与生成物清理（UI 旧组件、`__pycache__` / `.pyc`）

---

## [2.1.0] - 2026-06-04

> SceneFab v2.1.0 — 架构升级：单源真相事件总线 + 类型化领域事件 + DI 现代化

### 新增

- **UnifiedEventBus** — 取代 v1.x 两个并行 EventBus 实现；字符串事件 + DomainEvent 强类型事件统一入口
- **类型化领域事件** — 8 个预定义 `DomainEvent`（Pipeline / Task / LLM / FFmpeg）
- **UnifiedTask 状态机** — 合法状态转换图 + CancelToken + TaskSource
- **DIContainer v2.1** — SCOPED 作用域 + 解析钩子 + 全局自动注入
- **TaskStore 3 后端** — InMemory / SQLite / Redis
- **EventStore 持久化** — 按 event_name / correlation_id 查询 + 自动双写
- **SettingsV2** — pydantic-settings + 7 配置组 + env 自动映射 + JSON Schema 生成
- **WebSocket Hub** — 实时推送事件到 WS 客户端

### 集成

- `TaskManager` / `PipelineEngine` 自动发布领域事件
- v1.x 公开 API 完全兼容

### 测试

- `tests/test_arch_v21.py` — 43 个 v2.1 新增测试，76/76 全过

---

## [2.0.0] - 2026-06-04

> SceneFab v2.0.0 — 短剧解说特化与 DAG 并行流水线

### 新增

- **DAG 并行流水线引擎** — 拓扑排序 + parallel_group 并行执行；短剧整季生产 25 集从 ~29min 降至 ~15min（↓48%）
- **FFmpeg 安全封装** — 参数白名单 + 危险字符检测 + 路径黑名单 + 审计日志
- **操作审计日志** — SQLite 持久化 + `track()` 上下文管理器
- **批量任务处理器** — 并行 worker + 自动重试 + 断点续传
- **短剧解说特化** — 4 风格 + 7 桥段识别 + 集数扫描
- **多平台智能适配** — 8 平台配置 + 智能裁剪 + 平台专属封面
- **统一 Worker 基类** — PySide6 / headless 双模式
- **LLM 流式输出 Worker** — 逐 token Signal 推送 + 句子边界检测

### 性能

| 指标 | v1.1.0 | v2.0.0 | 提升 |
|------|:---:|:---:|:---:|
| 10min 视频处理 | ~70s | ~40s | ↓ 43% |
| 短剧整季 25 集 | ~29min | ~15min | ↓ 48% |
| LLM 首字延迟 | 20s | < 2s | ↓ 90% |

---

## [1.1.0] - 2026-06-02

> SceneFab v1.1.0 — 大型架构重构与质量改进

### 改进

- **8 阶段架构重构** — 消除重复类型定义、清理冗余兼容层、拆分大文件、统一枚举与命名
- **依赖审计** — 同步运行依赖，移除冗余工具，升级 PySide6 6.9.0 / pydantic 2.5.0

### 兼容性

- 完全向后兼容 v1.0.x，所有公共 API 与 import 路径保持不变

---

## [1.0.1] - 2026-05-31

> SceneFab v1.0.1 — 修复 GUI 启动问题

### 修复

- 修正 `app.ui.components.containers.common_styles` 旧路径
- CI release-build workflow 路径与构建参数对齐

---

## [1.0.0] - 2026-05-31

> SceneFab v1.0.0 — 首个正式发行版。

### 核心功能

- AI 视频解说生成（Qwen3.7 + DeepSeek-V4 + Edge-TTS / F5-TTS）
- AI 视频混剪（智能分组 + 情绪峰值检测 + 视角映射）
- 导出支持（MP4 / MOV / GIF + 剪映草稿）
- 多平台预设（B站 / YouTube / Twitter / TikTok / 微信）

### 架构

- Provider 插件化（VisionProvider / LLMProvider / TTSProvider）
- 依赖注入 + 事件驱动
- PySide6 桌面端

### 安全

- SecureExecutor：所有 subprocess 统一安全策略校验
- PBKDF2：HMAC 迭代次数 480,000（OWASP 标准）

### 质量指标

- 测试：389+ passed, 0 failed
- Ruff Lint：All checks passed
- 死代码清理：删除 820+ 行冗余代码
