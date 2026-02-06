from binance.client import Client
import os
from dotenv import load_dotenv


def get_futures_client():
    env_loaded = load_dotenv()

    api_key = os.getenv('BINANCE_API_KEY')
    api_secret = os.getenv('BINANCE_API_SECRET')

    if not api_key or not api_secret:
        error_message = "API Keys missing."
        if not env_loaded:
            error_message += " No .env file detected in the project root."
        else:
            error_message += " .env file found but BINANCE_API_KEY/SECRET are empty."
        raise ValueError(error_message)

    client = Client(api_key, api_secret, testnet=True)

    client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'
    return client