from typing import List

import reflex as rx
from reflex.components.radix.themes.components.table import TableRow, TableCell

from bourse.portfolio import Portfolio
from bourse.stock import load_stocks_from_yaml, Stock

portfolio = Portfolio(stocks=load_stocks_from_yaml("stocks.yml"))

MIN_GAIN = -20
MAX_GAIN = 20


def get_color_style(stock: Stock) -> str:
    normalized_value = (stock.gain_or_deficit - MIN_GAIN) / (MAX_GAIN - MIN_GAIN)
    g = int(255 * normalized_value)
    r = int(255 * (1 - normalized_value))
    return f"rgb({r}, {g}, 0)"


def index():
    headers = rx.table.header(
        rx.table.row(
            rx.table.column_header_cell("Name"),
            rx.table.column_header_cell("Date"),
            rx.table.column_header_cell("Cost"),
            rx.table.column_header_cell("Estimation"),
            rx.table.column_header_cell("+/-"),
            rx.table.column_header_cell("Status"),
        ),
    )
    rows = [rx.table.row(
        rx.table.cell(stock.name),
        rx.table.cell(stock.date),
        rx.table.cell(stock.cost),
        rx.table.cell(stock.estimation),
        rx.table.cell(f"{stock.difference_value_euros}€ ({round(stock.difference_value_percentage, 2)}%)"),
        rx.table.cell(stock.status),
        background=get_color_style(stock)
    ) for stock in portfolio.stocks]
    body = rx.table.body(*rows)
    return rx.table.root(
        headers,
        body,
    )


app = rx.App()
app.add_page(index)
