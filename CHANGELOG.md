# 更新日志

本文件记录 SceneFab 所有重要变更。格式遵循 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)，版本号遵循 [语义化版本控制](https://semver.org/lang/zh-CN/)。

---

## [Unreleased]

> UI Phase 1 + Phase 2A — 死代码清理 + 主窗口拆分 + application 注入 + HomePage ViewModel
>
> **Phase 2B + 2C (新增) — ProductionPage & AssetsPage ViewModel + MonologueMaker service 注册**
>
> **Phase 2B+1 + 2D+ + 3 + P1 refactor (新增) — Live runner + 导入 file dialog + 暗色主题 + 架构清理**

### ✨ Added (Phase 2B + 2C)

- **feat(ui): ProductionPage ViewModel + 5-step pipeline state machine** (Phase 2B)
  - `ui/viewmodels/production_viewmodel.py`(新):`ProductionPageViewModel` 暴露 `step_definitions` / `step_status` / `pipeline_state` / `current_step` 4 个属性,5 个变化信号 (`step_status_changed` / `pipeline_state_changed` / `current_step_changed` / `pipeline_finished` / `pipeline_failed`)
  - 5 步流水线状态机:`pending` → `active` → `done` (或 `error`)。`STEP_DEFINITIONS` 常量抽到 VM,ProductionPage 从 `vm.step_definitions` 拿,避免两边数据漂移
  - `QThreadPool` + `QRunnable` + 内部 `QObject` signals 实现 step 推进跨线程(为 Phase 2B+1 接 `MonologueMaker.generate_*` 留口子)
  - 状态切换 idle / running / done / failed,`start_pipeline(src, ctx)` / `reset_pipeline()` 公开方法
  - `ProductionPage` 接 `viewmodel=` 参数,5 个 step row 加 `setObjectName("step_badge/title/status")` 锚点,`findChild` + signal 驱动实时刷新状态文本和颜色
  - 6 个新测试 `tests/test_production_viewmodel.py`,覆盖:default state / step definitions 5 步 / start_pipeline 推进 / status label 中文化 / reset / 空 input no-op

- **feat(ui): AssetsPage ViewModel + recent projects + asset summary** (Phase 2C)
  - `ui/viewmodels/assets_viewmodel.py`(新):`AssetsPageViewModel` 暴露 `current_assets` (`AssetSummary`) / `recent_projects` (`list[RecentProjectInfo]`) 2 个属性,2 个变化信号
  - `RecentProjectInfo` dataclass:从 `ProjectManager.get_recent_projects()` 返回的 `list[str]` 包装成 UI 友好的元数据 (path / name / last_opened / size_mb / exists)
  - `AssetSummary` dataclass:media / script / audio / export 4 类计数 + `total` / `is_empty` 派生属性
  - 订阅 PM 5 个 signals (`project_opened` / `project_closed` / `project_saved` / `project_deleted` / `recent_projects_updated`),无 application 时 fallback 到空 summary
  - `open_recent(path)` / `import_media(files)` 公开方法,转发到 PM 并有 defensive 错误处理
  - `AssetsPage` 接 `viewmodel=` 参数,资产列表占位 + 最近项目摘要从 VM 拿;刷新按钮接 `vm.refresh()`
  - 8 个新测试 `tests/test_assets_viewmodel.py`,覆盖:default / 包装 / missing file fallback / total / signal / open_recent / import_media

- **chore(app): register MonologueMaker in DIContainer** (Phase 2B 硬前置)
  - `application.py` 在 `project_manager` 之后注册 `monologue_maker` (`MonologueMaker()`),`get_service(MonologueMaker)` 现在可用

- **refactor(ui): ViewModel wiring via registry factories** (Phase 2B + 2C)
  - `ui/main/registry.py` 新增 `_build_production` / `_build_assets` 工厂,`PAGE_BUILDERS["create"]` / `["assets"]` 改接 factory
  - 复用 Phase 2A 的 `PageBuilder` 签名 `(Application | None) -> QWidget`

### 🧪 Tests

- 新增 14 个测试 (6 production + 8 assets),共 **773 passed / 1 skipped** (基线 759 → +14)
- 关键路径测试覆盖:VM 在无 application 时的 fallback、PM signal 订阅、跨线程 step 推进、RecentProjectInfo 包装、AssetSummary 派生

### ⚠️ 不兼容变更

- (无新增;沿用 Phase 2A 的 `PageBuilder` 签名约定)

### 🔮 后续 (P1, 暂未实现)

- **Phase 2B+1**: `_StepRunner.run` 接真 `MonologueMaker.generate_*` (create_project / generate_script / generate_voice / generate_captions)
- **Phase 2D+**: 拖拽导入素材 (目前 `import_requested` signal 仅 emit,需在 router 层接 file dialog)
- **Phase 3**: 暗色主题切换 UI

### ✨ Added (Phase 2B+1 / 2D+ / 3 / P1 refactor)

- **feat(ui): wire 2B+1 live runner — env-gated MonologueMaker integration**
  - `ProductionPageViewModel` 新增 `runner_mode` 属性 (`"noop"` / `"live"`) + `_setup_pipeline()` + `_live_runner()` factory
  - `runner_mode` 由 `_has_runtime_keys()` 决定 — 检查 `SCENEFAB_TTS_KEY` / `SCENEFAB_LLM_KEY` 环境变量(任一非空即 live)
  - live mode 下: `_setup_pipeline` 调 `maker.create_project(src, ctx)`,失败自动降级 noop 并打 warning
  - 5 步 → runner 映射:0/1 = noop (`create_project` 内部处理), 2 = `generate_script`, 3 = `generate_voice + generate_captions`, 4 = `project.save()`
  - 新增 `_reset_step_state()` 方法(只重置 step 状态,保留 `_runner_mode` / `_current_project`)
  - 4 个新测试:runner_mode 默认 noop / env 触发 live / `_has_runtime_keys` 单元 / live 失败降级 noop

- **feat(ui): wire 2D+ import button to file dialog (拖拽导入素材 placeholder)**
  - `AssetsPage` `_on_import_requested` slot:点击"导入素材"按钮弹 `QFileDialog.getOpenFileNames` 多选
  - 过滤器支持视频 (mp4/mov/mkv/avi/flv/wmv) + 音频 (mp3/wav/m4a/flac) + 所有文件 fallback
  - 选中后调 `vm.import_media(paths)` 转发到 `ProjectManager.add_media_file`
  - 留口:`_show_import_dialog(parent)` 是 public 公开方法,后续可由 router/main_window 层重写支持拖拽 (dragEnterEvent / dropEvent)
  - 移除了 `import_requested` signal 的 emit — page 自治,信号无人接是 zombie(已无消费者)

- **feat(ui): Phase 3 dark theme palette + set_theme_mode runtime switch**
  - `ui/theme/ds_tokens.py` 新增 `DarkColors` class — 41 个 color token 全部镜像(深色背景 + 提亮主色 + 反转文字)
  - `set_theme_mode(mode: str) -> str` 全局函数:重新绑定 `_C` 所有颜色属性到 `Colors` / `DarkColors` 对应 palette
  - `get_theme_mode() -> str` 读 active 状态;支持 `"light"` / `"dark"`,未知 fallback light
  - **重要限制**:切换 mode **不自动 restyle** 已渲染 widget — caller 需自己重设 stylesheet(架构简化,Phase 3+ 接 settings toggle 时再补 `restyle_app()`)
  - 持久化由 Application / QSettings 层负责,函数只返回新 mode
  - 7 个新测试 `tests/test_theme.py`:default mode / dark rebind / light reset / unknown fallback / palette key 一致性 / idempotent / dark ≠ light

- **refactor(ui): drop zombie re-export of SceneFabMainWindow from __init__** (P1 架构清理)
  - `scenefab.ui.__init__` 删除 `from .main.main_window import SceneFabMainWindow` + `__all__`
  - 真消费者( `main.py` / tests)用 `from scenefab.ui.main.main_window import SceneFabMainWindow` 显式路径
  - **价值**:解 `import scenefab.ui.viewmodels.X` → `scenefab.ui.__init__` → `SceneFabMainWindow` → `PySide6.QtWidgets` → libEGL 链
  - 这是 06-30 早 + 06-30 晚两轮 libEGL 修复的**根因** —— 现在 viewmodel 测试不再触发 QtWidgets 加载
  - 单测 `tests/test_theme.py` 顺利在 CI 跑(纯 Python,无 libEGL 依赖)

### 🧪 Tests

- 新增 11 个测试 (4 production 2B+1 + 7 theme),共 **784 passed / 1 skipped** (基线 773 → +11)
- 关键覆盖:runner_mode 切换 (env-gated) / live 失败降级 noop / theme rebind / palette key 一致性 / unknown mode fallback

### 🔮 后续 (P1, 暂未实现)

- **Phase 3+**:settings page 加主题切换 UI + `restyle_app()` 函数遍历 QApplication.allWidgets() 重设 stylesheet

### ✅ Phase 3+ 闭环 (本次提交 05b885f)

- **feat(ui): wire Phase 3 runtime theme switcher + Settings UI**
  - `ui/theme/runtime.py`(新):`restyle_app(app=None) -> int` 遍历 `QApplication.allWidgets()`,对每个 widget 调 `style().unpolish(w) / polish(w) / w.update()`;headless/无 QApplication 路径返回 0
  - `ThemeAwareMixin` 让 `QWidget` 派生类持 `_build_stylesheet: Callable[[], str]`,`apply_theme()` 重新求值并 `setStyleSheet(qss)` 返回新 QSS
  - `ui/theme/__init__.py`(新):包级 re-export `restyle_app` / `ThemeAwareMixin` / `set_theme_mode` / `get_theme_mode` / 全部 design token,统一入口
  - `SceneFabMainWindow(QMainWindow, ThemeAwareMixin)`: 初始化时 `setStyleSheet(build_global_stylesheet())`,通过 `_wire_theme_switcher()` 懒连接 `SettingsPage.theme_changed` signal (用 `_theme_signal_wired` flag 去重,因为 router 缓存页面会重复 visit)
  - `_on_theme_switched(mode)`: 完整切换链 `set_theme_mode(mode)` → `self.apply_theme()` → 遍历 `router._page_map` 找所有 `ThemeAwareMixin` 页面 `apply_theme()` → `restyle_app()` 重 polish 非主题 widget (e.g. native dialog)
  - `SettingsPage(QFrame, ThemeAwareMixin)`: 新增 `_appearance_group` (浅色/深色 combo),`currentIndexChanged` 触发 `theme_changed` signal 传 `"light"` / `"dark"`;同时提供 `set_theme_mode_index(mode)` 在 startup 时从 QSettings 恢复用户偏好
  - `docs/public/logo-horizontal.svg`(新): 暗色主题配套横版 logo (与正方形 logo 同色系,横版布局适配 512x128)
  - **mypy 清理**: 删除 3 个未触发的 `# type: ignore` 注释 (`ThemeAwareMixin.__init__` / `getattr` 返回 `Any` 等);`restyle_app` 加 `isinstance(app, QApplication)` 收窄 `QCoreApplication` 类型差
  - **架构价值**: Phase 3 暗色主题从「token 切了但 UI 不刷新」升到「Settings → SettingsPage.combo → MainWindow → 所有页面 + 全局 widget 实时重 polish」端到端闭环

### 🧪 Tests (本次新增 7)

- 新增 7 个测试,共 **791 passed / 1 skipped** (基线 784 → +7)
- `tests/test_theme_runtime.py`:
  - `test_restyle_app_returns_zero_without_qapplication` / `test_restyle_app_returns_int` / `test_restyle_app_accepts_explicit_app_argument` — headless 路径 (mock QApplication.instance() → None)
  - `test_theme_aware_mixin_apply_theme_runs_builder` / `test_theme_aware_mixin_picks_up_token_changes` — builder 重新求值 + token 切换可观测
  - `test_theme_aware_mixin_does_not_require_qt` — mixin 与 Qt 解耦回归保护
  - `test_theme_package_exports_runtimes` — `scenefab.ui.theme` 包 re-export 完整性
- **修复 1 个真测试设计 bug**: `no_qapp` fixture 用 `monkeypatch.setattr(QApplication, "instance", ...)` 隔离跨测试 QApplication 单例污染 —— 此前 `test_home_viewmodel` 跑完后 `restyle_app` 静默遍历残留 widgets (140 个),headless 测试断言 `0 == 140` 一直假绿
- **Phase 2D+ 后**:drag-drop 文件拖拽 (`dragEnterEvent` / `dropEvent` override on `AssetsPage`)
- **分层错位彻底解决**:viewmodel 直接 import `scenefab.services.X` / `scenefab.models.X`,不 import `scenefab.ui.*` 任何东西(目前用 `TYPE_CHECKING` 解决 runtime,但逻辑分层仍耦合 UI 类型)

### 🧹 Chore

- **refactor(ui): drop dead theme + split main window + wire application** (commit `8e7c8f4`) — Phase 1 重构,净 **-1536 行**
  - 删除 1462 行死代码:`tokens.py` / `theme_manager.py` / `base_styles.py` / `resources/styles/*.qss` / 空 `__pycache__` 幽灵目录
  - `ui/main/registry.py`(新):`NAV_ITEMS` / `PAGE_TITLES` / `PAGE_BUILDERS` 单源真相,消除 `nav_components.NAV_ITEMS` 与 `main_window.PAGE_TITLES` 双源
  - `ui/main/page_router.py`(新):页面懒加载 + 路由
  - `ui/main/system_tray.py`(新):系统托盘生命周期
  - `ui/main/controls.py`(新):`ToggleSwitch` 抽离
  - `SceneFabMainWindow` 从 273 行(6 职责)缩为装配器,接 `application=` 注入(Phase 2 留口)
  - 测试 `test_ui_main_window` / `test_ui_module_smoke` 改为验证 `router.cached_pages()` + `registry.PAGE_BUILDERS` 而非原 `_page_map` 预填假设
  - 755 passed / 1 skipped(基线 562 → +193 项目成长)

- **feat(ui): HomePage ViewModel + service injection** (commit TBD) — Phase 2A,4 张状态卡接 `ProjectManager` 实时数据
  - `ui/viewmodels/__init__.py`(新):`ViewModelBase` 抽象基类
  - `ui/viewmodels/home_viewmodel.py`(新):`HomePageViewModel` 订阅 `project_opened` / `project_closed` / `project_saved` / `recent_projects_updated` 信号,暴露 5 个变化信号
  - `ui/main/registry.py`:`PageBuilder` 签名从 `() -> QWidget` 改为 `(Application | None) -> QWidget`,新增 `_build_home` 工厂
  - `PageRouter.__init__` 接 `application=`,转给 `PAGE_BUILDERS[page_id](app)`
  - `HomePage` 接 `viewmodel=` 参数,4 张状态卡改读 `vm.media_count` / `scene_count` / `script_status` / `export_config`,最近资产改读 `vm.recent_projects`
  - 无 project / 无 application 时,VM fallback 到"未导入 / 0 / 待生成 / 1080x1920" 默认文案(行为同 Phase 1)
  - 新增 4 个测试 `tests/test_home_viewmodel.py`,覆盖:无 application fallback / 有 application 无 project / 有 VM 渲染 / 无 VM 静态默认
  - **759 passed / 1 skipped**(755 → +4 ViewModel 测试)

### ⚠️ 不兼容变更

- `SceneFabMainWindow` 必传 `application=` 参数(主入口 `main.py` 已同步)
- 页面元数据(导航 / 标题 / 工厂)统一从 `scenefab.ui.main.registry` 导入
- `PageBuilder` 签名变更:`(Application | None) -> QWidget`,第三方自定义 page builder 需要更新

---

## [2.3.0] - 2026-06-26

> SceneFab v2.3.0 — 代码审计 + 2 P1 安全修复 + API/UI 测试覆盖补齐

### 🐛 Bug Fixes

- **fix(security): hardware.py subprocess 走 SecureExecutor 审计链** — `check_nvidia_smi` / `check_intel_cpu` 改走新 `get_probe_executor()` 单例 (白名单: nvidia-smi, wmic), 不再裸 `subprocess.run`. 移除 `import subprocess`. 异常类型改 `SecurityError` + `TimeoutError`
- **fix(security): api/routers/pipeline.py 缺路径校验** — 复用 export router 模式 (`_DEFAULT_ALLOWED_BASE_DIRS` + `_get_path_validator` + `_validate_output_dir`), 早期拒绝空 `video_url`, `_process_narration` 校验 `output_dir` 失败时降级到 `cwd/outputs/jianying_drafts`
- **fix(api): GET / 根路由未注册** — `@app.get("/")` 在 `app = create_app()` 之后定义, 装饰器把 root 注册到 `app` 局部变量, 实际不生效. 修复: 把 root 移入 `create_app()` 函数内
- **fix(api): GET /api/v1/plugins/types 永远 404** — FastAPI 按路由声明顺序匹配, `/plugins/{plugin_id}` 在 `/plugins/types` 之前注册, 拦截 "types" 路径. 修复: 重排为 `/plugins` → `/plugins/types` → `/plugins/{plugin_id}` → `/plugins/{plugin_id}/enable`
- **fix(ci): detect libEGL.so.1 to skip ui smoke in headless CI** (commit `3ea77e6`) — 之前 conftest 只在 PySide6 import 失败时 skip, 但 CI runner 装了 PySide6 + 无 libEGL 时 `importlib` 仍尝试加载 Qt → `libEGL.so.1` 缺失. 修复: 加 `ctypes.CDLL` 检测 libEGL, 缺则 skip ui smoke. 本地 PySide6 6.11 + offscreen 仍能跑全部 8 个测试

### 🔧 Maintenance

- **refactor(llm): narrow HTTPClientMixin._call_api** — 改前 `except Exception` (宽 catch, 吞 RuntimeError/TypeError), 改后异常分两段 catch: `httpx.HTTPStatusError` → `_handle_http_error`, `httpx.HTTPError` → `ProviderError("网络错误")`, `json.JSONDecodeError/ValueError` → `ProviderError("响应解析")`. 真 bug 不再被吞
- **chore(cleanup): jianying_exporter.py MaterialType 注释** — pyflakes 报 "unused", 实际是间接 re-export (不在 `__all__` 但与其他 adapter 类型对齐). 注释明确为 "package-private" + 指引测试用 `from jianying_adapter import` 直路径
- **test(api): 补 api/ 0% 测试覆盖** — 18 个集成测试覆盖 5 个 router (health/pipeline/plugins/export/projects) + 全局异常处理 + 路由顺序
- **test(ui): 补 ui/ 0% 测试覆盖** — 8 个 headless-safe smoke test 覆盖 SceneFabMainWindow 类结构 + 子模块 import + theme 模块
- **style: ruff auto-fix 49 lint errors + skip ui smoke in headless CI** (commit `fff0168`) — R13 audit 引入 49 个 ruff 错 (17 F401 + 15 I001 + 2 F841 + 8 UP0xx + 1 B007) 未跑 `ruff --fix`. `--fix --unsafe-fixes` 全自动清零, 19 文件 +39/-52. **0 行为变化**
- **chore(dead-code): drop 2 unused plugin example plugins (-655 LOC)** (commit `fcc8203`) — Dim 14 dead-file scan 报 40 候选, pytest 验证后仅 2 真死 (`plugins/examples/cinematic_subtitle` + `plugins/examples/deepseek_ai_generator`). 其余 38 个是 `_EXPORTS` lazy import / relative `__init__.py` import / `__main__.py` 隐式引用 / startup smoke test 引用 — 全保. **净效果**: 2 files / 655 LOC 真死删除, 0 行为变化

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
