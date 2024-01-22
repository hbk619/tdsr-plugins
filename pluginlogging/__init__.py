from . import logger


def with_logging(plugin_name, handler):
    return logger.with_logging(plugin_name, handler)