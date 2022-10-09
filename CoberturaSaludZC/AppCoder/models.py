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
    
class Afiliado(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    numero_de_afiliado = models.IntegerField()
    
class Cartillas(models.Model):
    prestador = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    email = models.EmailField()

class Autorizaciones(models.Model):
    estudio_a_realizar = models.CharField(max_length=30)
    numero_de_afiliado = models.EmailField()
    fecha_de_orden = models.DateField()

class Seguro_al_viajero(models.Model):
    numero_de_afiliado = models.EmailField()
    plan = models.CharField(max_length=30)
    destino = models.CharField(max_length=30)
    