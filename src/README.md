# t-strings Examples from PAO Charity Event 2025

This directory contains all the code examples from the t-strings presentation.

## Requirements

- Python 3.14+ (beta or later)
- uv (for managing Python versions)

## Setup

```bash
# Install Python 3.14 beta with uv
uv python install 3.14

# Create a virtual environment with Python 3.14
uv venv --python 3.14

# Activate the virtual environment
source .venv/bin/activate  # On Unix/macOS
# or
.venv\Scripts\activate  # On Windows
```

## Running Examples

Each file can be run independently:

```bash
python src/01_basics.py
python src/02_template_type.py
# ... etc
```

## File Structure

1. **01_basics.py** - Basic t-string syntax and Template objects
2. **02_template_type.py** - Template type structure (.strings and .interpolations)
3. **03_interpolation.py** - Interpolation type details
4. **04_evaluation.py** - Evaluation model and scoping
5. **05_api_overview.py** - Template API (iteration, values, concatenation)
6. **06_sql_example.py** - SQL injection prevention example
7. **07_html_example.py** - HTML escaping example
8. **08_logging.py** - Structured logging with templates
9. **09_use_cases.py** - Various use cases (email, config files)
10. **10_sublanguages.py** - Multi-line template examples

## Note on Libraries

Some examples include mock implementations of libraries that may not be available yet:
- `sql()` function (mimics sql-tstring)
- `html()` function (mimics tdom)
- Custom logging formatter

These are simplified versions to demonstrate the concepts.