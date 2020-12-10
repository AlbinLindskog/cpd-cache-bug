FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN pip install django==2.2.6 gunicorn==19.9.0

COPY ./docker/django/start /start
RUN sed -i 's/\r//' /start
RUN chmod +x /start

COPY ./django /app
WORKDIR /app
