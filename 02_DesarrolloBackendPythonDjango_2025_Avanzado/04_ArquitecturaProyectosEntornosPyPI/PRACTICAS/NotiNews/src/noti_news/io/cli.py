"""Command Line Interface."""

import sys
import argparse
import logging
from typing import Optional

from noti_news.core.services import NewsService
from noti_news.core.exceptions import NotiNewsError
from noti_news.io.display import display_articles, display_answer, display_error

# Configure logging
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="NotiNews CLI")

    # Global options
    parser.add_argument(
        "--log-level",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        default="ERROR",
        help="Set logging level",
    )

    subparsers = parser.add_subparsers(dest="command", help="Commands")

    # Search command
    search_parser = subparsers.add_parser("search", help="Search for news")
    search_parser.add_argument("query", help="Search query")

    # Ask command
    ask_parser = subparsers.add_parser("ask", help="Ask a question about news")
    ask_parser.add_argument("query", help="Topic to search for")
    ask_parser.add_argument("question", help="Question to ask")

    return parser.parse_args()


def main():
    """Main entry point."""
    args = parse_args()

    # Configure logging level
    if args.log_level:
        logging.getLogger().setLevel(getattr(logging, args.log_level))

    if not args.command:
        # Show help if no command provided
        from unittest.mock import patch  # Hack to print help

        # Actually just exit
        # parser.print_help() # Parser is local
        print("Usage: noti-news [search|ask] ...")
        sys.exit(1)

    try:
        service = NewsService()

        if args.command == "search":
            logger.info(f"Searching for: {args.query}")
            articles = service.get_articles(args.query)
            display_articles(articles)

        elif args.command == "ask":
            logger.info(f"Asking about: {args.query}")
            articles = service.get_articles(args.query)
            # Display context first
            display_articles(articles)

            print("\nAnalizando con IA...\n")
            answer = service.analyze_articles(articles, args.question)
            display_answer(answer)

    except NotiNewsError as e:
        logger.error(f"Application error: {e}")
        display_error(str(e))
        sys.exit(1)
    except Exception as e:
        logger.exception("Unexpected error")
        display_error(f"Unexpected error: {e}")
        sys.exit(1)
