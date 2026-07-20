#!/usr/bin/env python3
"""Application settings page."""

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QComboBox,
    QFrame,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from ...theme.ds_tokens import _C, FontSizes, FontWeights, Radii, ui_font
from .page_view_models import SETTINGS_GROUPS, SettingRowView
from .page_widgets import (
    action_button_style,
    header_panel,
    page_background_style,
    page_container,
    panel,
    scroll_area,
    section_title,
)


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


class SettingsPage(QFrame):
    """Professional settings surface."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("settings_page")
        self._tray_toggle: ToggleSwitch | None = None
        self._setup_style()
        self._setup_ui()
        self._connect_tray_signal()

    def _setup_style(self):
        self.setStyleSheet(page_background_style("settings_page"))

    def _setup_ui(self):
        root = QVBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)

        scroll = scroll_area()
        container = page_container()
        layout = container.layout()

        layout.addWidget(self._build_header())
        for title, rows in SETTINGS_GROUPS:
            layout.addWidget(self._settings_group(title, rows))
        layout.addStretch()

        scroll.setWidget(container)
        root.addWidget(scroll)

    def _connect_tray_signal(self):
        if self._tray_toggle is not None:
            self._tray_toggle.toggled.connect(self._on_tray_toggled)

    def _on_tray_toggled(self, checked: bool):
        window = self.window()
        if window is not None and hasattr(window, "set_minimize_to_tray"):
            window.set_minimize_to_tray(checked)

    def _build_header(self) -> QFrame:
        return header_panel(
            "settings_header", "系统设置", "配置默认工作区、AI 服务和导出参数"
        )

    def _settings_group(self, title: str, rows: tuple[SettingRowView, ...]) -> QFrame:
        group = self._group(title)
        layout = group.layout()
        for row in rows:
            layout.addWidget(
                self._row(row.label, self._control_for_row(row), row.description)
            )
        return group

    def _control_for_row(self, row: SettingRowView) -> QWidget:
        if row.control == "path":
            return self._path_input(row.value)
        if row.control == "combo":
            return self._combo(row.options)
        if row.control == "password":
            return self._password_input(row.placeholder)
        if row.control == "toggle":
            toggle = ToggleSwitch(row.checked)
            if row.key == "minimize_to_tray":
                self._tray_toggle = toggle
            return toggle
        raise ValueError(f"Unsupported settings control: {row.control}")

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

    def _path_input(self, value: str) -> QWidget:
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
        return wrapper

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
