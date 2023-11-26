import re

instructions = re.compile(r"\(use\s\"git\s.*\)")
staged = re.compile(r"Changes to be committed:")
status = re.compile(r"\s*(modified|added|removed|new file|renamed):.*")


def parse_output(lines):
    in_staged = False
    changes = []
    lines.reverse()
    for line in lines:
        if staged.match(line):
            in_staged = True
        elif in_staged:
            if status.match(line):
                changes.append(line.strip())
            elif len(line) == 0:
                break
    return changes if len(changes) else ['No staged files']
