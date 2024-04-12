from sanic import Blueprint
from .tasks import tasks_bp
from .customers import customer_bp

api = Blueprint('api')

api_bp = Blueprint.group(
    api,
    customer_bp,
    tasks_bp,
    url_prefix='/api',
)

