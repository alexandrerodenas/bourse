import yfinance as yf


def get_close_history(symbol: str, start_date: str):
    return yf.Ticker(symbol).history(start=start_date)["Close"]
