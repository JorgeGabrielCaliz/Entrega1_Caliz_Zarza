from django.shortcuts import render

from django.http import HttpResponse

def mostrar_inicio(request):
    return HttpResponse ("hola mundo")

def empadronamiento(request):
    return render(request, "AppCoder/cursos.html")
    
def afiliado(request):
    return render(request, "AppCoder/cursos.html")
    
def cartillas(request):
    return render(request, "AppCoder/cursos.html")

def autorizaciones(request):
    return render(request, "AppCoder/cursos.html")

def seguro_al_viajero(request):
    return render(request, "AppCoder/cursos.html")