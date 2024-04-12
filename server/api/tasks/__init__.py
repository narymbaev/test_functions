from sanic import Blueprint
from .list import TasksView

tasks_bp = Blueprint('tasks', url_prefix='/tasks')

tasks_bp.add_route(TasksView.as_view(), '/')
