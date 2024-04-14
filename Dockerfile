# syntax=docker/dockerfile:1

FROM python:3.12-alpine AS compile-image

RUN apk --update --no-cache add gcc build-base
RUN python -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.lock .

RUN sed '/-e/d' requirements.lock > requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.12-alpine AS build-image
COPY --from=compile-image /opt/venv /opt/venv

RUN apk add --no-cache tzdata

ENV TZ=Europe/Warsaw
ENV PATH="/opt/venv/bin:$PATH"
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONPATH=src

WORKDIR /opt/stelo
COPY . .

EXPOSE 80

ENTRYPOINT ["gunicorn"]
CMD ["bypass.server:make_app", "--bind=0.0.0.0:80", "--workers=2", "-k aiohttp.GunicornWebWorker"]
