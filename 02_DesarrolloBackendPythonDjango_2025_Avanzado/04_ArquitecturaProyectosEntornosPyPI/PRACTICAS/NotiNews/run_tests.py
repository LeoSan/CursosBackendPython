import sys
import unittest
import os
from pathlib import Path

# Add src to python path
src_path = Path(__file__).parent / "src"
sys.path.append(str(src_path))

# Mock env vars to prevent config errors during discovery
os.environ["GOOGLE_API_KEY"] = "AIzaSyDgvt951Qy1Lf5e-_O1Y5FwFkgVndZS9cQ"
os.environ["NEWSAPI_API_KEY"] = "fdaefbb239274dfc871349611971e9d9"

if __name__ == "__main__":
    loader = unittest.TestLoader()
    start_dir = "tests"
    suite = loader.discover(start_dir)

    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    
    if not result.wasSuccessful():
        sys.exit(1)
