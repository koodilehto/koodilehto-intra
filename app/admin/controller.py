from flask import render_template, abort, redirect, url_for, request
from flask.ext.security import roles_required, current_user
from flask_admin.contrib.peewee import ModelView

# from . import admin as blueprint  # blueprint

# HACK probably not the prettiest way to initialize flask-admin views.
# Discussed at https://github.com/flask-admin/flask-admin/issues/910
# def create_admin(app=None, *args, **kwargs):
#     return Admin(app, *args, **kwargs)


# Create customized model view class
# https://github.com/flask-admin/flask-admin/blob/master/examples/auth/app.py
class MyModelView(ModelView):
    def is_accessible(self):
        if not current_user.is_active() or not current_user.is_authenticated():
            return False
        if current_user.has_role('admin'):
            return True
        return False

    def _handle_view(self, name, **kwargs):
        """
        Override builtin _handle_view in order to redirect users when a view is
        not accessible.
        """
        if not self.is_accessible():
            if current_user.is_authenticated():
                # permission denied
                abort(403)
            else:
                # login
                return redirect(url_for('security.login', next=request.url))
