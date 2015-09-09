from flask import render_template
from . import main


@main.route('/')
def home():
    '''Main view'''
    return render_template('index.html')
