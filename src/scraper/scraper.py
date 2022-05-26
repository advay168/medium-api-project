import aiohttp
from ..schemas import Article

import re

import json
import pathlib

# Extracted from analyzing network requests
src = pathlib.Path(__file__).parent
with open(src / "trending_query.json") as file:
    trending_query = json.load(file)

with open(src / "tag_query.json") as file:
    tag_query = json.load(file)


async def list_tags() -> list[str]:
    url = "https://medium.com"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return re.findall(r"/tag/(.*?)\?", await response.text())


async def get_trending_articles(to: str) -> tuple[list[Article], str]:
    trending_query[0]["variables"]["feedPagingOptions"]["to"] = to
    async with aiohttp.ClientSession() as session:
        async with session.post(
            "https://medium.com/_/graphql", json=trending_query
        ) as response:
            json = await response.json()
    posts = json[0]["data"]["topic"]["latestPosts"]["postPreviews"]
    newTo = json[0]["data"]["topic"]["latestPosts"]["pagingInfo"]["next"]["to"]
    img_prefix = "https://miro.medium.com/fit/c/200/200/"
    return (
        [
            Article(
                author=post["post"]["creator"]["name"],
                title=post["post"]["title"],
                blurb=post["post"]["previewContent"]["subtitle"],
                time=post["post"]["readingTime"],
                thumbnail=img_prefix + post["post"]["previewImage"]["id"],
                link=post["post"]["mediumUrl"],
            )
            for post in posts
        ],
        newTo,
    )


async def get_trending_tagged_articles(tag: str, to: str) -> tuple[list[Article], str]:
    tag_query[0]["variables"]["paging"]["to"] = to
    tag_query[0]["variables"]["tagSlug"] = tag
    async with aiohttp.ClientSession() as session:
        async with session.post(
            "https://medium.com/_/graphql", json=tag_query
        ) as response:
            json = await response.json()
    posts = json[0]["data"]["tagFeed"]["items"]
    newTo = json[0]["data"]["tagFeed"]["pagingInfo"]["next"]["to"]
    img_prefix = "https://miro.medium.com/fit/c/200/200/"
    return (
        [
            Article(
                author=post["post"]["creator"]["name"],
                title=post["post"]["title"],
                blurb=post["post"]["extendedPreviewContent"]["subtitle"],
                time=post["post"]["readingTime"],
                thumbnail=img_prefix + post["post"]["previewImage"]["id"],
                link=post["post"]["mediumUrl"],
            )
            for post in posts
        ],
        newTo,
    )
