import re

error_lines = re.compile(r"E\s+(?:\+\s+)?(.*)")
results = re.compile(r"\[(?:ERROR|INFO){1}\]\sTests\srun:\s([0-9])+,\sFailures:\s([0-9]+),\sErrors:\s([0-9]+),\sSkipped:\s([0-9]+)")
total_test = re.compile(r"=+\s((?:[0-9]+\s(?:failed|passed|error))|no tests)(?:,\s)?(?:ran\s)?([0-9]\spassed)?.*=+")
line_details = re.compile(r"\[([0-9]+),([0-9]+)]")


def parse_output(lines):
    lines_to_say = []
    in_errors = False
    for index, line in enumerate(lines):
        matches = results.match(line)
        if matches:
            run = matches.groups()[0]
            failures = matches.groups()[1]
            errors = matches.groups()[2]
            skipped = matches.groups()[3]
            passed = int(run) - int(failures) - int(errors) - int(skipped)
            lines_to_say.append(f"{passed} passed {failures} failed")

            if passed < int(run):

                for test_details in lines[index+1:-1]:
                    if test_details.startswith("but: was"):
                        lines_to_say.append(test_details.replace("but: was ", "Got "))
                    elif test_details.startswith("Expected:"):
                        lines_to_say.append(test_details.replace("Expected:", "Expected"))
                    elif test_details.startswith("[ERROR] Failures"):
                        break
                    elif test_details.startswith("[ERROR]"):
                        with_decoration = test_details.replace("[ERROR] ", "Test is ")
                        lines_to_say.append(with_decoration.replace(":", " line "))

            break

        if line and line.startswith("[ERROR]"):
            sections = line.split(" ")
            if len(sections) > 2:
                start_of_file_name = sections[1].rfind("/")
                if start_of_file_name > -1:
                    in_errors = True
                    end_of_file_name = sections[1].rfind(":")
                    file_name = sections[1][start_of_file_name + 1:end_of_file_name]
                    error_position = line_details.search(sections[1])
                    lines_to_say += [file_name, f"line {error_position.group(1)} column {error_position.group(2)}",
                                    " ".join(sections[2:])]
                elif in_errors:
                    break

    return lines_to_say
