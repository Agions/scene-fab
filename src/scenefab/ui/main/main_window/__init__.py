"""
SceneFab 主窗口包

专业生产工作台布局:
- 左侧文本导航
- 顶部操作栏
- 中央生产页面
- 底部状态栏
"""

from __future__ import annotations

from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)

from scenefab.ui.theme.ds_tokens import _C, FontSizes, Radii

from .content_area import ContentArea
from .nav_components import Sidebar
from .status_bar import StatusBar
from .top_bar import TopBar


class SceneFabMainWindow(QMainWindow):
    """SceneFab 主窗口"""

    PAGE_TITLES = {
        "home": ("工作台", ""),
        "create": ("创作流程", ""),
        "assets": ("项目资产", ""),
        "settings": ("设置", ""),
    }

    def __init__(self, application=None):
        super().__init__()
        self._application = application
        self.setWindowTitle("SceneFab")
        self.setMinimumSize(1200, 720)
        self._tray = None
        self._minimize_to_tray_enabled = False
        self._quitting = False
        self._last_project = None  # 最近一次生产完成的项目（MonologueProject）
        self._setup_ui()
        self._connect_signals()
        self._apply_global_style()
        self._init_tray()

    def _setup_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        # 垂直布局：上半为 [侧边栏 | 主内容]，底部为状态栏
        outer = QVBoxLayout(central)
        outer.setContentsMargins(0, 0, 0, 0)
        outer.setSpacing(0)

        body = QWidget()
        root = QHBoxLayout(body)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        # 侧边栏
        self.sidebar = Sidebar()
        root.addWidget(self.sidebar)

        # 主内容
        self.content = ContentArea()
        self._lazy_load_pages()
        root.addWidget(self.content, 1)

        outer.addWidget(body, 1)

        # 顶部栏
        self.topbar = TopBar("工作台")
        self.setMenuWidget(self.topbar)

        # 状态栏（自绘 QFrame，置于底部，而非 QMainWindow.setStatusBar）
        self.statusbar = StatusBar()
        outer.addWidget(self.statusbar)

    def _lazy_load_pages(self):
        from scenefab.ui.main.pages.assets_page import AssetsPage
        from scenefab.ui.main.pages.home_page import HomePage
        from scenefab.ui.main.pages.production_page import ProductionPage
        from scenefab.ui.main.pages.settings_page import SettingsPage

        home = HomePage()
        home.create_project.connect(lambda: self._on_navigate("create"))
        home.open_project.connect(self._on_open_project)
        home.navigate.connect(self._on_navigate)

        production = ProductionPage()
        production.start_requested.connect(self._on_start_production)
        self._production_page = production

        project_manager = None
        settings_manager = None
        if self._application is not None:
            project_manager = self._application.get_service_by_name("project_manager")
            settings_manager = self._application.get_service_by_name(
                "settings_manager"
            )

        assets = AssetsPage(project_manager=project_manager)
        assets.import_requested.connect(self._on_import_assets)
        self._assets_page = assets
        self._project_manager = project_manager

        settings = SettingsPage(settings_manager=settings_manager)

        self.content.add_page("home", home)
        self.content.add_page("create", production)
        self.content.add_page("assets", assets)
        self.content.add_page("settings", settings)

        # 页面挂载到窗口后重新加载设置，确保托盘等窗口级状态同步
        if settings_manager is not None:
            settings.load_settings()

        # Populate HomePage with real data from ProjectManager
        if project_manager is not None:
            projects = project_manager.scan_projects()
            home.update_stats(
                projects_count=len(projects),
                assets_count=sum(
                    len(p.media_files) for p in project_manager.get_all_projects()
                ),
            )
            home.update_recent_projects(project_manager.get_recent_projects())

    def _connect_signals(self):
        self.sidebar.navigated.connect(self._on_navigate)
        self.topbar.action_triggered.connect(self._on_action)

    # ══════════════════════════════════════════════════════════════
    # 系统托盘集成
    # ══════════════════════════════════════════════════════════════

    def _init_tray(self):
        """初始化系统托盘（始终可用，是否激活由设置决定）"""
        try:
            from scenefab.ui.main.tray_manager import get_tray_manager

            self._tray = get_tray_manager()
            self._tray.show_window_requested.connect(self._restore_from_tray)
            self._tray.open_settings_requested.connect(self._open_settings_from_tray)
            self._tray.quit_requested.connect(self._quit_application)
        except Exception as e:
            import logging

            logging.getLogger(__name__).warning(f"Tray init failed: {e}")
            self._tray = None

    def set_minimize_to_tray(self, enabled: bool):
        """设置是否启用"关闭窗口时最小化到托盘" """
        self._minimize_to_tray_enabled = bool(enabled)
        if enabled and self._tray is not None and not self._tray.is_enabled:
            self._tray.enable(self.windowTitle())
        elif not enabled and self._tray is not None and self._tray.is_enabled:
            self._tray.disable()

    def _restore_from_tray(self):
        """从托盘恢复窗口"""
        self.showNormal()
        self.raise_()
        self.activateWindow()

    def _open_settings_from_tray(self):
        """从托盘菜单打开设置页"""
        self._restore_from_tray()
        self._on_navigate("settings")

    def _quit_application(self):
        """真正退出应用（绕过托盘拦截）"""
        self._quitting = True
        if self._tray is not None:
            self._tray.disable()
        self.close()
        QApplication.instance().quit()  # type: ignore[union-attr]

    def closeEvent(self, event):
        """窗口关闭事件"""
        if self._quitting:
            event.accept()
            return
        if (
            self._minimize_to_tray_enabled
            and self._tray is not None
            and self._tray.is_enabled
            and self._tray.is_available
        ):
            event.ignore()
            self.hide()
            if not hasattr(self, "_tray_hint_shown"):
                self._tray.show_notification(
                    "SceneFab",
                    "应用已最小化到系统托盘。双击图标或右键菜单可恢复窗口。",
                )
                self._tray_hint_shown = True
            return
        if self._tray is not None:
            self._tray.disable()
        event.accept()

    def _on_navigate(self, page_id: str):
        self.content.set_page(page_id)
        title, breadcrumb = self.PAGE_TITLES.get(page_id, (page_id, ""))
        self.topbar.set_title(title, breadcrumb)
        self.statusbar.set_status(f"当前: {title}")

    def navigate_to(self, page_id: str, **kwargs):
        """导航到指定页面（公共接口）"""
        self._on_navigate(page_id)

    @property
    def app(self):
        """获取 QApplication 实例"""
        return QApplication.instance()

    def show_message(self, message: str, level: str = "info"):
        """显示消息提示"""
        from PySide6.QtWidgets import QMessageBox

        if level == "error":
            QMessageBox.critical(self, "错误", message)
        elif level == "warning":
            QMessageBox.warning(self, "警告", message)
        else:
            QMessageBox.information(self, "提示", message)

    def show_loading(self, show: bool = True):
        """显示/隐藏加载状态"""
        self.statusbar.set_status("加载中..." if show else "就绪")

    def _on_action(self, action_id: str):
        if action_id == "export":
            self._on_export()

    def _on_export(self):
        """导出对话框：选择格式和输出目录，执行导出"""
        from PySide6.QtWidgets import QFileDialog, QInputDialog, QMessageBox

        # 必须已完成生产流程，才有真实项目数据可供导出
        if self._last_project is None:
            QMessageBox.warning(self, "无法导出", "请先完成生产流程")
            return

        # 选择导出格式
        formats = ["剪映草稿", "MP4 视频"]
        fmt_choice, ok = QInputDialog.getItem(
            self, "导出格式", "请选择导出格式:", formats, 0, False
        )
        if not ok:
            return

        # 选择输出目录
        output_dir = QFileDialog.getExistingDirectory(self, "选择导出目录")
        if not output_dir:
            return

        # 执行导出
        from scenefab.services.export.export_manager import (
            ExportConfig,
            ExportFormat,
            ExportManager,
        )

        export_format = (
            ExportFormat.JIANYING if fmt_choice == "剪映草稿" else ExportFormat.MP4
        )
        config = ExportConfig(format=export_format, output_path=output_dir)

        try:
            manager = ExportManager()
            project_data = self._build_export_data(export_format)
            manager.export(project_data, config)
            self.statusbar.set_status("导出成功")
            QMessageBox.information(self, "导出成功", f"已导出到:\n{output_dir}")
        except Exception as e:
            self.statusbar.set_status(f"导出失败: {e}")
            QMessageBox.critical(self, "导出失败", f"导出过程中出错:\n{e}")

    def _build_export_data(self, export_format):
        """将最近生产的项目转换为 ExportManager 期望的数据格式"""
        from scenefab.services.export.export_manager import ExportFormat

        project = self._last_project
        if export_format == ExportFormat.JIANYING:
            # 剪映导出需要带真实轨道的 JianyingDraft
            from scenefab.services.export.jianying_adapter import JianyingDraft
            from scenefab.services.video.track_builder import build_monologue_tracks

            draft = JianyingDraft(name=project.name)
            build_monologue_tracks(
                draft=draft,
                source_video=project.source_video,
                video_duration=project.video_duration,
                segments=project.segments,
                caption_style=project.caption_style,
            )
            return draft
        # MP4/MOV/GIF: DirectVideoExporter.export_commentary 需要项目对象本身
        return project

    # ══════════════════════════════════════════════════════════════
    # 生产流程接线
    # ══════════════════════════════════════════════════════════════

    def _on_start_production(self):
        """开始新生产流程：选择源视频 → 设置创作参数 → 后台运行 MonologueMaker"""
        from PySide6.QtWidgets import QFileDialog, QInputDialog

        video_path, _ = QFileDialog.getOpenFileName(
            self,
            "选择源视频",
            "",
            "视频文件 (*.mp4 *.mov *.avi *.mkv *.flv *.wmv);;所有文件 (*)",
        )
        if not video_path:
            return

        # 解说主题/上下文（create_project 的必填参数）
        context, ok = QInputDialog.getText(
            self, "创作设置", "解说主题/上下文:", text="第一人称影视解说"
        )
        if not ok or not context.strip():
            return

        # 情感风格
        emotions = ["neutral", "惆怅", "忧郁", "开心", "平静", "温柔", "excited"]
        emotion, ok = QInputDialog.getItem(
            self, "创作设置", "情感风格:", emotions, 0, False
        )
        if not ok:
            return

        self.statusbar.set_status(f"正在处理: {video_path}")
        self.show_loading(True)
        if hasattr(self, "_production_page"):
            self._production_page.reset_steps()
            self._production_page.update_step_status(
                "素材审片", "进行中", _C.PRIMARY
            )

        # 后台线程运行 MonologueMaker
        from scenefab.core.base_worker import BaseWorker

        class ProductionWorker(BaseWorker):
            def _run(self):
                from pathlib import Path

                from scenefab.services.video.monologue_maker import MonologueMaker

                maker = MonologueMaker()
                project = maker.create_project(
                    source_video=video_path,
                    context=context,
                    emotion=emotion,
                )
                if project is None:
                    raise RuntimeError("项目创建失败")
                self.emit_progress(1, 5, "场景分析完成")
                if self.check_cancel_or_pause():
                    return

                maker.generate_script(project)
                self.emit_progress(2, 5, "脚本生成完成")
                if self.check_cancel_or_pause():
                    return

                maker.generate_voice(project)
                self.emit_progress(3, 5, "配音合成完成")
                if self.check_cancel_or_pause():
                    return

                maker.generate_captions(project)
                self.emit_progress(4, 5, "字幕生成完成")

                # 保存项目到 .scenefab 文件，避免生产结果丢失
                output_path = Path(project.output_dir) / f"{project.name}.scenefab"
                project_path = project.save(str(output_path))
                self.emit_progress(5, 5, "项目已保存")

                return {"project": project, "project_path": project_path}

        self._production_worker = ProductionWorker(
            name="ProductionWorker", cancellable=True
        )
        self._production_worker.progress.connect(self._on_production_progress)
        self._production_worker.finished.connect(self._on_production_finished)
        self._production_worker.error.connect(self._on_production_error)
        self._production_worker.start()

    def _on_production_progress(self, current, total, message):
        self.statusbar.set_status(f"[{current}/{total}] {message}")
        # Map worker progress to production page step names
        _PROGRESS_STEP_MAP = {
            1: "素材审片",
            2: "冲突拆解",
            3: "配音字幕",
            4: "配音字幕",
        }
        step_name = _PROGRESS_STEP_MAP.get(current)
        if step_name and hasattr(self, "_production_page"):
            self._production_page.update_step_status(
                step_name, "已完成", "#52c41a"
            )

    def _on_production_finished(self, result):
        from PySide6.QtWidgets import QMessageBox

        self.show_loading(False)
        if not (result and result.success):
            self.statusbar.set_status("生产流程完成（有警告）")
            return

        # 保存最近一次生产的项目，供导出/另存使用
        data = result.data or {}
        self._last_project = data.get("project")
        project_path = data.get("project_path", "")
        self.statusbar.set_status("✅ 生产流程完成")

        msg = "第一人称解说视频生产完成！"
        if project_path:
            msg += f"\n项目已保存到:\n{project_path}"

        box = QMessageBox(self)
        box.setWindowTitle("生产完成")
        box.setText(msg)
        export_btn = box.addButton("导出成片", QMessageBox.ButtonRole.ActionRole)
        save_btn = box.addButton("保存项目", QMessageBox.ButtonRole.ActionRole)
        box.addButton("关闭", QMessageBox.ButtonRole.RejectRole)
        box.exec()

        clicked = box.clickedButton()
        if clicked == export_btn:
            self._on_export()
        elif clicked == save_btn:
            self._on_save_project()

    def _on_production_error(self, error_msg):
        self.show_loading(False)
        self.statusbar.set_status(f"❌ 生产失败: {error_msg}")
        self.show_message(f"生产流程出错:\n{error_msg}", level="error")

    def _on_open_project(self, path: str = ""):
        """打开已有的 .scenefab 项目文件"""
        from PySide6.QtWidgets import QFileDialog, QMessageBox

        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "打开项目",
            path or "",
            "SceneFab 项目 (*.scenefab);;所有文件 (*)",
        )
        if not file_path:
            return

        try:
            from scenefab.services.video.monologue_maker import MonologueProject

            project = MonologueProject.load(file_path)
        except Exception as e:
            QMessageBox.critical(self, "打开失败", f"无法加载项目:\n{e}")
            return

        self._last_project = project
        self.statusbar.set_status(f"已打开项目: {project.name}")
        QMessageBox.information(
            self,
            "项目已打开",
            f"项目: {project.name}\n"
            f"源视频: {project.source_video}\n"
            f"时长: {project.video_duration:.1f}s\n"
            f"片段数: {len(project.segments)}\n"
            f"上下文: {project.context}",
        )

    def _on_save_project(self):
        """将当前项目另存为 .scenefab 文件"""
        from PySide6.QtWidgets import QFileDialog, QMessageBox

        if self._last_project is None:
            QMessageBox.warning(self, "无法保存", "请先完成生产流程")
            return

        default_name = f"{self._last_project.name}.scenefab"
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "保存项目",
            default_name,
            "SceneFab 项目 (*.scenefab)",
        )
        if not file_path:
            return

        try:
            saved = self._last_project.save(file_path)
        except Exception as e:
            QMessageBox.critical(self, "保存失败", f"保存项目出错:\n{e}")
            return

        self.statusbar.set_status(f"项目已保存: {saved}")
        QMessageBox.information(self, "保存成功", f"项目已保存到:\n{saved}")

    def _on_import_assets(self):
        """导入素材：打开文件选择对话框，将素材添加到 AssetsPage 列表"""
        from PySide6.QtWidgets import QFileDialog

        files, _ = QFileDialog.getOpenFileNames(
            self,
            "导入素材",
            "",
            "媒体文件 (*.mp4 *.mov *.avi *.mkv *.mp3 *.wav *.jpg *.png);;所有文件 (*)",
        )
        if not files:
            return

        self.statusbar.set_status(f"已选择 {len(files)} 个素材文件")

        # Show imported files in the AssetsPage list
        if hasattr(self, "_assets_page"):
            self._assets_page.add_imported_files(files)

        # Register media files with the current project if one is open
        pm = getattr(self, "_project_manager", None)
        if pm is not None:
            current = pm.get_current_project()
            if current is not None:
                import shutil
                from pathlib import Path

                from scenefab.models.project_models import ProjectMedia

                media_dir = Path(current.path) / "media"
                media_dir.mkdir(parents=True, exist_ok=True)
                for fp in files:
                    src = Path(fp)
                    dst = media_dir / src.name
                    if not dst.exists():
                        shutil.copy2(src, dst)
                    media = ProjectMedia(
                        id=f"{src.stem}_{src.suffix.lstrip('.')}",
                        name=src.name,
                        type=src.suffix.lstrip(".").lower(),
                        path=str(dst),
                    )
                    current.add_media_file(media)
                pm.save_project(current.id)

    def _apply_global_style(self):
        self.setStyleSheet(f"""  # type: ignore[attr-defined]
            QMainWindow {{
                background: {_C.BG_BASE};
                outline: none;
            }}
            QToolButton#topbar_action_btn {{
                background: {_C.BG_SURFACE};
                border: 1px solid {_C.BORDER_DEFAULT};
                border-radius: {Radii.base};
                color: {_C.TEXT_SECONDARY};
                font-size: {FontSizes.xs}px;
                font-weight: 600;
            }}
            QToolButton#topbar_action_btn:hover {{
                background: {_C.PRIMARY_LIGHTEST};
                color: {_C.PRIMARY_DARKER};
                border-color: {_C.PRIMARY};
            }}
            QToolTip {{
                background: {_C.TEXT_PRIMARY};
                color: {_C.TEXT_INVERSE};
                border: 1px solid {_C.TEXT_PRIMARY};
                border-radius: {Radii.sm};
                padding: 6px 10px;
                font-size: {FontSizes.xs}px;
            }}
            QScrollBar:vertical {{
                background: transparent;
                width: 6px;
                margin: 0;
            }}
            QScrollBar::handle:vertical {{
                background: {_C.BORDER_DEFAULT};
                border-radius: 3px;
                min-height: 40px;
            }}
            QScrollBar::handle:vertical:hover {{
                background: {_C.PRIMARY};
            }}
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
                height: 0;
            }}
            QScrollBar:horizontal {{
                background: transparent;
                height: 6px;
                margin: 0;
            }}
            QScrollBar::handle:horizontal {{
                background: {_C.BORDER_DEFAULT};
                border-radius: 3px;
                min-width: 40px;
            }}
            * {{
                selection-background-color: {_C.PRIMARY};
                selection-color: {_C.TEXT_INVERSE};
            }}
        """)


__all__ = ["SceneFabMainWindow"]
