from __future__ import annotations

from abc import ABC, abstractmethod


class BaseClient(ABC):
    """Shared interface for all model API clients."""

    @abstractmethod
    async def complete(
        self,
        prompt: str,
        system: str | None = None,
        max_tokens: int = 1024,
        temperature: float = 0.0,
    ) -> str:
        """Return the model's text response to a prompt."""
        ...

    @property
    @abstractmethod
    def model_key(self) -> str:
        """Short identifier used in config and results (claude / openai / gemini)."""
        ...

    @property
    @abstractmethod
    def model_id(self) -> str:
        """Full model ID sent to the API."""
        ...
