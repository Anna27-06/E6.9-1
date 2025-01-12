"""
ASGI config for Messenger project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import Back.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Messenger.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    # указание корневой конфигурации маршрутизации
    'websocket': AuthMiddlewareStack(
        URLRouter(
            Back.routing.websocket_urlpatterns
        )
    ),
})