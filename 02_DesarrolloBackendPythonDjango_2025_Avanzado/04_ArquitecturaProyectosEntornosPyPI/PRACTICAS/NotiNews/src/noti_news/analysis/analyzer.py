"""News analyzer using Google Gemini."""

import google.generativeai as genai
from google.api_core import exceptions as google_exceptions

from noti_news.config import settings
from noti_news.core.exceptions import AnalysisError
from noti_news.core.models import Article


def get_analyzer():
    """Factory function to get an analyzer instance."""
    return GeminiAnalyzer(
        api_key=settings.google_api_key, model_name=settings.gemini_model
    )


class GeminiAnalyzer:
    """Analyzes news implementation using Google Gemini."""

    def __init__(self, api_key: str, model_name: str = "gemini-2.5-flash"):
        """Initialize the analyzer."""
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name)

    def analyze(self, articles: list[Article], question: str) -> str:
        """Analyze articles to answer a question."""
        if not articles:
            return "No provided articles to analyze."

        context = self._build_context(articles)
        prompt = f"Context:\n{context}\n\nQuestion: {question}\n\nAnswer based on the news provided:"

        try:
            response = self.model.generate_content(prompt)
            return response.text
        except google_exceptions.GoogleAPIError as e:
            raise AnalysisError(f"Error analyzing with Gemini: {e}")
        except Exception as e:
            raise AnalysisError(f"Unexpected error: {e}")

    def _build_context(self, articles: list[Article]) -> str:
        """Convert articles to a text context."""
        context_parts = []
        for i, article in enumerate(articles, 1):
            part = f"Article {i}:\nTitle: {article.title}\n"
            if article.description:
                part += f"Description: {article.description}\n"
            context_parts.append(part)
        return "\n".join(context_parts)
