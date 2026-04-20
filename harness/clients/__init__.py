from .claude_client import ClaudeClient
from .openai_client import OpenAIClient
from .gemini_client import GeminiClient
from .gemini_flash_client import GeminiFlashClient
from .base import BaseClient

__all__ = ["BaseClient", "ClaudeClient", "OpenAIClient", "GeminiClient", "GeminiFlashClient"]


def get_all_clients() -> dict[str, "BaseClient"]:
    return {
        "claude": ClaudeClient(),
        "openai": OpenAIClient(),
        "gemini_flash_lite": GeminiClient(),
        "gemini_flash": GeminiFlashClient(),
    }
