from flask import Blueprint, render_template

from flask.ext.login import login_required

index = Blueprint('index', __name__)


@index.route('/')
@login_required
def home():
    '''Main view'''
    return render_template('index.html')
