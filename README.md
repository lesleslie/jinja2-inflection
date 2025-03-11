# jinja2-inflection

[![Code style: crackerjack](https://img.shields.io/badge/code%20style-crackerjack-000042)](https://github.com/lesleslie/crackerjack)

A Jinja2 extension that integrates the [inflection](https://github.com/jpvanhal/inflection) library's string transformation functions as template filters.

## Overview

`jinja2-inflection` is a Jinja2 extension that provides a set of filters for string transformation using the `inflection` library. This package allows you to easily manipulate strings in your Jinja2 templates by converting between different naming conventions, pluralizing words, and more.

### Key Features

- **String Transformation Filters**: Access a variety of filters that apply `inflection` functions to strings in templates.
- **Easy Integration**: Seamlessly add the extension to your Jinja2 environment, making the filters available in all templates.
- **Reusable Logic**: Encapsulate `inflection` functions as filters to promote code reuse and consistency across templates.

## Filters

The extension provides the following filters:

- `camelize`: Converts strings to CamelCase.
- `dasherize`: Replaces underscores with dashes.
- `humanize`: Makes text more human-readable.
- `ordinal`: Returns the ordinal suffix for a number.
- `ordinalize`: Turns a number into an ordinal string.
- `parameterize`: Replaces special chars with hyphens.
- `pluralize`: Returns the plural form of a word.
- `singularize`: Returns the singular form of a word.
- `tableize`: Creates a table name from a class name.
- `titleize`: Capitalizes words in a string.
- `transliterate`: Replaces non-ASCII characters.
- `underscore`: Makes an underscored version.

## Installation

Install via pip:

```
pip install jinja2-inflection
```

## Usage

```
from jinja2 import Environment
from jinja2_inflection import InflectionExtension

# Set up Jinja2 environment with the extension
env = Environment(extensions=[InflectionExtension])

# Use filters in templates
template = env.from_string("{{ 'snake_case_string' | camelize }}")
print(template.render())  # Outputs: "SnakeCaseString"
```

## License

BSD-3-Clause

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

- This project uses the [inflection](https://github.com/jpvanhal/inflection) library to provide powerful string
transformation capabilities. Special thanks to the contributors of the inflection library for their work.
- Additionally, we acknowledge the [Jinja2](https://palletsprojects.com/p/jinja/)
project for providing a robust templating engine that makes this extension possible.
