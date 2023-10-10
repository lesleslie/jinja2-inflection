from inflection import camelize
from inflection import dasherize
from inflection import humanize
from inflection import ordinal
from inflection import ordinalize
from inflection import parameterize
from inflection import pluralize
from inflection import singularize
from inflection import tableize
from inflection import titleize
from inflection import transliterate
from inflection import underscore

from jinja2.ext import Extension
from jinja2 import Environment


class InflectionExtension(Extension):
    def __init__(self, environment: Environment) -> None:
        super().__init__(environment)
        inflection_filters = dict(
            camelize=camelize,
            dasherize=dasherize,
            humanize_inflection=humanize,
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
        environment.filters.update(inflection_filters)  # type: ignore
