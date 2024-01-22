from . import parse_git_status
from ..pluginlogging import with_logging

wrapped_handler = with_logging("git status", parse_git_status.parse_output)


def parse_output(lines):
    return wrapped_handler(lines)
