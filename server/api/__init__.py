from sanic import Blueprint
from .tasks import tasks_bp
from .customers import customers_bp

api = Blueprint('api')

api_bp = Blueprint.group(
    api,
    customers_bp,
    tasks_bp,
    url_prefix='/api',
)

