import uuid

from django.db import models
from django.contrib.auth import get_user_model 
# Create your models here.



User = get_user_model()



class Film(models.Model):
    slug = models.SlugField(max_length=250)
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    raiting = models.PositiveIntegerField(default=0)
    image = models.ImageField(blank=True, null=True, upload_to='image')
    

    def __str__(self):
        return f"Film {self.name}"


class Locals(models.Model):
    occupied = models.BooleanField(default=0)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    locals = models.ManyToManyField(Film, blank=True, null=True)
    meta = models.UUIDField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.id}"


class Midlle_locals(models.Model):
    film_key = models.OneToOneField(Film, on_delete=models.CASCADE)
    count_of_locals = models.PositiveIntegerField(default=0, blank=True, null=True)
    meta = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return f"{self.film_key} - {self.count_of_locals}"