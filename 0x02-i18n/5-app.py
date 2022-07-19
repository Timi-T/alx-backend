#!/usr/bin/env python3
"""
Creating an i18n application
"""

from multiprocessing.sharedctypes import Value
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union, Dict


app = Flask(__name__)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config():
    """Configuration class for babel"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = 'UTC'


babel = Babel(app)


def get_user() -> Union[Dict, None]:
    """Get a user information"""
    id = request.args.get('login_as')
    if id:
        try:
            id = int(id)
        except ValueError:
            id = None
    if id:
        return users.get(id)
    return None


@app.before_request
def before_request() -> None:
    """Execute before other commands"""
    g.user = get_user()


@app.route("/")
def home() -> str:
    """Home page"""
    return render_template('5-index.html')


@babel.localeselector
def get_locale(locale=None) -> str:
    """Select Language"""
    locale = request.args.get('locale')
    if locale and locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(Config.LANGUAGES)


if __name__ == "__main__":
    app.run()
