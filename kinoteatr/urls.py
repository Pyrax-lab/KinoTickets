from django.urls import path 
from . import views

urlpatterns = [
    path("kino/<slug:kino_slug>/", views.film, name='film')
]
