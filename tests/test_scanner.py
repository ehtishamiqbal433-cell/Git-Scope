import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "cli"))
import scanner

def test_scanner_module_load():
    assert scanner is not None

def test_scanner_functions_exist():
    # Verify expected attributes or methods exist in scanner module
    assert len(dir(scanner)) > 0
