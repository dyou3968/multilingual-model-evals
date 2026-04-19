from __future__ import annotations

import os
from openai import AsyncOpenAI
from tenacity import retry, stop_after_attempt, wait_exponential
from .base import BaseClient
from harness.config import MODELS


class OpenAIClient(BaseClient):
    def __init__(self):
        self._client = AsyncOpenAI(api_key=os.environ["OPENAI_API_KEY"])

    @property
    def model_key(self) -> str:
        return "openai"

    @property
    def model_id(self) -> str:
        return MODELS["openai"]

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(min=2, max=30))
    async def complete(
        self,
        prompt: str,
        system: str | None = None,
        max_tokens: int = 1024,
        temperature: float = 0.0,
    ) -> str:
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})

        response = await self._client.chat.completions.create(
            model=self.model_id,
            messages=messages,
            max_completion_tokens=max_tokens,
        )
        return response.choices[0].message.content.strip()
