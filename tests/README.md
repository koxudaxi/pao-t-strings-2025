# Unit Tests for t-strings Examples

This directory contains unit tests that verify the output of all example files.

## Running Tests

### Prerequisites

```bash
# Ensure Python 3.14 is installed and activated
uv python install 3.14
uv venv --python 3.14
source .venv/bin/activate
```

### Run All Tests

```bash
# From project root
python -m unittest discover tests

# Or run the test suite directly
python tests/test_all.py
```

### Run Individual Tests

```bash
# Test a specific example
python tests/test_01_basics.py
python tests/test_02_template_type.py
# ... etc
```

## Test Structure

Each test file:
1. Runs the corresponding example script as a subprocess
2. Captures the stdout output
3. Verifies that expected output is present
4. Checks for key sections and values

## What's Tested

- **test_01_basics.py** - Basic t-string syntax, Template type output
- **test_02_template_type.py** - Template structure, strings and interpolations
- **test_03_interpolation.py** - Interpolation attributes (value, expression, conversion, format_spec)
- **test_04_evaluation.py** - Eager evaluation, lexical scoping, complex expressions
- **test_05_api_overview.py** - Template iteration, .values property, concatenation
- **test_06_sql_example.py** - SQL injection prevention, parameterization
- **test_07_html_example.py** - XSS prevention, HTML escaping
- **test_08_logging.py** - Structured logging output, JSON format
- **test_09_use_cases.py** - Email templates, config files, f() function
- **test_10_sublanguages.py** - Multi-line SQL, HTML, GraphQL examples

## Notes

- Tests check for specific output strings to ensure examples are working correctly
- If Python 3.14 is not available, all tests will fail
- Tests use subprocess to run examples in isolation
- Output verification is based on expected strings and patterns