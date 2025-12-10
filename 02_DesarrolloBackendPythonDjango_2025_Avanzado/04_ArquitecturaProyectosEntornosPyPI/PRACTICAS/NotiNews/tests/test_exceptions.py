"""Tests for exceptions."""

import unittest
from noti_news.core.exceptions import NotiNewsError, APIError, AnalysisError

class TestExceptions(unittest.TestCase):
    """Test custom exceptions."""

    def test_exception_inheritance(self):
        """Test exceptions inherit from NotiNewsError."""
        self.assertTrue(issubclass(APIError, NotiNewsError))
        self.assertTrue(issubclass(AnalysisError, NotiNewsError))
        self.assertTrue(issubclass(NotiNewsError, Exception))
