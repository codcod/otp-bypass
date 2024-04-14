#!/usr/bin/env sh
#
# shellcheck disable=SC1091
set +x

. .env

curl -Gs \
    "https://api.twilio.com/2010-04-01/Accounts/$TWILIO_ACCOUNT_SID/IncomingPhoneNumbers.json" \
    -u "$TWILIO_ACCOUNT_SID:$TWILIO_AUTH_TOKEN"
