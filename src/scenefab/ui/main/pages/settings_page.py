#!/usr/bin/env python3
"""Application settings page."""

from typing import Any

from PySide6.QtCore import QSettings, Qt, Signal
from PySide6.QtWidgets import (
    QComboBox,
    QFileDialog,
    QFrame,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

<<<<<<< HEAD
from ...theme.ds_tokens import _C, FontSizes, FontWeights, Radii, ui_font
from .page_view_models import SETTINGS_GROUPS, SettingRowView
=======
from ...theme.ds_tokens import _C, FontSizes, Radii, get_theme_mode
from ...theme.runtime import ThemeAwareMixin
from ..controls import ToggleSwitch
>>>>>>> ee9c209ea90d432a86973b7316565e83ab68e46f
from .page_widgets import (
    action_button_style,
    header_panel,
    page_background_style,
    page_container,
    panel,
    scroll_area,
    section_title,
)

<<<<<<< HEAD
# 界面语言标签 ↔ ProjectSettingsManager 语言代码
_LANGUAGE_LABEL_TO_CODE = {"简体中文": "zh-CN", "English": "en-US"}
_LANGUAGE_CODE_TO_LABEL = {v: k for k, v in _LANGUAGE_LABEL_TO_CODE.items()}

# 编码选项标签 ↔ ProjectSettingsManager 编码器值
_CODEC_LABEL_TO_VALUE = {
    "MP4 / H.264": "h264",
    "MP4 / H.265": "h265",
    "MOV / ProRes": "prores",
}
_CODEC_VALUE_TO_LABEL = {v: k for k, v in _CODEC_LABEL_TO_VALUE.items()}

# 主题标签 ↔ ThemeManager 模式
_THEME_LABEL_TO_MODE = {"浅色": "light", "深色": "dark"}
_THEME_MODE_TO_LABEL = {v: k for k, v in _THEME_LABEL_TO_MODE.items()}

# QSettings 键（用于 SettingsManager 未覆盖的设置项）
_QSETTINGS_ORG = "SceneFab"
_QSETTINGS_APP = "Application"


class ToggleSwitch(QFrame):
    """Small binary setting control."""

    toggled = Signal(bool)

    def __init__(self, checked: bool = False, parent=None):
        super().__init__(parent)
        self._checked = checked
        self.setFixedSize(42, 22)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setProperty("checked", checked)
        self._setup_style()

    def _setup_style(self):
        self.setStyleSheet(f"""
            QFrame {{
                background: {_C.BG_ELEVATED};
                border: 1px solid {_C.BORDER_DEFAULT};
                border-radius: 11px;
            }}
            QFrame[checked="true"] {{
                background: {_C.PRIMARY};
                border-color: {_C.PRIMARY};
            }}
        """)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.setChecked(not self._checked)
            self.toggled.emit(self._checked)
        super().mousePressEvent(event)

    def isChecked(self) -> bool:
        return self._checked

    def setChecked(self, checked: bool):
        self._checked = checked
        self.setProperty("checked", checked)
        self.style().unpolish(self)
        self.style().polish(self)
=======
# Theme mode options presented in the appearance combo box.
THEME_OPTIONS = ("浅色", "深色")  # display labels
THEME_MODES = ("light", "dark")  # values emitted on theme_changed
>>>>>>> ee9c209ea90d432a86973b7316565e83ab68e46f


class SettingsPage(QFrame, ThemeAwareMixin):
    """Professional settings surface.

    Hosts the theme switcher in :meth:`_appearance_group`. Picking a
    new option emits :attr:`theme_changed`; :class:`SceneFabMainWindow`
    listens and applies the new palette via :func:`restyle_app` plus
    each :class:`ThemeAwareMixin.apply_theme`.
    """

    theme_changed = Signal(str)  # "light" / "dark"

    def __init__(
        self,
        settings_manager: Any = None,
        parent=None,
        *,
        theme_manager: Any = None,
        project_manager: Any = None,
    ):
        super().__init__(parent)
        self.setObjectName("settings_page")
        self._settings_manager = settings_manager
        self._theme_manager = theme_manager
        self._project_manager = project_manager
        self._tray_toggle: ToggleSwitch | None = None
<<<<<<< HEAD
        self._controls: dict[str, QWidget] = {}
        self._path_edits: dict[str, QLineEdit] = {}
        self._status_label: QLabel | None = None
        self._setup_style()
        self._setup_ui()
        self._connect_tray_signal()
        self._connect_auto_save_signal()
        self.load_settings()
=======
        self._theme_combo: QComboBox | None = None
        # Apply stylesheet once ThemeAwareMixin is in the MRO. The mixin
        # has no ``__init__`` — declaring it on the class is enough.
        ThemeAwareMixin.__init__(self)
        self.setStyleSheet(self._build_stylesheet())
        self._setup_ui()
        self._connect_tray_signal()
        self._connect_theme_signal()
>>>>>>> ee9c209ea90d432a86973b7316565e83ab68e46f

    def _setup_style(self):
        # Kept for backwards-compat: ThemeAwareMixin.__init__ now calls
        # build_stylesheet directly. Re-applied here so subclasses that
        # override ``_setup_style`` keep working.
        self.setStyleSheet(page_background_style("settings_page"))

    def _build_stylesheet(self) -> str:
        """Return the page-level stylesheet using the **current** ``_C``.

        Used by :class:`ThemeAwareMixin.apply_theme` to refresh colours
        after :func:`set_theme_mode`.
        """
        return page_background_style("settings_page")

    def _setup_ui(self):
        root = QVBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)

        scroll = scroll_area()
        container = page_container()
        layout = container.layout()
        assert layout is not None  # for type checker

        layout.addWidget(self._build_header())
