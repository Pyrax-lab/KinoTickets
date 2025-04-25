from django.contrib import admin
from .models import Film 
# Register your models here.


@admin.register(Film)
class AdminFilm(admin.ModelAdmin):
    ...