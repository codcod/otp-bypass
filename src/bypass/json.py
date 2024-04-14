from functools import partial

import orjson
from aiohttp.web_response import Response
from twilio.rest.api.v2010.account import incoming_phone_number, message

__all__ = ['dumps']

DEFAULT_MESSAGE_FIELDS = [
    'account_sid',
    'api_version',
    'body',
    'date_created',
    'date_sent',
    'date_updated',
    'direction',
    'error_code',
    'error_message',
    'feedback',
    'from_',
    'media',
    'messaging_service_sid',
    'num_media',
    'num_segments',
    'price',
    'price_unit',
    'sid',
    'status',
    'subresource_uris',
    'to',
    'uri',
]


DEFAULT_PHONE_FIELDS = [
    'account_sid',
    'address_requirements',
    'address_sid',
    'api_version',
    'assigned_add_ons',
    'beta',
    'bundle_sid',
    'capabilities',
    'date_created',
    'date_updated',
    'emergency_address_sid',
    'emergency_address_status',
    'emergency_status',
    'friendly_name',
    'identity_sid',
    'origin',
    'phone_number',
    'sid',
    'sms_application_sid',
    'sms_fallback_method',
    'sms_fallback_url',
    'sms_method',
    'sms_url',
    'status',
    'status_callback',
    'status_callback_method',
    'trunk_sid',
    'uri',
    'voice_application_sid',
    'voice_caller_id_lookup',
    'voice_fallback_method',
    'voice_fallback_url',
    'voice_method',
    'voice_receive_mode',
    'voice_url',
]


def default(obj):
    def _list_into_dict(keys, obj):
        pairs = [(k, getattr(obj, k)) for k in keys]
        return {k: v for k, v in pairs}

    if isinstance(obj, message.MessageInstance):
        keys = DEFAULT_MESSAGE_FIELDS
        return _list_into_dict(keys, obj)
    if isinstance(obj, incoming_phone_number.IncomingPhoneNumberInstance):
        keys = DEFAULT_PHONE_FIELDS
        return _list_into_dict(keys, obj)


dump = partial(orjson.dumps, default=default)  # returns bytes instead of str


def dumps(resp: Response) -> str:
    return dump(resp).decode('utf-8')
