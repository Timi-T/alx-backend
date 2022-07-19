#!/usr/bin/env python3
"""
Creating an i18n application
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config():
    """Configuration class for babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config(Config())
babel = Babel()


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def home():
    return render_template('0-index.html', home_header=_("opeyemi"))


if __name__ == "__main__":
    app.run()
