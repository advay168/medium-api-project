import json
import importlib.resources


# Extracted from analyzing network requests

file = importlib.resources.open_text(__package__, "trending_query.json")
trending_query = json.load(file)
file = importlib.resources.open_text(__package__, "tag_query.json")
tag_query = json.load(file)
