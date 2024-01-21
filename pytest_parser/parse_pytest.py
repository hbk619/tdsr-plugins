import re
from ..clipboard import clippy

error_lines = re.compile(r"E\s+(?:\+\s+)?(.*)")
location_lines = re.compile(r">\s+(?:\+\s+)?(.*)")
total_test = re.compile(r"=+\s((?:[0-9]+\s(?:failed|passed|error))|no tests)(?:,\s)?(?:ran\s)?([0-9]\spassed)?.*=+")


def parse_output(lines):
    lines_to_say = []
    for line in lines:
        matches = error_lines.match(line)
        if matches:
            lines_to_say.append(matches.groups()[0])
        matches = location_lines.match(line)
        if matches:
            lines_to_say.append(f"code is {matches.groups()[0]}")
        matches = total_test.match(line)
        if matches:
            if matches.groups()[0]: lines_to_say.append(matches.groups()[0])
            if matches.groups()[1]: lines_to_say.append(matches.groups()[1])

    return lines_to_say
