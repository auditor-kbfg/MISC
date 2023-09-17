from django.urls import re_path

from .func.consumer import *

websocket_urlpatterns=[
    re_path(r"chat/(?P<room_name>\w+)/$",ChatConsumer.as_asgi()),
]