from django.core.exceptions import FieldError, ObjectDoesNotExist
from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.CharField(max_length=10)
    description = models.TextField(blank=False, null=True)


class Hosted(models.Model):
    localisation = models.CharField(max_length=100)
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


class Host(models.Model):
    ville = models.CharField(max_length=100)

    host = models.OneToOneField('core.User', on_delete=models.CASCADE, related_name='host', null=True, blank=True,
                                default=None)

    def __str__(self):
        return f'Host {self.host.username}'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        try:
            self.host.hosted
            raise FieldError("Un Utilisateur ne peut être à la fois Host et Hosted")
        except Host.DoesNotExist:
            super().save(force_insert, force_update, using, update_fields)
