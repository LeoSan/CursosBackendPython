"""Data models for Platzi News."""

from dataclasses import dataclass


@dataclass
class Article:
    """Represents a news article with its essential metadata.

    This class serves as a standard data transfer object (DTO) for news items
    across the application, ensuring consistency between different news sources.

    Attributes:
        title (str): The headline or main title of the news article.
        description (str): A brief summary, snippet, or lead paragraph of the article.
        url (str): The direct HTTP link to the full article on the source's website.
    """

    title: str
    description: str
    url: str
