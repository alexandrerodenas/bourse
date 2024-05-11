import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from typing import List
import pandas as pd
from portfolio import Portfolio
from stock import load_stocks_from_yaml, Stock


def create_stock_datatable(stocks: List[Stock]):
    def populate_treeview():
        for stock in stocks:
            # Color rows with negative difference in red
            if stock.difference_value_euros < 0:
                tree.insert('', 'end', values=(
                    stock.name,
                    stock.date,
                    stock.cost,
                    stock.current_price,
                    stock.difference_value_euros,
                    stock.difference_value_percentage,
                    stock.gain_or_deficit,
                    stock.number,
                    stock.status,
                    stock.estimation
                ), tags=('red_row',))
            else:
                tree.insert('', 'end', values=(
                    stock.name,
                    stock.date,
                    stock.cost,
                    stock.current_price,
                    stock.difference_value_euros,
                    stock.difference_value_percentage,
                    stock.gain_or_deficit,
                    stock.number,
                    stock.status,
                    stock.estimation
                ))

    def create_columns():
        tree.heading('Name', text='Name', command=lambda: sort_column('Name'))
        tree.heading('Date', text='Date', command=lambda: sort_column('Date'))
        tree.heading('Cost', text='Cost', command=lambda: sort_column('Cost'))
        tree.heading('Current Price', text='Current Price', command=lambda: sort_column('Current Price'))
        tree.heading('Difference (€)', text='Difference (€)', command=lambda: sort_column('Difference (€)'))
        tree.heading('Difference (%)', text='Difference (%)', command=lambda: sort_column('Difference (%)'))
        tree.heading('Gain/Deficit', text='Gain/Deficit', command=lambda: sort_column('Gain/Deficit'))
        tree.heading('Number', text='Number', command=lambda: sort_column('Number'))
        tree.heading('Status', text='Status', command=lambda: sort_column('Status'))
        tree.heading('Estimation', text='Estimation', command=lambda: sort_column('Estimation'))

        tree.column('Name', width=100)
        tree.column('Date', width=80)
        tree.column('Cost', width=80)
        tree.column('Current Price', width=100)
        tree.column('Difference (€)', width=120)
        tree.column('Difference (%)', width=120)
        tree.column('Gain/Deficit', width=100)
        tree.column('Number', width=80)
        tree.column('Status', width=80)
        tree.column('Estimation', width=120)

    def sort_column(col):
        data = [(tree.set(child, col), child) for child in tree.get_children('')]
        data.sort(reverse=reverse_sort[col])
        for index, item in enumerate(data):
            tree.move(item[1], '', index)
        reverse_sort[col] = not reverse_sort[col]

    root = tk.Tk()
    root.title("Stocks Data Table")

    tree = ttk.Treeview(root, columns=(
        'Name', 'Date', 'Cost', 'Current Price',
        'Difference (€)', 'Difference (%)', 'Gain/Deficit',
        'Number', 'Status', 'Estimation'
    ))

    reverse_sort = {col: False for col in ('Name', 'Date', 'Cost', 'Current Price',
                                           'Difference (€)', 'Difference (%)', 'Gain/Deficit',
                                           'Number', 'Status', 'Estimation')}

    create_columns()

    # Add tag configuration for red rows
    tree.tag_configure('red_row', background='red')

    populate_treeview()
    tree.pack(expand=True, fill='both')

    root.mainloop()


portfolio = Portfolio(load_stocks_from_yaml("stocks.yml"))
create_stock_datatable(portfolio.stocks)
