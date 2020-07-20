FROM python:3.6
MAINTAINER ckreuzberger@localhost

WORKDIR /app

COPY ./app/requirements /app/requirements

RUN pip install --no-cache-dir -r requirements/prod.txt

COPY ./app /app

COPY ./docker/prod/python/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

