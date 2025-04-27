from django.db import models

# Create your models here.
class Locals(models.Model):
    number_total = models.PositiveIntegerField(null=True, blank=True)
    occupied = models.PositiveIntegerField(null=True, blank=True)
    free = models.PositiveIntegerField(null=True, blank=True)
    
    

class Film(models.Model):
    slug = models.SlugField(max_length=250)
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    raiting = models.PositiveIntegerField(default=0)
    image = models.ImageField(blank=True, null=True, upload_to='image')
    locals = models.OneToOneField(Locals, on_delete=models.CASCADE)

    def __str__(self):
        return f"Film {self.name}"

class OneLocal(models.Model):



    

