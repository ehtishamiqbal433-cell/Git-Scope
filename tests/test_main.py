import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "cli"))
import main

def test_main_module_load():
    assert main is not None
