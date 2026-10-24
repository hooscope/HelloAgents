"""工具系统。

可选功能（如协议、评测和强化学习）的依赖仅在其对应工具被使用时导入。
"""

from importlib import import_module

_EXPORTS = {
    "Tool": ".base",
    "ToolParameter": ".base",
    "ToolRegistry": ".registry",
    "global_registry": ".registry",
    "SearchTool": ".builtin.search_tool",
    "CalculatorTool": ".builtin.calculator",
    "MemoryTool": ".builtin.memory_tool",
    "RAGTool": ".builtin.rag_tool",
    "NoteTool": ".builtin.note_tool",
    "TerminalTool": ".builtin.terminal_tool",
    "MCPTool": ".builtin.protocol_tools",
    "A2ATool": ".builtin.protocol_tools",
    "ANPTool": ".builtin.protocol_tools",
    "BFCLEvaluationTool": ".builtin.bfcl_evaluation_tool",
    "GAIAEvaluationTool": ".builtin.gaia_evaluation_tool",
    "LLMJudgeTool": ".builtin.llm_judge_tool",
    "WinRateTool": ".builtin.win_rate_tool",
    "RLTrainingTool": ".builtin.rl_training_tool",
    "ToolChain": ".chain",
    "ToolChainManager": ".chain",
    "create_research_chain": ".chain",
    "create_simple_chain": ".chain",
    "AsyncToolExecutor": ".async_executor",
    "run_parallel_tools": ".async_executor",
    "run_batch_tool": ".async_executor",
    "run_parallel_tools_sync": ".async_executor",
    "run_batch_tool_sync": ".async_executor",
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
