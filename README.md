# Cursor Rules

Cursor rules organized into atomic, focused, and actionable units.

## Organization

Rules are organized into category folders, with each rule file containing a single, atomic requirement:

```
/projects/cursor_rules/
├── README.md
├── git/
│   ├── user-config.mdc          # Git user configuration
│   ├── commit-format.mdc         # Commit message format
│   ├── push-requirement.mdc      # Push after commit
│   └── upstream-sync.mdc         # Upstream sync workflow
├── makefile/
│   ├── variable-escaping.mdc     # Variable escaping
│   ├── target-dependencies.mdc   # Target dependencies
│   └── phony-venv.mdc            # .PHONY exclusion
├── python/
│   ├── venv-required.mdc         # Virtual environment requirement
│   ├── venv-naming.mdc            # Venv naming convention
│   ├── venv-paths.mdc             # Venv paths in Makefiles
│   ├── typing.mdc                 # Mypy typing
│   ├── documentation.mdc          # NumPy docstrings
│   ├── pyproject-toml.mdc          # pyproject.toml requirement
│   ├── python-version.mdc         # Python 3.10+ and modern practices
│   ├── click-required.mdc          # Click library requirement for CLI projects
│   └── click-completions.mdc       # Click CLI shell completions (bash/zsh/fish)
├── ai/
│   ├── training-scripts.mdc       # Training scripts and shell wrappers
│   ├── makefile-integration.mdc   # Makefile targets for ML workflows
│   ├── model-naming.mdc           # Model naming conventions
│   ├── checkpoints-resume.mdc     # Checkpointing and resume
│   ├── experiment-tracking.mdc    # Experiment logging and tracking
│   ├── data-versioning.mdc        # Data versioning and reproducibility
│   ├── model-evaluation.mdc       # Model evaluation scripts
│   └── config-management.mdc      # Configuration file management
├── safety/
│   ├── no-home-rm.mdc             # Home directory protection
│   ├── no-sudo.mdc                # Sudo prohibition
│   └── command-line.mdc           # Command line safety
├── tools/
│   └── mitmproxy-logs.mdc         # Mitmproxy log handling
├── endpoints/
│   ├── prefer-real.mdc            # Real endpoints over mocks
│   ├── authentication.mdc         # Authentication handling
│   └── error-handling.mdc         # Error handling
├── requirements/
│   ├── hierarchy.mdc              # Document hierarchy
│   ├── workflow.mdc               # Workflow commands
│   └── practices.mdc              # Best practices
├── requirements-strictdoc/
│   ├── hierarchy.mdc              # MIL-STD-498 document hierarchy
│   ├── workflow.mdc               # StrictDoc workflow and make targets
│   ├── pre-commit-generation.mdc  # Pre-commit HTML generation
│   ├── html-output.mdc            # HTML output directory structure
│   └── practices.mdc              # StrictDoc best practices
└── workflow.mdc                    # General workflow
```

## Rule Quality Standards

All rules:
- Are focused, actionable, and scoped
- Are under 500 lines
- Are composable (split large rules into multiple rules)
- Provide concrete examples or referenced files
- Avoid vague guidance (written like clear internal docs)
- Are reusable when repeating prompts in chat

## File-Specific Application

Rules use globs patterns in frontmatter to apply only to relevant files:
- Python rules apply to `*.py` files
- Makefile rules apply to `Makefile` and `makefile` files
- AI/ML rules apply to ML-related files (`*.py`, `*.sh`, config files, Makefiles)
- Safety and git rules apply to all files (universal requirements)
- Tool rules apply to specific file types (e.g., `*.log` for mitmproxy)
- Endpoint rules apply to test and API files
- Requirements rules apply to requirements documentation files
- StrictDoc rules apply to `.sdoc` files and StrictDoc-related operations

This ensures rules like NumPy documentation requirements only apply to Python files, not MATLAB files.

## Requirements Management Tool Selection

Two requirements management systems are available:
- **doorstop**: Rules in `requirements/` folder
- **strictdoc**: Rules in `requirements-strictdoc/` folder

Users SHALL choose which system to use by including the appropriate rules in their `.cursor/rules` directory. Both systems can coexist, but typically only one is used per project.

## Requirements Language

All rules use requirements language:
- **SHALL** - Mandatory requirement
- **SHALL NOT** - Prohibited action
- **MUST** - Required for correctness
- **SHOULD** - Recommended but not mandatory