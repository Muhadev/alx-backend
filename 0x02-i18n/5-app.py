#!/usr/bin/env python3
"""
Basic Flask app with user login emulation and i18n support
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext


class Config:
    """
    Configuration class for Babel
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)

# Mock user table (simulating a database)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id):
    """
    Returns the user dictionary based on user_id
    if found, otherwise returns None.
    """
    return users.get(user_id)


@app.before_request
def before_request():
    """
    Before request handler to check login_as
    parameter and set g.user if valid user.
    """
    user_id = request.args.get('login_as')
    if user_id and user_id.isdigit():
        g.user = get_user(int(user_id))
    else:
        g.user = None


@babel.localeselector
def get_locale():
    """
    Determine the best match for supported languages
    or force a specific locale if specified.
    """
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Index route that renders the welcome message
    based on user login status.
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
