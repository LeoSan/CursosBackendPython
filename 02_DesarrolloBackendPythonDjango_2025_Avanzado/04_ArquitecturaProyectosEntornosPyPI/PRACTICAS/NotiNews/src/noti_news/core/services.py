"""Core business logic services."""

from typing import List, Optional

from noti_news.analysis.analyzer import GeminiAnalyzer
from noti_news.config import settings
from noti_news.core.models import Article
from noti_news.sources.newsapi import NewsAPIClient


class NewsService:
    """Orchestrates news fetching and analysis."""

    def __init__(self):
        self.newsapi_client = NewsAPIClient(
            api_key=settings.newsapi_api_key, timeout=settings.request_timeout
        )
        self.analyzer = GeminiAnalyzer(
            api_key=settings.google_api_key, model_name=settings.gemini_model
        )

    def get_articles(self, query: str, limit: int = 5) -> List[Article]:
        """Fetch articles from the configured source."""
        # Only NewsAPI is supported now
        return self.newsapi_client.get_top_headlines(query, limit)

    def analyze_articles(self, articles: List[Article], question: str) -> str:
        """Analyze articles using AI."""
        if not articles:
            return "No hay artículos para analizar."

        return self.analyzer.analyze(articles, question)
