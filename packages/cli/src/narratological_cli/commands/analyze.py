"""CLI commands for analyzing scripts and stories."""

import json
from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table

from narratological_cli.llm_config import (
    BASE_URL_OPTION_HELP,
    MODEL_OPTION_HELP,
    PROVIDER_OPTION_HELP,
    get_provider,
)
from narratological_cli.parser import load_input, parse_script

app = typer.Typer(help="Analyze scripts and stories")
console = Console()


def _display_coverage_report(report) -> None:
    """Display a coverage report."""
    from narratological.models.report import RecommendationType

    # Recommendation color
    rec_colors = {
        RecommendationType.CONSIDER: "green",
        RecommendationType.PASS: "red",
        RecommendationType.DEVELOP: "yellow",
        RecommendationType.URGENT: "cyan",
    }
    rec_color = rec_colors.get(report.recommendation, "white")

    console.print(Panel(
        f"[bold]Recommendation:[/bold] [{rec_color}]{report.recommendation.value}[/{rec_color}]\n\n"
        f"[bold]Logline:[/bold] {report.logline}\n\n"
        f"[dim]{report.synopsis[:500]}{'...' if len(report.synopsis) > 500 else ''}[/dim]",
        title=f"Coverage: {report.title}",
    ))

    # Ratings table
    table = Table(title="Ratings")
    table.add_column("Category")
    table.add_column("Score", justify="center")
    table.add_column("Rating")

    ratings = [
        ("Premise", report.premise_rating),
        ("Structure", report.structure_rating),
        ("Character", report.character_rating),
        ("Dialogue", report.dialogue_rating),
        ("Originality", report.originality_rating),
        ("Marketability", report.marketability_rating),
    ]

    for name, score in ratings:
        color = "green" if score >= 7 else "yellow" if score >= 5 else "red"
        rating_bar = "[green]" + "=" * score + "[/green]" + "[dim]" + "-" * (10 - score) + "[/dim]"
        table.add_row(name, f"[{color}]{score}/10[/{color}]", rating_bar)

    console.print(table)

    # Strengths and weaknesses
    if report.strengths:
        console.print("\n[bold green]Strengths[/bold green]")
        for s in report.strengths[:5]:
            console.print(f"  + {s}")

    if report.weaknesses:
        console.print("\n[bold red]Weaknesses[/bold red]")
        for w in report.weaknesses[:5]:
            console.print(f"  - {w}")

    if report.opportunities:
        console.print("\n[bold cyan]Opportunities[/bold cyan]")
        for o in report.opportunities[:3]:
            console.print(f"  * {o}")

    if report.comparables:
        console.print(f"\n[bold]Comparables:[/bold] {', '.join(report.comparables)}")


def _display_beat_map_report(report) -> None:
    """Display a beat map report."""
    avg_tension = f"{report.average_tension:.1f}/10" if report.average_tension is not None else "N/A"
    console.print(Panel(
        f"[bold]Total Scenes:[/bold] {report.total_scenes}\n"
        f"[bold]Average Tension:[/bold] {avg_tension}",
        title=f"Beat Map: {report.title}",
    ))

    # Function distribution
    if report.function_distribution:
        console.print("\n[bold]Function Distribution:[/bold]")
        for func, count in sorted(report.function_distribution.items(), key=lambda x: -x[1]):
            bar_len = min(count * 2, 20)
            console.print(f"  {func:12} {'=' * bar_len} {count}")

    # Connector distribution
    if report.connector_distribution:
        console.print("\n[bold]Connector Distribution:[/bold]")
        total = sum(report.connector_distribution.values())
        for conn, count in report.connector_distribution.items():
            pct = count / total * 100 if total else 0
            color = "green" if conn in ("BUT", "THEREFORE") else "red" if conn == "AND THEN" else "yellow"
            console.print(f"  [{color}]{conn:12}[/{color}] {count:3} ({pct:.0f}%)")

    # Beat entries (sample)
    if report.entries:
        console.print(f"\n[bold]Scenes ({len(report.entries)} total):[/bold]")
        table = Table()
        table.add_column("#", justify="right", width=4)
        table.add_column("Slug", width=25)
        table.add_column("Function", width=12)
        table.add_column("Connector", width=10)
        table.add_column("Tension", justify="center", width=8)

        for entry in report.entries[:10]:  # Show first 10
            tension_color = "green" if entry.tension >= 7 else "yellow" if entry.tension >= 4 else "dim"
            connector = entry.connector.value if entry.connector else "-"
            table.add_row(
                str(entry.scene_number),
                entry.slug[:25],
                entry.function.value,
                connector,
                f"[{tension_color}]{entry.tension}[/{tension_color}]",
            )

        console.print(table)
        if len(report.entries) > 10:
            console.print(f"  [dim]... and {len(report.entries) - 10} more scenes[/dim]")


