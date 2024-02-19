from . import parse_terraform
from ..pluginlogging import with_logging

wrapped_handler = with_logging("terraform", parse_terraform.parse_output)


def parse_output(lines):
    return wrapped_handler(lines)
