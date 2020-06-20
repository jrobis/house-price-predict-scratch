from flask import request, Blueprint, jsonify, render_template

from xgboost_model import __version__ as _version
from api import __version__ as api_version

prediction_app = Blueprint('prediction_app', __name__)


@prediction_app.route('/', methods=['GET'])
def home():
    if request.method == 'GET':
        return render_template("home.html")


@prediction_app.route('/about', methods=['GET'])
def about():
    if request.method == 'GET':
        return render_template("about.html")


@prediction_app.route('/health', methods=['GET'])
def health():
    if request.method == 'GET':
        # _logger.info('health status OK')
        return 'ok'


@prediction_app.route('/version', methods=['GET'])
def version():
    if request.method == 'GET':
        return jsonify({'model_version': _version,
                        'api_version': api_version})


@prediction_app.route('/foo', methods=['GET'])
def foo():
    if request.method == 'GET':
        return "You did it!"
