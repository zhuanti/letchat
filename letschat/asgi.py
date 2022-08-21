"""
ASGI config for letschat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
import letschat_app.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'letschat.settings')
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            letschat_app.routing.websocket_urlpatterns
        )
    ),
})
