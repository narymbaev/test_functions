import hashlib
import traceback
from functools import partial, wraps
from sanic import response
from sanic.request import Request
from typing import Optional, Tuple, Union

from core import errors


class Auth:
    app = None
    defined_user = {
        'id': 1,
        'username': 'username'
    }
    host_name = 'demo.kz'


    def initialize(self, app):
        self.app = app

    @classmethod
    def generate_token(cls, user_id) -> Optional[str]:
        if user_id:
            token = hashlib.md5()
            token.update(bytes(str(user_id), encoding='utf-8'))
            return token.hexdigest()
        else:
            return None

    @classmethod
    def generate_secret_sign(cls, user_id) -> Optional[str]:
        if user_id:
            sha256 = hashlib.sha256()
            sha256.update(bytes(str(user_id), encoding='utf-8'))
            sha256.update(b'somesalt#$%^&*(')
            return sha256.hexdigest()
        else:
            return None

    @classmethod
    def generate_password_hash(cls, username, password) -> Optional[str]:
        if username and password:
            sha256 = hashlib.sha256()
            sha256.update(bytes(password, encoding='utf-8'))
            sha256.update(b'somesalt#$%^&*(')
            sha256.update(bytes(username, encoding='utf-8'))
            return sha256.hexdigest()
        else:
            return None

    @classmethod
    async def unauthorized_handler(cls, _: Request):
        return response.json({'_success': False}, status=401)

    def login_required(
        self,
        route=None,
        *,
        role_ids: list = None,
        scopes: list = None,
        unauthorized_handler=None,
        lenient=False
    ):
        if route is None:
            return partial(
                self.login_required,
                role_ids=role_ids,
                scopes=scopes,
                unauthorized_handler=unauthorized_handler,
                lenient=lenient
            )

        @wraps(route)
        async def privileged(request, *args, **kwargs):
            session_id = request.headers.get('X-API-Token') or request.args.get('token') or request.cookies.get('sid')

            user = self.defined_user
            if user is None:
                if lenient:
                    resp = await route(request, *args, **kwargs)
                else:
                    if unauthorized_handler:
                        resp = await unauthorized_handler(request)
                    else:
                        resp = await self.unauthorized_handler(request)
            else:
                user.update({
                    'host_name': self.host_name,
                    'domain': self.host_name,
                    'token': session_id,
                })

                kwargs['user'] = user

                resp = await route(request, *args, **kwargs)

            return resp

        return privileged


    async def login(self, request, username, passwd) -> Tuple[bool, Union[dict, errors.Error]]:
        """
        Status
        is_blocked: 0
        is_correct: 1
        is_migrated: 2

        Replaced
        False: change password
        True: good
        """
        user = {
            'id': 1,
            'username': 'username'
        }
        return True, user

    @classmethod
    async def logout(cls, request) -> bool:
        try:
            request.ctx.session['_delete'] = True
        except Exception as e:
            traceback.print_exc()
            return False

        return True


auth = Auth()
