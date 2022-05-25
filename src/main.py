from fastapi import FastAPI

from schemas import Article
import scraper
import scraper_new

import time

app = FastAPI()


@app.get("/")
def index():
    return "This is the index page"


@app.get("/tags", response_model=list[str])
def tags():
    return scraper.list_tags()


@app.get("/hot/{limit}", response_model=list[Article])
def hot(limit: int):
    articles = []
    to = str(time.time() * 1000)
    while len(articles) < limit:
        more, to = scraper_new.get_trending_articles(to)
        articles += more
    return articles


@app.get("/hot/tag/{tag_name}/{limit}", response_model=list[Article])
def hot_tag(tag_name: str, limit: int):
    articles = []
    to = "0"
    while len(articles) < limit:
        more, to = scraper_new.get_trending_tagged_articles(tag_name, to)
        articles += more
    return articles
