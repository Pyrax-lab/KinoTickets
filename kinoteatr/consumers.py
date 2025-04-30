import json
import random, time


from channels.generic.websocket import WebsocketConsumer
from kino.models import Locals, Midlle_locals, Film
from django.shortcuts import get_object_or_404

class KinoWb(WebsocketConsumer):

    def connect(self):
        self.accept()
        
        
        

    def receive(self, text_data):
        curent_film = get_object_or_404(Film, name=text_data)
        locals = Midlle_locals.objects.filter(film_key = curent_film)
        count = locals[0].count_of_locals
      
        

        self.send(json.dumps({"message": count}))