from flask import render_template
from . import public

@public.route('/')
def view():
    return render_template('index.html')
