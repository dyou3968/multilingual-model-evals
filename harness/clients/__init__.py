from .claude_client import ClaudeClient
from .openai_client import OpenAIClient
from .gemini_client import GeminiClient
from .base import BaseClient

__all__ = ["BaseClient", "ClaudeClient", "OpenAIClient", "GeminiClient"]


def get_all_clients() -> dict[str, "BaseClient"]:
    return {
        "claude": ClaudeClient(),
        "openai": OpenAIClient(),
        "gemini": GeminiClient(),
    }
