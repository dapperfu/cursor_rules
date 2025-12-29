#!/usr/bin/env python3
"""Batch update cursor rules submodule across multiple projects.

This script scans a directory for projects that have .cursor/rules/ as a git
submodule and runs the cursor-rules script to update them.
"""

import subprocess
import sys
from pathlib import Path
from typing import List, Optional

import click


def is_git_repo(directory: Path) -> bool:
    """Check if a directory is a git repository.

    Parameters
    ----------
    directory : Path
        The directory to check.

    Returns
    -------
    bool
        True if the directory is a git repository, False otherwise.
    """
    git_dir = directory / ".git"
    return git_dir.exists() or git_dir.is_dir()


def has_cursor_rules_submodule(directory: Path) -> bool:
    """Check if a directory has .cursor/rules as a git submodule.

    Parameters
    ----------
    directory : Path
        The directory to check.

    Returns
    -------
    bool
        True if .cursor/rules exists and is a git submodule, False otherwise.
    """
    cursor_rules_path = directory / ".cursor" / "rules"
    
    if not cursor_rules_path.exists():
        return False
    
    # Use git command to check if it's a submodule
    try:
        result = subprocess.run(
            ["git", "submodule", "status", ".cursor/rules"],
            cwd=directory,
            capture_output=True,
            text=True,
            check=False,
        )
        # If exit code is 0, it's a submodule
        return result.returncode == 0
    except (FileNotFoundError, subprocess.SubprocessError):
        # Fallback: check .gitmodules file
        gitmodules_path = directory / ".gitmodules"
        if not gitmodules_path.exists():
            return False
        
        try:
            gitmodules_content = gitmodules_path.read_text()
            return ".cursor/rules" in gitmodules_content or "cursor/rules" in gitmodules_content
        except (OSError, IOError):
            return False


def find_cursor_rules_script() -> Optional[Path]:
    """Find the cursor-rules script in common locations.

    Returns
    -------
    Optional[Path]
        Path to the cursor-rules script if found, None otherwise.
    """
    # Check common locations
    locations = [
        Path.home() / ".local" / "bin" / "cursor-rules",
        Path("/usr/local/bin/cursor-rules"),
        Path("/usr/bin/cursor-rules"),
        Path("cursor-rules"),  # Current directory
    ]
    
    # Also check PATH
    try:
        result = subprocess.run(
            ["which", "cursor-rules"],
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode == 0:
            locations.insert(0, Path(result.stdout.strip()))
    except (FileNotFoundError, subprocess.SubprocessError):
        pass
    
    for location in locations:
        if location.exists() and location.is_file():
            return location
    
    return None


def run_cursor_rules(project_dir: Path, cursor_rules_script: Path, dry_run: bool) -> bool:
    """Run cursor-rules script in a project directory.

    Parameters
    ----------
    project_dir : Path
        The project directory to update.
    cursor_rules_script : Path
        Path to the cursor-rules script.
    dry_run : bool
        If True, only print what would be done without executing.

    Returns
    -------
    bool
        True if successful, False otherwise.
    """
    if dry_run:
        click.echo(f"  [DRY RUN] Would run: {cursor_rules_script} {project_dir}")
        return True
    
    try:
        result = subprocess.run(
            [str(cursor_rules_script), str(project_dir)],
            cwd=project_dir,
            capture_output=True,
            text=True,
            check=False,
        )
        
        if result.returncode == 0:
            click.echo(f"  ✓ Successfully updated {project_dir.name}")
            if result.stdout:
                click.echo(f"    {result.stdout.strip()}")
            return True
        else:
            click.echo(f"  ✗ Failed to update {project_dir.name}", err=True)
            if result.stderr:
                click.echo(f"    Error: {result.stderr.strip()}", err=True)
            return False
    except Exception as e:
        click.echo(f"  ✗ Error running cursor-rules: {e}", err=True)
        return False


@click.command()
@click.argument(
    "projects_dir",
    type=click.Path(exists=True, file_okay=False, dir_okay=True, path_type=Path),
    default=Path("/projects"),
)
@click.option(
    "--dry-run",
    is_flag=True,
    help="Show what would be done without actually running cursor-rules.",
)
@click.option(
    "--cursor-rules-path",
    type=click.Path(exists=True, file_okay=True, dir_okay=False, path_type=Path),
    default=None,
    help="Path to the cursor-rules script. If not provided, will search common locations.",
)
def main(
    projects_dir: Path,
    dry_run: bool,
    cursor_rules_path: Optional[Path],
) -> None:
    """Batch update cursor rules submodule across multiple projects.
    
    Scans the specified directory for projects that have .cursor/rules/ as a
    git submodule and runs the cursor-rules script to update them.
    
    Parameters
    ----------
    projects_dir : Path
        Directory containing multiple projects to scan.
    dry_run : bool
        If True, only show what would be done without executing.
    cursor_rules_path : Optional[Path]
        Path to the cursor-rules script. If None, will search for it.
    """
    click.echo(f"Scanning {projects_dir} for projects with cursor_rules submodule...")
    click.echo("")
    
    # Find cursor-rules script
    if cursor_rules_path is None:
        cursor_rules_path = find_cursor_rules_script()
        if cursor_rules_path is None:
            click.echo(
                "Error: cursor-rules script not found. Please install it or specify --cursor-rules-path",
                err=True,
            )
            sys.exit(1)
    
    click.echo(f"Using cursor-rules script: {cursor_rules_path}")
    click.echo("")
    
    # Find all projects with cursor_rules submodule
    projects: List[Path] = []
    
    try:
        for item in projects_dir.iterdir():
            if not item.is_dir():
                continue
            
            # Skip hidden directories
            if item.name.startswith("."):
                continue
            
            # Check if it's a git repo
            if not is_git_repo(item):
                continue
            
            # Check if it has cursor_rules submodule
            if has_cursor_rules_submodule(item):
                projects.append(item)
    except PermissionError as e:
        click.echo(f"Error: Permission denied accessing {projects_dir}: {e}", err=True)
        sys.exit(1)
    except Exception as e:
        click.echo(f"Error scanning directory: {e}", err=True)
        sys.exit(1)
    
    if not projects:
        click.echo("No projects with cursor_rules submodule found.")
        sys.exit(0)
    
    click.echo(f"Found {len(projects)} project(s) with cursor_rules submodule:")
    for project in projects:
        click.echo(f"  - {project.name}")
    click.echo("")
    
    if dry_run:
        click.echo("DRY RUN MODE - No changes will be made")
        click.echo("")
    
    # Update each project
    success_count = 0
    for project in projects:
        click.echo(f"Updating {project.name}...")
        if run_cursor_rules(project, cursor_rules_path, dry_run):
            success_count += 1
        click.echo("")
    
    # Summary
    click.echo("=" * 60)
    click.echo(f"Summary: {success_count}/{len(projects)} projects updated successfully")
    
    if success_count < len(projects):
        sys.exit(1)


if __name__ == "__main__":
    main()