@app.command("script")
def analyze_script(
    script_path: Annotated[
        Path,
        typer.Argument(help="Path to script file (txt, pdf, fdx)"),
    ],
    framework: Annotated[
        str | None,
        typer.Option("--framework", "-f", help="Primary framework/study to apply"),
    ] = None,
    output: Annotated[
        Path | None,
        typer.Option("--output", "-o", help="Output directory for reports"),
    ] = None,
    reports: Annotated[
        str,
        typer.Option("--reports", "-r", help="Reports to generate: all, coverage, beatmap, structural, character, diagnostic"),
    ] = "coverage",
    provider: Annotated[
        str,
        typer.Option("--provider", "-p", help=PROVIDER_OPTION_HELP),
    ] = "ollama",
    model: Annotated[
        str | None,
        typer.Option("--model", "-m", help=MODEL_OPTION_HELP),
    ] = None,
    base_url: Annotated[
        str | None,
        typer.Option("--base-url", help=BASE_URL_OPTION_HELP),
    ] = None,
) -> None:
    """Analyze a script using narratological algorithms.

    This command ingests a script and generates analysis reports
    based on the selected framework(s).
    """
    from narratological.generators.base import GeneratorConfig
    from narratological.generators.beat_map import BeatMapReportGenerator
    from narratological.generators.coverage import CoverageReportGenerator

    if not script_path.exists():
        console.print(f"[red]Script file not found: {script_path}[/red]")
        raise typer.Exit(1)

    console.print(Panel(
        f"[bold]Analyzing:[/bold] {script_path.name}\n"
        f"[bold]Framework:[/bold] {framework or 'auto-detect'}\n"
        f"[bold]Reports:[/bold] {reports}",
        title="Script Analysis",
    ))

    # Parse the script
    try:
        script = parse_script(script_path)
        console.print(f"[dim]Parsed {len(script.scenes)} scenes, {len(script.characters)} characters[/dim]")
    except (FileNotFoundError, ValueError) as e:
        console.print(f"[red]Failed to parse script: {e}[/red]")
        raise typer.Exit(1) from e

    # Get LLM provider
    try:
        llm = get_provider(provider, model=model, base_url=base_url, verbose=True)
    except (OSError, ValueError, ImportError) as e:
        console.print(f"[red]{e}[/red]")
        raise typer.Exit(1) from e

    # Configure generators
    config = GeneratorConfig(
        primary_framework=framework,
        active_studies=[framework] if framework else [],
    )

    # Determine which reports to generate
    report_types = reports.lower().split(",")
    if "all" in report_types:
        report_types = ["coverage", "beatmap"]

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        results = {}

        for report_type in report_types:
            report_type = report_type.strip()

            if report_type == "coverage":
                task = progress.add_task("Generating coverage report...", total=None)
                try:
                    generator = CoverageReportGenerator(provider=llm, config=config)
                    report = generator.generate(script)
                    results["coverage"] = report
                    progress.update(task, description="[green]Coverage report complete[/green]")
                except Exception as e:
                    progress.update(task, description=f"[red]Coverage failed: {e}[/red]")

            elif report_type == "beatmap":
                task = progress.add_task("Generating beat map...", total=None)
                try:
                    generator = BeatMapReportGenerator(provider=llm, config=config)
                    report = generator.generate(script)
                    results["beatmap"] = report
                    progress.update(task, description="[green]Beat map complete[/green]")
                except Exception as e:
                    progress.update(task, description=f"[red]Beat map failed: {e}[/red]")

            else:
                console.print(f"[yellow]Unknown report type: {report_type}[/yellow]")

    # Display results
    if "coverage" in results:
        console.print()
        _display_coverage_report(results["coverage"])

    if "beatmap" in results:
        console.print()
        _display_beat_map_report(results["beatmap"])

    # Save outputs if requested
    if output:
        output.mkdir(parents=True, exist_ok=True)
        for name, report in results.items():
            report_path = output / f"{script_path.stem}_{name}.json"
            report_path.write_text(report.model_dump_json(indent=2), encoding="utf-8")
            console.print(f"[dim]Saved: {report_path}[/dim]")


