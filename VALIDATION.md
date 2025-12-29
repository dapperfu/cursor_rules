# MDC File Validation

This document describes the validation process for `.mdc` files to ensure compliance with the Cursor.sh specification.

## Specification Requirements

All `.mdc` files in this repository must meet the following requirements:

### 1. YAML Frontmatter

Each file must start with YAML frontmatter enclosed by `---` delimiters:

```yaml
---
description: Brief summary of the rule's purpose
globs: ["*.py", "**/*.py"]
alwaysApply: true
---
```

**Required Fields:**
- `description`: A non-empty string describing the rule's purpose
- `globs`: An array of file patterns using standard glob syntax
- `alwaysApply`: A boolean indicating if the rule should always be active

### 2. Formatting Requirements

- Opening `---` must be on the first line
- Closing `---` must follow the frontmatter
- A blank line must follow the closing `---`
- Markdown content must start with a `#` heading

### 3. Content Structure

- Markdown content must follow the frontmatter
- Content must start with a heading (`#`)

## Validation Script

The validation script `validate_mdc.py` checks all `.mdc` files against these requirements.

### Usage

```bash
python3 validate_mdc.py
```

### What It Checks

1. **File Structure:**
   - File starts with `---`
   - Contains closing `---`
   - Has blank line after frontmatter
   - Content starts with heading

2. **Frontmatter Validation:**
   - Valid YAML syntax
   - Contains `description` field (non-empty string)
   - Contains `globs` field (array/list)
   - Contains `alwaysApply` field (boolean)

3. **Content Validation:**
   - Has content after frontmatter
   - Content starts with `#` heading

## Validation Results

**Last Validation:** All 109 `.mdc` files validated successfully.

- **Total files checked:** 109
- **Valid files:** 109
- **Invalid files:** 0

All files in the repository meet the Cursor.sh `.mdc` file specification requirements.

## Files Validated

The validation script checks all `.mdc` files across these directories:

- `ai/` (8 files)
- `c/` (10 files)
- `c++/` (10 files)
- `cursor/` (9 files)
- `endpoints/` (3 files)
- `git/` (6 files)
- `html/` (11 files)
- `LaTeX/` (7 files)
- `makefile/` (3 files)
- `python/` (17 files)
- `requirements/` (3 files)
- `requirements-strictdoc/` (5 files)
- `rust/` (10 files)
- `safety/` (3 files)
- `strictdoc/` (2 files)
- `tools/` (1 file)
- Root level (3 files: `claude-commit-override.mdc`, `project-naming.mdc`, `workflow.mdc`)

## Running Validation

To validate all `.mdc` files:

```bash
python3 validate_mdc.py
```

The script will:
- Check all `.mdc` files recursively
- Report any validation errors
- Exit with code 0 if all files are valid, 1 if any files are invalid

## Integration

The validation script can be integrated into:

- **Pre-commit hooks:** Validate files before commits
- **CI/CD pipelines:** Ensure compliance in automated workflows
- **Manual validation:** Run when needed to verify compliance

## Example Output

```
MDC File Validation Report
============================================================
Total files checked: 109
Valid files: 109
Invalid files: 0
============================================================

✓ All files are valid!
```

