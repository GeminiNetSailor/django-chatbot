from django.conf import settings
from django.db import models


class Bot(models.Model):
    name = models.CharField("bot name", max_length=30, unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='bots', on_delete=models.CASCADE)
