from core.stock_metadata import StockMetadata


class Stock:
    def __init__(self, metadata: StockMetadata, current_price: int):
        self.name = metadata.name
        self.number = metadata.number
        self.date = metadata.date
        self.status = metadata.status
        self.symbol = metadata.symbol
        self.investment = metadata.unit_cost * metadata.number
        self.unit_cost = metadata.unit_cost
        self.current_price = current_price
        self.gain_or_deficit = self.calculate_gain_or_deficit()
        self.estimation = self.calculate_stock_value_estimation()
        self.difference_value_euros = self.calculate_difference_value_euros()
        self.difference_value_percentage = self.calculate_difference_value_percentage()

    def calculate_gain_or_deficit(self):
        if self.status == "pending":
            return 0
        current_value = round(self.current_price * self.number, 2)
        return round(current_value - self.investment, 2)

    def calculate_stock_value_estimation(self):
        return self.current_price * self.number

    def calculate_difference_value_euros(self):
        return round(self.estimation - self.investment, 2)

    def calculate_difference_value_percentage(self):
        return round((self.difference_value_euros / self.investment) * 100 if self.investment != 0 else 0, 2)

    def transform_to_dict(self):
        return {
            'name': self.name,
            'number': self.number,
            'date': self.date,
            'status': self.status,
            'unit_cost': self.unit_cost,
            'current_price': self.current_price,
            'gain_or_deficit': self.gain_or_deficit,
            'stock_value_investment': self.investment,
            'stock_value_estimation': self.estimation,
            'difference_value_euros': self.difference_value_euros,
            'difference_value_percentage': self.difference_value_percentage
        }
