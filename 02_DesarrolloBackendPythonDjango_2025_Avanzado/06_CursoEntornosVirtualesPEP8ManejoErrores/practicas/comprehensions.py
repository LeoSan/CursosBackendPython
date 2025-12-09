"""Ejemplos y explicaciones de comprehensions en Python."""

from sample_data import sample_articles


def extract_titles_traditional(articles):
    """Extrae solo los titulos usando un for"""
    titles = []
    for article in articles:
        if len(article["title"]) > 200:
            titles.append(article["title"])
    return titles


def extract_titles(articles):
    """Extrae solo los titulos usando un comprehension"""
    return [article["title"] for article in articles if len(article["title"]) > 200]


def extract_article_summaries(articles):
    return {
        article["title"]: article["description"]
        for article in articles
        if len(article["description"]) > 5
    }


print(extract_titles_traditional(sample_articles))
print("======")
print(extract_titles(sample_articles))
print(extract_article_summaries(sample_articles))


def get_sources_traditional(articles):
    sources = set()
    for article in articles:
        if article.get("source") and article.get("source").get("name"):
            sources.add(article.get("source").get("name"))
    return sources


def get_sources(articles):
    return {
        article.get("source").get("name")
        for article in articles
        if article.get("source") and article.get("source").get("name")
    }


def categorize_traditional(articles):
    sources = get_sources(articles)
    results = {}

    for source in sources:
        if source not in results:
            results[source] = []

        for article in articles:
            if source == article.get("source").get("name"):
                results[source].append(article)

    return results


def categorize(articles):
    sources = get_sources(articles)
    return {
        source: [
            article
            for article in articles
            if source == article.get("source").get("name")
        ]
        for source in sources
    }


print(categorize_traditional(sample_articles))
print("===")
print(categorize(sample_articles))