import datetime

from core.stock_metadata import StockMetadata


class Dividend:
    def __init__(
            self,
            name: str,
            stock_metadata: StockMetadata,
            detachment_date: datetime.date,
            amount: float
    ):
        self._name = name
        self._detachment_date = detachment_date
        self._amount = amount
        self._income = self._compute_income(stock_metadata.date, stock_metadata.number)

    def _compute_income(self, acquisition_date, number):
        if acquisition_date < self._detachment_date and self._amount:
            return self._amount * number
        return 0

    def transform_as_dict(self):
        return {
            "name": self._name,
            "detachment_date": self._detachment_date,
            "amount": self._amount,
            "income": self._income
        }
