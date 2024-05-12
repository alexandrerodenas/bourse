import logging
import os

from flask import Flask, jsonify
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


if __name__ == '__main__':
    app.config['CORS_HEADERS'] = 'Content-Type'
    logging.basicConfig(level="INFO", format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
    history = History.build_from_file(os.getenv("STOCK_FILE"))
    app.run(host='0.0.0.0', port=8000)
