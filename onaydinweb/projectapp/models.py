from django.db import models
from django.utils import timezone

class Professional_second(models.Model):
    title = models.CharField(max_length=50)
    max_proje = models.CharField(max_length=50)
    fiyati = models.IntegerField()
    metin = models.CharField(max_length=50)
    depolama_alani = models.CharField(max_length=50)
    ek_bilgi = models.CharField(max_length=50)
    ek_bilgi2 = models.CharField(max_length=50)
    bilgi2 = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.__class__.__name__}"

class Feature(models.Model):
    titlef = models.CharField(max_length=50)
    metinf = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.__class__.__name__}"

class Destlast(models.Model):
    titlel = models.CharField(max_length=50)
    name_date = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='img')

    def __str__(self):
        return f"{self.__class__.__name__}"

class Featurepricing(models.Model):
    ozellik = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.__class__.__name__}"