"""Main CLI entry point for narratological analysis."""

import json
import logging
import sys
from typing import Annotated

import click
import typer
from rich.console import Console
from rich.table import Table

from narratological_cli.commands import algorithm, analyze, diagnose, generate, study, validate

app = typer.Typer(
    name="narratological",
    help="Narratological Algorithmic Lenses - Analyze narratives using formalized algorithms",
    no_args_is_help=True,
)

# Add subcommands
app.add_typer(study.app, name="study", help="Explore narratological studies")
app.add_typer(algorithm.app, name="algorithm", help="Explore and execute algorithms")
app.add_typer(analyze.app, name="analyze", help="Analyze scripts and stories")
app.add_typer(diagnose.app, name="diagnose", help="Run diagnostic tests")
app.add_typer(generate.app, name="generate", help="Generate narrative structures")
app.add_typer(validate.app, name="validate", help="Validate data integrity")

console = Console()
error_console = Console(stderr=True)

class JSONFormatter(logging.Formatter):
    """JSON structured logger formatter."""
    def format(self, record: logging.LogRecord) -> str:
        log_data = {
            "timestamp": self.formatTime(record, self.datefmt),
            "level": record.levelname,
            "message": record.getMessage(),
            "logger": record.name,
        }
        for key, value in record.__dict__.items():
            if key not in ["args", "asctime", "created", "exc_info", "exc_text", "filename", "funcName", "levelname", "levelno", "lineno", "message", "module", "msecs", "msg", "name", "pathname", "process", "processName", "relativeCreated", "stack_info", "thread", "threadName", "taskName"]:
                log_data[key] = value

        if record.exc_info:
            log_data["exception"] = self.formatException(record.exc_info)
        return json.dumps(log_data)

logger = logging.getLogger("narratological_cli")
logger.setLevel(logging.WARNING)
_handler = logging.StreamHandler(sys.stderr)
_handler.setFormatter(JSONFormatter())
logger.addHandler(_handler)



@app.command()
def version() -> None:
    """Show version information."""
    from narratological import __version__ as core_version
    from narratological_cli import __version__ as cli_version

    console.print(f"[bold]narratological-cli[/bold] v{cli_version}")
    console.print(f"[bold]narratological[/bold] (core) v{core_version}")


@app.command()
def info() -> None:
    """Show information about available studies."""
    from narratological.loader import get_study_summary

    studies = get_study_summary()

    table = Table(title="Available Narratological Studies")
    table.add_column("ID", style="cyan")
    table.add_column("Creator", style="green")
    table.add_column("Work")
    table.add_column("Category", style="yellow")
    table.add_column("Axioms", justify="right")
    table.add_column("Algorithms", justify="right")

    for s in studies:
        table.add_row(
            s["id"],
            s["creator"],
            s["work"][:40] + "..." if len(s["work"]) > 40 else s["work"],
            s["category"],
            s["axiom_count"],
            s["algorithm_count"],
        )

    console.print(table)


@app.callback()
def main(
    verbose: Annotated[
        bool,
        typer.Option("--verbose", "-v", help="Enable verbose output"),
    ] = False,
) -> None:
    """Narratological Algorithmic Lenses CLI.

    Analyze scripts and stories using formalized algorithms extracted
    from master storytellers including Bergman, Tarkovsky, Pixar, and more.
    """
    if verbose:
        logger.setLevel(logging.INFO)
        console.print("[dim]Verbose mode enabled[/dim]")



if __name__ == "__main__":
    try:
        app()
    except click.exceptions.Exit:
        raise
    except click.exceptions.Abort:
        raise
    except Exception as e:
        logger.error(f"Unhandled exception in CLI: {e}", exc_info=True)
        error_console.print(f"[bold red]An unexpected error occurred:[/bold red] {e}")
        sys.exit(1)
