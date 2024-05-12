from typing import List

import pandas as pd

from core.portfolio import Portfolio
from core.stock import Stock
from core.stock_metadata import StockMetadata
from core.yfinance_utils import get_close_history


class History:
    def __init__(self, stocks_metadata: List[StockMetadata]):
        stocks_history = pd.DataFrame([
            {
                "stock": Stock(stock_metadata, close_value),
                "history_date": close_date.date()
            }
            for stock_metadata in stocks_metadata
            for close_date, close_value in get_close_history(stock_metadata.symbol, stock_metadata.date).items()
        ]).groupby("history_date")['stock'].apply(list)
        self.portfolios = [
            Portfolio(stocks)
            for stocks in stocks_history
        ]

    def transform_to_dict(self):
        return [
            portfolio.transform_to_dict()
            for portfolio in self.portfolios
        ]
