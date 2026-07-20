"""
SceneFab UI 模块

提供 PySide6 图形界面组件
"""

from typing import Any


def __getattr__(name: str) -> Any:
    """Lazily import Qt widgets so headless utility modules stay importable."""
    if name == "SceneFabMainWindow":
        from .main.main_window import SceneFabMainWindow

        return SceneFabMainWindow
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


__all__ = ["SceneFabMainWindow"]
