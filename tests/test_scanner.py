import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "cli"))
import scanner

def test_scan_repository_valid(tmp_path):
    # Create dummy files in a temporary directory
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "hello.txt"
    p.write_text("hello world")

    result = scanner.scan_repository(str(tmp_path))
    assert result["total_files"] == 1
    assert "sub/hello.txt" in result["file_list"]

def test_scan_repository_invalid_path():
    with pytest.raises(FileNotFoundError):
        scanner.scan_repository("non_existent_path_12345")
