"""
v2.2 解说生成状态机 — Phase 1 骨架

公开 API:
- NarrationContext / Persona / Platform / NarrationStyle / Bridge / BridgeType
- NarrationState / NarrationStateMachine / NarrationConfig / StepResult
- register_default_steps (Phase 1 骨架 Step)

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
]
