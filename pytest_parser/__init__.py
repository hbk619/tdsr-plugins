from . import parse_pytest
from ..pluginlogging import with_logging

wrapped_handler = with_logging("pytest", parse_pytest.parse_output)


def parse_output(lines):
    return wrapped_handler(lines)
