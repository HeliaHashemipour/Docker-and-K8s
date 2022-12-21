FROM python:3.11.0a6-alpine3.15

LABEL maintainer="Helia Hashemipour  <heliahashemipour2@gmail.com>"

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD python app.py



