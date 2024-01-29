from .write import parse_output


def test_calls_original_method_and_returns_lines():
    lines = ['Some', 'command', 'output']
    assert parse_output(lines) == lines
