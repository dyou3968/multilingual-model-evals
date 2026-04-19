import os
import google.generativeai as genai
from tenacity import retry, stop_after_attempt, wait_exponential
from .base import BaseClient
from harness.config import MODELS


class GeminiClient(BaseClient):
    def __init__(self):
        genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
        self._model = genai.GenerativeModel(MODELS["gemini"])

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
        full_prompt = f"{system}\n\n{prompt}" if system else prompt
        config = genai.types.GenerationConfig(
            max_output_tokens=max_tokens,
            temperature=temperature,
        )
        response = await self._model.generate_content_async(
            full_prompt, generation_config=config
        )
        return response.text.strip()
