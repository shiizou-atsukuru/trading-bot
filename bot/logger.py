import logging
import os
import http.client as http_client


LOG_DIR = "/app/logs"
LOG_FILE = os.path.join(LOG_DIR, "trading_bot.log")

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("trading_bot")

def log_api_call(action, details):
    logger.info(f"Action: {action} | Details: {details}")

def log_error(message):
    logger.error(f"{message}")

def enable_debug_logging():
    http_client.HTTPConnection.debuglevel = 1

    requests_log = logging.getLogger("urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True