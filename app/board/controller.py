from flask import render_template
from flask.ext.security import roles_accepted
from . import board


@board.route('/board')
@roles_accepted('admin', 'board')
def view():
    return render_template('board.html')
