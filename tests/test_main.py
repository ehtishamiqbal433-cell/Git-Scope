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

def test_cli_install(tmp_path, monkeypatch):
    runner = CliRunner()
    # Change directory to temporary path so .git/hooks can be tested safely
    monkeypatch.chdir(tmp_path)
    git_dir = tmp_path / ".git" / "hooks"
    git_dir.mkdir(parents=True)

    result = runner.invoke(main.cli, ["install"])
    assert result.exit_code == 0
    assert "successfully installed" in result.output
    assert (git_dir / "pre-push").exists()
