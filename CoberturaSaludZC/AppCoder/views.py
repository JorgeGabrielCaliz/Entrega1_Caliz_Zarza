from django.shortcuts import render

from django.http import HttpResponse
from AppCoder.models import Cartillas, Autorizaciones, Seguro_al_viajero

def inicio(request):
    return render(request, "AppCoder/inicio.html")
    
def cartillas(request):
    if request.method != "POST":
        return render(request, "AppCoder/cartilla.html")
    
    cartillas = Cartillas(prestador=request.POST["prestador"], direccion=request.POST["direccion"], email=request.POST["email"])
    cartillas.save()
    return render(request, "AppCoder/datos_guardados.html")


def autorizaciones(request):
    if request.method != "POST":
        return render(request, "AppCoder/autorizaciones.html")
    
    autorizaciones = Autorizaciones(estudio_a_realizar=request.POST["estudio_a_realizar"], numero_de_afiliado=request.POST["numero_de_afiliado"], fecha_de_orden=request.POST["fecha_de_orden"])
    autorizaciones.save()
    return render(request, "AppCoder/datos_guardados.html")

def seguro_al_viajero(request):
    if request.method != "POST":
        return render(request, "AppCoder/seguro_al_viajero.html")
    
    seguro_al_viajero = Seguro_al_viajero(numero_de_afiliado=request.POST["numero_de_afiliado"], plan=request.POST["plan"], destino=request.POST["destino"])
    seguro_al_viajero.save()
    return render(request, "AppCoder/datos_guardados.html")

def busqueda_2(request):
    return render(request, "AppCoder/busqueda_2.html")

def buscar_2(request):

    if not request.GET["numero_de_afiliado"]:
         return HttpResponse("No enviaste datos")
    else:
        numero_de_afiliado_a_buscar = request.GET["numero_de_afiliado"]
        afiliado = Afiliado.objects.filter(numero_de_afiliado=numero_de_afiliado_a_buscar)


        contexto = {
            "numero_de_afiliado": numero_de_afiliado_a_buscar,
            "afiliados_encontrados": afiliado
        }
        
        return render(request, "AppCoder/resultado_busqueda.html", contexto)
