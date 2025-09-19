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

        def camelize_filter(string: str, uppercase_first_letter: bool = True) -> str:
            return camelize(string, uppercase_first_letter)  # type: ignore[no-any-return]

        def parameterize_filter(string: str, separator: str = "-") -> str:
            return parameterize(string, separator)  # type: ignore[no-any-return]

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
