from flask import request, Blueprint

prediction_app = Blueprint('prediction_app', __name__)


@prediction_app.route('/health', methods=['GET'])
def health():
    if request.method == 'GET':
        # _logger.info('health status OK')
        return 'ok'