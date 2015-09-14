# http://pythonhosted.org/Flask-Testing/
from flask import current_app
from flask.ext.testing import TestCase
from app import create_app as the_create_app  # , db


class BasicsTestCase(TestCase):
    def create_app(self):
        return the_create_app('testing')

    # def setUp(self):
    #     self.app = create_app()
    #     self.app_context = self.app.app_context()
    #     self.app_context.push()
    #     # db.create_all()

    # def tearDown(self):
    #     # db.session.remove()
    #     # db.drop_all()
    #     self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])
