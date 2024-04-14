"""
Main app.
"""

import logging
import logging.config

from aiohttp import web
from dotenv import load_dotenv

from .connector import TwilioClient
from .settings import LOGGING
from .views import routes

logging.config.dictConfig(LOGGING)
load_dotenv()


async def setup_app(app: web.Application) -> None:
    tc = TwilioClient()
    app['twilio_connect'] = tc


async def teardown_app(app: web.Application) -> None:
    ...


async def make_app() -> web.Application:
    app = web.Application()
    app.on_startup.append(setup_app)
    app.on_cleanup.append(teardown_app)
    app.add_routes(routes)
    return app
