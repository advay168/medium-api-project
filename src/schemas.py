from pydantic import BaseModel


class Article(BaseModel):
    author: str
    title: str
    blurb: str
    time: str
    thumbnail: str
    link: str
