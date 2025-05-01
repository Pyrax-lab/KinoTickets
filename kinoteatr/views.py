from django.shortcuts import render
from kino.models import Film
from django.shortcuts import get_object_or_404

# Create your views here.
def film(request, kino_slug):
    curent_film = get_object_or_404(Film, slug=kino_slug)
    

    return render(request, "zal.html", context={'curent_film': curent_film})



def buy_place(request):
    
    