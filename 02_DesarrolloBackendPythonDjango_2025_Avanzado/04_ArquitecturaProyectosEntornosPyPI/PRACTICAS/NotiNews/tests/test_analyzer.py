"""Tests for the analyzer module."""

import unittest
from unittest.mock import MagicMock, patch

from noti_news.analysis.analyzer import GeminiAnalyzer, get_analyzer
from noti_news.core.exceptions import AnalysisError
from noti_news.core.models import Article


class TestAnalyzer(unittest.TestCase):
    """Test the GeminiAnalyzer class."""

    def setUp(self):
        """Set up test fixtures."""
        self.api_key = "fake_key"
        self.analyzer = GeminiAnalyzer(api_key=self.api_key)
        self.articles = [
            Article("Title 1", "Description 1", "http://example1.com"),
            Article("Title 2", "Description 2", "http://example2.com"),
        ]

    def test_build_context(self):
        """Test context building from articles."""
        context = self.analyzer._build_context(self.articles)
        self.assertIn("Title 1", context)
        self.assertIn("Description 1", context)
        self.assertIn("Title 2", context)

    @patch("noti_news.analysis.analyzer.genai")
    def test_analyze_success(self, mock_genai):
        """Test successful analysis."""
        # Setup mock
        mock_model = MagicMock()
        mock_response = MagicMock()
        mock_response.text = "Analysis result"
        mock_model.generate_content.return_value = mock_response
        self.analyzer.model = mock_model

        result = self.analyzer.analyze(self.articles, "Question")

        self.assertEqual(result, "Analysis result")
        mock_model.generate_content.assert_called_once()

    def test_analyze_empty_articles(self):
        """Test analysis with empty articles list."""
        result = self.analyzer.analyze([], "Question")
        self.assertEqual(result, "No provided articles to analyze.")

    @patch("noti_news.analysis.analyzer.genai")
    def test_analyze_api_error(self, mock_genai):
        """Test analysis handling API error."""
        # Setup mock to raise error
        mock_model = MagicMock()
        from google.api_core import exceptions as google_exceptions

        mock_model.generate_content.side_effect = google_exceptions.GoogleAPIError(
            "API error"
        )
        self.analyzer.model = mock_model

        with self.assertRaises(AnalysisError):
            self.analyzer.analyze(self.articles, "Question")

    @patch("noti_news.config.settings")
    def test_get_analyzer_success(self, mock_settings):
        """Test factory function."""
        mock_settings.google_api_key = "fake_key"
        mock_settings.gemini_model = "gemini-pro"

        # We need to patch genai inside analyzer module
        # to avoid real network calls during init
        with patch("noti_news.analysis.analyzer.genai"):
            analyzer = get_analyzer()
            self.assertIsInstance(analyzer, GeminiAnalyzer)
