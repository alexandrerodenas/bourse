from typing import List

import yfinance as yf

from stock_metadata import StockMetadata


class Stock:
    def __init__(self, metadata: StockMetadata):
        self.name = metadata.name
        self.number = metadata.number
        self.date = metadata.date
        self.status = metadata.status
        self.yf_ticker = yf.Ticker(metadata.symbol)
        self.cost = metadata.unit_cost * metadata.number
        self.current_price = self.get_current_price()
        self.gain_or_deficit = self.calculate_gain_or_deficit()
        self.estimation = self.calculate_stock_value_estimation()
        self.difference_value_euros = self.calculate_difference_value_euros()
        self.difference_value_percentage = self.calculate_difference_value_percentage()

    def get_current_price(self):
        return round(self.yf_ticker.history(period="1d")["Close"].iloc[-1], 3)

    def get_close_history(self):
        return self.yf_ticker.history(start=self.date)["Close"].values

    def calculate_gain_or_deficit(self):
        if self.status == "pending":
            return 0
        current_value = round(self.current_price * self.number, 2)
        return round(current_value - self.cost, 2)

    def calculate_stock_value_estimation(self):
        return self.current_price * self.number

    def calculate_difference_value_euros(self):
        return round(self.estimation - self.cost, 2)

    def calculate_difference_value_percentage(self):
        return round((self.difference_value_euros / self.cost) * 100 if self.cost != 0 else 0, 2)

    def transform_to_dict(self):
        return {
            'name': self.name,
            'number': self.number,
            'cost': self.cost,
            'date': self.date,
            'status': self.status,
            'current_price': self.current_price,
            'gain_or_deficit': self.gain_or_deficit,
            'stock_value_estimation': self.estimation,
            'difference_value_euros': self.difference_value_euros,
            'difference_value_percentage': self.difference_value_percentage
        }

    def to_string(self):
        return f"Name: {self.name}\nNumber of Shares: {self.number}\nCost: {self.cost}\nDate: {self.date}\nStatus: {self.status}\nCurrent Price: {self.current_price}\nGain or Deficit: {self.gain_or_deficit}\nStock Value Estimation: {self.estimation}\nDifference Value (Euros): {self.difference_value_euros}\nDifference Value (Percentage): {self.difference_value_percentage:.2f}%\n"

    @staticmethod
    def build_from_metadata(stock_metadata: List[StockMetadata]) -> List['Stock']:
        return [Stock(metadata) for metadata in stock_metadata]