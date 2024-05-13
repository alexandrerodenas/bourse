import datetime
import logging
import os

from flask import Flask, jsonify, request
from flask_cors import CORS

from core.history import History

app = Flask(__name__)
CORS(app)


@app.route('/portfolio', methods=['GET'])
def get_current_portfolio():
    return jsonify(history.get_current_portfolio().transform_to_dict())


@app.route('/history', methods=['GET'])
def get_portfolio_history():
    return jsonify(history.transform_to_dict())


@app.route('/history/gain-loss', methods=['GET'])
def get_gain_loss_history():
    return jsonify(history.get_gain_loss_history())


@app.route('/history/investment', methods=['GET'])
def get_investment_history():
    return jsonify(history.get_investment_evolution())


@app.route('/history/stock-values', methods=['GET'])
def get_stock_values_history():
    start_date_str = request.args.get('start_date')
    if not start_date_str:
        return jsonify({'error': 'Missing start_date parameter'}), 400

    return jsonify(history.get_stock_values(start_date_str))


if __name__ == '__main__':
    app.config['CORS_HEADERS'] = 'Content-Type'
    logging.basicConfig(level="INFO", format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
    history = History.build_from_file(os.getenv("STOCK_FILE", "../stocks.yml"))
    app.run(host='0.0.0.0', port=8000)
