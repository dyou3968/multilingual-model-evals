from abc import ABC, abstractmethod


class Benchmark(ABC):
    """Base class for all benchmark loaders."""

    name: str = ""

    @abstractmethod
    def load(self, language_code: str) -> list[dict]:
        """
        Load examples for a single language.
        Each example must contain at minimum:
          - 'id': unique identifier
          - 'language': language name (canonical)
          - 'prompt': formatted prompt string ready to send to a model
          - 'reference': expected answer for scoring
          - 'scoring_type': 'mcq' | 'numeric' | 'generation'
        """
        ...

    @abstractmethod
    def score(self, prediction: str, example: dict) -> dict:
        """
        Score a single prediction against an example.
        Returns a dict with at minimum {'correct': bool} for MCQ/numeric
        or {'rouge_l': float, 'chrf': float} for generation.
        """
        ...
