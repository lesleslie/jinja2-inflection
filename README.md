# jinja2-inflection

[![Code style: crackerjack](https://img.shields.io/badge/code%20style-crackerjack-000042)](https://github.com/lesleslie/crackerjack)
[![Python Versions](https://img.shields.io/pypi/pyversions/jinja2-inflection.svg)](https://pypi.org/project/jinja2-inflection/)

A Jinja2 extension that integrates the [inflection](https://github.com/jpvanhal/inflection) library's string transformation functions as template filters.

## Overview

`jinja2-inflection` is a Jinja2 extension that provides a set of filters for string transformation using the `inflection` library. This package allows you to easily manipulate strings in your Jinja2 templates by converting between different naming conventions, pluralizing words, and more.

### Key Features

- **String Transformation Filters**: Access a variety of filters that apply `inflection` functions to strings in templates.
- **Easy Integration**: Seamlessly add the extension to your Jinja2 environment, making the filters available in all templates.
- **Reusable Logic**: Encapsulate `inflection` functions as filters to promote code reuse and consistency across templates.
- **Parameter Support**: Filters support optional parameters for customized string transformations.

## Filters

The extension provides the following filters:

| Filter | Description | Example |
|--------|-------------|---------|
| `camelize` | Converts strings to CamelCase | `{{ 'product_category' \| camelize }}` → `ProductCategory` |
| `dasherize` | Replaces underscores with dashes | `{{ 'first_name' \| dasherize }}` → `first-name` |
| `humanize` | Makes text more human-readable | `{{ 'employee_salary' \| humanize }}` → `Employee salary` |
| `ordinal` | Returns the ordinal suffix for a number | `{{ 1 \| ordinal }}` → `st` |
| `ordinalize` | Turns a number into an ordinal string | `{{ 1 \| ordinalize }}` → `1st` |
| `parameterize` | Replaces special chars with hyphens | `{{ 'Donald E. Knuth' \| parameterize }}` → `donald-e-knuth` |
| `pluralize` | Returns the plural form of a word | `{{ 'octopus' \| pluralize }}` → `octopi` |
| `singularize` | Returns the singular form of a word | `{{ 'mice' \| singularize }}` → `mouse` |
| `tableize` | Creates a table name from a class name | `{{ 'UserAccount' \| tableize }}` → `user_accounts` |
| `titleize` | Capitalizes words in a string | `{{ 'api_responses' \| titleize }}` → `Api Responses` |
| `transliterate` | Replaces non-ASCII characters | `{{ 'café' \| transliterate }}` → `cafe` |
| `underscore` | Makes an underscored version | `{{ 'DeviceType' \| underscore }}` → `device_type` |

### Filters with Parameters

Some filters support optional parameters:

- **camelize**: `{{ 'product_category' | camelize(uppercase_first_letter=False) }}` → `productCategory`
- **parameterize**: `{{ 'Donald E. Knuth' | parameterize(separator='_') }}` → `donald_e_knuth`

## Installation

### Using pip

```bash
pip install jinja2-inflection
```

### Using uv

```bash
uv pip install jinja2-inflection
```

### Using Poetry

```bash
poetry add jinja2-inflection
```

### Using PDM

```bash
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
examples = [
    # Basic string transformations
    "{{ 'snake_case_string' | camelize }}",                      # Outputs: "SnakeCaseString"
    "{{ 'first_name' | dasherize }}",                            # Outputs: "first-name"
    "{{ 'employee_salary' | humanize }}",                        # Outputs: "Employee salary"
    "{{ 'DeviceType' | underscore }}",                           # Outputs: "device_type"

    # Number transformations
    "{{ 1 | ordinal }}",                                         # Outputs: "st"
    "{{ 2 | ordinalize }}",                                      # Outputs: "2nd"

    # Pluralization and singularization
    "{{ 'octopus' | pluralize }}",                               # Outputs: "octopi"
    "{{ 'mice' | singularize }}",                                # Outputs: "mouse"

    # Other transformations
    "{{ 'UserAccount' | tableize }}",                            # Outputs: "user_accounts"
    "{{ 'api_responses' | titleize }}",                          # Outputs: "Api Responses"
    "{{ 'café' | transliterate }}",                              # Outputs: "cafe"

    # Using parameters
    "{{ 'product_category' | camelize(uppercase_first_letter=False) }}", # Outputs: "productCategory"
    "{{ 'Donald E. Knuth' | parameterize(separator='_') }}",     # Outputs: "donald_e_knuth"
]

# Render and print each example
for example in examples:
    template = env.from_string(example)
    print(f"{example} → {template.render()}")
```

### Using with FastAPI

```python
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from jinja2_inflection import InflectionExtension

app = FastAPI()

# Configure Jinja2Templates with the extension
templates = Jinja2Templates(directory="templates")
templates.env.add_extension(InflectionExtension)

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "snake_case_var": "user_profile"}
    )
```

In your template (`templates/index.html`):
```html
<!DOCTYPE html>
<html>
<head>
    <title>FastAPI with jinja2-inflection</title>
</head>
<body>
    <h1>Variable in CamelCase: {{ snake_case_var | camelize }}</h1>
    <!-- Outputs: Variable in CamelCase: UserProfile -->
</body>
</html>
```

### Using with Starlette

```python
from starlette.applications import Starlette
from starlette.routing import Route
from starlette.templating import Jinja2Templates
from starlette.requests import Request
from jinja2_inflection import InflectionExtension

# Configure Jinja2Templates with the extension
templates = Jinja2Templates(directory="templates")
templates.env.add_extension(InflectionExtension)

async def homepage(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "table_name": "user_accounts"}
    )

routes = [
    Route("/", homepage)
]

app = Starlette(debug=True, routes=routes)
```

### Using with Flask

```python
from flask import Flask, render_template
from jinja2_inflection import InflectionExtension

app = Flask(__name__)
app.jinja_env.add_extension(InflectionExtension)

@app.route('/')
def index():
    return render_template('index.html')  # Now your templates can use inflection filters
```

### Using with Django

In your Django settings:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [...],
        'APP_DIRS': True,
        'OPTIONS': {
            'environment': 'myapp.jinja2.environment',
            ...
        },
    },
]
```

Then in `myapp/jinja2.py`:

```python
from jinja2 import Environment
from jinja2_inflection import InflectionExtension

def environment(**options):
    env = Environment(**options)
    env.add_extension(InflectionExtension)
    return env
```

## Requirements

- Python 3.13+
- Jinja2 3.1.6+
- inflection 0.5.1+

## License

BSD-3-Clause

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Acknowledgments

- This project uses the [inflection](https://github.com/jpvanhal/inflection) library to provide powerful string
transformation capabilities. Special thanks to the contributors of the inflection library for their work.
- Additionally, we acknowledge the [Jinja2](https://palletsprojects.com/p/jinja/)
project for providing a robust templating engine that makes this extension possible.
