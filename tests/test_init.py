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
from jinja2_inflection import InflectionExtension


class TestInflectionExtension:
    def test_filters_registered_to_environment(self) -> None:
        env = Environment(autoescape=True)
        InflectionExtension(env)
        expected_filters = {
            "camelize": camelize,
            "dasherize": dasherize,
            "humanize": humanize,
            "ordinal": ordinal,
            "ordinalize": ordinalize,
            "parameterize": parameterize,
            "pluralize": pluralize,
            "singularize": singularize,
            "tableize": tableize,
            "titleize": titleize,
            "transliterate": transliterate,
            "underscore": underscore,
        }
        for filter_name, filter_func in expected_filters.items():
            assert filter_name in env.filters
            assert env.filters[filter_name] == filter_func

    def test_humanize_filter_mapping(self) -> None:
        env = Environment(autoescape=True)
        InflectionExtension(env)
        assert "humanize" in env.filters
        assert env.filters["humanize"] == humanize
        template = env.from_string("{{ 'employee_salary' | humanize }}")
        assert template.render() == "Employee salary"
        template = env.from_string("{{ 'author_id' | humanize }}")
        assert template.render() == "Author"

    def test_extension_initialization(self) -> None:
        env = Environment(extensions=[InflectionExtension], autoescape=True)
        extension_found = False
        for ext in env.extensions.values():
            if isinstance(ext, InflectionExtension):
                extension_found = True
                break
        assert extension_found
        assert issubclass(InflectionExtension, Extension)
        template = env.from_string("{{ 'device_type' | camelize }}")
        assert template.render() == "DeviceType"
        template = env.from_string("{{ 'DeviceType' | underscore }}")
        assert template.render() == "device_type"
