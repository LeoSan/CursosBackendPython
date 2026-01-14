import os
import sys
import unittest
from pathlib import Path

# Add src to python path
src_path = Path(__file__).parent / "src"
sys.path.append(str(src_path))

# Mock env vars to prevent config errors during discovery
os.environ["GOOGLE_API_KEY"] = ""
os.environ["NEWSAPI_API_KEY"] = ""

if __name__ == "__main__":
    loader = unittest.TestLoader()
    start_dir = "tests"
    suite = loader.discover(start_dir)

    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    if not result.wasSuccessful():
        sys.exit(1)
