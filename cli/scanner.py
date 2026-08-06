import os
from pathlib import Path

def scan_repository(target_path: str = ".") -> dict:
    """
    Scans the target directory for files and returns basic statistics.
    """
    path = Path(target_path)
    if not path.exists():
        raise FileNotFoundError(f"Path not found: {target_path}")
    
    files = [f for f in path.rglob("*") if f.is_file() and ".git" not in f.parts]
    return {
        "target": str(path.absolute()),
        "total_files": len(files),
        "file_list": [str(f.relative_to(path)) for f in files]
    }

def scan_file(file_path: str) -> dict:
    """
    Scans a single file and returns metadata and basic analysis.
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    return {
        "file": str(path.absolute()),
        "size_bytes": path.stat().st_size,
        "status": "scanned"
    }
