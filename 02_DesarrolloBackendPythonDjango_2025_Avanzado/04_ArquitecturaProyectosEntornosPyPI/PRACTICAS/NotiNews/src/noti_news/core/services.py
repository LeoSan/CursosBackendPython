"""Core business logic services."""

import logging

from noti_news.analysis.analyzer import GeminiAnalyzer
from noti_news.config import settings
from noti_news.core.models import Article
from noti_news.sources.newsapi import NewsAPIClient

logger = logging.getLogger(__name__)


class NewsService:
    """Orchestrates news fetching and analysis."""

    def __init__(self):
        logger.debug("Initializing NewsService")
        self.newsapi_client = NewsAPIClient(
            api_key=settings.newsapi_api_key, timeout=settings.request_timeout
        )
        self.analyzer = GeminiAnalyzer(
            api_key=settings.google_api_key, model_name=settings.gemini_model
        )

    def get_articles(self, query: str, limit: int = 5) -> list[Article]:
        """Fetch articles from the configured source."""
        logger.info(f"Fetching articles for query='{query}' limit={limit}")
        # Only NewsAPI is supported now
        articles = self.newsapi_client.get_top_headlines(query, limit)
        logger.debug(f"Found {len(articles)} articles")
        return articles

    def analyze_articles(self, articles: list[Article], question: str) -> str:
        """Analyze articles using AI."""
        if not articles:
            logger.warning("No articles provided for analysis")
            return "No hay artículos para analizar."

        logger.info(f"Analyzing {len(articles)} articles with question='{question}'")
        return self.analyzer.analyze(articles, question)
