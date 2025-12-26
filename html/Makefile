# Makefile for HTML formatting and linting
# Requires: HTML Tidy and W3C Validator

# Detect tools
TIDY := $(shell command -v tidy 2> /dev/null)
TIDY_NPM := $(shell command -v htmltidy 2> /dev/null)
VNU := $(shell command -v vnu 2> /dev/null)
VNU_JAR := $(shell command -v vnu.jar 2> /dev/null)

# HTML Tidy configuration
TIDY_OPTS := -i -m -w 80 --tidy-mark no --drop-empty-elements no --drop-proprietary-attributes no --indent-spaces 4

# HTML files to process
HTML_FILES := $(shell find . -name "*.html" -type f)

.PHONY: check-tools format lint check format-file lint-file help

help:
	@echo "HTML Makefile Targets:"
	@echo "  make format      - Format all HTML files using HTML Tidy"
	@echo "  make lint        - Validate all HTML files using W3C Validator"
	@echo "  make check       - Run both format and lint"
	@echo "  make format-file - Format a single HTML file (interactive)"
	@echo "  make lint-file   - Validate a single HTML file (interactive)"
	@echo "  make check-tools - Check if required tools are installed"

check-tools:
	@echo "Checking for required tools..."
	@if [ -z "$(TIDY)" ] && [ -z "$(TIDY_NPM)" ]; then \
		echo "ERROR: HTML Tidy not found."; \
		echo "Install with: sudo apt-get install tidy"; \
		echo "Or with npm: npm install -g htmltidy"; \
		exit 1; \
	fi
	@if [ -z "$(VNU)" ] && [ -z "$(VNU_JAR)" ]; then \
		echo "WARNING: W3C Validator (vnu) not found."; \
		echo "Install with: npm install -g vnu-jar"; \
		echo "Or download from: https://github.com/validator/validator/releases"; \
		echo "Linting will use online validator as fallback."; \
	fi
	@echo "Tools check complete."

format: check-tools
	@echo "Formatting HTML files..."
	@if [ -n "$(TIDY)" ]; then \
		for file in $(HTML_FILES); do \
			echo "Formatting $$file..."; \
			$(TIDY) $(TIDY_OPTS) "$$file" 2>/dev/null || true; \
		done; \
	elif [ -n "$(TIDY_NPM)" ]; then \
		for file in $(HTML_FILES); do \
			echo "Formatting $$file..."; \
			$(TIDY_NPM) -i -m -w 80 "$$file" || true; \
		done; \
	else \
		echo "ERROR: HTML Tidy not found. Run 'make check-tools' for installation instructions."; \
		exit 1; \
	fi
	@echo "Formatting complete."

lint: check-tools
	@echo "Validating HTML files..."
	@ERRORS=0; \
	if [ -n "$(VNU)" ]; then \
		for file in $(HTML_FILES); do \
			echo "Validating $$file..."; \
			if ! $(VNU) "$$file" 2>&1 | grep -q "The document validates"; then \
				echo "ERROR: $$file failed validation"; \
				$(VNU) "$$file"; \
				ERRORS=$$((ERRORS + 1)); \
			fi; \
		done; \
	elif [ -n "$(VNU_JAR)" ]; then \
		for file in $(HTML_FILES); do \
			echo "Validating $$file..."; \
			if ! java -jar $(VNU_JAR) "$$file" 2>&1 | grep -q "The document validates"; then \
				echo "ERROR: $$file failed validation"; \
				java -jar $(VNU_JAR) "$$file"; \
				ERRORS=$$((ERRORS + 1)); \
			fi; \
		done; \
	else \
		echo "WARNING: W3C Validator not found locally."; \
		echo "Using online validator (requires internet connection)..."; \
		for file in $(HTML_FILES); do \
			echo "Validating $$file..."; \
			if ! curl -s -F "out=json" -F "content=@$$file" https://validator.w3.org/nu/ | grep -q '"type":"error"'; then \
				echo "ERROR: $$file failed validation"; \
				ERRORS=$$((ERRORS + 1)); \
			fi; \
		done; \
	fi; \
	if [ $$ERRORS -gt 0 ]; then \
		echo "Validation failed with $$ERRORS error(s)."; \
		exit 1; \
	else \
		echo "All HTML files validated successfully."; \
	fi

check: format lint
	@echo "Formatting and linting complete."

format-file: check-tools
	@read -p "Enter HTML file path: " file; \
	if [ -n "$(TIDY)" ]; then \
		$(TIDY) $(TIDY_OPTS) "$$file" 2>/dev/null || true; \
	elif [ -n "$(TIDY_NPM)" ]; then \
		$(TIDY_NPM) -i -m -w 80 "$$file" || true; \
	else \
		echo "ERROR: HTML Tidy not found."; \
		exit 1; \
	fi

lint-file: check-tools
	@read -p "Enter HTML file path: " file; \
	if [ -n "$(VNU)" ]; then \
		$(VNU) "$$file"; \
	elif [ -n "$(VNU_JAR)" ]; then \
		java -jar $(VNU_JAR) "$$file"; \
	else \
		echo "Validating $$file using online validator..."; \
		curl -F "out=json" -F "content=@$$file" https://validator.w3.org/nu/; \
	fi




