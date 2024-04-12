#!/usr/bin/env python3
"""
module to create logins
"""
from flask import Flask, g, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)

# Mock user database
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user(user_id):
    """
    Get user information from the mock database.

    Args:
        user_id (int): The ID of the user to retrieve.

    Returns:
        dict or None: A dictionary containing user information if the user is found,
        otherwise None.
    """
    return users.get(user_id)

@app.before_request
def before_request():
    """
    Execute before each request to set the global user.

    This function extracts the user ID from the request arguments and
    retrieves the corresponding user information from the mock database.
    It then sets the user information as a global variable on Flask's
    'g' object.
    """
    user_id = request.args.get('login_as', type=int)
    g.user = get_user(user_id) if user_id else None

@app.route('/')
def index():
    """
    Render the index page with a welcome message.

    Returns:
        str: HTML content to render.
    """
    if g.user:
        message = _("You are logged in as %(username)s.", username=g.user["name"])
    else:
        message = _("You are not logged in.")
    return render_template('index.html', message=message)

@babel.localeselector
def get_locale():
    """
    Determine the user's preferred language locale.

    This function is called by Flask-Babel to determine the language locale
    to use for localization. If the user is logged in and has a preferred
    locale, it will be used; otherwise, it falls back to the browser's
    preferred language.

    Returns:
        str: The selected language locale.
    """
    if g.user and g.user["locale"]:
        return g.user["locale"]
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])

if __name__ == '__main__':
    app.run(debug=True, port='0.0.0.0', port=5000)
