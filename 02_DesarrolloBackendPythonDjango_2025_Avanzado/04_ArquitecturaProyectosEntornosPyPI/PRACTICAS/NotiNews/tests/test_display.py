"""Tests for display."""

import unittest
from unittest.mock import patch

from noti_news.core.models import Article
from noti_news.io.display import display_answer, display_articles, display_error


class TestDisplay(unittest.TestCase):
    """Test display functions."""

    def setUp(self):
        """Set up test fixtures."""
        self.articles = [
            Article("Title 1", "Description 1", "http://example1.com"),
            Article("Title 2", "Description 2", "http://example2.com"),
        ]

    @patch("noti_news.io.display.console")
    def test_display_articles_with_articles(self, mock_console):
        """Test display_articles with articles."""
        display_articles(self.articles)
        mock_console.print.assert_called()

    @patch("noti_news.io.display.console")
    def test_display_articles_empty(self, mock_console):
        """Test display_articles with no articles."""
        display_articles([])
        mock_console.print.assert_called_with(
            "[yellow]No se encontraron artículos.[/yellow]"
        )

    @patch("noti_news.io.display.console")
    def test_display_answer(self, mock_console):
        """Test display_answer."""
        display_answer("Test answer")
        mock_console.print.assert_called_with(unittest.mock.ANY)

    @patch("noti_news.io.display.console")
    def test_display_error(self, mock_console):
        """Test display_error."""
        display_error("Test error")
        mock_console.print.assert_called_with("[bold red]Error:[/bold red] Test error")
