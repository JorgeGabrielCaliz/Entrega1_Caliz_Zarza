from encodings import normalize_encoding
from logging.config import dictConfig
from django.db import models

# Create your models here.

class Plan(models.Model):
    nombre_del_plan = models.CharField(max_length = 30)
    descripcion = models.CharField(max_length=100)
    numero_de_afiliado = models.IntegerField()
    
class Cartillas(models.Model):
    prestador = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    email = models.EmailField()

class Autorizaciones(models.Model):
    estudio_a_realizar = models.CharField(max_length=30)
    numero_de_afiliado = models.IntegerField()
    fecha_de_orden = models.DateField()

class Seguro_al_viajero(models.Model):
    numero_de_afiliado = models.IntegerField()
    plan = models.CharField(max_length=30)
    destino = models.CharField(max_length=30)
