#!/usr/bin/env python3
'''
internationalize module
'''

from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    '''
    accepted languages
    '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale():
    '''
    using the get_locale babel selector
    '''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def get_index() -> str:
    '''
    template render
    '''
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
