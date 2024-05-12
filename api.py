from flask import Flask, jsonify

from portfolio import Portfolio

app = Flask(__name__)


@app.route('/stocks', methods=['GET'])
def get_portfolio():
    portfolio = Portfolio.build_from_file("stocks.yml")

    return jsonify(portfolio.transform_to_dict())


if __name__ == '__main__':
    app.run(debug=True)