<<<<<<< HEAD
        for title, rows in SETTINGS_GROUPS:
            layout.addWidget(self._settings_group(title, rows))
        layout.addWidget(self._build_footer())
=======
        layout.addWidget(self._workspace_group())
        layout.addWidget(self._appearance_group())
        layout.addWidget(self._ai_group())
        layout.addWidget(self._export_group())
        layout.addWidget(self._behavior_group())
>>>>>>> ee9c209ea90d432a86973b7316565e83ab68e46f
        layout.addStretch()

        scroll.setWidget(container)
        root.addWidget(scroll)

    def _connect_tray_signal(self):
        if self._tray_toggle is not None:
            self._tray_toggle.toggled.connect(self._on_tray_toggled)

    def _connect_theme_signal(self):
        if self._theme_combo is not None:
            self._theme_combo.currentIndexChanged.connect(self._on_theme_changed)

    def _on_theme_changed(self, index: int) -> None:
        if 0 <= index < len(THEME_MODES):
            mode = THEME_MODES[index]
            self.theme_changed.emit(mode)

    def set_theme_mode_index(self, mode: str) -> None:
        """Programmatically select a theme option without firing the signal.

        Used by :class:`SceneFabMainWindow` when restoring the user's
        persisted preference on startup. Falls back silently when the
        combo has not been built yet (headless test path).
        """
        if self._theme_combo is None or mode not in THEME_MODES:
            return
        target = THEME_MODES.index(mode)
        self._theme_combo.blockSignals(True)
        self._theme_combo.setCurrentIndex(target)
        self._theme_combo.blockSignals(False)

    def _on_tray_toggled(self, checked: bool):
        window = self.window()
        if window is not None and hasattr(window, "set_minimize_to_tray"):
            window.set_minimize_to_tray(checked)

    def _connect_auto_save_signal(self):
        auto_save = self._controls.get("auto_save")
        if isinstance(auto_save, ToggleSwitch):
            auto_save.toggled.connect(self._on_auto_save_toggled)

    def _on_auto_save_toggled(self, checked: bool):
        pm = self._project_manager
        if pm is not None and hasattr(pm, "auto_save_timer"):
            if checked:
                pm.auto_save_timer.start(60000)
            else:
                pm.auto_save_timer.stop()

    def _on_theme_changed(self, label: str):
        mode = _THEME_LABEL_TO_MODE.get(label)
        if mode is None:
            return
        if self._theme_manager is None:
            from ...theme.theme_manager import ThemeManager

            self._theme_manager = ThemeManager()
        self._theme_manager.set_theme_mode(mode)

    # ══════════════════════════════════════════════════════════════
    # 设置持久化
    # ══════════════════════════════════════════════════════════════

    def save_settings(self) -> bool:
        """读取所有控件值并写入 SettingsManager / QSettings。"""
        qsettings = QSettings(_QSETTINGS_ORG, _QSETTINGS_APP)
        manager = self._settings_manager

        # 工作区路径（SettingsManager 未定义，使用 QSettings 持久化）
        for key, qkey in (
            ("project_dir", "workspace/project_dir"),
            ("export_dir", "workspace/export_dir"),
        ):
            edit = self._path_edits.get(key)
            if edit is not None:
                qsettings.setValue(qkey, edit.text().strip())

        # API Key（通过 SettingsManager 的安全密钥存储）
        self._save_api_key()

        # 主题
        theme_label = self._combo_text("theme")
        theme_mode = _THEME_LABEL_TO_MODE.get(theme_label)
        if theme_mode:
            qsettings.setValue("appearance/theme_mode", theme_mode)

        if manager is not None:
            # 语言
            language_label = self._combo_text("language")
            if language_label:
                manager.set_setting(
                    "ui.language",
                    _LANGUAGE_LABEL_TO_CODE.get(language_label, language_label),
                )

            # 默认模型
            model = self._combo_text("default_model")
            if model:
                manager.set_setting("ai.default_model", model)

            # 帧率（"30 fps" → 30）
            fps_text = self._combo_text("fps")
            fps_value = self._parse_fps(fps_text)
            if fps_value is not None:
                manager.set_setting("video.fps", fps_value)

            # 自动保存 / 最小化到托盘
            auto_save = self._controls.get("auto_save")
            if isinstance(auto_save, ToggleSwitch):
                manager.set_setting("auto_save.enabled", auto_save.isChecked())
            if self._tray_toggle is not None:
                manager.set_setting(
                    "ui.minimize_to_tray", self._tray_toggle.isChecked()
                )

            # 画布与编码：SettingsManager 校验未通过时退回 QSettings
            self._save_validated_combo(
                manager, qsettings, "canvas", "video.resolution", "export/canvas"
            )
            self._save_validated_combo(
                manager,
                qsettings,
                "codec",
                "video.codec",
                "export/codec",
                _CODEC_LABEL_TO_VALUE,
            )

        self._show_status("已保存")
        return True

    def load_settings(self):
        """从 SettingsManager / QSettings 读取值并填充控件。"""
        qsettings = QSettings(_QSETTINGS_ORG, _QSETTINGS_APP)
        manager = self._settings_manager

        # 工作区路径
        for key, qkey in (
            ("project_dir", "workspace/project_dir"),
            ("export_dir", "workspace/export_dir"),
        ):
            edit = self._path_edits.get(key)
            value = qsettings.value(qkey, "", type=str)
            if edit is not None and value:
                edit.setText(value)

        # API Key
        self._load_api_key()

        # 主题
        theme_mode = qsettings.value("appearance/theme_mode", "light", type=str)
        theme_label = _THEME_MODE_TO_LABEL.get(theme_mode, "浅色")
        self._set_combo_text("theme", theme_label)

        if manager is None:
            return

        # 语言
        language_code = manager.get_setting("ui.language")
        language_label = _LANGUAGE_CODE_TO_LABEL.get(language_code, language_code)
        self._set_combo_text("language", language_label)

        # 默认模型
        self._set_combo_text("default_model", manager.get_setting("ai.default_model"))

        # 帧率（30 → "30 fps"）
        fps_value = manager.get_setting("video.fps")
        if fps_value is not None:
            self._set_combo_text("fps", f"{fps_value} fps")

        # 画布与编码：优先使用 QSettings 回退值（保留竖屏等自定义项）
        self._load_validated_combo(
            manager, qsettings, "canvas", "video.resolution", "export/canvas"
        )
        self._load_validated_combo(
            manager,
            qsettings,
            "codec",
            "video.codec",
            "export/codec",
            _CODEC_VALUE_TO_LABEL,
        )

        # 自动保存 / 最小化到托盘
        auto_save = self._controls.get("auto_save")
        if isinstance(auto_save, ToggleSwitch):
            auto_save.setChecked(bool(manager.get_setting("auto_save.enabled", True)))
        if self._tray_toggle is not None:
            checked = bool(manager.get_setting("ui.minimize_to_tray", False))
            self._tray_toggle.setChecked(checked)
            self._on_tray_toggled(checked)

    # ── 持久化辅助方法 ────────────────────────────────────────────

    def _combo_text(self, key: str) -> str:
        widget = self._controls.get(key)
        if isinstance(widget, QComboBox):
            return widget.currentText()
        return ""

    def _set_combo_text(self, key: str, value: Any):
        widget = self._controls.get(key)
        if isinstance(widget, QComboBox) and value in self._combo_items(widget):
            widget.setCurrentText(str(value))

    @staticmethod
    def _combo_items(combo: QComboBox) -> list[str]:
        return [combo.itemText(i) for i in range(combo.count())]

    @staticmethod
    def _parse_fps(text: str) -> int | None:
        try:
            return int(text.split()[0])
        except (ValueError, IndexError, AttributeError):
            return None

    def _save_validated_combo(
        self,
        manager: Any,
        qsettings: QSettings,
        key: str,
        manager_key: str,
        fallback_qkey: str,
        label_map: dict[str, str] | None = None,
    ):
        label = self._combo_text(key)
        if not label:
            return
        stored = (label_map or {}).get(label, label)
        if manager.set_setting(manager_key, stored):
            qsettings.remove(fallback_qkey)
        else:
            qsettings.setValue(fallback_qkey, label)

    def _load_validated_combo(
        self,
        manager: Any,
        qsettings: QSettings,
        key: str,
        manager_key: str,
        fallback_qkey: str,
        value_map: dict[str, str] | None = None,
    ):
        fallback = qsettings.value(fallback_qkey, "", type=str)
        if fallback:
            self._set_combo_text(key, fallback)
            return
        stored = manager.get_setting(manager_key)
        if stored is None:
            return
        label = (value_map or {}).get(str(stored), str(stored))
        self._set_combo_text(key, label)

    def _save_api_key(self):
        api_input = self._controls.get("api_key")
        if not isinstance(api_input, QLineEdit):
            return
        api_key = api_input.text().strip()
        if not api_key:
            return
        key_manager = self._secure_key_manager()
        if key_manager is None:
            return
        try:
            key_manager.store_api_key(self._api_provider(), api_key)
        except Exception:
            pass

    def _load_api_key(self):
        api_input = self._controls.get("api_key")
        if not isinstance(api_input, QLineEdit):
            return
        key_manager = self._secure_key_manager()
        if key_manager is None:
            return
        try:
            key_data = key_manager.get_api_key(self._api_provider())
        except Exception:
            key_data = None
        if key_data and key_data.get("api_key"):
            api_input.setText(str(key_data["api_key"]))

    def _secure_key_manager(self) -> Any:
        manager = self._settings_manager
        if manager is not None and hasattr(manager, "secure_key_manager"):
            return manager.secure_key_manager
        try:
            from scenefab.secure_key_manager import get_secure_key_manager

            return get_secure_key_manager()
        except Exception:
            return None

    @staticmethod
    def _api_provider() -> str:
        try:
            from scenefab.settings.config import config_manager

            return config_manager.config.default_llm
        except Exception:
            return "deepseek"

    def _show_status(self, message: str):
        if self._status_label is not None:
            self._status_label.setText(message)

    def _build_header(self) -> QFrame:
