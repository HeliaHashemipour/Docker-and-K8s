FROM tiangolo/uwsgi-nginx-flask:python3.11

LABEL maintainer="Helia Hashemipour  <heliahashemipour2@gmail.com>"

WORKDIR /code

COPY requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir -r /tmp/requirements.txt

ENV CACHE_EXPIRE_TIME 300
ENV CACHE_PORT 80
ENV COIN_NAME 'bitcoin'

COPY app.py /app/main.py
