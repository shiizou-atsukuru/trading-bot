def validate_input(symbol: str, side: str, quantity: float, price: float=None):
    if side.upper() not in ("BUY", "SELL"):
        raise ValueError("Side must be BUY or SELL")
    
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")
    
    if price is not None and price<=0:
        raise ValueError("Price must be greater than 0 for LIMIT orders")
    
    return True