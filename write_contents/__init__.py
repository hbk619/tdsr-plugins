from . import write
from ..pluginlogging import with_logging

wrapped_handler = with_logging("write contents", write.parse_output)


def parse_output(lines):
    return wrapped_handler(lines)