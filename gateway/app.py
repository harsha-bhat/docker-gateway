from flask import Flask

from .backend import get_backend_details
from .proxy import create_proxy
from . import stats


def create_app(config):
    """Create flask app"""
    app = Flask(__name__)
    routes = config["routes"]

    @app.route("/")
    def index():
        return "<p>Gateway Service Running</p>"

    for route in routes:
        create_proxy(app, route["path_prefix"], route["backend"], config["backends"])

    @app.errorhandler(404)
    def route_not_found(e):
        stats.update_error()
        return (
            config["default_response"]["body"],
            config["default_response"]["status_code"],
        )

    @app.route("/stats")
    def get_stats():
        return stats.get_stats()

    return app
