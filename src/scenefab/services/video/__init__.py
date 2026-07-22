"""
视频制作服务。

活跃工具模块（来自 video）：
- FFmpegTool        FFmpeg 封装（视频/音频处理便捷门面）
- hardware          硬件加速检测（HWAccelType + detect_hw_accel 等）
- probe             ffprobe 视频元数据探测
- CaptionGenerator  动态字幕生成
- BaseVideoProcessor / IVideoProcessor  视频处理基类
"""

from __future__ import annotations

from importlib import import_module
from typing import Any

# 视频工具（原 video/__init__.py）
from . import hardware, probe
from .tool_base import (
    BaseVideoProcessor,
    IVideoProcessor,
    ProcessingResult,
    VideoMetadata,
)
from .caption_gen import Caption, CaptionConfig, CaptionGenerator, CaptionStyle
from .ffmpeg_tool import FFmpegTool, HWAccelType

# 视频制作服务（原 video/__init__.py，延迟加载）
_EXPORTS = {
    "BaseVideoMaker": ".base_maker",
    "MonologueMaker": ".monologue_maker",
    "MonologueProject": ".monologue_maker",
    "MonologueSegment": ".monologue_maker",
    "MonologueStyle": ".monologue_maker",
    "EmotionType": ".models.monologue",
    "PerspectiveMapper": ".perspective_mapper",
    "VideoInterleaver": ".video_interleaver",
    "SceneSegment": ".models.perspective",
    "KeyFrame": ".models.perspective",
    "PerspectiveShot": ".models.perspective",
    "NarrationSegment": ".models.perspective",
    "ClipSegment": ".models.perspective",
    "InterleaveTimeline": ".models.perspective",
    "InterleaveDecision": ".models.perspective",
    "InterleaveMode": ".models.perspective",
    "TransitionType": ".models.perspective",
    "FirstPersonExtractor": ".extraction.first_person",
    "VideoSegment": ".extraction.first_person",
    "EmotionPeakDetector": ".extraction.emotion_peak",
    "EmotionPeak": ".extraction.emotion_peak",
    "HighlightDetector": ".highlight_detector",
    "HighlightSegment": ".highlight_detector",
    "HighlightReason": ".highlight_detector",
    "HighlightDetectorConfig": ".highlight_detector",
    "SceneConverter": ".scene_converter",
    "EmotionCurveGenerator": ".scene_converter",
    "PipelineIntegrator": ".pipeline_integrator",
    "VideoFrameCache": ".cache",
    "FFmpegSession": ".session",
    "VideoAnalyzer": ".analyzer",
    "VideoProcessor": ".processor",
}


def __getattr__(name: str) -> Any:
    module_name = _EXPORTS.get(name)
    if module_name is None:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    module = import_module(module_name, __name__)
    value = getattr(module, name)
    globals()[name] = value
    return value


__all__ = list(_EXPORTS) + [
    # 工具
    "FFmpegTool",
    "HWAccelType",
    # 拆出的子模块
    "hardware",
    "probe",
    # 基类
    "IVideoProcessor",
    "BaseVideoProcessor",
    "VideoMetadata",
    "ProcessingResult",
    # 字幕生成
    "CaptionGenerator",
    "Caption",
    "CaptionConfig",
    "CaptionStyle",
]
