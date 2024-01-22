from . import parse_maven
from ..pluginlogging import with_logging

wrapped_handler = with_logging("maven", parse_maven.parse_output)


def parse_output(lines):
    return wrapped_handler(lines)
