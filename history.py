from typing import List

import pandas as pd

from portfolio import Portfolio
from stock import Stock
from stock_metadata import StockMetadata
from yfinance_utils import get_close_history


class StockNoFound(Exception):
    def __init__(self, name: str):
        super().__init__(f"Stock not found for name {name}.")


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


if __name__ == '__main__':
    metadata = StockMetadata.load_from_file("stocks.yml")
