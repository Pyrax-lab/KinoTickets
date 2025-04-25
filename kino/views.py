from django.shortcuts import render
from .models import Film 
# Create your views here.

def all_films(request):
    films = Film.objects.all()
    return render(request, 'kino.html', context={"films": films})