@app.command("protocol")
def analyze_protocol(
    script_path: Annotated[
        Path,
        typer.Argument(help="Path to script file (txt, pdf, fountain, fdx)"),
    ],
    level: Annotated[
        str,
        typer.Option("--level", "-l", help="Protocol level (P1-P7)"),
    ] = "P3",
    output: Annotated[
        Path | None,
        typer.Option("--output", "-o", help="Output directory or file path for reports"),
    ] = None,
    provider: Annotated[
        str,
        typer.Option("--provider", "-p", help=PROVIDER_OPTION_HELP),
    ] = "ollama",
    model: Annotated[
        str | None,
        typer.Option("--model", "-m", help=MODEL_OPTION_HELP),
    ] = None,
    base_url: Annotated[
        str | None,
        typer.Option("--base-url", help=BASE_URL_OPTION_HELP),
    ] = None,
) -> None:
    """Analyze a script using a specific protocol level (P1-P7).

    Runs the appropriate combination of narrative reports, diagnostic tests,
    and analyses matching the selected protocol level.
    """
    from pydantic import BaseModel
    from rich.markdown import Markdown

    from narratological.loader import load_compendium
    from narratological.protocols.registry import get_protocol
    from narratological.protocols.runner import ProtocolRunner

    if not script_path.exists():
        console.print(f"[red]Script file not found: {script_path}[/red]")
        raise typer.Exit(1)

    try:
        spec = get_protocol(level)
    except KeyError:
        console.print(f"[red]Invalid protocol level: {level}. Must be one of P1-P7.[/red]")
        raise typer.Exit(1) from None

    console.print(Panel(
        f"[bold]Analyzing:[/bold] {script_path.name}\n"
        f"[bold]Protocol:[/bold] {spec.level} — {spec.name}\n"
        f"[bold]Purpose:[/bold] {spec.purpose}\n"
        f"[bold]Roles Activated:[/bold] {', '.join(r.value.upper() for r in spec.roles)}\n"
        f"[bold]Time Estimate:[/bold] {spec.time_estimate}",
        title="Protocol Analysis",
    ))

    # Parse the script
    try:
        script = parse_script(script_path)
        console.print(f"[dim]Parsed {len(script.scenes)} scenes, {len(script.characters)} characters[/dim]")
    except (FileNotFoundError, ValueError) as e:
        console.print(f"[red]Failed to parse script: {e}[/red]")
        raise typer.Exit(1) from e

    # Get LLM provider
    try:
        llm = get_provider(provider, model=model, base_url=base_url, verbose=True)
    except (OSError, ValueError, ImportError) as e:
        console.print(f"[red]{e}[/red]")
        raise typer.Exit(1) from e

    # Run analysis
    with console.status(f"[bold magenta]Running Protocol {spec.level}..."):
        try:
            compendium = load_compendium()
            runner = ProtocolRunner(llm, compendium)
            results = runner.run(script, spec.level)
        except Exception as e:
            console.print(f"[red]Protocol execution failed: {e}[/red]")
            raise typer.Exit(1) from e

    # Print combined markdown
    console.print()
    console.print(Markdown(results["combined_markdown"]))

    # Save output if requested
    if output:
        try:
            if output.is_dir() or not output.suffix:
                # If output is a directory or has no extension, save all parts inside it
                output.mkdir(parents=True, exist_ok=True)

                # Save master report
                master_path = output / f"{script_path.stem}_protocol_{spec.level}_master.md"
                master_path.write_text(results["combined_markdown"], encoding="utf-8")
                console.print(f"\n[green]Saved master report to: {master_path}[/green]")

                # Save individual JSON models or Markdown outputs
                for name, report in results.items():
                    if name == "combined_markdown":
                        continue
                    report_path = None
                    if isinstance(report, str):
                        report_path = output / f"{script_path.stem}_{name}.md"
                        report_path.write_text(report, encoding="utf-8")
                    elif isinstance(report, BaseModel):
                        report_path = output / f"{script_path.stem}_{name}.json"
                        report_path.write_text(report.model_dump_json(indent=2), encoding="utf-8")

                    if report_path:
                        console.print(f"[dim]Saved: {report_path}[/dim]")
            else:
                # Save just the master file
                output.parent.mkdir(parents=True, exist_ok=True)
                output.write_text(results["combined_markdown"], encoding="utf-8")
                console.print(f"\n[green]Saved master report to: {output}[/green]")
        except Exception as e:
            console.print(f"[yellow]Failed to save outputs: {e}[/yellow]")


