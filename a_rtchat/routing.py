from django.urls import path
from .consumers import *

websocket_urlpatterns = [
    path("ws/chat-room/<chatroom_name>", ChatroomConsumer.as_asgi()),
    # path("ws/online-status/", OnlineStatusConsumer.as_asgi()),
]