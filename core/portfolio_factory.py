from abc import ABC
from typing import List

import pandas as pd
from pandas import Series

from core.portfolio import Portfolio
from core.stock import Stock
from core.stock_metadata import StockMetadata
from core.yfinance_utils import get_close_history


class PortfolioFactory(ABC):

    @staticmethod
    def build_portfolio_history(stocks_metadata: List[StockMetadata]):
        stocks_history: Series = pd.DataFrame([
            {
                "stock": Stock(stock_metadata, close_value),
                "history_date": close_date.date()
            }
            for stock_metadata in stocks_metadata
            for close_date, close_value in get_close_history(stock_metadata.symbol, stock_metadata.date).items()
        ]).groupby("history_date")['stock'].apply(list)
        return [
            Portfolio(stocks, date)
            for date, stocks in stocks_history.items()
        ]