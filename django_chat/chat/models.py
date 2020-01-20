from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.db import models

User = get_user_model()

alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')


class Room(models.Model):
    name = models.CharField("Room name", max_length=30, unique=True, validators=[alphanumeric])
    owner = models.ForeignKey(User, related_name='chat_rooms', on_delete=models.CASCADE)


class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, related_name='chat_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
