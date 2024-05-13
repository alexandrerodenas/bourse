from typing import List

import yfinance as yf


def get_close_history(symbol: str, start_date: str):
    return yf.Ticker(symbol).history(start=start_date)["Close"]


def download_history(symbols: List[str], start_date: str):
    return yf.download(symbols, start=start_date)
