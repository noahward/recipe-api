from asgiref.wsgi import WsgiToAsgi

from recipe_api.config import config
from recipe_api.app_factory import init_app

app = init_app(config)

if __name__ == "__main__":
    app.run(host=config.server.host, port=config.server.port, debug=config.debug)
else:
    asgi_app = WsgiToAsgi(app)
