# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete_room/<int:id>/', views.delete_room, name='delete-room'),
    path('<str:room_name>/', views.room, name='room'),
]
