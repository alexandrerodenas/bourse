from typing import List

from stock import Stock


class Portfolio:
    def __init__(self, stocks: List[Stock]):
        self.stocks = stocks

    def total_investment_amount(self):
        return sum(stock.cost for stock in self.stocks)

    def total_market_value(self):
        return sum(stock.current_price * stock.number for stock in self.stocks)

    def total_gain_or_deficit(self):
        return round(sum(stock.gain_or_deficit for stock in self.stocks), 2)

    def transform_to_dict(self):
        return {
            'total_investment_amount': self.total_investment_amount(),
            'total_market_value': self.total_market_value(),
            'total_gain_deficit': self.total_gain_or_deficit(),
            'stocks': [stock.transform_to_dict() for stock in self.stocks]
        }

    def to_string(self):
        total_investment = self.total_investment_amount()
        total_market_value = self.total_market_value()
        total_gain_deficit = self.total_gain_or_deficit()

        return f"Total Investment Amount: {total_investment}\nTotal Market Value: {total_market_value}\nTotal Gain or Deficit: {total_gain_deficit}\n"
