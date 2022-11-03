from django.db import models

from django.contrib.auth.models import User


class Mensaje(models.Model):
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE)
    mensaje = models.CharField(max_length=100)
