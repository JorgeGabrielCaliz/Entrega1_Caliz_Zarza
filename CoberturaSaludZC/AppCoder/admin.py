from django.contrib import admin
from AppCoder.models import Cartillas, Autorizaciones, Seguro_al_viajero, Plan

# Register your models here.

admin.site.register(Plan)
admin.site.register(Cartillas)
admin.site.register(Autorizaciones)
admin.site.register(Seguro_al_viajero)
