FROM python:3.7-alpine

LABEL maintainer="Helia Hashemipour <heliahashemipour2@gmail.com>"

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY app.py ./

CMD python app.py