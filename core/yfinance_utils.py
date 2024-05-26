import datetime
import logging
from typing import List

import yfinance as yf


def get_close_history(symbol: str, start_date: str):
    return yf.Ticker(symbol).history(start=start_date)["Close"]


def download_history(symbols: List[str], start_date: str):
    return yf.download(symbols, start=start_date)


def get_last_dividend(symbol: str):
    calendar = yf.Ticker(symbol).calendar
    date = calendar['Ex-Dividend Date']
    dividend = calendar['Earnings Average']
    if date < datetime.date.today():
        dividend = yf.Ticker(symbol).dividends.iloc[-1]
    try:
        return {
            "detachment_date": date,
            "amount": dividend
        }
    except KeyError as e:
        logging.error(e)
