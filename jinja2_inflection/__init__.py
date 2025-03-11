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
        inflection_filters = dict(
            camelize=camelize,
            dasherize=dasherize,
            humanize=humanize,
            ordinal=ordinal,
            ordinalize=ordinalize,
            parameterize=parameterize,
            pluralize=pluralize,
            singularize=singularize,
            tableize=tableize,
            titleize=titleize,
            transliterate=transliterate,
            underscore=underscore,
        )
        environment.filters.update(inflection_filters)
