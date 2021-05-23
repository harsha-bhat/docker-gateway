import logging

log_fmt = "%(asctime)s - %(levelname)s - %(message)s"

logging.basicConfig(level=logging.INFO, format=log_fmt)
logger = logging.getLogger("logger")
