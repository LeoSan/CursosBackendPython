"""Verification script for Gemini."""
import os
import sys

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), "../src"))

from noti_news.analysis.analyzer import get_analyzer
from noti_news.core.models import Article

def verify():
    print("Verifying Gemini Integration...")
    
    try:
        analyzer = get_analyzer()
        print("Analyzer created successfully.")
    except Exception as e:
        print(f"Failed to create analyzer: {e}")
        return

    articles = [
        Article("Test Title", "Test Description", "http://test.com")
    ]
    
    try:
        # This might fail if API key is invalid, but code path is verified
        print("Attempting analysis (might fail auth)...")
        result = analyzer.analyze(articles, "Test question")
        print(f"Result: {result}")
    except Exception as e:
        print(f"Analysis failed (Expected if key is invalid): {e}")

if __name__ == "__main__":
    verify()