@app.command("scene")
def analyze_scene(
    scene_text: Annotated[
        str,
        typer.Argument(help="Scene text to analyze (or path to file)"),
    ],
    framework: Annotated[
        str | None,
        typer.Option("--framework", "-f", help="Framework to apply"),
    ] = None,
    provider: Annotated[
        str,
        typer.Option("--provider", "-p", help=PROVIDER_OPTION_HELP),
    ] = "ollama",
    model: Annotated[
        str | None,
        typer.Option("--model", "-m", help=MODEL_OPTION_HELP),
    ] = None,
    base_url: Annotated[
        str | None,
        typer.Option("--base-url", help=BASE_URL_OPTION_HELP),
    ] = None,
) -> None:
    """Analyze a single scene using narratological algorithms.

    Provides quick analysis of beat function, tension, and structure.
    """
    from pydantic import BaseModel, Field

    # Check if it's a file path
    scene_path = Path(scene_text)
    if scene_path.exists():
        text = scene_path.read_text(encoding="utf-8")
    else:
        text = scene_text

    console.print(Panel(
        f"[dim]{text[:500]}{'...' if len(text) > 500 else ''}[/dim]",
        title="Scene Text",
    ))

    # Get LLM provider
    try:
        llm = get_provider(provider, model=model, base_url=base_url)
    except (OSError, ValueError, ImportError) as e:
        console.print(f"[red]{e}[/red]")
        raise typer.Exit(1) from e

    # Define response model for scene analysis
    class SceneAnalysis(BaseModel):
        """Scene analysis response."""
        function: str = Field(description="Primary beat function (SETUP, INCITE, ESCALATE, REVEAL, CRISIS, CLIMAX, RESOLVE, etc.)")
        secondary_function: str | None = Field(default=None, description="Secondary function if applicable")
        tension_level: int = Field(ge=1, le=10, description="Tension level 1-10")
        connector_to_next: str | None = Field(default=None, description="How this connects to next scene (BUT, THEREFORE, AND THEN, MEANWHILE)")
        key_characters: list[str] = Field(default_factory=list, description="Characters present/mentioned")
        summary: str = Field(description="One-sentence summary of what happens")
        notes: str | None = Field(default=None, description="Additional observations")

    # Analyze with LLM
    system_prompt = """You are a professional script analyst using narratological frameworks.
Analyze the given scene text and provide structured analysis including:
- Beat function (what narrative purpose it serves)
- Tension level (1-10 scale)
- Connection type (how it would connect to the next scene)
- Key characters and a brief summary"""

    prompt = f"""Analyze this scene:

{text}

Provide analysis as a JSON object."""

    try:
        result = llm.complete_structured(prompt, SceneAnalysis, system=system_prompt)

        # Display results
        console.print("\n[bold]Scene Analysis[/bold]")

        func_color = {
            "SETUP": "cyan",
            "INCITE": "yellow",
            "ESCALATE": "orange3",
            "REVEAL": "blue",
            "CRISIS": "red",
            "CLIMAX": "bold red",
            "RESOLVE": "green",
        }.get(result.function.upper(), "white")

        console.print(f"  [bold]Function:[/bold] [{func_color}]{result.function}[/{func_color}]")
        if result.secondary_function:
            console.print(f"  [bold]Secondary:[/bold] {result.secondary_function}")

        tension_color = "green" if result.tension_level >= 7 else "yellow" if result.tension_level >= 4 else "dim"
        console.print(f"  [bold]Tension:[/bold] [{tension_color}]{result.tension_level}/10[/{tension_color}]")

        if result.connector_to_next:
            conn_color = "green" if result.connector_to_next.upper() in ("BUT", "THEREFORE") else "red"
            console.print(f"  [bold]Connector:[/bold] [{conn_color}]{result.connector_to_next}[/{conn_color}]")

        if result.key_characters:
            console.print(f"  [bold]Characters:[/bold] {', '.join(result.key_characters)}")

        console.print(f"\n  [bold]Summary:[/bold] {result.summary}")

        if result.notes:
            console.print(f"\n  [dim]Notes: {result.notes}[/dim]")

    except Exception as e:
        console.print(f"[red]Analysis failed: {e}[/red]")
        raise typer.Exit(1) from e


