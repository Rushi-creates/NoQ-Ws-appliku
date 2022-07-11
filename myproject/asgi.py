import os
from django.core.asgi import get_asgi_application
import django


from channels.routing import ProtocolTypeRouter , URLRouter
import ws_core.routing
os.environ.setdefault ( 'DJANGO_SETTINGS_MODULE' , 'myproject.settings' )
django.setup()


application = ProtocolTypeRouter ({
    'http' : get_asgi_application() ,
    'websocket' : URLRouter (
        ws_core.routing.websocket_urlpatterns
        )
})
