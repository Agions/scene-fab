#!/usr/bin/env python3
"""Main production workspace page."""

from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QVBoxLayout,
)

from ...theme.ds_tokens import _C, FontSizes, FontWeights, Radii, ui_font
from .page_defaults import default_delivery_summary
from .page_view_models import (
    DELIVERY_PARAMETERS,
    HOME_STATUS_CARDS,
    HOME_WORKFLOW_STEPS,
)
from .page_widgets import (
    action_button,
    empty_state,
    header_panel,
    key_value_row,
    page_background_style,
    page_container,
    panel,
    scroll_area,
    section_title,
)


class HomePage(QFrame):
    """Production dashboard for first-person narration work."""

    create_project = Signal()
    open_project = Signal(str)
    navigate = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("home_page")
        self._setup_style()
        self._setup_ui()

    def _setup_style(self):
        self.setStyleSheet(page_background_style("home_page"))

    def _setup_ui(self):
        root = QVBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        scroll = scroll_area()
        container = page_container()
        layout = container.layout()

        layout.addWidget(self._build_header())
        layout.addWidget(self._build_status_grid())

        main_grid = QGridLayout()
        main_grid.setHorizontalSpacing(18)
        main_grid.setVerticalSpacing(18)
        main_grid.addWidget(self._build_workflow_panel(), 0, 0, 2, 1)
        main_grid.addWidget(self._build_delivery_panel(), 0, 1)
        main_grid.addWidget(self._build_recent_panel(), 1, 1)
        main_grid.setColumnStretch(0, 3)
        main_grid.setColumnStretch(1, 2)
        layout.addLayout(main_grid)
        layout.addStretch()

        scroll.setWidget(container)
        root.addWidget(scroll)

    def _build_header(self) -> QFrame:
        create_btn = action_button("开始生产", primary=True)
        create_btn.clicked.connect(self.create_project.emit)

        assets_btn = action_button("项目资产")
        assets_btn.clicked.connect(lambda: self.navigate.emit("assets"))
        return header_panel(
            "workspace_header",
            "第一人称短剧解说工作台",
            default_delivery_summary(),
            create_btn,
            assets_btn,
        )

    def _build_status_grid(self) -> QFrame:
        frame = QFrame()
        layout = QGridLayout(frame)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setHorizontalSpacing(14)
        layout.setVerticalSpacing(14)

        for index, item in enumerate(HOME_STATUS_CARDS):
            layout.addWidget(
                self._status_card(item.title, item.status, item.value), 0, index
            )
        return frame

    def _build_workflow_panel(self) -> QFrame:
        frame = panel("workflow_panel")
        layout = QVBoxLayout(frame)
        layout.setContentsMargins(20, 18, 20, 18)
        layout.setSpacing(12)

        layout.addWidget(section_title("生产流程"))
        for step in HOME_WORKFLOW_STEPS:
            layout.addWidget(self._workflow_row(step.number, step.name, step.detail))
        layout.addStretch()
        return frame

    def _build_delivery_panel(self) -> QFrame:
        frame = panel("delivery_panel")
        layout = QVBoxLayout(frame)
        layout.setContentsMargins(20, 18, 20, 18)
        layout.setSpacing(12)

        layout.addWidget(section_title("交付参数"))
        for item in DELIVERY_PARAMETERS:
            layout.addWidget(key_value_row(item.label, item.value))
        layout.addStretch()
        return frame

    def _build_recent_panel(self) -> QFrame:
        frame = panel("recent_panel")
        layout = QVBoxLayout(frame)
        layout.setContentsMargins(20, 18, 20, 18)
        layout.setSpacing(14)

        row = QHBoxLayout()
        row.addWidget(section_title("最近资产"))
        row.addStretch()
        open_btn = action_button("打开")
        open_btn.clicked.connect(lambda: self.navigate.emit("assets"))
        row.addWidget(open_btn)
        layout.addLayout(row)

        layout.addWidget(empty_state("暂无项目资产", 120), 1)
        return frame

    def _status_card(self, title: str, status: str, value: str) -> QFrame:
        card = panel(f"status_{title}")
        layout = QVBoxLayout(card)
        layout.setContentsMargins(16, 14, 16, 14)
        layout.setSpacing(6)

        label = QLabel(title)
        label.setFont(ui_font(FontSizes.xs, FontWeights.Medium))
        label.setStyleSheet(f"color: {_C.TEXT_MUTED};")
        layout.addWidget(label)

        val = QLabel(value)
        val.setFont(ui_font(FontSizes.lg, FontWeights.Bold))
        val.setStyleSheet(f"color: {_C.TEXT_PRIMARY};")
        layout.addWidget(val)

        state = QLabel(status)
        state.setFont(ui_font(FontSizes.xs))
        state.setStyleSheet(f"color: {_C.TEXT_DISABLED};")
        layout.addWidget(state)
        return card

    def _workflow_row(self, step: str, name: str, status: str) -> QFrame:
        row = QFrame()
        row.setObjectName("workflow_row")
        row.setStyleSheet(f"""
            QFrame#workflow_row {{
                background: {_C.BG_BASE};
                border: 1px solid {_C.BORDER_SUBTLE};
                border-radius: {Radii.base};
            }}
        """)
        layout = QHBoxLayout(row)
        layout.setContentsMargins(14, 10, 14, 10)
        layout.setSpacing(12)

        step_label = QLabel(step)
        step_label.setFixedWidth(32)
        step_label.setFont(ui_font(FontSizes.xs, FontWeights.Bold))
        step_label.setStyleSheet(f"color: {_C.PRIMARY};")
        layout.addWidget(step_label)

        name_label = QLabel(name)
        name_label.setFont(ui_font(FontSizes.sm, FontWeights.Medium))
        name_label.setStyleSheet(f"color: {_C.TEXT_PRIMARY};")
        layout.addWidget(name_label, 1)

        status_label = QLabel(status)
        status_label.setFont(ui_font(FontSizes.xs))
        status_label.setStyleSheet(f"color: {_C.TEXT_MUTED};")
        layout.addWidget(status_label)
        return row
