from __future__ import annotations

import asyncio
import os
import anthropic
from tenacity import retry, stop_after_attempt, wait_exponential
from .base import BaseClient
from harness.config import MODELS

# Tier 1 = 50 RPM; with concurrency=3: sleep = 3*60/50 - avg_latency ≈ 2.5s
_CLAUDE_MIN_INTERVAL = float(os.getenv("CLAUDE_MIN_INTERVAL", "2.5"))


class ClaudeClient(BaseClient):
    def __init__(self):
        self._client = anthropic.AsyncAnthropic(
            api_key=os.environ["ANTHROPIC_API_KEY"]
        )

    @property
    def model_key(self) -> str:
        return "claude"

    @property
    def model_id(self) -> str:
        return MODELS["claude"]

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(min=2, max=30))
    async def complete(
        self,
        prompt: str,
        system: str | None = None,
        max_tokens: int = 1024,
        temperature: float = 0.0,
    ) -> str:
        await asyncio.sleep(_CLAUDE_MIN_INTERVAL)
        # temperature is deprecated for claude-opus-4-7 and later models
        kwargs = dict(
            model=self.model_id,
            max_tokens=max_tokens,
            messages=[{"role": "user", "content": prompt}],
        )
        if system:
            kwargs["system"] = system

        response = await self._client.messages.create(**kwargs)
        if not response.content:
            return ""
        return response.content[0].text.strip()
