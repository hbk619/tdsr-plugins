import re

error_lines = re.compile(r"^│\sError:\s(.+)")
results = re.compile(r"^#\s(.+)")
containing_line = re.compile(r"^│\s{3}(\d+):\s.+")
extra_error_details = re.compile(r"^│\s(.+)")


def parse_output(lines):
    lines_to_say = []
    in_errors = False
    found_line_number = False
    lines.reverse()
    for index, line in enumerate(lines):
        results_matches = results.match(line)
        error_matches = error_lines.match(line)
        if results_matches:
            action = results_matches.groups()[0]
            lines_to_say.append(action)

        elif error_matches:
            in_errors = True
            error_message = error_matches.groups()[0]
            lines_to_say.append(f"Error {error_message}")

        elif in_errors:
            error_line_matches = containing_line.match(line)
            extra_error_details_matches = extra_error_details.match(line)

            if error_line_matches:
                line_number = error_line_matches.groups()[0]
                lines_to_say.append(f"line {line_number}")
                found_line_number = True
            elif found_line_number and extra_error_details_matches:
                extra_details = extra_error_details_matches.groups()[0]
                lines_to_say.append(extra_details)
                found_line_number = False

        if line == '╵':
            in_errors = False
            found_line_number = False

    return lines_to_say
