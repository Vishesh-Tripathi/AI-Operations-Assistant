import os
import requests
from tools.retry import retry

BASE_URL = "https://newsapi.org/v2"

def _fetch_news(topic, limit=5):
    api_key = os.getenv("NEWS_API_KEY")

    url = f"{BASE_URL}/everything"
    params = {
        "q": topic,
        "language": "en",
        "sortBy": "relevancy",
        "pageSize": limit,
        "apiKey": api_key
    }

    response = requests.get(url, params=params, timeout=5)
    response.raise_for_status()
    data = response.json()

    return [
        {
            "title": article["title"],
            "source": article["source"]["name"],
            "url": article["url"]
        }
        for article in data.get("articles", [])
    ]

def get_news(topic, limit=5):
    return retry(lambda: _fetch_news(topic, limit))
