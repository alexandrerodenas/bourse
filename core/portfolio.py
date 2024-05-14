import datetime
from typing import List
from uuid import uuid4

from core.stock import Stock
from core.stock_metadata import StockMetadata


class Portfolio:
    def __init__(self, stocks: List[Stock], portfolio_date=datetime.datetime.now()):
        self.stocks = stocks
        self.date = portfolio_date
        self.id = uuid4()

    def total_investment_amount(self):
        return sum(stock.investment for stock in self.stocks)

    def total_market_value(self):
        return sum(stock.current_price * stock.number for stock in self.stocks)

    def total_gain_or_deficit(self):
        return round(sum(stock.gain_or_deficit for stock in self.stocks), 2)

    def transform_to_dict(self):
        return {
            'total_investment_amount': self.total_investment_amount(),
            'total_market_value': self.total_market_value(),
            'total_gain_deficit': self.total_gain_or_deficit(),
            'portfolio_date': self.date,
            'id': self.id,
            'stocks': [stock.transform_to_dict() for stock in self.stocks]
        }
