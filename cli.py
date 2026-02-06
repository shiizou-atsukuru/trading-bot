import typer
from bot.orders import place_market_order, place_limit_order
from bot.validators import validate_input
from bot.logger import log_error

app = typer.Typer()

@app.command()
def main(
    symbol: str,
    side: str,
    order_type: str,
    quantity: float,
    price: float = typer.Option(None, help="Required for limit orders")
):
    try:
        validate_input(symbol, side, quantity, price)
    
        typer.echo(f"Sending {order_type} {side} order for {symbol}...")

        if order_type.upper() == "MARKET":
            response = place_market_order(symbol, side, quantity)
        elif order_type.upper() == 'LIMIT':
            response = place_limit_order(symbol, side, quantity, price)
        else:
            print(f"Unknown order type: {order_type}")
            return

        typer.echo(response)

    except Exception as e:
        log_error(str(e))
        print(f"Error: {e}")


if __name__ == "__main__":
    app()