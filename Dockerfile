FROM python:3.8-alpine
ENV PYTHONUNBUFFERED 1

WORKDIR /src
VOLUME /src
ADD ./django_chat /src
COPY ./requirements.txt /

RUN apk update \
    && pip install -r /requirements.txt

COPY ./entrypoint.sh /
RUN chmod +x /entrypoint.sh
RUN ["chmod", "+x", "/entrypoint.sh"]
ENTRYPOINT ["/entrypoint.sh"]