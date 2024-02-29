import logging
from logging.handlers import RotatingFileHandler
import os

logger = logging.getLogger('hbk619-plugins')
logger.setLevel(logging.INFO)

FIVE_MEG_IN_BYTES = 5000000
handler = RotatingFileHandler(os.path.join(os.getenv('HOME'), 'hbk619-plugins.log'), maxBytes=FIVE_MEG_IN_BYTES, backupCount=1)
handler.setLevel(logging.INFO)

logger.addHandler(handler)


def with_logging(plugin_name, handler):
    def execute(lines):
        logger.info(f"begin {plugin_name} output\n")

        results = handler(lines)

        logger.info("\n".join(results))
        logger.info(f"\nend {plugin_name} output\n")

        return results
    return execute
