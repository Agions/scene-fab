#!/usr/bin/env python3
"""Project assets page."""

from __future__ import annotations

from typing import TYPE_CHECKING

from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QVBoxLayout,
    QWidget,
)

from ...theme.ds_tokens import _C, FontSizes, FontWeights, Radii, ui_font
from .page_view_models import ASSET_SOURCE_ITEMS, ASSET_TABLE_COLUMNS
from .page_widgets import (
    action_button,
    empty_state,
    header_panel,
    page_background_style,
    page_container,
    panel,
    scroll_area,
    section_title,
)

if TYPE_CHECKING:
    from scenefab.project_manager import ProjectManager


class AssetsPage(QFrame):
    """Project and media assets workspace."""

    import_requested = Signal()

    def __init__(self, parent=None, *, project_manager: ProjectManager | None = None):
        super().__init__(parent)
        self._project_manager = project_manager
        self.setObjectName("assets_page")
        self._setup_style()
        self._setup_ui()

    def _setup_style(self):
        self.setStyleSheet(page_background_style("assets_page"))

    def _setup_ui(self):
        root = QVBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)

        scroll = scroll_area()
        container = page_container()
        layout = container.layout()

        layout.addWidget(self._build_header())
        layout.addWidget(self._build_asset_table(), 1)
        layout.addWidget(self._build_source_panel())
        layout.addStretch()

        scroll.setWidget(container)
        root.addWidget(scroll)

    def _build_header(self) -> QFrame:
        import_btn = action_button("导入素材", primary=True)
        import_btn.clicked.connect(self.import_requested.emit)
        return header_panel(
            "assets_header",
            "项目资产",
            "管理素材、脚本、配音、字幕与导出文件",
            import_btn,
        )

    def _build_asset_table(self) -> QFrame:
        frame = panel("asset_table")
        layout = QVBoxLayout(frame)
        layout.setContentsMargins(20, 18, 20, 18)
        layout.setSpacing(14)

        header = QHBoxLayout()
        header.addWidget(section_title("资产列表"))
        header.addStretch()
        refresh_btn = action_button("刷新")
        refresh_btn.clicked.connect(self.refresh_projects)
        header.addWidget(refresh_btn)
        layout.addLayout(header)

        columns = self._row(*ASSET_TABLE_COLUMNS, header=True)
        layout.addWidget(columns)

        # Container for dynamically added project rows
        self._rows_container = QWidget()
        self._rows_layout = QVBoxLayout(self._rows_container)
        self._rows_layout.setContentsMargins(0, 0, 0, 0)
        self._rows_layout.setSpacing(6)
        layout.addWidget(self._rows_container, 1)

        # Empty state shown when no projects exist
        self._empty_state = empty_state(
            "暂无资产。导入视频素材后，系统会在这里显示拆分场景、脚本、配音和导出记录。",
            180,
            padding=24,
        )
        layout.addWidget(self._empty_state, 1)

        # Initial load
        self.refresh_projects()
        return frame

    def refresh_projects(self) -> None:
        """Query the ProjectManager and repopulate the project list."""
        # Clear existing rows
        while self._rows_layout.count():
            item = self._rows_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        projects = []
        if self._project_manager is not None:
            projects = self._project_manager.scan_projects()

        if not projects:
            self._empty_state.setVisible(True)
            self._rows_container.setVisible(False)
            return

        self._empty_state.setVisible(False)
        self._rows_container.setVisible(True)

        for project in projects:
            meta = project.metadata
            type_name = (
                meta.project_type.display_name
                if hasattr(meta.project_type, "display_name")
                else str(meta.project_type)
            )
            date_str = (meta.created_at or "")[:10] or "—"
            row = self._row(type_name, meta.name or "未命名项目", date_str)
            self._rows_layout.addWidget(row)

    def _build_source_panel(self) -> QFrame:
        frame = panel("source_panel")
        layout = QHBoxLayout(frame)
        layout.setContentsMargins(20, 16, 20, 16)
        layout.setSpacing(16)

        for item in ASSET_SOURCE_ITEMS:
            layout.addWidget(self._source_item(item.label, item.value))
        layout.addStretch()
        return frame

    def _row(self, kind: str, name: str, status: str, header: bool = False) -> QFrame:
        row = QFrame()
        row.setObjectName("asset_row")
        bg = _C.BG_ELEVATED if header else _C.BG_BASE
        row.setStyleSheet(f"""
            QFrame#asset_row {{
                background: {bg};
                border: 1px solid {_C.BORDER_SUBTLE};
                border-radius: {Radii.sm};
            }}
        """)
        layout = QHBoxLayout(row)
        layout.setContentsMargins(12, 8, 12, 8)
        for text, stretch in [(kind, 1), (name, 3), (status, 1)]:
            label = QLabel(text)
            label.setFont(ui_font(FontSizes.xs, FontWeights.Medium))
            label.setStyleSheet(
                f"color: {_C.TEXT_MUTED if header else _C.TEXT_SECONDARY};"
            )
            layout.addWidget(label, stretch)
        return row

    def _source_item(self, title: str, desc: str) -> QFrame:
        item = QFrame()
        item.setObjectName("source_item")
        item.setStyleSheet(f"""
            QFrame#source_item {{
                background: {_C.BG_BASE};
                border: 1px solid {_C.BORDER_SUBTLE};
                border-radius: {Radii.sm};
            }}
        """)
        layout = QVBoxLayout(item)
        layout.setContentsMargins(12, 10, 12, 10)
        layout.setSpacing(4)

        title_label = QLabel(title)
        title_label.setFont(ui_font(FontSizes.xs, FontWeights.Medium))
        title_label.setStyleSheet(f"color: {_C.TEXT_MUTED};")
        layout.addWidget(title_label)

        desc_label = QLabel(desc)
        desc_label.setFont(ui_font(FontSizes.sm, FontWeights.Medium))
        desc_label.setStyleSheet(f"color: {_C.TEXT_SECONDARY};")
        layout.addWidget(desc_label)
        return item
