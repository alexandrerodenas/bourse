from dataclasses import dataclass
from typing import List

import yaml


@dataclass
class StockMetadata:
    def __init__(self, name, symbol, number, date, status, unit_cost):
        self.name = name
        self.symbol = symbol
        self.number = number
        self.date = date
        self.status = status
        self.unit_cost = unit_cost

    @staticmethod
    def load_from_file(filepath: str) -> List['StockMetadata']:
        with open(filepath, "r") as file:
            data = yaml.safe_load(file)

        return [
            StockMetadata(
                name=stock_name,
                symbol=stock_data["symbol"],
                number=stock_data["number"],
                unit_cost=stock_data["cost"],
                date=stock_data["date"],
                status=stock_data["status"]
            )
            for stock_name, stock_data in data.items()
        ]
