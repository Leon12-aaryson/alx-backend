#!/usr/bin/env python3
'''
internationalize module
'''

from flask import Flask, render_template, request
from flask_babel import Babel, _


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    '''
    accepted languages
    '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    '''
    using the get_locale babel selector
    '''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    '''
    template render
    '''
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
