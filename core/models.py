from django.core.exceptions import FieldError, ObjectDoesNotExist
from django.core.mail import send_mail
from django.db import models

from django.contrib.auth.models import AbstractUser

import geopy.distance
from django.db.models import signals
from django.dispatch import receiver


class User(AbstractUser):
    phone_number = models.CharField(max_length=10)
    description = models.TextField(blank=False, null=True)
    city_name = models.CharField(max_length=200)
    city_lat = models.CharField(max_length=100)
    city_lng = models.CharField(max_length=100)
    # TODO vérifier que la localisation n'existe pas avant de la créer


class Hosted(models.Model):
    localisation_radius = models.IntegerField()
    addictions = models.TextField(blank=True, null=True)
    video = models.FileField(blank=True, null=True)
    compensations = models.TextField(blank=True, null=True)

    hosted = models.OneToOneField('core.User', on_delete=models.CASCADE, related_name='hosted', null=True,
                                  blank=True, default=None)

    def __str__(self):
        return f'Hosted {self.hosted.username}'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        try:
            self.hosted.host
            raise FieldError("Un Utilisateur ne peut être à la fois Host et Hosted")
        except Host.DoesNotExist:
            super().save(force_insert, force_update, using, update_fields)

    def create(self):
        pass


class Host(models.Model):
    host = models.OneToOneField('core.User', on_delete=models.CASCADE, related_name='host', null=True, blank=True,
                                default=None)

    def __str__(self):
        return f'Host {self.host.username}'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        try:
            self.host.hosted
            raise FieldError("Un Utilisateur ne peut être à la fois Host et Hosted")
        except Hosted.DoesNotExist:
            super().save(force_insert, force_update, using, update_fields)


class City(models.Model):
    name = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name


@receiver(signals.post_save, sender=Host)
def host_post_save(sender, instance, created, *args, **kwargs):
    if created:
        hosteds = [i.hosted.email for i in Hosted.objects.all() if geopy.distance.vincenty(
            (i.hosted.city_lat, i.hosted.city_lng),
            (instance.host.city_lat, instance.host.city_lng)
        ) <= i.localisation_radius]
        send_mail('un hébergeur correspondant a vos critères a été trouvé !', instance.host.email,
                  'contact@heberge-un-sdf.fr', hosteds)


@receiver(signals.post_save, sender=Hosted)
def hosted_post_save(sender, instance, created, *args, **kwargs):
    if created:
        hosts = [i.host.email for i in Host.objects.all() if geopy.distance.vincenty(
            (i.host.city_lat, i.host.city_lng),
            (instance.hosted.city_lat, instance.hosted.city_lng)
        ) <= i.localisation_radius]
