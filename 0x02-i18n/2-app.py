#!/usr/bin/env python3
"""
Creating an i18n application
"""

from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
class Config():
    """Configuration class for babel"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = 'UTC'


babel = Babel(app)


@app.route("/")
def home() -> str:
    """Home page"""
    return render_template('2-index.html')


@babel.localeselector
def get_locale() -> str:
    return request.accept_languages.best_match(Config.LANGUAGES)


if __name__ == "__main__":
    app.run()
