import os
import subprocess
import sys
import click
from scanner import scan_file

@click.group()
def cli():
    """Git-Scope: Local Pre-Push AST Taint Interceptor"""
    pass

@cli.command()
def install():
    """Install Git-Scope as a local git pre-push hook"""
    hook_path = ".git/hooks/pre-push"
    hook_content = """#!/bin/sh
# Git-Scope Pre-Push Hook Interceptor
python3 cli/main.py scan --staged
"""
    with open(hook_path, "w") as hook_file:
        hook_file.write(hook_content)
    os.chmod(hook_path, 0o755)
    click.echo("[+] Git-Scope pre-push hook successfully installed.")

@cli.command()
@click.option('--staged', is_flag=True, help="Scan staged files or files about to be pushed")
def scan(staged):
    """Run AST taint analysis on modified files"""
    result = subprocess.run(["git", "diff", "--cached", "--name-only"], capture_output=True, text=True)
    files = result.stdout.splitlines()
    
    failed = False
    for file in files:
        if file.endswith(".py"):
            click.echo(f"Scanning {file} via AST Taint Engine...")
            violations = scan_file(file)
            if violations:
                failed = True

    if failed:
        click.echo("\n[ERROR] Git-Scope blocked push due to detected secrets or taint violations.")
        sys.exit(1)
    click.echo("[SUCCESS] All files passed AST security checks.")
    sys.exit(0)

if __name__ == "__main__":
    cli()
