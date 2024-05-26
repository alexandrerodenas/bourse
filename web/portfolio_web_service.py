from flask import jsonify

from core.dividend import Dividend
from core.portfolio import Portfolio
from core.portfolio_factory import PortfolioFactory
from core.stock_metadata import StockMetadata
from core.yfinance_utils import download_history, get_last_dividend


class PortfolioWebService:

    def __init__(self, stock_metadata: [StockMetadata]):
        self._stock_metadata = stock_metadata
        self._portfolios = PortfolioFactory.build_portfolio_history(stock_metadata)
        self._dividends = [
            Dividend(
                name=metadata.name,
                stock_metadata=metadata,
                **get_last_dividend(metadata.symbol)
            )
            for metadata in self._stock_metadata
        ]

    def get_current_portfolio(self):
        return jsonify(self._portfolios[-1].transform_to_dict())

    def get_portfolios(self):
        return jsonify([
            portfolio.transform_to_dict()
            for portfolio in self._portfolios
        ])

    def get_gain_loss_history(self):
        return jsonify([
            {
                "name": "gain loss",
                "data": [(portfolio.date.strftime('%Y-%m-%d'), round(portfolio.total_gain_or_deficit(), 2))
                         for portfolio in self._portfolios]
            }
        ])

    def get_gain_loss_history_per_stock(self, stock_name):
        return jsonify([
            {
                "name": f"gain loss for " + stock_name,
                "data": [
                    (
                        portfolio.date.strftime('%Y-%m-%d'),
                        self._get_stock_gain_or_deficit(portfolio, stock_name)
                    )
                    for portfolio in self._portfolios
                ]
            }
        ])

    def get_investment_evolution(self):
        return jsonify([
            {
                "name": "total_market_value",
                "data": [(portfolio.date.strftime('%Y-%m-%d'), round(portfolio.total_market_value(), 2))
                         for portfolio in self._portfolios]
            },
            {
                "name": "total_investment_amount",
                "data": [
                    (portfolio.date.strftime('%Y-%m-%d'), round(portfolio.total_investment_amount(), 2))
                    for portfolio in self._portfolios
                ]
            },
        ])

    def get_stock_values(self, start_date: str):
        stock_values = []
        symbols = [stock.symbol for stock in self._portfolios[-1].stocks]
        data = download_history(symbols, start_date)
        closes = data['Close']
        for column in closes.columns:
            stock_symbol = column.split('.')[0]
            values = closes[column].reset_index().values.tolist()
            stock_values.append({
                "name": [stock.name for stock in self._portfolios[-1].stocks if stock.symbol == f'{stock_symbol}.PA'][
                    0],
                "data": [[value[0].strftime('%Y-%m-%d'), value[1]] for value in values]
            })
        return jsonify(stock_values)

    def get_dividends(self):
        return [
            dividend.transform_as_dict()
            for dividend in self._dividends
        ]


    @staticmethod
    def _get_stock_gain_or_deficit(portfolio, stock_name):
        stock = portfolio.get_stock_by_name(stock_name)
        if stock:
            return round(stock.gain_or_deficit, 2)
        return 0


