from django.contrib import admin
from .models import Film,Locals 
# Register your models here.


@admin.register(Film)
class AdminFilm(admin.ModelAdmin):
    ...

@admin.register(Locals)
class AdminLocals(admin.ModelAdmin):
    ...
    