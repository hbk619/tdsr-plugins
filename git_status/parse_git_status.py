import re

instructions = re.compile(r"\(use\s\"git\s.*\)")
staged = re.compile(r"Changes to be committed:")
unstaged = re.compile(r"Changes not staged for commit:")
status = re.compile(r"\s*(modified|added|removed|new file|renamed):.*")


def parse_output(lines):
    in_staged = False
    in_unstaged = False
    staged_files = []
    unstaged_files = []
    lines.reverse()
    for line in lines:
        if staged.match(line):
            in_staged = True
            staged_files.append("Staged")
        elif unstaged.match(line):
            in_unstaged = True
            unstaged_files.append("Not staged")
        elif in_staged:
            if status.match(line):
                staged_files.append(line.strip())
            elif len(line) == 0:
                in_staged = False
        elif in_unstaged:
            if status.match(line):
                unstaged_files.append(line.strip())
            elif len(line) == 0:
                in_unstaged = False

    staged_files = ['No staged files'] if len(staged_files) == 0 else staged_files
    unstaged_files = ['No unstaged files'] if len(unstaged_files) == 0 else unstaged_files
    return staged_files + unstaged_files
