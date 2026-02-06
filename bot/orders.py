from bot.client import get_futures_client
from bot.logger import log_api_call, log_error

def place_market_order(symbol, side, quantity):
    client = get_futures_client()
    log_api_call("API REQUEST", {"symbol": symbol, "side": side, "type": "MARKET", "quantity": quantity})
    try:
        response = client.futures_create_order(
            symbol=symbol.upper(),
            side=side.upper(),
            type="MARKET",
            quantity=quantity
        )
        log_api_call(f"API RESPONSE - MARKET {side}", response)
        return response
    except Exception as e:
        log_error(str(e))
        return {"error": str(e)}
    
def place_limit_order(symbol, side, quantity, price):
    client = get_futures_client()
    log_api_call("API REQUEST", {"symbol": symbol, "side": side, "type": "LIMIT", "quantity": quantity, "price": price})
    try:
        response = client.futures_create_order(
            symbol=symbol.upper(),
            side=side.upper(),
            type="LIMIT",
            timeInForce="GTC",
            quantity=quantity,
            price=str(price)
        )
        log_api_call(f"API RESPONSE - LIMIT {side}", response)
        return response
    except Exception as e:
        log_error(str(e))
        return {"error": str(e)}