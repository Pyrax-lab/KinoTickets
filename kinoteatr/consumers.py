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

        locals_midlle = Midlle_locals.objects.filter(film_key = curent_film)[0]
        count = locals_midlle.count_of_locals

        meta_info = locals_midlle.meta
        locals_list = list(Locals.objects.filter(meta=meta_info).values("occupied"))
        
        

        self.send(json.dumps({"message": count, "list_of_locals": locals_list}))