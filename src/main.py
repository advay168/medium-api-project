from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from schemas import Article
import scraper

import time

app = FastAPI()


@app.get("/")
def index():
    return HTMLResponse(
        """
        <h1>
            Visit
                <a href='/docs'>/docs</a>
            to view the documentation and different endpoints
        </h1>"""
    )


@app.get("/tags", response_model=list[str])
async def tags():
    """
    Returns a list of popular tags that can be used for searching by tags at /hot/tag
    """
    return await scraper.list_tags()


@app.get("/hot/{limit}", response_model=list[Article])
async def hot(limit: int):
    """
    Returns a list of {limit} trending articles
    """
    articles: list[Article] = []
    to = str(time.time() * 1000)
    while len(articles) < limit:
        more, to = await scraper.get_trending_articles(to)
        articles += more
    return articles


@app.get("/hot/tag/{tag_name}/{limit}", response_model=list[Article])
async def hot_tag(tag_name: str, limit: int):
    """
    Returns a list of {limit} trending articles for a particular tag
    """
    articles: list[Article] = []
    to = "0"
    while len(articles) < limit:
        more, to = await scraper.get_trending_tagged_articles(tag_name, to)
        articles += more
    return articles
