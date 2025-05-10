from jinja2 import Environment
from jinja2.ext import Extension
from jinja2_inflection import InflectionExtension


class TestInflectionExtension:
    def test_filters_registered_to_environment(self) -> None:
        env = Environment(autoescape=True)
        InflectionExtension(env)

        expected_filter_names = [
            "camelize",
            "dasherize",
            "humanize",
            "ordinal",
            "ordinalize",
            "parameterize",
            "pluralize",
            "singularize",
            "tableize",
            "titleize",
            "transliterate",
            "underscore",
        ]

        for filter_name in expected_filter_names:
            assert filter_name in env.filters

    def test_humanize_filter_mapping(self) -> None:
        env = Environment(autoescape=True)
        InflectionExtension(env)
        assert "humanize" in env.filters
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

    def test_filter_with_parameters(self) -> None:
        env = Environment(extensions=[InflectionExtension], autoescape=True)

        template = env.from_string(
            "{{ 'product_category' | camelize(uppercase_first_letter=False) }}"
        )
        assert template.render() == "productCategory"

        template = env.from_string(
            "{{ 'product_category' | camelize(uppercase_first_letter=True) }}"
        )
        assert template.render() == "ProductCategory"

        template = env.from_string(
            "{{ 'Donald E. Knuth' | parameterize(separator='_') }}"
        )
        assert template.render() == "donald_e_knuth"

        template = env.from_string("{{ 'Donald E. Knuth' | parameterize }}")
        assert template.render() == "donald-e-knuth"

    def test_all_filters_functionality(self) -> None:
        env = Environment(extensions=[InflectionExtension], autoescape=True)

        test_cases = [
            ("{{ 'snake_case_string' | camelize }}", "SnakeCaseString"),
            ("{{ 'first_name' | dasherize }}", "first-name"),
            ("{{ 'employee_salary' | humanize }}", "Employee salary"),
            ("{{ 1 | ordinal }}", "st"),
            ("{{ 2 | ordinal }}", "nd"),
            ("{{ 1 | ordinalize }}", "1st"),
            ("{{ 'Donald E. Knuth' | parameterize }}", "donald-e-knuth"),
            ("{{ 'octopus' | pluralize }}", "octopi"),
            ("{{ 'mice' | singularize }}", "mouse"),
            ("{{ 'UserAccount' | tableize }}", "user_accounts"),
            ("{{ 'api_responses' | titleize }}", "Api Responses"),
            ("{{ 'café' | transliterate }}", "cafe"),
            ("{{ 'DeviceType' | underscore }}", "device_type"),
        ]

        for template_str, expected in test_cases:
            template = env.from_string(template_str)
            assert template.render() == expected
