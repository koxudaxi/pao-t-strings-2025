# t-strings: Template Strings in Python 3.14

A presentation about PEP 750 (Template Strings) for the PAO (Python Asia Organization) Charity Event 2025.

## 🎯 Overview

This repository contains:
1. **Slidev Presentation** - A 30-minute talk about t-strings in Python 3.14
2. **Example Code** - Runnable examples of all t-string features shown in the presentation

## 📊 Presentation

The presentation covers:
- Motivation for t-strings (security, structured text)
- How t-strings work (Template and Interpolation types)
- Real-world examples (SQL, HTML, logging)
- Building the future (ecosystem and community)

### Running the Presentation

```bash
# Install dependencies
pnpm install

# Start dev server
pnpm dev

# Build for production
pnpm build
```

## 💻 Example Code

The `/src/` directory contains 10 example files demonstrating t-string features:

### Setup Python 3.14 with uv

```bash
# Install dependencies and set up environment
make install

# Or manually:
uv python install 3.14
uv venv --python 3.14
uv sync
```

### Run Examples with uv

```bash
# Check if t-strings are available
make check

# Run all examples
make run-examples

# Run individual examples
make basics         # Run 01_basics.py
make template       # Run 02_template_type.py
make interpolation  # Run 03_interpolation.py
make evaluation     # Run 04_evaluation.py
make api           # Run 05_api_overview.py
make sql           # Run 06_sql_example.py
make html          # Run 07_html_example.py
make logging       # Run 08_logging.py
make usecases      # Run 09_use_cases.py
make sublanguages  # Run 10_sublanguages.py

# Or directly with uv
uv run python src/01_basics.py
```

### Run Tests

```bash
# Run all unit tests with uv
make test

# Or directly
uv run python tests/test_all.py
```

### Using Make Commands

```bash
make help         # Show all available commands
make setup        # Set up Python 3.14 environment
make install      # Install dependencies with uv
make test         # Run all unit tests
make run-examples # Run all example files
make check        # Check t-strings availability
make slides       # Start slidev dev server
make clean        # Clean up generated files
```

### Example Contents

1. **01_basics.py** - Introduction to t-string syntax
2. **02_template_type.py** - Understanding Template objects
3. **03_interpolation.py** - Interpolation type details
4. **04_evaluation.py** - Eager evaluation and scoping
5. **05_api_overview.py** - Template API (iteration, concatenation)
6. **06_sql_example.py** - Preventing SQL injection
7. **07_html_example.py** - Safe HTML generation
8. **08_logging.py** - Structured logging
9. **09_use_cases.py** - Email templates, config files
10. **10_sublanguages.py** - Multi-line SQL, HTML, etc.

## 🔗 Resources

- **PEP 750**: [Template Strings](https://peps.python.org/pep-0750/)
- **Official Help**: [t-strings.help](https://t-strings.help/)
- **Language Hints Discussion**: [discuss.python.org/t/94311](https://discuss.python.org/t/language-hints-for-pep-750-template-strings/94311)
- **t-linter**: [VSCode](https://github.com/koxudaxi/t-linter) | [PyCharm](https://github.com/koxudaxi/t-linter-pycharm-plugin)
- **Libraries**: [sql-tstring](https://github.com/pgjones/sql-tstring) | [tdom](https://github.com/t-strings/tdom)
- **Awesome List**: [awesome-t-strings](https://github.com/t-strings/awesome-t-strings)

## 👤 Author

**Koudai Aono** (@koxudaxi)
- Co-author of PEP 750
- Creator of t-linter (VSCode/PyCharm plugins)
- OSS Developer at Mirascope

## 📄 License

MIT License