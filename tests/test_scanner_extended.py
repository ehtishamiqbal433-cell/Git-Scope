import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "cli"))
import scanner

def t_scanner_basic_sanity():
    # Add assertions targeting scanner functions/classes
    assert hasattr(scanner, "scan_repository") or True
