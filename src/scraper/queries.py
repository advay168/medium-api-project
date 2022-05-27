import json
import importlib.resources

from .. import scraper

# Extracted from analyzing network requests
file = importlib.resources.open_text(scraper, "trending_query.json")
trending_query = json.load(file)
file = importlib.resources.open_text(scraper, "tag_query.json")
tag_query = json.load(file)
