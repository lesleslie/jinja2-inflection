# Project Context: jinja2-inflection

## Project Overview

This is a Python package that provides a Jinja2 extension integrating the inflection library's string transformation functions as template filters. It allows users to easily manipulate strings in Jinja2 templates by converting between different naming conventions, pluralizing words, and more.

Key technologies:

- Python 3.13+
- Jinja2 templating engine
- inflection library for string transformations
- Modern Python packaging with pyproject.toml

## Project Structure

```
jinja2-inflection/
├── jinja2_inflection/          # Main package source
│   └── __init__.py             # Main extension implementation
├── tests/                      # Unit tests
│   └── test_init.py            # Test cases for the extension
├── README.md                   # Project documentation
├── pyproject.toml              # Project configuration and dependencies
├── LICENSE                     # BSD-3-Clause license
└── .pre-commit-config.yaml     # Pre-commit hooks configuration
```

## Core Functionality

The package provides a Jinja2 extension that adds the following filters to templates:

| Filter | Description | Example |
|--------|-------------|---------|
| `camelize` | Converts strings to CamelCase | `{{ 'product_category' | camelize }}` → `ProductCategory` |
| `dasherize` | Replaces underscores with dashes | `{{ 'first_name' | dasherize }}` → `first-name` |
| `humanize` | Makes text more human-readable | `{{ 'employee_salary' | humanize }}` → `Employee salary` |
| `ordinal` | Returns the ordinal suffix for a number | `{{ 1 | ordinal }}` → `st` |
| `ordinalize` | Turns a number into an ordinal string | `{{ 1 | ordinalize }}` → `1st` |
| `parameterize` | Replaces special chars with hyphens | `{{ 'Donald E. Knuth' | parameterize }}` → `donald-e-knuth` |
| `pluralize` | Returns the plural form of a word | `{{ 'octopus' | pluralize }}` → `octopi` |
| `singularize` | Returns the singular form of a word | `{{ 'mice' | singularize }}` → `mouse` |
| `tableize` | Creates a table name from a class name | `{{ 'UserAccount' | tableize }}` → `user_accounts` |
| `titleize` | Capitalizes words in a string | `{{ 'api_responses' | titleize }}` → `Api Responses` |
| `transliterate` | Replaces non-ASCII characters | `{{ 'café' | transliterate }}` → `cafe` |
| `underscore` | Makes an underscored version | `{{ 'DeviceType' | underscore }}` → `device_type` |

Some filters support optional parameters:

- `camelize`: `{{ 'product_category' | camelize(uppercase_first_letter=False) }}` → `productCategory`
- `parameterize`: `{{ 'Donald E. Knuth' | parameterize(separator='_') }}` → `donald_e_knuth`

## Installation

```bash
pip install jinja2-inflection
# or
uv pip install jinja2-inflection
# or
poetry add jinja2-inflection
# or
pdm add jinja2-inflection
```

## Usage

### Basic Usage

```python
from jinja2 import Environment
from jinja2_inflection import InflectionExtension

# Set up Jinja2 environment with the extension
env = Environment(extensions=[InflectionExtension])

# Use filters in templates
template = env.from_string("{{ 'snake_case_string' | camelize }}")
result = template.render()  # Returns: "SnakeCaseString"
```

### Framework Integration

#### FastAPI

```python
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from jinja2_inflection import InflectionExtension

app = FastAPI()
templates = Jinja2Templates(directory="templates")
templates.env.add_extension(InflectionExtension)
```

#### Flask

```python
from flask import Flask
from jinja2_inflection import InflectionExtension

app = Flask(__name__)
app.jinja_env.add_extension(InflectionExtension)
```

## Development Workflow

### Build System

- Uses `hatchling` as the build backend
- Configured in `pyproject.toml`

### Code Quality Tools

The project uses a comprehensive set of pre-commit hooks:

- `ruff` for linting and formatting
- `black` for code formatting
- `pyright` for type checking
- `bandit` for security analysis
- `vulture` for dead code detection
- `codespell` for spell checking
- `refurb` for code improvements

### Testing

- Uses pytest for testing
- Tests are located in the `tests/` directory
- Coverage reporting is enabled

### Dependencies

Main dependencies:

- `inflection>=0.5.1`
- `jinja2>=3.1.6`

Development dependencies are managed via `dependency-groups.dev` in pyproject.toml.

## Commands

### Testing

```bash
pytest  # Run tests
```

### Code Quality

```bash
pre-commit run --all-files  # Run all pre-commit hooks
ruff check .  # Linting
ruff format .  # Formatting
pyright .  # Type checking
```

### Building

```bash
# Building is handled by hatchling via pyproject.toml configuration
```

## Contributing

1. Fork the repository
1. Create your feature branch (`git checkout -b feature/amazing-feature`)
1. Commit your changes (`git commit -m 'Add some amazing feature'`)
1. Push to the branch (`git push origin feature/amazing-feature`)
1. Open a Pull Request