@app.command("compare")
def compare_scripts(
    script_a: Annotated[Path, typer.Argument(help="First script", exists=True, file_okay=True, dir_okay=False, readable=True)],
    script_b: Annotated[Path, typer.Argument(help="Second script", exists=True, file_okay=True, dir_okay=False, readable=True)],
    provider: Annotated[
        str,
        typer.Option("--provider", "-p", help=PROVIDER_OPTION_HELP),
    ] = "ollama",
    model: Annotated[
        str | None,
        typer.Option("--model", "-m", help=MODEL_OPTION_HELP),
    ] = None,
    base_url: Annotated[
        str | None,
        typer.Option("--base-url", help=BASE_URL_OPTION_HELP),
    ] = None,
    output: Annotated[
        Path | None,
        typer.Option("--output", "-o", help="Output path for comparison report"),
    ] = None,
) -> None:
    """Compare two scripts structurally.

    Analyzes structural similarities and differences between scripts.
    """
    from narratological.diagnostics.runner import create_diagnostic_runner

    if not script_a.exists() or not script_b.exists():
        console.print("[red]One or both script files not found[/red]")
        raise typer.Exit(1)

    console.print(f"Comparing: [cyan]{script_a.name}[/cyan] vs [cyan]{script_b.name}[/cyan]")

    # Parse both scripts
    try:
        script_1 = parse_script(script_a)
        script_2 = parse_script(script_b)
    except (FileNotFoundError, ValueError) as e:
        console.print(f"[red]Failed to parse scripts: {e}[/red]")
        raise typer.Exit(1) from e

    # Get LLM provider
    try:
        llm = get_provider(provider, model=model, base_url=base_url)
    except (OSError, ValueError, ImportError) as e:
        console.print(f"[red]{e}[/red]")
        raise typer.Exit(1) from e

    # Run diagnostics on both
    runner = create_diagnostic_runner(provider=llm)

    console.print("\n[bold]Analyzing scripts...[/bold]")

    _, context_a = load_input(script_a)
    _, context_b = load_input(script_b)

    report_a = runner.run_all(context_a, include_framework=False)
    report_b = runner.run_all(context_b, include_framework=False)

    # Comparison table
    table = Table(title="Structural Comparison")
    table.add_column("Metric")
    table.add_column(script_a.stem, justify="right")
    table.add_column(script_b.stem, justify="right")
    table.add_column("Difference", justify="right")

    comparisons = [
        ("Scenes", len(script_1.scenes), len(script_2.scenes)),
        ("Characters", len(script_1.characters), len(script_2.characters)),
        ("Causal Binding", report_a.causal_binding_ratio, report_b.causal_binding_ratio),
        ("Reorderability", report_a.reorderability_score, report_b.reorderability_score),
        ("Necessity", report_a.necessity_score, report_b.necessity_score),
    ]

    for name, val_a, val_b in comparisons:
        if isinstance(val_a, float):
            diff = val_b - val_a
            diff_str = f"{diff:+.1%}" if abs(diff) > 0.01 else "~"
            table.add_row(name, f"{val_a:.1%}", f"{val_b:.1%}", diff_str)
        else:
            diff = val_b - val_a
            diff_str = f"{diff:+d}" if diff != 0 else "="
            table.add_row(name, str(val_a), str(val_b), diff_str)

    console.print(table)

    # Health comparison
    console.print("\n[bold]Overall Health:[/bold]")
    console.print(f"  {script_a.stem}: {report_a.overall_health}")
    console.print(f"  {script_b.stem}: {report_b.overall_health}")

    # Save output if requested
    if output:
        comparison = {
            "script_a": {"title": script_1.title, "metrics": report_a.model_dump()},
            "script_b": {"title": script_2.title, "metrics": report_b.model_dump()},
        }
        output.write_text(json.dumps(comparison, indent=2, default=str), encoding="utf-8")
        console.print(f"\n[dim]Comparison saved to: {output}[/dim]")


