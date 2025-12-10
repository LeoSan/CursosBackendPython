"""Display utilities using Rich."""

from typing import List
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.markdown import Markdown

from noti_news.core.models import Article

console = Console()

def display_articles(articles: List[Article]):
    """Display a list of articles in a table."""
    if not articles:
        console.print("[yellow]No se encontraron artículos.[/yellow]")
        return

    table = Table(title=f"Noticias Encontradas ({len(articles)})")
    table.add_column("Título", style="cyan", no_wrap=False)
    table.add_column("Descripción", style="white")
    table.add_column("Link", style="blue")

    for article in articles:
        table.add_row(
            article.title, 
            article.description or "N/A", 
            article.url
        )

    console.print(table)

def display_answer(answer: str):
    """Display the AI answer."""
    console.print(Panel(Markdown(answer), title="🤖 Análisis de IA", border_style="green"))

def display_error(message: str):
    """Display an error message."""
    console.print(f"[bold red]Error:[/bold red] {message}")
