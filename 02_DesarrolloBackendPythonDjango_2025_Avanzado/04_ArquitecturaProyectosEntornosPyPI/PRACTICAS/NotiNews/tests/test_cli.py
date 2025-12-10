"""Tests for CLI."""

import unittest
from unittest.mock import MagicMock, patch

from noti_news.core.exceptions import NotiNewsError
from noti_news.io.cli import main


class TestCLI(unittest.TestCase):
    """Test CLI functions."""

    @patch("noti_news.io.cli.NewsService")
    @patch("sys.exit")
    def test_main_search_command(self, mock_exit, mock_service_class):
        """Test search command execution."""
        mock_service = MagicMock()
        mock_service.get_articles.return_value = []
        mock_service_class.return_value = mock_service

        # Mock args
        with patch("sys.argv", ["noti-news", "search", "test"]):
            main()

        mock_service.get_articles.assert_called_with("test")

    @patch("noti_news.io.cli.NewsService")
    @patch("sys.exit")
    def test_main_ask_command(self, mock_exit, mock_service_class):
        """Test ask command execution."""
        mock_service = MagicMock()
        mock_service.get_articles.return_value = []
        mock_service.analyze_articles.return_value = "Answer"
        mock_service_class.return_value = mock_service

        with patch("sys.argv", ["noti-news", "ask", "test", "question"]):
            main()

        mock_service.get_articles.assert_called_with("test")
        mock_service.analyze_articles.assert_called()

    @patch("noti_news.io.cli.NewsService")
    @patch("sys.exit")
    def test_main_no_args(self, mock_exit, mock_service_class):
        """Test execution with no args."""
        with patch("sys.argv", ["noti-news"]):
            main()
        mock_exit.assert_called_with(1)

    @patch("noti_news.io.cli.NewsService")
    @patch("sys.exit")
    def test_main_error_handling(self, mock_exit, mock_service_class):
        """Test application error handling."""
        mock_service = MagicMock()
        mock_service.get_articles.side_effect = NotiNewsError("Test error")
        mock_service_class.return_value = mock_service

        with patch("sys.argv", ["noti-news", "search", "test"]):
            main()

        mock_exit.assert_called_with(1)
