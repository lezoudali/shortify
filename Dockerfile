FROM python:3.6-alpine
LABEL maintainer='lezou.dali@gmail.com'

RUN pip3 install pipenv

WORKDIR '/usr/local/shortify'
COPY . .

RUN pipenv install --system


