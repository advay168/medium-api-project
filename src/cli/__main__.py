import typer
import time
import asyncio
from asyncio import run as aiorun
from rich.table import Table
from rich.console import Console

from .. import scraper
from ..schemas import Article

app = typer.Typer()

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


def display_articles(articles: list[Article]):
    table = Table(title="Articles", show_lines=True)
    table.add_column("Author", max_width=12)
    table.add_column("Title", max_width=15)
    table.add_column("Blurb")
    table.add_column("Time to read", max_width=5)
    table.add_column("Link")
    for article in articles:
        table.add_row(
            article.author,
            article.title,
            article.blurb,
            str(round(float(article.time))),
            f"[link={article.link}]" + article.link + "[/link]",
        )
    console = Console()
    console.print(table)

@app.command()
def list_tags():
    """
    List the top tags from medium.com.
    """
    async def _():
        print(*await scraper.list_tags(), sep="\n")
    aiorun(_())


@app.command()
def trending(limit: int = 10):
    """
    Display {limit} trending articles from the homepage of medium.com
    """

    async def _():
        articles: list[Article] = []
        to = str(time.time() * 1000)
        while len(articles) < limit:
            more, to = await scraper.get_trending_articles(to)
            articles += more
        articles = articles[:limit]
        display_articles(articles)

    aiorun(_())


@app.command()
def tag(tag: str, limit: int = 10):
    """
    Display {limit} trending articles for a particular {tag}. 
   
   \b
    List top tags with the `list-tags` command
    """
    async def _():
        articles: list[Article] = []
        to = "0"
        while len(articles) < limit:
            more, to = await scraper.get_trending_tagged_articles(tag, to)
            articles += more
        articles = articles[:limit]
        display_articles(articles)

    aiorun(_())


if __name__ == "__main__":
    app()
