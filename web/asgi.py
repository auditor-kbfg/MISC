"""
ASGI config for web project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter,URLRouter
from django.core.asgi import get_asgi_application
from channels.security.websocket import AllowedHostsOriginValidator
from chat.routing  import websocket_url

import chat.routing
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web.settings")	# mysite 는 django 프로젝트 이름
# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.
asgi_app=get_asgi_application()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web.settings')
application =ProtocolTypeRouter({
    "http":asgi_app,
    # "websocket":AllowedHostsOriginValidator([
    #         URLRouter(
    #             chat.routing.websocket_urlpatterns
    #         )
    #     ]
    # )
    "websocket":AllowedHostsOriginValidator(
            URLRouter(
                chat.routing.websocket_url
            )
    )
    # 장고 세션 사용하면 인증 필요시 사용
    # "websocket":AllowedHostsOriginValidator({  
    #     AuthMiddlewareStack(
    #         URLRouter(
    #             websocket_url
    #         ))
    #     }
    # )
})

#let socket = new WebSocket("ws://127.0.0.1:8000/chat/test1") 이렇게 client 에서 사용