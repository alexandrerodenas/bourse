from flask import Flask, jsonify

from portfolio import Portfolio
from stock import load_stocks_from_yaml

app = Flask(__name__)


@app.route('/portfolio', methods=['GET'])
def get_portfolio():
    portfolio = Portfolio(
        load_stocks_from_yaml("../stocks.yml")
    )

    return jsonify(portfolio.transform_to_dict())


if __name__ == '__main__':
    app.run(debug=True)
