# Copilot Instructions for cursor_rules

## Project Overview

**cursor_rules** is a curated collection of atomic, reusable AI coding rules organized by category. Each rule is a single-purpose `.mdc` (Markdown with Code) file that encodes development practices, safety requirements, and language-specific conventions. The project serves as a submodule that developers can integrate into their own projects via `.cursor/rules/`.

## Architecture & Organization

### Rule Structure
- **Atomic design**: Each file contains exactly ONE focused requirement
- **File format**: `.mdc` files with YAML frontmatter + Markdown content
- **Frontmatter fields**: `description`, `globs` (file patterns), `alwaysApply` (boolean)
- **Location**: Organized in category folders (`python/`, `git/`, `ai/`, `safety/`, etc.)

### Category Reference
- **`safety/`** - Mandatory safety constraints (no sudo, no `rm -rf ~`, command-line safety)
- **`git/`** - Git workflows and commit message formatting with technical attribution
- **`python/`** - Python-specific practices (venv, typing, documentation, pyproject.toml)
- **`ai/`** - ML/AI workflows (training scripts, checkpointing, experiment tracking, model naming)
- **`makefile/`** - Makefile patterns (variable escaping, target dependencies)
- **`endpoints/`** - API/web service patterns (authentication, error handling, preferring real endpoints)
- **`requirements/`** - Doorstop requirements management (hierarchy, workflow)
- **`requirements-strictdoc/`** - StrictDoc MIL-STD-498 compliance (hierarchy, HTML output, pre-commit hooks)
- **`tools/`** - Tool-specific rules (mitmproxy debugging)
- **`workflow.mdc`** - General development workflow (cross-cutting concerns)

## Critical Patterns & Conventions

### Commit Message Format
Commits use a structured format with technical attribution:
```
Brief one-liner

- Change 1
- Change 2

-----
Prompt: {{prompt}}
Context: {{description}}

Technical details:
- Model: {{llm_model}}
- IDE: Cursor {{version}}
- Generation method: AI-assisted pair programming
- Code style: {{language_style}}
- Dependencies: {{key_deps}}
```

See `git/commit-format.mdc` for full specification.

### Rule File Creation Guidelines
When adding new rules:
1. Keep under 500 lines
2. Use requirements language: **SHALL** (mandatory), **SHALL NOT** (prohibited), **SHOULD** (recommended)
3. Provide concrete examples from real code patterns
4. Set appropriate `globs` patterns (empty for universal rules)
5. Set `alwaysApply: true` only for safety/workflow rules, `false` for language-specific
6. Reference related rules via file paths (e.g., "See `git/commit-format.mdc`")

### Selection by Project Type
Developers choose rule sets based on project needs:
- **All projects**: `safety/`, `git/`, `workflow.mdc`
- **Python projects**: Add `python/` category
- **ML projects**: Add `ai/` on top of `python/`
- **API projects**: Add `endpoints/`
- **Requirements management**: Choose **either** `requirements/` (doorstop) **or** `requirements-strictdoc/` (strictdoc)

### Python Requirements Language
Rules use consistent terminology across the codebase:
- **Requirements language** (SHALL/SHALL NOT/MUST/SHOULD) defined in README.md
- Applies to all documentation and rule specifications
- AI agents should mirror this language when discussing constraints

## Key Files for Reference

- **`README.md`** - Installation methods (submodule vs. direct clone), usage guidance, rule selection, organization structure
- **`git/commit-format.mdc`** - Exact commit message structure with attribution template
- **`python/venv-required.mdc`** - Python virtual environment enforcement (no system pip)
- **`ai/training-scripts.mdc`** - Rich dashboard requirements, shell wrappers, hyperparameter CLIs
- **`safety/no-home-rm.mdc`** - Home directory protection
- **`safety/no-sudo.mdc`** - Sudo prohibition

## Development Workflows

### Adding a New Rule
1. Create `.mdc` file in appropriate category folder
2. Write YAML frontmatter with `description`, `globs`, `alwaysApply`
3. Include concrete examples from the domain
4. Keep focused on one requirement
5. Commit with proper commit message format
6. Update `README.md` organization table if adding new rule category

### Testing/Verification
- Rules are loaded automatically by Cursor into `.cursor/rules/`
- No automated tests; validation is through real-world usage in Cursor
- AI agents should verify rules work by checking they appear in Cursor settings

### Integration Strategy
- Projects use rules as git submodules in `.cursor/rules/` directory
- Selective rule inclusion via symlinking or copying specific files
- Submodule updates: `cd .cursor/rules && git pull origin main`

## Important Constraints & Safety

1. **Never remove or modify core safety rules** (`safety/`)
2. **Commit message format is mandatory** - all commits must include technical attribution section
3. **Git user configuration required** - see `git/user-config.mdc`
4. **Python venv requirement** - never use system Python in rules targeting Python projects
5. **Two requirements systems** - projects choose **either** doorstop or strictdoc, not both (though they can coexist)

## When Modifying Existing Rules

- Preserve backward compatibility where possible
- Update `README.md` organization table if changing rule names/locations
- Ensure `globs` patterns still match intended file types
- Test that rule references (e.g., "See `git/commit-format.mdc`") still resolve correctly
- If splitting a rule into multiple rules, update references in other rules and README.md

## Question Clarification Points

When unsure about a change, consider:
- Does this require file pattern matching (`globs`)? If not, likely `alwaysApply: true`
- Is this universally applicable or category-specific?
- Does this depend on or relate to another rule? Reference it explicitly.
- Could this be split into smaller atomic rules?
- Do concrete examples from existing rules need updating?
