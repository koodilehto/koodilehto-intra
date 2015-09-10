#!/usr/bin/env python
import os
from app import create_app, db
from app.models import User, Role
from flask import url_for
from flask.ext.script import Manager, Shell
from app.scripts import ResetDB, PopulateDB
# from flask.ext.migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)


def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)

manager.add_command("shell", Shell(make_context=make_shell_context))

manager.add_command('reset_db', ResetDB())
manager.add_command('populate_db', PopulateDB())


@manager.command
def list_routes():
    from tabulate import tabulate
    output = [["Endpoint function", "Methods", "Url"]]
    for rule in app.url_map.iter_rules():
        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)
        methods = ','.join(rule.methods)
        url = url_for(rule.endpoint, **options)
        output.append([rule.endpoint, methods, url])
    print(tabulate(output, headers="firstrow"))


@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()
