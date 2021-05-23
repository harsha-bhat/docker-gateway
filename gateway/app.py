from flask import Flask

from .backend import get_backend_details
from .proxy import create_proxy


def create_app(config):
    app = Flask(__name__)
    backends = get_backend_details(config["backends"])
    routes = config["routes"]

    @app.route("/")
    def index():
        return "<p>Gateway Service Running</p>"

    for route in routes:
        create_proxy(
            app, route["path_prefix"], route["backend"], backends[route["backend"]]
        )

    @app.errorhandler(404)
    def route_not_found(e):
        return (
            config["default_response"]["body"],
            config["default_response"]["status_code"],
        )

    return app
