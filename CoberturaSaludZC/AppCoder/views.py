from django.shortcuts import render

from django.http import HttpResponse
from AppCoder.models import Cartillas

def inicio(request):
    return render(request, "AppCoder/cursos.html")

def empadronamiento(request):
    return render(request, "AppCoder/cursos.html")
    
def afiliado(request):
    return render(request, "AppCoder/cursos.html")
    
def cartillas(request):
    if request.method != "POST":
        return render(request, "AppCoder/cartilla.html")
    
    cartillas = Cartillas(prestador=request.POST["prestador"], direccion=request.POST["direccion"], email=request.POST["email"])
    cartillas.save()
    return render(request, "AppCoder/inicio.html")


def autorizaciones(request):
    return render(request, "AppCoder/cursos.html")

def seguro_al_viajero(request):
    return render(request, "AppCoder/cursos.html")