from flask import request, Blueprint, jsonify, render_template

from api.form_model import InputForm
from xgboost_model.predict import make_prediction
from xgboost_model import __version__ as _version
from api import __version__ as api_version

prediction_app = Blueprint('prediction_app', __name__)


# @prediction_app.route('/', methods=['GET'])
# def home():
#     if request.method == 'GET':
#         return render_template("home.html")


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


@prediction_app.route('/', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():

        data = {'title': form.title.data
                                  , 'address': form.address.data
                                  , 'city': form.city.data
                                  , 'state': form.state.data
                                  , 'postal_code': form.postal_code.data
                                  , 'facts and features': form.facts_and_features.data
                                  , 'real estate provider': form.real_estate_provider
                                  , 'url': form.url}
        result = make_prediction(data)
    else:
        result = None

    return render_template('home.html', form=form, result=result)

