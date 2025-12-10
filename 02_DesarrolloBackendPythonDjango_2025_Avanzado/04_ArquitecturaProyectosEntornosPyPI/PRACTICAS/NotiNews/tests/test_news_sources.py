"""Tests for news sources."""

import unittest
from unittest.mock import MagicMock, patch

from requests import RequestException

from noti_news.core.exceptions import APIError
from noti_news.core.models import Article
from noti_news.sources.newsapi import NewsAPIClient


class TestNewsAPIClient(unittest.TestCase):
    """Test NewsAPIClient."""

    def setUp(self):
        self.client = NewsAPIClient("api_key")

    @patch("noti_news.sources.newsapi.requests.get")
    def test_get_top_headlines_success(self, mock_get):
        """Test successful fetch."""
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "status": "ok",
            "articles": [
                {
                    "title": "Title 1",
                    "description": "Desc 1",
                    "url": "http://example.com/1",
                }
            ],
        }
        mock_get.return_value = mock_response

        articles = self.client.get_top_headlines("query")
        self.assertEqual(len(articles), 1)
        self.assertIsInstance(articles[0], Article)

    @patch("noti_news.sources.newsapi.requests.get")
    def test_get_top_headlines_removed(self, mock_get):
        """Test filtering removed articles."""
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "status": "ok",
            "articles": [
                {
                    "title": "[Removed]",
                    "description": "Desc 1",
                    "url": "http://example.com/1",
                },
                {
                    "title": "Valid",
                    "description": "Desc 2",
                    "url": "http://example.com/2",
                },
            ],
        }
        mock_get.return_value = mock_response

        articles = self.client.get_top_headlines("query")
        self.assertEqual(len(articles), 1)
        self.assertEqual(articles[0].title, "Valid")

    @patch("noti_news.sources.newsapi.requests.get")
    def test_get_top_headlines_error_response(self, mock_get):
        """Test API error response."""
        mock_response = MagicMock()
        mock_response.json.return_value = {"status": "error", "message": "Bad request"}
        mock_get.return_value = mock_response

        with self.assertRaises(APIError):
            self.client.get_top_headlines("query")

    @patch("noti_news.sources.newsapi.requests.get")
    def test_get_top_headlines_network_error(self, mock_get):
        """Test network error."""
        mock_get.side_effect = RequestException("Network error")

        with self.assertRaises(APIError):
            self.client.get_top_headlines("query")