@app.command("batch")
def batch_analyze(
    directory: Annotated[
        Path,
        typer.Argument(help="Directory containing scripts", exists=True, file_okay=False, dir_okay=True, readable=True),
    ],
    pattern: Annotated[
        str,
        typer.Option("--pattern", "-p", help="File pattern to match"),
    ] = "*.txt",
    output: Annotated[
        Path | None,
        typer.Option("--output", "-o", help="Output directory"),
    ] = None,
    provider: Annotated[
        str,
        typer.Option("--provider", help=PROVIDER_OPTION_HELP),
    ] = "ollama",
    model: Annotated[
        str | None,
        typer.Option("--model", "-m", help=MODEL_OPTION_HELP),
    ] = None,
    base_url: Annotated[
        str | None,
        typer.Option("--base-url", help=BASE_URL_OPTION_HELP),
    ] = None,
) -> None:
    """Batch analyze multiple scripts.

    Process all matching scripts in a directory.
    """
    from narratological.diagnostics.runner import create_diagnostic_runner

    if not directory.exists():
        console.print(f"[red]Directory not found: {directory}[/red]")
        raise typer.Exit(1)

    scripts = list(directory.glob(pattern))
    console.print(f"Found [cyan]{len(scripts)}[/cyan] scripts matching '{pattern}'")

    if not scripts:
        console.print("[yellow]No scripts to process[/yellow]")
        return

    # Get LLM provider
    try:
        llm = get_provider(provider, model=model, base_url=base_url)
    except (OSError, ValueError, ImportError) as e:
        console.print(f"[red]{e}[/red]")
        raise typer.Exit(1) from e

    runner = create_diagnostic_runner(provider=llm)

    # Process each script
    results = []
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        for script_path in scripts:
            task = progress.add_task(f"Analyzing {script_path.name}...", total=None)

            try:
                _, context = load_input(script_path)
                report = runner.run_all(context, include_framework=False)
                results.append({
                    "script": script_path.name,
                    "health": report.overall_health,
                    "causal_binding": report.causal_binding_ratio,
                    "issues": report.critical_count + report.warning_count,
                })
                progress.update(task, description=f"[green]{script_path.name}: {report.overall_health}[/green]")
            except Exception as e:
                results.append({
                    "script": script_path.name,
                    "health": "Error",
                    "causal_binding": 0,
                    "issues": -1,
                    "error": str(e),
                })
                progress.update(task, description=f"[red]{script_path.name}: Error[/red]")

    # Summary table
    console.print()
    table = Table(title=f"Batch Analysis Results ({len(results)} scripts)")
    table.add_column("Script")
    table.add_column("Health")
    table.add_column("Causal Binding", justify="right")
    table.add_column("Issues", justify="right")

    for r in results:
        health_color = {"Excellent": "green", "Good": "green", "Fair": "yellow", "Poor": "red", "Critical": "red", "Error": "red"}.get(r["health"], "white")
        cb = f"{r['causal_binding']:.0%}" if r["causal_binding"] else "-"
        issues = str(r["issues"]) if r["issues"] >= 0 else "N/A"
        table.add_row(r["script"], f"[{health_color}]{r['health']}[/{health_color}]", cb, issues)

    console.print(table)

    # Save output if requested
    if output:
        output.mkdir(parents=True, exist_ok=True)
        summary_path = output / "batch_summary.json"
        summary_path.write_text(json.dumps(results, indent=2), encoding="utf-8")
        console.print(f"\n[dim]Summary saved to: {summary_path}[/dim]")


def _display_script_doctor_result(result) -> None:
    """Display a Script Doctor analysis result."""
    console.print(Panel(
        f"[bold]Pair:[/bold] {result.pair.primary_id} & {result.pair.secondary_id}\n"
        f"[bold]Theme:[/bold] {result.pair.theme}",
        title="Script Doctor Analysis",
        border_style="magenta",
    ))

    # Display debate rounds if present
    if result.debate_rounds:
        console.print("\n[bold yellow]Multi-Agent Debate Rounds:[/bold yellow]")
        for round_data in result.debate_rounds:
            round_name = round_data.get("round", "Unknown Round")
            console.print(f"\n[bold underline]{round_name}[/bold underline]")
            content = round_data.get("content", "")
            if isinstance(content, list):
                for entry in content:
                    c = entry.get("creator", "Creator")
                    f = entry.get("feedback", "")
                    console.print(f"  [bold cyan]{c}:[/bold cyan] {f}")
            else:
                console.print(f"  {content}")

    # Display dialogue
    console.print("\n[bold italic magenta]Collaborative Dialogue:[/bold italic magenta]")
    for entry in result.dialogue:
        name = entry.get("creator", "Unknown")
        feedback = entry.get("feedback", "")
        console.print(f"\n[bold cyan]{name}:[/bold cyan] [italic]{feedback}[/italic]")

    # Joint recommendations
    if result.joint_recommendations:
        console.print("\n[bold green]Joint Recommendations[/bold green]")
        for rec in result.joint_recommendations:
            console.print(f"  + {rec}")

    # Creative tension
    if result.creative_tension:
        console.print("\n[bold yellow]Creative Tension[/bold yellow]")
        for tension in result.creative_tension:
            console.print(f"  ~ {tension}")

    # Final Prescription
    console.print(Panel(
        f"[bold white]{result.final_prescription}[/bold white]",
        title="Final Prescription",
        border_style="bold green",
    ))


