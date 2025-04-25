from django.db import models

# Create your models here.


class Film(models.Model):
    slug = models.SlugField(max_length=250)
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    raiting = models.PositiveIntegerField(default=0)
    image = models.ImageField(blank=True, null=True, upload_to='image')


    def __str__(self):
        return f"Film {self.name}"
    