"""内置工具集合。

通过延迟导入避免基础 Agent 加载未安装的可选功能依赖。
"""

from importlib import import_module

_EXPORTS = {
    "SearchTool": ".search_tool",
    "CalculatorTool": ".calculator",
    "MemoryTool": ".memory_tool",
    "RAGTool": ".rag_tool",
    "NoteTool": ".note_tool",
    "TerminalTool": ".terminal_tool",
    "MCPTool": ".protocol_tools",
    "A2ATool": ".protocol_tools",
    "ANPTool": ".protocol_tools",
    "BFCLEvaluationTool": ".bfcl_evaluation_tool",
    "GAIAEvaluationTool": ".gaia_evaluation_tool",
    "LLMJudgeTool": ".llm_judge_tool",
    "WinRateTool": ".win_rate_tool",
}

__all__ = list(_EXPORTS)


def __getattr__(name: str):
    module_name = _EXPORTS.get(name)
    if module_name is None:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

    value = getattr(import_module(module_name, __name__), name)
    globals()[name] = value
    return value


def __dir__():
    return sorted(set(globals()) | set(__all__))
