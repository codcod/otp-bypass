import logging

from aiohttp import web
from aiohttp.web_request import Request
from aiohttp.web_response import Response
from twilio.twiml.messaging_response import MessagingResponse

from .connector import TwilioClient
from .json import dumps

routes = web.RouteTableDef()


@routes.post('/')
async def index(req: Request) -> Response:
    for count, value in enumerate(await req.json()):
        logging.info(f'{count}: {value}')

    resp = MessagingResponse()
    resp.message('The robots are coming')
    return web.Response(text=str(resp), content_type='text/xml')


@routes.get(r'/messages')
async def fetch_messages(req: Request) -> Response:
    tc = req.app['twilio_connect']
    messages = await tc.get_messages(limit=1)
    return web.json_response(messages, dumps=dumps)


@routes.get(r'/phones')
async def fetch_phones(req: Request) -> Response:
    tc: TwilioClient = req.app['twilio_connect']
    phones = await tc.get_phone_numbers(limit=1)
    return web.json_response(phones, dumps=dumps)
