import requests
from bs4 import BeautifulSoup

from dataclasses import dataclass
import re


from rich import pretty
pretty.install()
print = pretty.pprint


@dataclass
class Article:
    author: str
    title: str
    blurb: str
    time: str
    thumbnail: str
    link: str

def list_tags():
    url = "https://medium.com"
    req = requests.get(url)
    return re.findall(r"/tag/(.*?)\?", req.text)
print(list_tags())


def extract_articles_from_home():
    url = "https://medium.com"
    req = requests.get(url)
    soup = BeautifulSoup(req.content, features="html.parser").body
    secs = soup.find_all("div", {"class", "pw-homefeed-item"})
    articles = []
    for sec in secs:
        author = sec.h4.text
        title = sec.h2.text
        blurb = sec.h3.text
        time = sec.find("span", {"class": "pw-reading-time"}).text
        img = sec.find("img", {"height": "100"})["src"]
        link: str = sec.find_all("a")[-1]["href"]
        if not link.startswith("https"):
            link = "https://medium.com" + link
        # print(f"{title=}\n{blurb=}\n{time=}\n{img=}\n{author=}\n{link=}")
        articles.append(Article(author, title, blurb, time, img, link))
    return articles


def extract_articles_from_tag(tag: str) -> list[Article]:
    url = "https://medium.com/tag/" + tag
    req = requests.get(url)
    soup = BeautifulSoup(req.content, features="html.parser").body
    articles = []
    for article in soup.find_all("article"):
        Title = article.select_one('[aria-label="Post Preview Title"]')
        Reading_Time = article.select_one('[aria-label="Post Preview Reading Time"]')
        Image = article.select_one('[aria-label="Post Preview Image"]')
        title = blurb = ""
        if Title is not None:
            title = Title.h2.text
            blurb = Title.p.text
        time = ""
        if Reading_Time is not None:
            time = Reading_Time.span.text
        img = ""
        if Image is not None:
            img = Image.img["src"]
        author = article.find_all("a")[1].p.text
        link = article.find_all("a")[3]["href"]
        if not link.startswith("https"):
            link = "https://medium.com" + link
        # print(f"{title=}\n{blurb=}\n{time=}\n{img=}\n{name=}\n{link=}")
        articles.append(Article(author, title, blurb, time, img, link))
    return articles
