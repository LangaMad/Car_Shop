FROM python:3.10-slim
RUN mkdir car_shop
WORKDIR car_shop
ADD . /car_shop/
ADD .env.docker /car_shop/.env
# Устанавливаем зависимости PostgreSQL
RUN apt-get update && apt-get install -y libpq-dev gcc
ENV APP_NAME = DOCKER_DEMO
RUN pip install -r requirements.txt
CMD gunicorn config.wsgi:application -b 0.0.0.0:8000













