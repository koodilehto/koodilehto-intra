from flask import Flask
from flask.ext.bootstrap import Bootstrap
from playhouse.flask_utils import FlaskDB

from config import config

bootstrap = Bootstrap()

# create a peewee database instance -- our models will use this database to
# persist information
db = FlaskDB()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)

    app.jinja_env.line_statement_prefix = '%'
    bootstrap.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
