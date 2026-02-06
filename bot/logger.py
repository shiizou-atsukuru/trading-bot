import logging
import os
import http.client as http_client


LOG_DIR = "/app/logs"
LOG_FILE = os.path.join(LOG_DIR, "trading_bot.log")

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

def setup_logging():
    root_logger = logging.getLogger()

    if not root_logger.handlers:
        root_logger.setLevel(logging.INFO)

        # file handler
        fh = logging.FileHandler(LOG_FILE)
        fh.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))

        # stream handler
        ch = logging.StreamHandler()
        ch.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))

        root_logger.addHandler(fh)
        root_logger.addHandler(ch)

setup_logging()
logger = logging.getLogger("trading-bot")

def log_api_call(action, details):
    logger.info(f"Action: {action} | Details: {details}")

def log_error(message):
    logger.error(f"{message}")