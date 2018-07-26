# Pull base image
FROM python:3.6-alpine
MAINTAINER Lezou Dali <lezou.dali@gmail.com>

# Ensures that console output is not buffered by Docker
ENV PYTHONDONTWRITEBYTECODE 1

# Ensures that Python does not write `.pyc` files
ENV PYTHONUNBUFFERED 1

ENV PYTHONPATH /app/shortify


# Set work directory
WORKDIR /app

# Install dependencies
RUN pip install --upgrade pip && pip install pipenv

COPY . /app
RUN pipenv install --system --skip-lock


CMD ["gunicorn", "--workers=2", "--bind=0.0.0.0:8000", "shortify.app"]

