
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Midlle_locals, Locals

# sender – класс модели, которая отправила сигнал.

# instance – экземпляр модели.

# created (bool) – True, если объект только что создан (актуально для post_save).


@receiver(post_save, sender=Midlle_locals)
def create_locals(sender, instance, created, **kwargs):
    if created : 
        
        count = instance.count_of_locals
        film = instance.film_key
        meta = instance.meta

        for i in range(count):
            local_instance = Locals.objects.create(meta = meta)
            local_instance.locals.add(film)


@receiver(post_delete, sender=Midlle_locals)
def delete_locals(sender, instance, **kwargs):
    count = instance.count_of_locals
    film = instance.film_key 
    meta_info = instance.meta

    local_instance = Locals.objects.filter(meta = meta_info)

    for i in local_instance:
        i.locals.clear()
        i.delete()