@app.command("script-doctor")
def script_doctor(
    script_path: Annotated[
        Path,
        typer.Argument(help="Path to script file", exists=True, file_okay=True, dir_okay=False, readable=True),
    ],
    sequence: Annotated[
        str | None,
        typer.Option("--sequence", "-s", help="Sequence ID (A-G) or name (e.g., 'B' or 'Cinematic Interiority')"),
    ] = None,
    primary: Annotated[
        str | None,
        typer.Option("--primary", "-p1", help="Primary study ID (if not using sequence)"),
    ] = None,
    secondary: Annotated[
        str | None,
        typer.Option("--secondary", "-p2", help="Secondary study ID (if not using sequence)"),
    ] = None,
    debate: Annotated[
        bool,
        typer.Option("--debate", "-d", help="Enable exhaustive multi-agent debate mode"),
    ] = False,
    provider: Annotated[
        str,
        typer.Option("--provider", "-p", help=PROVIDER_OPTION_HELP),
    ] = "ollama",
    model: Annotated[
        str | None,
        typer.Option("--model", "-m", help=MODEL_OPTION_HELP),
    ] = None,
    base_url: Annotated[
        str | None,
        typer.Option("--base-url", help=BASE_URL_OPTION_HELP),
    ] = None,
) -> None:
    """Perform a collaborative 'Script Doctor' analysis using creator pairs.

    This command uses paired narratological lenses to provide synthesized,
    multi-dimensional feedback on your script.
    """
    from narratological.llm.script_doctor import ScriptDoctorAnalyst
    from narratological.loader import load_compendium
    from narratological.models.analyst import AnalystContext

    if not script_path.exists():
        console.print(f"[red]Script file not found: {script_path}[/red]")
        raise typer.Exit(1)

    # Resolve studies
    compendium = load_compendium()
    study1 = None
    study2 = None

    if sequence:
        pair = compendium.get_pair_from_sequence(sequence)
        if pair:
            study1, study2 = pair
        else:
            console.print(f"[red]Sequence '{sequence}' not found.[/red]")
            raise typer.Exit(1)
    elif primary and secondary:
        study1 = compendium.get_study(primary)
        study2 = compendium.get_study(secondary)
        if not study1 or not study2:
            missing = primary if not study1 else secondary
            console.print(f"[red]Study '{missing}' not found.[/red]")
            raise typer.Exit(1)
    else:
        console.print("[red]Must provide either --sequence or both --primary and --secondary[/red]")
        raise typer.Exit(1)

    console.print(Panel(
        f"[bold]Analyzing:[/bold] {script_path.name}\n"
        f"[bold]Doctors:[/bold] {study1.creator} & {study2.creator}\n"
        f"[bold]Debate Mode:[/bold] {'Enabled' if debate else 'Disabled'}",
        title="Script Doctor Consultation",
    ))

    # Parse script
    try:
        script = parse_script(script_path)
        context = AnalystContext.from_script(script)
    except Exception as e:
        console.print(f"[red]Failed to parse script: {e}[/red]")
        raise typer.Exit(1) from e

    # Get provider and analyst
    try:
        llm = get_provider(provider, model=model, base_url=base_url, verbose=True)
        doctor = ScriptDoctorAnalyst(llm)
    except Exception as e:
        console.print(f"[red]Initialization failed: {e}[/red]")
        raise typer.Exit(1) from e

    with console.status("[bold magenta]Consulting the doctors..."):
        try:
            result = doctor.analyze(context, study1, study2, debate_mode=debate)
            _display_script_doctor_result(result)
        except Exception as e:
            console.print(f"[red]Analysis failed: {e}[/red]")
            raise typer.Exit(1) from e
