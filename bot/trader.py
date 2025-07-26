import yaml
from binance.client import Client

class Trader:
    def __init__(self, config):
        self.api_key = config['binance']['api_key']
        self.api_secret = config['binance']['api_secret']
        self.symbol = config['trade']['symbol']
        self.quantity = config['trade']['quantity']
        self.strategy = config['trade']['strategy']
        self.client = Client(self.api_key, self.api_secret)

    def run(self):
        # Example: simple buy order
        order = self.client.create_order(
            symbol=self.symbol,
            side='BUY',
            type='MARKET',
            quantity=self.quantity
        )
        print(f"Order executed: {order}")
