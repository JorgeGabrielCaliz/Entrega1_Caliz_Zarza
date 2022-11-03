from django.shortcuts import render

from django.http import HttpResponse
from AppCoder.models import Cartillas, Autorizaciones, Seguro_al_viajero, Plan

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def cartillas(request):
    if request.method != "POST":
        return render(request, "AppCoder/cartilla.html")
    
    cartillas = Cartillas(prestador=request.POST["prestador"], direccion=request.POST["direccion"], email=request.POST["email"])
    cartillas.save()
    return render(request, "AppCoder/datos_guardados.html")

def plan(request):
    if request.method != "POST":
        return render(request, "AppCoder/plan.html")
    
    plan = Plan(nombre_del_plan=request.POST["nombre_del_plan"], descripcion=request.POST["descripcion"], numero_de_afiliado=request.POST["numero_de_afiliado"])
    plan.save()
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
        afiliado = Plan.objects.filter(numero_de_afiliado=numero_de_afiliado_a_buscar)
        # afiliado = Afiliado.objects.all()


        contexto = {
            "numero_de_afiliado": numero_de_afiliado_a_buscar,
            "afiliados_encontrados": afiliado
        }
        
        return render(request, "AppCoder/resultado_busqueda.html", contexto)
    
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

class PlanList(ListView):
    model = Plan
    template_name = "AppCoder/plan_list.html"

class PlanDetalle(DetailView):
    model = Plan
    template_name = "AppCoder/plan_detalle.html"

class PlanCreacion(CreateView):
    model = Plan
    success_url = "/AppCoder/plan/list"
    fields = ["nombre_del_plan", "descripcion", "numero_de_afiliado"]

class PlanUpdateView(UpdateView):
    model = Plan
    success_url = "/AppCoder/plan/list"
    fields = ["nombre_del_plan", "descripcion"]

class PlanDelete(DeleteView):
    model = Plan
    success_url = "/AppCoder/plan/list"