from sanic import Blueprint
from .list import CustomersView

customers_bp = Blueprint('customers', url_prefix='/customers')

customers_bp.add_route(CustomersView.as_view(), '/')
