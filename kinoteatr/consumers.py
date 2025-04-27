from channels.generic.websocket import WebsocketConsumer
import json
import random, time
class KinoWb(WebsocketConsumer):
    def connect(self):
        self.accept() 


        