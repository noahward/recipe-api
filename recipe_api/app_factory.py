from flask import Flask
from omegaconf.dictconfig import DictConfig
from omegaconf.listconfig import ListConfig

from recipe_api.extensions import init_extensions


def init_app(config: DictConfig | ListConfig) -> Flask:
    app = Flask(__name__.split(".")[0])
    app.config.update(
        DEBUG=config.debug,
        SECRET_KEY=config.secret_key,
        SQLALCHEMY_DATABASE_URI=config.database_uri,
    )

    app = init_extensions(app)
    app = register_blueprints(app)

    return app


def register_blueprints(app: Flask) -> Flask:
    return app
