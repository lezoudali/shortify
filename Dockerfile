FROM ubuntu:18.04

RUN apt update && apt install python3-pip -y && pip3 install pipenv


COPY . /app
WORKDIR /app

RUN pipenv install --system


ENTRYPOINT