import pytest
import sys
from pathlib import Path

# Add cli directory to module search path
sys.path.insert(0, str(Path(__file__).parent.parent / "cli"))

import scanner

def test_scanner_module_exists():
    assert scanner is not None
