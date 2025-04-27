
from django.urls import path 

from .consumers import KinoWb

websocket_urlpatterns = [
    path('ws/kinozal/', KinoWb.as_asgi()),
]