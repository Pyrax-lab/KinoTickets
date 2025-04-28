from django.contrib import admin
from .models import Film,Locals,Midlle_locals
# Register your models here.


@admin.register(Film)
class AdminFilm(admin.ModelAdmin):
    ...

@admin.register(Locals)
class AdminLocals(admin.ModelAdmin):
    ...
    
@admin.register(Midlle_locals)
class AdminMidlle_locas(admin.ModelAdmin):
    fields = ['film_key', 'count_of_locals']


    