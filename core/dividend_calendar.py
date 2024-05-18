from core.stock_metadata import StockMetadata
from core.yfinance_utils import get_last_dividend


class DividendCalendar:
    def __init__(self, stock_metadata: [StockMetadata]):
        self.last_dividends = [
            get_last_dividend(metadata.symbol)
            for metadata in stock_metadata
        ]
