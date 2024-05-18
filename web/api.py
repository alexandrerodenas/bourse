import datetime
import logging
import os

from flask import Flask, jsonify, request
from flask_cors import CORS

from core.portfolio_factory import PortfolioFactory
from core.stock_metadata import StockMetadata
from core.yfinance_utils import get_last_dividend
from web.portfolio_web_service import PortfolioWebService

app = Flask(__name__)
CORS(app)


@app.route('/portfolio', methods=['GET'])
def get_current_portfolio():
    return portfolios_service.get_current_portfolio()


@app.route('/portfolio/all', methods=['GET'])
def get_portfolio_history():
    return portfolios_service.get_portfolios()


@app.route('/portfolio/gain-loss', methods=['GET'])
def get_gain_loss_history():
    stock_name = request.args.get('stock_name')
    if not stock_name:
        return portfolios_service.get_gain_loss_history()
    return portfolios_service.get_gain_loss_history_per_stock(stock_name)


@app.route('/portfolio/investment', methods=['GET'])
def get_investment_history():
    return portfolios_service.get_investment_evolution()


@app.route('/portfolio/stock-value', methods=['GET'])
def get_stock_values_history():
    start_date_str = request.args.get('start_date')
    if not start_date_str:
        return jsonify({'error': 'Missing start_date parameter'}), 400
    return portfolios_service.get_stock_values(start_date=start_date_str)


@app.route('/portfolio/dividend', methods=['GET'])
def get_dividend_calendar():
    return portfolios_service.get_dividend_calendar()

if __name__ == '__main__':
    app.config['CORS_HEADERS'] = 'Content-Type'
    logging.basicConfig(level="INFO", format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
    portfolios_service = PortfolioWebService(
        StockMetadata.load_from_file(
            os.getenv("STOCK_FILE", "../stocks.yml")
        )
    )
    app.run(host='0.0.0.0', port=8000)
