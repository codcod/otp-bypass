# OTP Bypass with Twilio

[![Run validations](https://github.com/codcod/otp-bypass/actions/workflows/validate.yaml/badge.svg)](https://github.com/codcod/otp-bypass/actions/workflows/validate.yaml)

Little server that helps to bypass OTP using Twilio account.

    $ rye sync

    $ rye run db:schema
    $ rye run db:seed
    $ # rye run db:reset

    $ rye run server
    $ rye run build-image
    $ rye run container

    $ cat .env
    TWILIO_ACCOUNT_SID=AC304...
    TWILIO_AUTH_TOKEN=d59639...
    TWILIO_PHONE_NO=1...
    DEV_NGROK_SERVER=https://1b87-xx-xx-xx-xx.ngrok-free.app
    DEV_TWILIO_SENDER="+10000000000"
    DEV_TWILIO_RECIPIENT="+10000000000


Remember

    $ rye config --set-bool behavior.use-uv=true
