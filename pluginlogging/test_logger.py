from unittest.mock import patch, MagicMock, call
from .logger import with_logging


@patch('hbk619.pluginlogging.logger.logger')
def test_calls_original_method_and_returns_lines(mock_logger):
    handler = MagicMock()
    lines = ['Some', 'command', 'output']
    expected = ['Some', 'parsed', 'output']
    handler.return_value = expected
    wrapped = with_logging('test_plugin', handler)
    result = wrapped(lines)

    handler.assert_called_once_with(lines)
    assert result == expected


@patch('hbk619.pluginlogging.logger.logger')
def test_writes_to_tmp_with_correct_lines(mock_logger):

    handler = MagicMock()
    lines = ['Some', 'commands', 'output']
    handler.return_value = lines
    wrapped = with_logging('test_plugin', handler)
    wrapped(lines)
    mock_logger.info.assert_has_calls([
        call("begin test_plugin output\n"), call("Some\ncommands\noutput"), call("\nend test_plugin output\n")])
