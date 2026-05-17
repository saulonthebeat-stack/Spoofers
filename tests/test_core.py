"""Tests for the core module."""

import pytest
from spoofers.core import main


class TestCore:
    """Test cases for core functionality."""

    def test_main_function(self):
        """Test that main function runs successfully."""
        result = main()
        assert result is True

    def test_main_returns_bool(self):
        """Test that main returns a boolean."""
        result = main()
        assert isinstance(result, bool)