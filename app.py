from flask import Flask, jsonify
from config import Config
from logging_setup import setup_logging

app = Flask(__name__)
app.config.from_object(Config)
setup_logging(app.config['LOG_LEVEL'])

@app.route('/')
def index():
    return jsonify(app='minimal-flask-demo', status='ok', message='Minimal Flask app is running')

@app.route('/health')
def health():
    return jsonify(status='healthy')

if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'])