import yfinance as yf


def get_current_price(symbol: str):
    return round(yf.Ticker(symbol).history(period="1d")["Close"].iloc[-1], 3)


def get_close_history(symbol: str, start_date: str):
    return yf.Ticker(symbol).history(start=start_date)["Close"]
