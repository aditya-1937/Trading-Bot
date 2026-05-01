from app.client import BinanceClient

class Trader:

    def __init__(self):
        self.client = BinanceClient()

    def execute_trade(self, symbol, side, order_type, quantity, price=None):
        return self.client.place_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price
        )
