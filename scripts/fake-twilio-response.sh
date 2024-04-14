#!/usr/bin/env sh
# shellcheck disable=SC1091
set +x

. .env

CONTENT="./scripts/fake-twilio-response-content.json"

if type http > /dev/null 2>&1; then
    http POST "$DEV_NGROK_SERVER" @"$CONTENT"
else
    curl \
    -X POST \
    -H "Content-Type: application/json" \
    -H "Accepts: application/xml" \
    -d @"$CONTENT" \
    "$DEV_NGROK_SERVER"
fi
