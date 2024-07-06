#!/usr/bin/env python3
"""
Basic Flask app with Babel for i18n and locale selection
"""
from flask import Flask, render_template, request
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


@babel.localeselector
def get_locale():
    """
    Determine the best match for supported languages
    or force a specific locale if specified.
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Index route that renders the welcome page with translated text
    """
    return render_template('4-index.html',
                           title=gettext('home_title'),
                           header=gettext('home_header'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
