from django.db import models


class Avto(models.Model):
    nomi = models.CharField(max_length=255)
    narxi = models.PositiveIntegerField()
    yili = models.PositiveSmallIntegerField()
