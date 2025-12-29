#!/usr/bin/env python3
"""
Validation script for .mdc files to ensure compliance with Cursor.sh specification.

This script validates that all .mdc files in the repository meet the required format:
- YAML frontmatter with description, globs, and alwaysApply fields
- Proper formatting with blank line after frontmatter
- Content starting with a heading
"""

import yaml
import sys
from pathlib import Path
from typing import List, Tuple, Dict, Any


class MDCValidationError(Exception):
    """Custom exception for MDC validation errors."""
    pass


def validate_mdc_file(file_path: Path) -> Tuple[bool, List[str]]:
    """
    Validate a single .mdc file against the Cursor.sh specification.

    Parameters
    ----------
    file_path : Path
        Path to the .mdc file to validate

    Returns
    -------
    Tuple[bool, List[str]]
        Tuple of (is_valid, list_of_errors)
    """
    errors: List[str] = []

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.splitlines(keepends=True)
    except Exception as e:
        return False, [f"Error reading file: {e}"]

    # Check file starts with ---
    if not content.startswith('---'):
        errors.append("File does not start with '---'")
        return False, errors

    # Split frontmatter from content
    parts = content.split('---', 2)
    if len(parts) < 3:
        errors.append("Missing closing '---' delimiter")
        return False, errors

    frontmatter_text = parts[1]
    content_after_frontmatter = parts[2]

    # Validate YAML frontmatter
    try:
        frontmatter_data = yaml.safe_load(frontmatter_text)
        if not isinstance(frontmatter_data, dict):
            errors.append("Frontmatter is not a dictionary")
            return False, errors
    except yaml.YAMLError as e:
        errors.append(f"YAML syntax error in frontmatter: {e}")
        return False, errors

    # Check required fields
    if 'description' not in frontmatter_data:
        errors.append("Missing required field: 'description'")
    elif not isinstance(frontmatter_data['description'], str):
        errors.append("Field 'description' must be a string")
    elif not frontmatter_data['description'].strip():
        errors.append("Field 'description' cannot be empty")

    if 'globs' not in frontmatter_data:
        errors.append("Missing required field: 'globs'")
    elif not isinstance(frontmatter_data['globs'], list):
        errors.append("Field 'globs' must be a list/array")

    if 'alwaysApply' not in frontmatter_data:
        errors.append("Missing required field: 'alwaysApply'")
    elif not isinstance(frontmatter_data['alwaysApply'], bool):
        errors.append("Field 'alwaysApply' must be a boolean")

    # Check formatting: blank line after frontmatter
    # Find the line after closing ---
    closing_dash_idx = None
    for i, line in enumerate(lines):
        if i > 0 and line.strip() == '---':
            closing_dash_idx = i
            break

    if closing_dash_idx is None:
        errors.append("Could not find closing '---' in file")
    else:
        # Check for blank line after closing ---
        if closing_dash_idx + 1 >= len(lines):
            errors.append("No content after frontmatter")
        else:
            next_line = lines[closing_dash_idx + 1]
            if next_line.strip() != '':
                errors.append(
                    f"Missing blank line after frontmatter "
                    f"(line {closing_dash_idx + 2} is not blank)"
                )

            # Check if content starts with heading
            if closing_dash_idx + 2 >= len(lines):
                errors.append("No content after blank line")
            else:
                first_content_line = lines[closing_dash_idx + 2]
                if not first_content_line.strip().startswith('#'):
                    errors.append(
                        f"Content does not start with heading '#' "
                        f"(line {closing_dash_idx + 3} starts with: "
                        f"{repr(first_content_line[:50])})"
                    )

    return len(errors) == 0, errors


def validate_all_mdc_files(root_dir: Path) -> Dict[str, Any]:
    """
    Validate all .mdc files in the repository.

    Parameters
    ----------
    root_dir : Path
        Root directory to search for .mdc files

    Returns
    -------
    Dict[str, Any]
        Dictionary with validation results including:
        - total_files: Total number of files checked
        - valid_files: Number of valid files
        - invalid_files: Number of invalid files
        - file_results: List of tuples (file_path, is_valid, errors)
    """
    mdc_files = sorted(root_dir.rglob('*.mdc'))
    results: List[Tuple[Path, bool, List[str]]] = []

    for mdc_file in mdc_files:
        is_valid, errors = validate_mdc_file(mdc_file)
        results.append((mdc_file, is_valid, errors))

    valid_count = sum(1 for _, is_valid, _ in results if is_valid)
    invalid_count = len(results) - valid_count

    return {
        'total_files': len(results),
        'valid_files': valid_count,
        'invalid_files': invalid_count,
        'file_results': results
    }


def main() -> int:
    """
    Main entry point for the validation script.

    Returns
    -------
    int
        Exit code: 0 if all files are valid, 1 if any files are invalid
    """
    root_dir = Path(__file__).parent
    results = validate_all_mdc_files(root_dir)

    print(f"MDC File Validation Report")
    print(f"{'=' * 60}")
    print(f"Total files checked: {results['total_files']}")
    print(f"Valid files: {results['valid_files']}")
    print(f"Invalid files: {results['invalid_files']}")
    print(f"{'=' * 60}\n")

    # Report invalid files
    invalid_files = [
        (path, errors) for path, is_valid, errors in results['file_results']
        if not is_valid
    ]

    if invalid_files:
        print("Files with validation errors:\n")
        for file_path, errors in invalid_files:
            rel_path = file_path.relative_to(root_dir)
            print(f"  {rel_path}:")
            for error in errors:
                print(f"    - {error}")
            print()
        return 1
    else:
        print("✓ All files are valid!")
        return 0


if __name__ == '__main__':
    sys.exit(main())

