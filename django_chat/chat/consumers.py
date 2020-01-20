# chat/consumers.py
# chat/consumers.py
import json
from django.conf import settings
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from django_bot import get_bot
from .models import Message, Room


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        self.user = self.scope["user"]

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        user = self.user
        # Send message to room group

        bot = get_bot(message)
        if bot:
            bot_response = bot.get_response()
            if bot_response:
                message = bot_response
                if settings.BOT_RESPONSE_AS_OWNER and settings.BOT_RESPONSE_AS_OWNER is False:
                    user = bot.user

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': user.username + ": " + message
            }
        )
        self.save_message(message, user)

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))

    def save_message(self, content, user):
        room = Room.objects.get(name=self.room_name)
        message = Message.objects.create(
            owner=user,
            content=content,
            room=room)

