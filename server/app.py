import locale

from sanic import Sanic, response

from api import api_bp


class App(Sanic):

    def __init__(self):
        super().__init__(name='qbox-deployment')

    def set_config(self, **kwargs):
        for attr, value in kwargs.items():
            self.config.__setattr__(attr, value)


app = App()


@app.route('/', methods=['GET', 'HEAD'], name='root_index')
async def index(request):
    return response.html('<html>Welcome</html>', status=200)


@app.before_server_start
async def before_server_start(_app, _loop):
    locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')


@app.before_server_stop
async def before_server_stop(_app, _loop):
    app.purge_tasks()


app.blueprint([
    api_bp
])