import requests
from flask import request, Response

from . import stats
from .logging import logger

PROTOCOL = "http://"
METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]
EXCLUDE_HEADERS = [
    "content-encoding",
    "content-length",
    "transfer-encoding",
    "connection",
]


def create_proxy(app, prefix, name, backend):
    """Create a proxy route to respective backend container"""

    def proxy(*args, **kwargs):
        try:
            resp = requests.request(
                method=request.method,
                url=request.url.replace(
                    request.host_url, f"{PROTOCOL}{backend['host']}:{backend['port']}/"
                ),
                headers={
                    key: value for (key, value) in request.headers if key != "Host"
                },
                data=request.get_data(),
                cookies=request.cookies,
                allow_redirects=False,
            )

            headers = [
                (name, value)
                for (name, value) in resp.raw.headers.items()
                if name.lower() not in EXCLUDE_HEADERS
            ]

            response = Response(resp.content, resp.status_code, headers)
            stats.update_time(resp.elapsed.total_seconds() * 1000)
            stats.update_success()
        except:
            logger.error(f"Service unavailable: {name}")
            response = Response("Service Unavailable", 503)
            stats.update_error()

        return response

    proxy.__name__ = name

    app.route(f"{prefix}", methods=METHODS)(proxy)
    app.route(f"{prefix}/<path:path>", methods=METHODS)(proxy)
