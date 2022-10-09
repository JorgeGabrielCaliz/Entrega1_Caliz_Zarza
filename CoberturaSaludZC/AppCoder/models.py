from encodings import normalize_encoding
from logging.config import dictConfig
from django.db import models

# Create your models here.

class Empadronamiento(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dni = models.IntegerField()
    plan = models.CharField(max_length=30)
    email = models.EmailField()
    