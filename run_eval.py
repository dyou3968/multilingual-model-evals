"""
CLI entry point for the multilingual evaluation harness.

Usage examples:
  python run_eval.py                                    # all benchmarks, all models, all languages
  python run_eval.py --benchmarks belebele mgsm        # specific benchmarks
  python run_eval.py --models claude openai            # specific models
  python run_eval.py --languages hi bn mr              # specific language codes
  python run_eval.py --results-dir custom/output/dir
"""
import asyncio
import logging
from pathlib import Path
from typing import Optional

import typer
from rich.console import Console
from rich.logging import RichHandler

from harness.benchmarks import BENCHMARKS
from harness.config import MODELS
from harness.runner import run_all

app = typer.Typer(add_completion=False)
console = Console()

_TIER1 = ["belebele", "mgsm", "include", "blend", "indicgenbench"]


def _setup_logging(verbose: bool) -> None:
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(message)s",
        handlers=[RichHandler(console=console, show_path=False)],
    )


@app.command()
def main(
    benchmarks: Optional[list[str]] = typer.Option(
        None,
        "--benchmarks", "-b",
        help=f"Benchmarks to run. Defaults to Tier 1 suite: {_TIER1}",
    ),
    models: Optional[list[str]] = typer.Option(
        None,
        "--models", "-m",
        help=f"Model keys to evaluate. Defaults to all: {list(MODELS.keys())}",
    ),
    languages: Optional[list[str]] = typer.Option(
        None,
        "--languages", "-l",
        help="Language codes to include (benchmark-specific format). Defaults to all.",
    ),
    results_dir: Path = typer.Option(
        Path("results"),
        "--results-dir", "-o",
        help="Directory for JSONL output files.",
    ),
    verbose: bool = typer.Option(False, "--verbose", "-v"),
) -> None:
    _setup_logging(verbose)

    selected_benchmarks = benchmarks or _TIER1
    selected_models = models or list(MODELS.keys())

    # Validate
    for b in selected_benchmarks:
        if b not in BENCHMARKS:
            console.print(f"[red]Unknown benchmark: {b}. Available: {list(BENCHMARKS.keys())}[/red]")
            raise typer.Exit(1)
    for m in selected_models:
        if m not in MODELS:
            console.print(f"[red]Unknown model key: {m}. Available: {list(MODELS.keys())}[/red]")
            raise typer.Exit(1)

    console.print(f"[bold]Benchmarks:[/bold] {selected_benchmarks}")
    console.print(f"[bold]Models:[/bold] {selected_models}")
    if languages:
        console.print(f"[bold]Languages:[/bold] {languages}")
    console.print(f"[bold]Output dir:[/bold] {results_dir}")
    console.print()

    asyncio.run(
        run_all(
            benchmark_names=selected_benchmarks,
            model_keys=selected_models,
            language_codes=languages,
            results_dir=results_dir,
        )
    )

    console.print("[green]Evaluation complete.[/green]")


if __name__ == "__main__":
    app()
