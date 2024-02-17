from . import custom_voice
from ..pluginlogging import with_logging


wrapped_handler = with_logging("maven", custom_voice.parse_output)


def parse_output(lines):
    return wrapped_handler(lines)
