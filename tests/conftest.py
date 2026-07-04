"""Shared fixtures for Codemap tests."""

import tempfile
from pathlib import Path

import pytest


@pytest.fixture
def sample_project():
    """Create a temporary project directory with sample Python files."""
    with tempfile.TemporaryDirectory() as tmpdir:
        project_path = Path(tmpdir)

        # Create a simple Python project structure
        src_dir = project_path / "src"
        src_dir.mkdir()

        # Main module
        (src_dir / "__init__.py").write_text('"""Sample package."""\n')

        (src_dir / "main.py").write_text(
            '''"""Main entry point."""

from src.utils import helper


def main():
    """Run the application."""
    result = helper("test")
    print(result)


if __name__ == "__main__":
    main()
'''
        )

        (src_dir / "utils.py").write_text(
            '''"""Utility functions."""


def helper(value: str) -> str:
    """Process a value."""
    return f"processed: {value}"


def unused_function():
    """This function is never called (dead code)."""
    return "dead code"
'''
        )

        # Test file
        tests_dir = project_path / "tests"
        tests_dir.mkdir()
        (tests_dir / "__init__.py").write_text("")
        (tests_dir / "test_utils.py").write_text(
            '''"""Tests for utils module."""

from src.utils import helper


def test_helper():
    """Test helper function."""
    assert helper("input") == "processed: input"
'''
        )

        yield project_path


@pytest.fixture
def sample_dart_project():
    """Create a temporary Dart project structure."""
    with tempfile.TemporaryDirectory() as tmpdir:
        project_path = Path(tmpdir)

        lib_dir = project_path / "lib"
        lib_dir.mkdir()

        (lib_dir / "main.dart").write_text(
            '''void main() {
  print("Hello, world!");
}

class MyClass {
  int _counter = 0;
  
  void increment() {
    _counter++;
  }
  
  int get counter => _counter;
}
'''
        )

        yield project_path
