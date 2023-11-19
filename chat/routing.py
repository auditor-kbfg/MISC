from django.urls import re_path

from .func.consumers import ChatConsumer

websocket_url=[
    # re_path(r'ws/chat/(?P<room_name>\w+)/$',ChatConsumer.as_asgi()),
    re_path(r'ws/chat/(?P<room_name>[\w-]+)/$',ChatConsumer.as_asgi()),
]