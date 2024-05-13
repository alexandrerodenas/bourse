from typing import List

import pandas as pd
from pandas import Series

from core.portfolio import Portfolio
from core.stock import Stock
from core.stock_metadata import StockMetadata
from core.yfinance_utils import get_close_history


class History:
    def __init__(self, stocks_metadata: List[StockMetadata]):
        stocks_history: Series = pd.DataFrame([
            {
                "stock": Stock(stock_metadata, close_value),
                "history_date": close_date.date()
            }
            for stock_metadata in stocks_metadata
            for close_date, close_value in get_close_history(stock_metadata.symbol, stock_metadata.date).items()
        ]).groupby("history_date")['stock'].apply(list)
        self._portfolios = [
            Portfolio(stocks, date)
            for date, stocks in stocks_history.items()
        ]

    def transform_to_dict(self):
        return [
            portfolio.transform_to_dict()
            for portfolio in self._portfolios
        ]

    def get_gain_loss_history(self):
        return [
            {
                "value": portfolio.total_gain_or_deficit(),
                "date": portfolio.date
            }
            for portfolio in self._portfolios
        ]

    def get_investment_evolution(self):
        return [
            {
                "total_market_value": portfolio.total_market_value(),
                "total_investment_amount": portfolio.total_investment_amount(),
                "date": portfolio.date
            }
            for portfolio in self._portfolios
        ]

    def get_current_portfolio(self):
        return self._portfolios[-1]

    @classmethod
    def build_from_file(cls, filepath: str) -> 'History':
        return History(
            StockMetadata.load_from_file(filepath)
        )


