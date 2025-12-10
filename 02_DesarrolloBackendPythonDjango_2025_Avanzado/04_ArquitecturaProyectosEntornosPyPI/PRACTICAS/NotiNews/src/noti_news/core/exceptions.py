"""Custom exceptions for the application."""

class NotiNewsError(Exception):
    """Base exception for the application."""
    pass

class APIError(NotiNewsError):
    """Raised when an API request fails."""
    pass

class AnalysisError(NotiNewsError):
    """Raised when analysis fails."""
    pass
