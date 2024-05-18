import logging
from typing import List

import yfinance as yf


def get_close_history(symbol: str, start_date: str):
    return yf.Ticker(symbol).history(start=start_date)["Close"]


def download_history(symbols: List[str], start_date: str):
    return yf.download(symbols, start=start_date)


def get_last_dividend(symbol: str):
    calendar = yf.Ticker(symbol).calendar
    try:
        return calendar['Ex-Dividend Date'], calendar['Earnings Average']
    except KeyError as e:
        logging.error(e)
