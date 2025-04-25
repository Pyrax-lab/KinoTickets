from django.shortcuts import render
from kino.models import Film
from django.shortcuts import get_object_or_404

# Create your views here.
def film(request, kino_slug):
    current_film = get_object_or_404(Film, slug=kino_slug)
    print(current_film)