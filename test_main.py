# This is the test suite our ReplicatorAgent will run.
import sys
import os
import pytest

# Add the parent directory to the path so we can import 'main'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import add, buggy_subtract

def test_add():
    """This test will PASS."""
    assert add(2, 2) == 4

def test_buggy_subtract():
    """This test will FAIL, allowing our agent to validate the bug."""
    assert buggy_subtract(10, 5) == 5