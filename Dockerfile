FROM python:3.6-alpine

MAINTAINER Lezou Dali <lezou.dali@gmail.com>

ENV PYTHONPATH=/app/\
    PYTHONUNBUFFERED=1\
    PYTHONDONTWRITEBYTECODE=1

RUN pip install --upgrade pip && pip install pipenv

ADD . /app
WORKDIR /app


RUN pipenv install --system --skip-lock


EXPOSE 5000

CMD ["gunicorn", "--workers=2", "--bind=0.0.0.0:5000", "shortify.app"]
