import re


def parse_output(lines):
    options = []
    command = lines[-1]
    for line in lines[0:-1]:
        if line and not command.startswith(line):
            options += line.split()

    return [" ".join(options)] if len(options) else ['Nothing listed']
