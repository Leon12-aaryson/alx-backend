#!/usr/bin/env python3
'''
use babel localeselector to specify the language
'''

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    '''
    accepted languages and reggions
    '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    '''
    get locale and accept languages
    '''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    '''
    renders template
    '''
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
