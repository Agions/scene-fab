"""
v2.2 解说生成状态机 — Phase 1 骨架 + Phase 2 真实实现

公开 API:
- NarrationContext / Persona / Platform / NarrationStyle / Bridge / BridgeType
- NarrationState / NarrationStateMachine / NarrationConfig / StepResult
- register_default_steps (Phase 1 骨架 Step)
- register_phase2_steps (Phase 2 真实实现 — 替换 UNDERSTAND/STORYGRAPH/DRAFT)

v2.2 决策: 见 docs/adr/007-narration-state-machine.md
"""

from .narration_context import (
    PLATFORM_SPECS,
    Bridge,
    BridgeType,
    FewShot,
    HistorySegment,
    NarrationContext,
    NarrationStyle,
    Persona,
    Platform,
    PlatformSpec,
)
from .narration_state_machine import (
    NarrationConfig,
    NarrationState,
    NarrationStateMachine,
    StateTransition,
    StepResult,
    TransitionReason,
)
from .narration_steps import register_default_steps
from .narration_steps_phase2 import (
    _build_narration_prompt,
    draft_step,
    register_phase2_steps,
    storygraph_step,
    understand_step,
)

__all__ = [
    # Context
    "Bridge",
    "BridgeType",
    "FewShot",
    "HistorySegment",
    "NarrationContext",
    "NarrationStyle",
    "Persona",
    "Platform",
    "PLATFORM_SPECS",
    "PlatformSpec",
    # State machine
    "NarrationConfig",
    "NarrationState",
    "NarrationStateMachine",
    "StateTransition",
    "StepResult",
    "TransitionReason",
    # Steps
    "register_default_steps",
    "register_phase2_steps",
    "understand_step",
    "storygraph_step",
    "draft_step",
    "_build_narration_prompt",
]
