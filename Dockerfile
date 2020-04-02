FROM python:3.7-alpine
MAINTAINER Ayoub Bensakhria

#tells python to don't buffer the outputs and print them directly 
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN pip install -r requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D runner
USER runner