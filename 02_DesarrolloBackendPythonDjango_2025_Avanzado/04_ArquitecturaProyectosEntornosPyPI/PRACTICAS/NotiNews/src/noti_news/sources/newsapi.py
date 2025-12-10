"""Client for News API."""

from typing import List, Optional
import requests

from noti_news.core.exceptions import APIError
from noti_news.core.models import Article


class NewsAPIClient:
    """Client for fetching news from NewsAPI."""

    BASE_URL = "https://newsapi.org/v2"

    def __init__(self, api_key: str, timeout: int = 10):
        self.api_key = api_key
        self.timeout = timeout

    def get_top_headlines(self, query: str, limit: int = 5) -> List[Article]:
        """Fetch top headlines matching the query."""
        params = {
            "q": query,
            "apiKey": self.api_key,
            "pageSize": limit,
            "language": "es",
        }

        try:
            response = requests.get(
                f"{self.BASE_URL}/top-headlines", params=params, timeout=self.timeout
            )
            response.raise_for_status()
            data = response.json()

            if data.get("status") != "ok":
                raise APIError(f"NewsAPI error: {data.get('message')}")

            return self._parse_articles(data.get("articles", []))

        except requests.RequestException as e:
            raise APIError(f"Failed to fetch articles from NewsAPI: {e}")

    def _parse_articles(self, raw_articles: List[dict]) -> List[Article]:
        """Convert raw API response to Article objects."""
        articles = []
        for item in raw_articles:
            # Skip removed articles or missing essential data
            if item.get("title") == "[Removed]" or not item.get("url"):
                continue

            articles.append(
                Article(
                    title=item.get("title", "No Title"),
                    description=item.get("description") or "No description",
                    url=item.get("url", ""),
                )
            )
        return articles
