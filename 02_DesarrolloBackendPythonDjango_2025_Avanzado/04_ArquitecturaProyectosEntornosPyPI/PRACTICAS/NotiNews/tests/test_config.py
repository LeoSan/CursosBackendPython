"""Tests for configuration."""

import os
import unittest
from unittest.mock import patch

from noti_news.config import Settings


class TestConfig(unittest.TestCase):
    """Test configuration loading."""

    def test_settings_load_from_env(self):
        """Test loading settings from environment variables."""
        with patch.dict(
            os.environ,
            {
                "NEWSAPI_API_KEY": "test_news_key",
                "GOOGLE_API_KEY": "test_google_key",
                "GEMINI_MODEL": "gemini-test",
                "MAX_ARTICLES": "10",
            },
        ):
            settings = Settings()
            self.assertEqual(settings.newsapi_api_key, "test_news_key")
            self.assertEqual(settings.google_api_key, "test_google_key")
            self.assertEqual(settings.gemini_model, "gemini-test")
            self.assertEqual(settings.max_articles, 10)

