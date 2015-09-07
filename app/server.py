# Main initialization file

from flask import Flask
from flask.ext.script import Manager, Server
from flask.ext.bootstrap import Bootstrap
from authentication import authentication, login_manager
from index import index

# import authentication

app = Flask(__name__)
app.jinja_env.line_statement_prefix = '%'

Bootstrap(app)

app.config["SECRET_KEY"] = "ITSASECRET"

app.register_blueprint(authentication)
login_manager.init_app(app)

app.register_blueprint(index)


manager = Manager(app)
manager.add_command("dev", Server(host="localhost", port=5000,
                                  use_debugger=True, use_reloader=True))
manager.add_command("run", Server(host="0.0.0.0", port=5001,
                                  use_debugger=False, use_reloader=True))

#  manager.add_command("init_db", InitDb())
#  manager.add_command("drop_db", DropDb()) TODO

if __name__ == '__main__':
    manager.run()
