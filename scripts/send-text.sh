#!/usr/bin/env sh
#
# shellcheck disable=SC1091
set +x

TIMESTAMP=$(date "+DATE: %D | TIME: %T")

. .env

curl -s -X POST \
    "https://api.twilio.com/2010-04-01/Accounts/$TWILIO_ACCOUNT_SID/Messages.json" \
    --data-urlencode "To=$DEV_TWILIO_RECIPIENT" \
    --data-urlencode "From=$DEV_TWILIO_SENDER" \
    --data-urlencode "Body=Test message sent from shell $TIMESTAMP" \
    -u "$TWILIO_ACCOUNT_SID:$TWILIO_AUTH_TOKEN"
