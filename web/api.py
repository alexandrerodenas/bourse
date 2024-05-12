from flask import Flask, jsonify

from core.history import History
from core.portfolio import Portfolio
from core.stock_metadata import StockMetadata

STOCKS_YML = "../stocks.yml"

app = Flask(__name__)


@app.route('/portfolio', methods=['GET'])
def get_current_portfolio():
    portfolio = Portfolio.build_from_file(STOCKS_YML)

    return jsonify(portfolio.transform_to_dict())


@app.route('/history', methods=['GET'])
def get_portfolio_history():
    history = History(
        StockMetadata.load_from_file(STOCKS_YML)
    )

    return jsonify(history.transform_to_dict())


if __name__ == '__main__':
    app.run(debug=True)
