import logging
import argparse

# Set up logging
parser = argparse.ArgumentParser(description="Telegram Expense Bot")
parser.add_argument("--log", dest="loglevel", default="INFO", help="Set the logging level")
args = parser.parse_args()
loglevel = args.loglevel.upper()
numeric_level = getattr(logging, loglevel, "INFO")
if not isinstance(numeric_level, int):
    raise ValueError('Invalid log level: %s' % loglevel)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=numeric_level)
logger = logging.getLogger(__name__)
