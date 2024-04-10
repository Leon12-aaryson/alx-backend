#!/usr/bin/env python3
'''
instantiate babel in the python app module
'''

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    '''
    list of accepted configaration languages
    and regions
    '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.object('Config')


@app.route('/')
def index():
    '''
    use template render
    '''
    return render_template('1-index.html')
