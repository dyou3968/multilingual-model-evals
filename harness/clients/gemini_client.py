from __future__ import annotations

import os
from google import genai
from google.genai import types
from tenacity import retry, stop_after_attempt, wait_exponential
from .base import BaseClient
from harness.config import MODELS


class GeminiClient(BaseClient):
    def __init__(self):
        self._client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])

    @property
    def model_key(self) -> str:
        return "gemini"

    @property
    def model_id(self) -> str:
        return MODELS["gemini"]

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(min=2, max=30))
    async def complete(
        self,
        prompt: str,
        system: str | None = None,
        max_tokens: int = 1024,
        temperature: float = 0.0,
    ) -> str:
        config = types.GenerateContentConfig(
            system_instruction=system or "",
            max_output_tokens=max_tokens,
            temperature=temperature,
        )
        response = await self._client.aio.models.generate_content(
            model=self.model_id,
            contents=prompt,
            config=config,
        )
        return response.text.strip()
