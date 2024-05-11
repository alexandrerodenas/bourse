import yaml
import yfinance as yf


class Stock:
    def __init__(self, symbol, number, unit_cost, date, status):
        self.symbol = symbol
        self.number = number
        self.date = date
        self.status = status
        self.cost = unit_cost * number
        self.current_price = self.get_current_price()
        self.gain_or_deficit = self.calculate_gain_or_deficit()
        self.stock_value_estimation = self.calculate_stock_value_estimation()
        self.difference_value_euros = self.calculate_difference_value_euros()
        self.difference_value_percentage = self.calculate_difference_value_percentage()

    def get_current_price(self):
        stock = yf.Ticker(self.symbol)
        return round(stock.history(period="1d")["Close"].iloc[-1], 3)

    def calculate_gain_or_deficit(self):
        if self.status == "pending":
            return 0
        current_value = round(self.current_price * self.number, 2)
        return round(current_value - self.cost, 2)

    def calculate_stock_value_estimation(self):
        return self.current_price * self.number

    def calculate_difference_value_euros(self):
        return round(self.stock_value_estimation - self.cost, 2)

    def calculate_difference_value_percentage(self):
        return (self.difference_value_euros / self.cost) * 100 if self.cost != 0 else 0

    def transform_to_dict(self):
        return {
            'symbol': self.symbol,
            'number': self.number,
            'cost': self.cost,
            'date': self.date,
            'status': self.status,
            'current_price': self.current_price,
            'gain_or_deficit': self.gain_or_deficit,
            'stock_value_estimation': self.stock_value_estimation,
            'difference_value_euros': self.difference_value_euros,
            'difference_value_percentage': self.difference_value_percentage
        }

    def to_string(self):
        return f"Symbol: {self.symbol}\nNumber of Shares: {self.number}\nCost: {self.cost}\nDate: {self.date}\nStatus: {self.status}\nCurrent Price: {self.current_price}\nGain or Deficit: {self.gain_or_deficit}\nStock Value Estimation: {self.stock_value_estimation}\nDifference Value (Euros): {self.difference_value_euros}\nDifference Value (Percentage): {self.difference_value_percentage:.2f}%\n"


def load_stocks_from_yaml(file_path):
    stocks = []

    # Load YAML data
    with open(file_path, "r") as file:
        data = yaml.safe_load(file)

    for stock_name, stock_data in data.items():
        stock = Stock(
            symbol=stock_data["symbol"],
            number=stock_data["number"],
            unit_cost=stock_data["cost"],
            date=stock_data["date"],
            status=stock_data["status"]
        )
        stocks.append(stock)

    return stocks
