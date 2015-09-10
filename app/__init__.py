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
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    app.jinja_env.line_statement_prefix = '%'
    bootstrap.init_app(app)

    db.init_app(app)
    user_datastore = PeeweeUserDatastore(db, User, Role, UserRoles)
    security = Security(app, user_datastore)

    for Model in (Role, User, UserRoles):
        Model.drop_table(fail_silently=True)
        Model.create_table(fail_silently=True)
    user_datastore.create_user(email='jarkko.saltiola@koodilehto.fi',
                               password='topsecret')

    from .public import public as public_blueprint
    app.register_blueprint(public_blueprint)

    from .member import member as member_blueprint
    app.register_blueprint(member_blueprint)

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint)

    return app
