"""Jinja2 extension for inflection library's string transformation functions."""

__all__ = ["InflectionExtension"]

from inflection import (
    camelize,
    dasherize,
    humanize,
    ordinal,
    ordinalize,
    parameterize,
    pluralize,
    singularize,
    tableize,
    titleize,
    transliterate,
    underscore,
)
from jinja2 import Environment
from jinja2.ext import Extension


class InflectionExtension(Extension):
    def __init__(self, environment: Environment) -> None:
        super().__init__(environment)

        def camelize_filter(string: str, uppercase_first_letter: bool = True):
            return camelize(string, uppercase_first_letter)

        def parameterize_filter(string: str, separator: str = "-"):
            return parameterize(string, separator)

        inflection_filters = dict(
            camelize=camelize_filter,
            parameterize=parameterize_filter,
            dasherize=dasherize,
            humanize=humanize,
            ordinal=ordinal,
            ordinalize=ordinalize,
            pluralize=pluralize,
            singularize=singularize,
            tableize=tableize,
            titleize=titleize,
            transliterate=transliterate,
            underscore=underscore,
        )
        environment.filters.update(inflection_filters)
