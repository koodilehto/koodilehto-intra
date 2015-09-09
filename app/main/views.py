from flask import render_template
from flask.ext.security import login_required
from . import main


@main.route('/')
@login_required
def home():
    '''Main view'''
    return render_template('index.html')
