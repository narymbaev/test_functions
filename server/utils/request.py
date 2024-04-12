from .base import BaseAPI as ParentBaseAPI
from core.auth import auth


class BaseAPI(ParentBaseAPI):
    decorators = [auth.login_required()]
