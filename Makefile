# Makefile for t-strings presentation and examples

.PHONY: help setup test run-examples slides clean install

# Use uv to manage Python environment
UV := uv
PYTHON := $(UV) run python
PIP := $(UV) pip

help:
	@echo "Available commands:"
	@echo "  make setup        - Set up Python 3.14 environment with uv"
	@echo "  make install      - Install dependencies"
	@echo "  make test         - Run all unit tests"
	@echo "  make run-examples - Run all example files"
	@echo "  make slides       - Start slidev dev server"
	@echo "  make clean        - Clean up generated files"

setup:
	@echo "Setting up Python 3.14 environment with uv..."
	$(UV) python install 3.14
	$(UV) venv --python 3.14
	@echo "Environment created with uv"

install: setup
	@echo "Installing dependencies..."
	$(UV) sync
	@echo "Trying to install t-strings libraries (may not be available yet)..."
	-$(PIP) install tdom || echo "tdom not available yet"
	-$(PIP) install sql-tstring || echo "sql-tstring not available yet"

test: 
	@echo "Running unit tests with uv..."
	$(PYTHON) tests/test_all.py

run-examples:
	@echo "Running all examples with uv..."
	$(PYTHON) src/run_all.py

run-example:
	@echo "Running example: $(FILE)"
	$(PYTHON) src/$(FILE)

check:
	@echo "Checking t-strings availability..."
	$(PYTHON) src/check_tstrings.py

slides:
	@echo "Starting Slidev development server..."
	pnpm dev

clean:
	@echo "Cleaning up..."
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	rm -rf .venv

# Individual example shortcuts
basics:
	@$(MAKE) run-example FILE=01_basics.py

template:
	@$(MAKE) run-example FILE=02_template_type.py

interpolation:
	@$(MAKE) run-example FILE=03_interpolation.py

evaluation:
	@$(MAKE) run-example FILE=04_evaluation.py

api:
	@$(MAKE) run-example FILE=05_api_overview.py

sql:
	@$(MAKE) run-example FILE=06_sql_example.py

html:
	@$(MAKE) run-example FILE=07_html_example.py

logging:
	@$(MAKE) run-example FILE=08_logging.py

usecases:
	@$(MAKE) run-example FILE=09_use_cases.py

sublanguages:
	@$(MAKE) run-example FILE=10_sublanguages.py