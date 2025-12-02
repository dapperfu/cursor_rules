# Cursor Rules

Cursor rules organized into atomic, focused, and actionable units.

## Installation

### Adding as a Git Submodule

To use these rules in your project, add this repository as a git submodule in your project's `.cursor/rules` directory:

```bash
# Navigate to your project root
cd /path/to/your/project

# Create .cursor directory if it doesn't exist
mkdir -p .cursor

# Add this repository as a submodule
git submodule add git@github.com:dapperfu/cursor_rules.git .cursor/rules

# Initialize and update submodules
git submodule update --init --recursive
```

### Updating the Submodule

To update to the latest rules in your project:

```bash
cd .cursor/rules
git pull origin main
cd ../..
git add .cursor/rules
git commit -m "Update cursor rules submodule"
```

### Cloning a Project with Submodules

If you're cloning a project that already uses this submodule:

```bash
git clone --recurse-submodules git@github.com:user/project.git
```

Or if you've already cloned without submodules:

```bash
git submodule update --init --recursive
```

## Usage

Once installed, Cursor will automatically load all `.mdc` files from `.cursor/rules/` and its subdirectories. Rules are applied based on their `globs` patterns and `alwaysApply` settings defined in each rule's frontmatter.

### Rule Selection by Project Type

Not all rules are relevant to every project. Here's guidance on which rule categories to use:

**Universal Rules (Recommended for all projects):**
- `safety/` - Safety rules (no sudo, no home directory deletion, command-line safety)
- `git/` - Git workflow and commit formatting rules
- `workflow.mdc` - General development workflow

**Python Projects:**
- `python/` - Python-specific rules (venv, typing, documentation, etc.)
- `makefile/` - If using Makefiles for Python project management

**AI/ML Projects:**
- `ai/` - Machine learning specific rules (training, checkpoints, experiment tracking, etc.)
- `python/` - Python rules (required for ML projects)
- `makefile/` - If using Makefiles for ML workflows

**API/Web Service Projects:**
- `endpoints/` - API endpoint development rules
- `python/` - If using Python for backend

**Requirements Management Projects:**
- `requirements/` - For projects using `doorstop` for requirements management
- `requirements-strictdoc/` - For projects using `strictdoc` with MIL-STD-498 standards

**Tool-Specific Rules:**
- `tools/mitmproxy-logs.mdc` - Only if using mitmproxy for network debugging

### Selective Rule Inclusion

You can selectively include only the rules you need by:

1. **Symlinking specific directories:**
   ```bash
   cd .cursor/rules
   # Remove all, then symlink only what you need
   rm -rf python ai endpoints
   ln -s ../cursor_rules/python python
   ln -s ../cursor_rules/git git
   ```

2. **Copying specific rule files:**
   ```bash
   # Copy only the rules you need
   cp cursor_rules/git/*.mdc .cursor/rules/
   cp cursor_rules/python/venv-*.mdc .cursor/rules/
   ```

3. **Using `.cursorignore`** (if supported by Cursor) to exclude specific rules

### Verifying Rules are Loaded

Cursor will automatically load rules from `.cursor/rules/`. You can verify rules are being applied by checking Cursor's settings or by observing rule behavior in AI-assisted coding sessions.

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
│   └── target-dependencies.mdc   # Target dependencies
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