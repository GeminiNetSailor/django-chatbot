# Django Chat Bot

## Content
- [Built With](#Built with)
- [Top-level directory layout](#Top-level directory layout)
- [Installation](#Installation)
- [Use bot own user for responses](#Use bot own user for responses)

## Built With
- [Django 3.0](https://docs.djangoproject.com/en/3.0/)
- [SQLite](https://www.sqlite.org)
- [Docker](https://www.docker.com/) & [Docker Compose](https://docs.docker.com/compose/)
    - Django Server Base Image [python:3.8-alpine](https://hub.docker.com/_/python)
    - RabbitMQ Base Image [rabbitmq:3.7-management-alpine](https://hub.docker.com/_/rabbitmq)
- For authentication we are using the Django built-in Auth [django.contrib.auth](https://docs.djangoproject.com/en/3.0/topics/auth/)
    - [Cookie-based user sessions](https://docs.djangoproject.com/en/3.0/topics/http/sessions/)
    - [Cross Site Request Forgery protection (csrf)](https://docs.djangoproject.com/en/3.0/ref/csrf/)
- [django Channels](https://channels.readthedocs.io/en/latest/) for WebSockets used by the Chat

### Top-level directory layout

    .
    ├── django_bot              # Reusable Django Bot package (Imported on django chat to process chat messages)
    ├── django_chat             # Main Django Project
    ├── stock_market            # Package to retrieval stock market data. (stooq.com connection)
    ├── docker-compose.yml      # File defining Docker services, networks and volumes.
    ├── Dockerfile              # Django Project Docker image configuration
    ├── entrypoint              # Django Project started commands
    ├── requirements.txt        # python package required for the project
    └── README.md

##Installation
- Make sure to have docker and Docker Compose running in your Machine.
- Make sure that no other service is using the port 8000.

*In case you need to change the port you can do it through the docker-compose.yml file
changing the port mapping for the server service.*

To start the containers Run the next command on the root of the project `/django_chat `
```sqlite-sql
> docker-compose up
```
The Django Web Application Chat will be running on [http://localhost:8000](http://localhost:8000) 

A RabbitMQ Management Console Will be accessible on the port `15672` [http://localhost:15672](http://localhost:15672)
The default access for the rabbitMq Console will be:
- User: guest 
- Password: guest

*For more information you can visit the Image Docker Hub [https://hub.docker.com/_/rabbitmq](https://hub.docker.com/_/rabbitmq)*

## Test
Django_bot test location is on django_bot/test

## Use bot own user for responses.
The Current Requirements for the project are *The post owner will be the bot.* but django_bot have their own bot users that can do the response.
you can enable this by settings `BOT_RESPONSE_AS_OWNER` to *false* in `django_chat/core/settings.py`
```
BOT_RESPONSE_AS_OWNER = False
```

