FROM python:3.10.13-alpine

ENV WORK_DIR=/home/python

WORKDIR $WORK_DIR
COPY . $WORK_DIR

RUN apk update
RUN pip install --no-cache-dir -r requirements.txt
