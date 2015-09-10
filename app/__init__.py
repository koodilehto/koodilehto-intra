from flask import Flask
from flask.ext.bootstrap import Bootstrap
from playhouse.flask_utils import FlaskDB
from flask.ext.security import Security, PeeweeUserDatastore

from config import config

bootstrap = Bootstrap()

# create a peewee database instance -- our models will use this database to
# persist information
db = FlaskDB()

from .models import Role, User, UserRoles


def create_app(config_name):
    '''Flask application factory function'''
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    app.jinja_env.line_statement_prefix = '%'
    bootstrap.init_app(app)

    db.init_app(app)
    app.user_datastore = PeeweeUserDatastore(db, User, Role, UserRoles)
    security = Security(app, app.user_datastore)

    from .public import public as public_blueprint
    app.register_blueprint(public_blueprint)

    from .member import member as member_blueprint
    app.register_blueprint(member_blueprint)

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint)

    return app
