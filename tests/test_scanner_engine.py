import pytest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent / "cli"))
from scanner import scan_file

def test_scan_file_result(tmp_path):
    test_file = tmp_path / "sample.py"
    test_file.write_text("print('test')\n")
    result = scan_file(str(test_file))
    assert isinstance(result, dict)
    assert result["status"] == "scanned"
    assert result["file"] == str(test_file)
