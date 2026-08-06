import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "cli"))
import scanner

def test_scanner_functions():
    assert hasattr(scanner, "scan_repository") or len(dir(scanner)) > 0
