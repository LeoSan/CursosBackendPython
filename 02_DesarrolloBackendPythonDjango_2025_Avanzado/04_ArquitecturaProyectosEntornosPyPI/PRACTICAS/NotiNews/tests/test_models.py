"""Tests for models."""

import unittest
from noti_news.core.models import Article


class TestModels(unittest.TestCase):
    """Test data models."""

    def test_article_init(self):
        """Test Article initialization."""
        article = Article("Title", "Desc", "URL")
        self.assertEqual(article.title, "Title")
        self.assertEqual(article.description, "Desc")
        self.assertEqual(article.url, "URL")
