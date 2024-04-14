import logging
import os
import typing as tp
from datetime import datetime

from twilio.base import values
from twilio.http.async_http_client import AsyncTwilioHttpClient
from twilio.rest import Client
from twilio.rest.api.v2010.account import incoming_phone_number, message


class TwilioClient:
    _client = None

    def __init__(self) -> None:
        if self._client is None:
            account_sid = os.environ['TWILIO_ACCOUNT_SID']
            auth_token = os.environ['TWILIO_AUTH_TOKEN']

            http_client = AsyncTwilioHttpClient()
            http_client.logger.setLevel(logging.DEBUG)

            self._client = Client(
                account_sid,
                auth_token,
                # region='ie1',
                # edge='frankfurt',
                http_client=http_client,
            )

    async def get_phone_numbers(  # noqa: PLR0913
        self,
        beta: tp.Union[bool, object] = values.unset,
        friendly_name: tp.Union[str, object] = values.unset,
        phone_number: tp.Union[str, object] = values.unset,
        origin: tp.Union[str, object] = values.unset,
        limit: tp.Optional[int] = None,
        page_size: tp.Optional[int] = None,
    ) -> tp.List[incoming_phone_number.IncomingPhoneNumberInstance]:
        return await self._client.incoming_phone_numbers.list_async(  # noqa: PLR0913
            beta=beta,
            friendly_name=friendly_name,
            phone_number=phone_number,
            origin=origin,
            limit=limit,
            page_size=page_size,
        )

    async def get_messages(  # noqa: PLR0913
        self,
        to: tp.Union[str, object] = values.unset,
        from_: tp.Union[str, object] = values.unset,
        date_sent: tp.Union[datetime, object] = values.unset,
        date_sent_before: tp.Union[datetime, object] = values.unset,
        date_sent_after: tp.Union[datetime, object] = values.unset,
        limit: tp.Optional[int] = None,
        page_size: tp.Optional[int] = None,
    ) -> tp.List[message.MessageInstance]:
        return await self._client.messages.list_async(
            to=to,
            from_=from_,
            date_sent=date_sent,
            date_sent_after=date_sent_after,
            date_sent_before=date_sent_before,
            limit=limit,
            page_size=page_size,
        )
