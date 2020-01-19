FROM python:3.8-alpine
ENV PYTHONUNBUFFERED 1

WORKDIR /src
VOLUME /src
ADD ./django_chat /src
COPY ./requirements.txt /

RUN apk update \
    && apk add --virtual base-build-deps gcc musl-dev libffi-dev python3-dev \
    && apk add --virtual openssl-build-dep openssl-dev \
    && pip install -r /requirements.txt \
    && apk del base-build-deps \
    && apk del openssl-build-dep

COPY ./entrypoint.sh /
RUN chmod +x /entrypoint.sh
RUN ["chmod", "+x", "/entrypoint.sh"]
ENTRYPOINT ["/entrypoint.sh"]