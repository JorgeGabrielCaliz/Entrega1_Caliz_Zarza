"""CoberturaSaludZC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include

from AppCoder.views import (
    inicio,
    empadronamiento,
    afiliado,
    cartillas,
    autorizaciones,
    seguro_al_viajero,
)

urlpatterns = [
    path('inicio/',inicio, name="inicio"),
    path('empadronamiento/', empadronamiento, name="empadronamiento"),
    path('afiliado/', afiliado, name="afiliado"),
    path('cartillas/', cartillas, name="cartillas"),
    path('autorizaciones/', autorizaciones, name="autorizaciones"),
    path('seguro_al_viajero/', seguro_al_viajero, name="seguro_al_viajero")
]