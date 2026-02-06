from binance.client import Client
import os


def get_futures_client():
    api_key = os.getenv('BINANCE_API_KEY')
    api_secret = os.getenv('BINANCE_API_SECRET')

    client = Client(api_key, api_secret, testnet=True)

    client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'
    return client