import tkinter as tk
from tkinter import ttk

from portfolio import Portfolio


def populate_treeview(tree, portfolio):
    rows = []

    for stock in portfolio.stocks:
        row_values = [
            stock.name.capitalize(),
            stock.date,
            stock.cost,
            stock.current_price,
            stock.difference_value_euros,
            stock.difference_value_percentage,
            stock.number,
            stock.status,
            stock.estimation
        ]
        rows.append(row_values)

    rows.sort(key=lambda x: x[0])

    for row in rows:
        if row[4] < 0:  # Color rows with negative difference in red
            tree.insert('', 'end', values=row, tags=('red_row',))
        else:
            tree.insert('', 'end', values=row)


def create_columns(tree, reverse_sort):
    columns = [
        ('Name', 'Name'),
        ('Date', 'Date'),
        ('Cost', 'Cost'),
        ('Current Price', 'Current Price'),
        ('Difference (€)', 'Difference (€)'),
        ('Difference (%)', 'Difference (%)'),
        ('Number', 'Number'),
        ('Status', 'Status'),
        ('Estimation', 'Estimation')
    ]

    for col_id, col_name in columns:
        tree.heading(col_id, text=col_name, command=lambda col=col_id: sort_column(tree, col, reverse_sort))
        tree.column(col_id, width=80 if col_id == 'Date' else 120)


def sort_column(tree, col, reverse_sort):
    data = [(tree.set(child, col), child) for child in tree.get_children('')]
    data.sort(reverse=reverse_sort[col])
    for index, (val, child) in enumerate(data):
        tree.move(child, '', index)
    reverse_sort[col] = not reverse_sort[col]


def create_stock_datatable(portfolio: Portfolio):
    root = tk.Tk()
    root.title("Stocks Data Table")

    tree = ttk.Treeview(root, columns=(
        'Name', 'Date', 'Cost', 'Current Price',
        'Difference (€)', 'Difference (%)', 'Number', 'Status', 'Estimation'
    ))

    reverse_sort = {col: False for col in ('Name', 'Date', 'Cost', 'Current Price',
                                           'Difference (€)', 'Difference (%)', 'Number', 'Status', 'Estimation')}

    create_columns(tree, reverse_sort)

    tree.tag_configure('red_row', background='red')
    tree.tag_configure('total_row', font=('TkDefaultFont', 10, 'bold'))

    additional_info_label = tk.Label(root, text='')
    additional_info_label.pack()
    additional_info_label.config(text=f'''
        Investment: {portfolio.total_investment_amount():.2f}
        Total market value: {portfolio.total_market_value():.2f}
        Gain/Deficit: {portfolio.total_gain_or_deficit():.2f}
        ''')

    populate_treeview(tree, portfolio)
    tree.pack(expand=False)
    tree["show"] = "headings"

    root.mainloop()


portfolio = Portfolio.build_from_file("stocks.yml")
create_stock_datatable(portfolio)
