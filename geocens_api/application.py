"""
application.py
- creates a Flask app instance and registers the database object
"""

from flask import Flask
from flask_cors import CORS


def create_app(app_name='GEOCENS_API'):
    app = Flask(app_name)
    app.config.from_object('geocens_api.config.BaseConfig')
    app.url_map.strict_slashes = False

    cors = CORS(app, resources={r"/*": {"origins": "*"}})

    from geocens_api.api.platform_api import platform_api

    app.register_blueprint(platform_api, url_prefix="/platform")

    return app
