import os
import sys

# Ensure repository root is on sys.path so tests can import top-level modules
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from main import main  # noqa: E402


def test_main_runs():
    assert main() is True