<<<<<<< HEAD
        return header_panel(
            "settings_header", "系统设置", "配置默认工作区、AI 服务和导出参数"
=======
        return header_panel("settings_header", "系统设置", "配置默认工作区、AI 服务和导出参数")

    def _workspace_group(self) -> QFrame:
        group = self._group("工作区")
        layout = group.layout()
        assert layout is not None  # for type checker
        layout.addWidget(
            self._row("项目目录", self._path_input("~/SceneFab/projects"), "默认项目保存位置")
>>>>>>> ee9c209ea90d432a86973b7316565e83ab68e46f
        )

<<<<<<< HEAD
    def _build_footer(self) -> QFrame:
        footer = panel("settings_footer")
        layout = QHBoxLayout(footer)
        layout.setContentsMargins(20, 14, 20, 14)

        self._status_label = QLabel("")
        self._status_label.setFont(ui_font(FontSizes.xs))
        self._status_label.setStyleSheet(f"color: {_C.SUCCESS};")
        layout.addWidget(self._status_label, 1)

        save_button = QPushButton("保存设置")
        save_button.setObjectName("settings_save_button")
        save_button.setFixedHeight(36)
        save_button.setCursor(Qt.CursorShape.PointingHandCursor)
        save_button.setStyleSheet(action_button_style(primary=True))
        save_button.clicked.connect(self.save_settings)
        layout.addWidget(save_button)
        return footer

    def _settings_group(self, title: str, rows: tuple[SettingRowView, ...]) -> QFrame:
        group = self._group(title)
        layout = group.layout()
        for row in rows:
            layout.addWidget(
                self._row(row.label, self._control_for_row(row), row.description)
=======
    def _appearance_group(self) -> QFrame:
        """Theme selector — emits ``theme_changed`` on pick.

        The combo is captured on the instance so that
        :meth:`set_theme_mode_index` can sync it to the persisted
        preference without bouncing the signal back.
        """
        group = self._group("外观")
        layout = group.layout()
        assert layout is not None  # for type checker
        theme_combo = self._combo(list(THEME_OPTIONS))
        # Default to the active theme (light on startup).
        theme_combo.setCurrentIndex(THEME_MODES.index(get_theme_mode()))
        self._theme_combo = theme_combo
        layout.addWidget(
            self._row(
                "界面主题",
                theme_combo,
                "切换后立即生效",
            )
        )
        return group

    def _ai_group(self) -> QFrame:
        group = self._group("AI 服务")
        layout = group.layout()
        assert layout is not None  # for type checker
        api_input = QLineEdit()
        api_input.setEchoMode(QLineEdit.EchoMode.Password)
        api_input.setPlaceholderText("输入 API Key")
        api_input.setFixedWidth(280)
        api_input.setStyleSheet(self._input_style())
        layout.addWidget(self._row("API Key", api_input, "用于脚本生成和画面理解"))
        layout.addWidget(
            self._row(
                "默认模型",
                self._combo(["deepseek-v4-pro", "gpt-5", "gemini-3.1-pro", "qwen3.7-max", "claude-sonnet-4-6"]),
                "影响脚本质量和响应速度",
>>>>>>> ee9c209ea90d432a86973b7316565e83ab68e46f
            )
        return group

<<<<<<< HEAD
    def _control_for_row(self, row: SettingRowView) -> QWidget:
        if row.control == "path":
            wrapper, edit, button = self._path_input(row.value)
            self._path_edits[row.key] = edit
            button.clicked.connect(lambda checked=False, e=edit: self._choose_directory(e))
            self._controls[row.key] = wrapper
            return wrapper
        if row.control == "combo":
            combo = self._combo(row.options)
            if row.key == "theme":
                combo.currentTextChanged.connect(self._on_theme_changed)
            self._controls[row.key] = combo
            return combo
        if row.control == "password":
            password = self._password_input(row.placeholder)
            self._controls[row.key] = password
            return password
        if row.control == "toggle":
            toggle = ToggleSwitch(row.checked)
            if row.key == "minimize_to_tray":
                self._tray_toggle = toggle
            self._controls[row.key] = toggle
            return toggle
        raise ValueError(f"Unsupported settings control: {row.control}")
=======
    def _export_group(self) -> QFrame:
        group = self._group("导出默认值")
        layout = group.layout()
        assert layout is not None  # for type checker
        layout.addWidget(
            self._row(
                "画布",
                self._combo(["1080x1920", "720x1280", "1920x1080"]),
                "短视频默认使用竖屏 9:16",
            )
        )
        layout.addWidget(self._row("帧率", self._combo(["30 fps", "60 fps", "24 fps"])))
        layout.addWidget(
            self._row(
                "编码",
                self._combo(["MP4 / H.264", "MP4 / H.265", "MOV / ProRes"]),
            )
        )
        return group

    def _behavior_group(self) -> QFrame:
        group = self._group("应用行为")
        layout = group.layout()
        assert layout is not None  # for type checker
        layout.addWidget(self._row("自动保存", ToggleSwitch(True), "每 5 分钟保存项目状态"))
        self._tray_toggle = ToggleSwitch(False)
        layout.addWidget(
            self._row("关闭到系统托盘", self._tray_toggle, "关闭窗口时保持后台运行")
        )
        return group
>>>>>>> ee9c209ea90d432a86973b7316565e83ab68e46f

    def _group(self, title: str) -> QFrame:
        group = panel(f"settings_{title}")
        layout = QVBoxLayout(group)
        layout.setContentsMargins(20, 18, 20, 18)
        layout.setSpacing(14)
        layout.addWidget(section_title(title))
        return group

    def _row(self, label: str, widget: QWidget, desc: str = "") -> QFrame:
        row = QFrame()
        row.setObjectName("settings_row")
        row.setStyleSheet(f"""
            QFrame#settings_row {{
                background: {_C.BG_BASE};
                border: 1px solid {_C.BORDER_SUBTLE};
                border-radius: {Radii.sm};
            }}
        """)
        layout = QHBoxLayout(row)
        layout.setContentsMargins(14, 10, 14, 10)
        layout.setSpacing(16)

        text = QVBoxLayout()
        text.setSpacing(2)
        title = QLabel(label)
        title.setFont(ui_font(FontSizes.sm, FontWeights.Medium))
        title.setStyleSheet(f"color: {_C.TEXT_PRIMARY};")
        text.addWidget(title)
        if desc:
            desc_label = QLabel(desc)
            desc_label.setFont(ui_font(FontSizes.xs))
            desc_label.setStyleSheet(f"color: {_C.TEXT_MUTED};")
            text.addWidget(desc_label)
        layout.addLayout(text, 1)
        layout.addWidget(widget)
        return row

    def _combo(self, items: tuple[str, ...]) -> QComboBox:
        combo = QComboBox()
        combo.addItems(items)
        combo.setFixedWidth(180)
        combo.setStyleSheet(self._input_style())
        return combo

    def _password_input(self, placeholder: str) -> QLineEdit:
        api_input = QLineEdit()
        api_input.setEchoMode(QLineEdit.EchoMode.Password)
        api_input.setPlaceholderText(placeholder)
        api_input.setFixedWidth(280)
        api_input.setStyleSheet(self._input_style())
        return api_input

    def _path_input(self, value: str) -> tuple[QFrame, QLineEdit, QPushButton]:
        wrapper = QFrame()
        layout = QHBoxLayout(wrapper)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(8)

        edit = QLineEdit(value)
        edit.setFixedWidth(280)
        edit.setStyleSheet(self._input_style())
        layout.addWidget(edit)

        button = QPushButton("选择")
        button.setFixedHeight(32)
        button.setCursor(Qt.CursorShape.PointingHandCursor)
        button.setStyleSheet(action_button_style(padding=12))
        layout.addWidget(button)
        return wrapper, edit, button

    def _choose_directory(self, edit: QLineEdit):
        """打开目录选择对话框并回填路径输入框"""
        directory = QFileDialog.getExistingDirectory(self, "选择目录", edit.text())
        if directory:
            edit.setText(directory)

    def _input_style(self) -> str:
        return f"""
            QComboBox, QLineEdit {{
                background: {_C.BG_ELEVATED};
                border: 1px solid {_C.BORDER_DEFAULT};
                border-radius: {Radii.sm};
                padding: 6px 10px;
                color: {_C.TEXT_PRIMARY};
                font-size: {FontSizes.xs}px;
            }}
            QComboBox:focus, QLineEdit:focus {{
                border-color: {_C.PRIMARY};
            }}
        """
