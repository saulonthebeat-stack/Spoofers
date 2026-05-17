"""
Tests for the core module.
"""

import pytest
from spoofers.core import main


class TestCore:
    """Test cases for core module."""

    def test_main_runs_without_error(self, capsys):
        """Test that main function runs without errors."""
        main()
        captured = capsys.readouterr()
        assert "Welcome to Spoofers" in captured.out

    def test_main_output_contains_version(self, capsys):
        """Test that main output contains version info."""
        main()
        captured = capsys.readouterr()
        assert "v0.1.0" in captured.out
