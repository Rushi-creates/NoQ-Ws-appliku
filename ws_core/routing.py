from django.urls import path
from ws_core import consumers
 

websocket_urlpatterns = [
    path('ws/queueUserLiveData/' , consumers.QueueLiveData.as_asgi()),



    # path('ws/jwc/' , consumers.QueueSocket.as_asgi()),
    # path('ws/queueUserWs/' , consumers.QueueUserSocket.as_asgi()),
    # path('ws/yourNumberWs/' , consumers.YourNumberWs.as_asgi()),
    # path('ws/scheduledNotificationWs/' , consumers.ScheduledNotificationWs.as_asgi()),
 ]
 