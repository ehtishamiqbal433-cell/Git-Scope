import pytest
import sys
from pathlib import Path
from click.testing import CliRunner

sys.path.insert(0, str(Path(__file__).parent.parent / "cli"))
import main

def test_main_module_load():
    assert main is not None

def test_cli_help():
    runner = CliRunner()
    result = runner.invoke(main.cli, ["--help"])
    assert result.exit_code == 0
    assert "Git-Scope" in result.output
