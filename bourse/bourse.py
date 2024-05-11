from typing import List

import reflex as rx

from bourse.portfolio import Portfolio
from bourse.stock import load_stocks_from_yaml

portfolio = Portfolio(stocks=load_stocks_from_yaml("stocks.yml"))


class State(rx.State):
    data: List = [stock.transform_to_dict() for stock in portfolio.stocks]
    columns: List[str] = ["symbol"]


def index():
    return rx.data_table(
        data=State.data,
        columns=State.columns,
    )


app = rx.App()
app.add_page(index)
