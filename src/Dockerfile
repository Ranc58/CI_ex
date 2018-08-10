FROM alpine

LABEL author="Aleshin Vladimir <rancvova@gmail.com>"
LABEL description="Docker file with tornado API"


RUN apk update && apk upgrade && \
  apk add --update bash python3 python3-dev postgresql-client postgresql-dev build-base gettext
ENV PYTHONPATH /data/web

RUN mkdir -p /data/web
WORKDIR /data/web
COPY . /data/web

RUN pip3 install -r requirements.txt


ENTRYPOINT ["/data/web/entrypoint.sh", "start"]
