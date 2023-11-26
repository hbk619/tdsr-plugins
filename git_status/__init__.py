from . import parse_git_status


def parse_output(lines):
    return parse_git_status.parse_output(lines)
