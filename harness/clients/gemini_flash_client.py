from __future__ import annotations

import asyncio
import os
from google import genai
from google.genai import types
from tenacity import retry, stop_after_attempt, wait_exponential
from .base import BaseClient
from harness.config import MODELS

# gemini_flash = 1K RPM; with concurrency=3: sleep = 3*60/1000 ≈ 0.18s
_GEMINI_FLASH_MIN_INTERVAL = float(os.getenv("GEMINI_FLASH_MIN_INTERVAL", "0.18"))


class GeminiFlashClient(BaseClient):
    def __init__(self):
        project = os.environ.get("GOOGLE_CLOUD_PROJECT")
        if project:
            self._client = genai.Client(
                vertexai=True,
                project=project,
                location=os.environ.get("GOOGLE_CLOUD_LOCATION", "us-central1"),
            )
        else:
            self._client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])

    @property
    def model_key(self) -> str:
        return "gemini_flash"

    @property
    def model_id(self) -> str:
        return MODELS["gemini_flash"]

    @retry(stop=stop_after_attempt(4), wait=wait_exponential(min=30, max=90))
    async def complete(
        self,
        prompt: str,
        system: str | None = None,
        max_tokens: int = 1024,
        temperature: float = 0.0,
    ) -> str:
        await asyncio.sleep(_GEMINI_FLASH_MIN_INTERVAL)
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
        return response.text.strip() if response.text else ""
