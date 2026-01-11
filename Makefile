.PHONY: install uninstall check clean build run help

# Variables
SCRIPT_NAME := cursor-rules
INSTALL_DIR := $$HOME/.local/bin
SCRIPT_PATH := $(CURDIR)/$(SCRIPT_NAME)
INSTALL_PATH := $(INSTALL_DIR)/$(SCRIPT_NAME)

# Shell configuration files
BASHRC := $$HOME/.bashrc
ZSHRC := $$HOME/.zshrc
FISH_CONFIG := $$HOME/.config/fish/config.fish

# PATH entry markers (to identify our additions)
BASH_PATH_LINE := export PATH="$$HOME/.local/bin:$$PATH"
ZSH_PATH_LINE := export PATH="$$HOME/.local/bin:$$PATH"
FISH_PATH_LINE := set -gx PATH "$$HOME/.local/bin" $$PATH

help: ## Display available targets and descriptions
	@echo "Available targets:"
	@echo "  make install    - Install cursor-rules to ~/.local/bin and add to PATH"
	@echo "  make uninstall  - Remove cursor-rules installation and PATH entries"
	@echo "  make check      - Validate and lint project files"
	@echo "  make clean      - Remove temporary files and build artifacts"
	@echo "  make build      - No-op for this interpreted project"
	@echo "  make run        - Show help message"
	@echo "  make help        - Display this help message"

install: ## Install cursor-rules script to ~/.local/bin and configure shell PATH
	@echo "Installing $(SCRIPT_NAME)..."
	@mkdir -p $(INSTALL_DIR)
	@cp $(SCRIPT_PATH) $(INSTALL_PATH)
	@chmod +x $(INSTALL_PATH)
	@echo "Script installed to $(INSTALL_PATH)"
	@$(MAKE) -f Makefile add-to-bashrc
	@$(MAKE) -f Makefile add-to-zshrc
	@$(MAKE) -f Makefile add-to-fish
	@echo ""
	@echo "Installation complete!"
	@echo "You may need to restart your shell or run: source $$HOME/.bashrc (or .zshrc)"

add-to-bashrc:
	@if [ -f $(BASHRC) ]; then \
		if ! grep -qF "$(BASH_PATH_LINE)" $(BASHRC); then \
			echo "" >> $(BASHRC); \
			echo "# Added by cursor-rules install" >> $(BASHRC); \
			echo "$(BASH_PATH_LINE)" >> $(BASHRC); \
			echo "Added PATH to $(BASHRC)"; \
		else \
			echo "PATH already in $(BASHRC)"; \
		fi; \
	else \
		echo "Creating $(BASHRC)"; \
		echo "# Added by cursor-rules install" > $(BASHRC); \
		echo "$(BASH_PATH_LINE)" >> $(BASHRC); \
	fi

add-to-zshrc:
	@if [ -f $(ZSHRC) ]; then \
		if ! grep -qF "$(ZSH_PATH_LINE)" $(ZSHRC); then \
			echo "" >> $(ZSHRC); \
			echo "# Added by cursor-rules install" >> $(ZSHRC); \
			echo "$(ZSH_PATH_LINE)" >> $(ZSHRC); \
			echo "Added PATH to $(ZSHRC)"; \
		else \
			echo "PATH already in $(ZSHRC)"; \
		fi; \
	fi

add-to-fish:
	@if [ -f $(FISH_CONFIG) ]; then \
		if ! grep -qF "$(FISH_PATH_LINE)" $(FISH_CONFIG); then \
			echo "" >> $(FISH_CONFIG); \
			echo "# Added by cursor-rules install" >> $(FISH_CONFIG); \
			echo "$(FISH_PATH_LINE)" >> $(FISH_CONFIG); \
			echo "Added PATH to $(FISH_CONFIG)"; \
		else \
			echo "PATH already in $(FISH_CONFIG)"; \
		fi; \
	fi

uninstall: ## Remove cursor-rules installation and PATH entries
	@echo "Uninstalling $(SCRIPT_NAME)..."
	@if [ -f $(INSTALL_PATH) ]; then \
		rm -f $(INSTALL_PATH); \
		echo "Removed $(INSTALL_PATH)"; \
	else \
		echo "$(INSTALL_PATH) not found"; \
	fi
	@$(MAKE) -f Makefile remove-from-bashrc
	@$(MAKE) -f Makefile remove-from-zshrc
	@$(MAKE) -f Makefile remove-from-fish
	@if [ -d $(INSTALL_DIR) ] && [ -z "$$(ls -A $(INSTALL_DIR) 2>/dev/null)" ]; then \
		rmdir $(INSTALL_DIR); \
		echo "Removed empty directory $(INSTALL_DIR)"; \
	fi
	@echo "Uninstallation complete!"

remove-from-bashrc:
	@if [ -f $(BASHRC) ]; then \
		if grep -qF "# Added by cursor-rules install" $(BASHRC); then \
			sed -i '/# Added by cursor-rules install/,+1d' $(BASHRC); \
			echo "Removed PATH from $(BASHRC)"; \
		else \
			echo "No cursor-rules entries found in $(BASHRC)"; \
		fi; \
	fi

remove-from-zshrc:
	@if [ -f $(ZSHRC) ]; then \
		if grep -qF "# Added by cursor-rules install" $(ZSHRC); then \
			sed -i '/# Added by cursor-rules install/,+1d' $(ZSHRC); \
			echo "Removed PATH from $(ZSHRC)"; \
		else \
			echo "No cursor-rules entries found in $(ZSHRC)"; \
		fi; \
	fi

remove-from-fish:
	@if [ -f $(FISH_CONFIG) ]; then \
		if grep -qF "# Added by cursor-rules install" $(FISH_CONFIG); then \
			sed -i '/# Added by cursor-rules install/,+1d' $(FISH_CONFIG); \
			echo "Removed PATH from $(FISH_CONFIG)"; \
		else \
			echo "No cursor-rules entries found in $(FISH_CONFIG)"; \
		fi; \
	fi

check: ## Validate and lint project files
	@echo "Running validation checks..."
	@echo ""
	@echo "1. Validating MDC files..."
	@python3 validate_mdc.py || (echo "MDC validation failed!" && exit 1)
	@echo ""
	@echo "2. Checking cursor-rules script with shellcheck..."
	@if command -v shellcheck >/dev/null 2>&1; then \
		shellcheck $(SCRIPT_PATH) || (echo "shellcheck failed!" && exit 1); \
		echo "shellcheck passed"; \
	else \
		echo "shellcheck not found, skipping..."; \
	fi
	@echo ""
	@echo "3. Checking Python files with ruff..."
	@if command -v ruff >/dev/null 2>&1; then \
		ruff check validate_mdc.py batch_update_cursor_rules.py || (echo "ruff check failed!" && exit 1); \
		echo "ruff check passed"; \
	else \
		echo "ruff not found, skipping..."; \
	fi
	@echo ""
	@echo "All checks passed!"

clean: ## Remove temporary files and build artifacts
	@echo "Cleaning temporary files..."
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete 2>/dev/null || true
	@find . -type f -name "*.pyo" -delete 2>/dev/null || true
	@find . -type f -name ".DS_Store" -delete 2>/dev/null || true
	@echo "Clean complete!"

build: ## No-op for this interpreted project
	@echo "This is an interpreted project. No build step required."

run: ## Show help message
	@echo "This project provides cursor rules for development."
	@echo "Run 'make help' to see available targets."
	@echo "Run 'make install' to install the cursor-rules script."
