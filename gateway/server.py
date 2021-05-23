import click
import bjoern

from .config import load_config
from .app import create_app
from .logging import logger


@click.command()
@click.option("--port", default=8080, type=int)
@click.option("--config", required=True, type=str)
def run(port, config):
    """Starts the server"""
    logger.info(f"Loading config file: {config}")
    settings = load_config(config)

    app = create_app(settings)

    logger.info(f"Starting server on port: {port}")
    bjoern.run(app, "127.0.0.1", port)
