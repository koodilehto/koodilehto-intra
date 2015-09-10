from flask import render_template
from flask.ext.security import roles_required
from . import admin


@admin.route('/admin')
@roles_required('admin')
def view():
    return render_template('admin.html')
