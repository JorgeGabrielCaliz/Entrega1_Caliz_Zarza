from django.shortcuts import render

from django.http import HttpResponse

from AppCoder.models import Cartillas, Autorizaciones, Seguro_al_viajero, Plan

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from AppCoder.models import Avatar
from datetime import date
from datetime import datetime



@login_required
def inicio(request):
    return render(request, "AppCoder/inicio.html")


def about(request):
    return render(request, "AppCoder/about.html")


from AppCoder.models import Cartillas, Autorizaciones, Seguro_al_viajero

def inicio(request):
    avatar = Avatar.objects.filter(user=request.user.id).first()
    if avatar is not None:
        contexto = {"avatar": avatar.imagen.url}
    else:
        contexto = {}

    return render(request, "AppCoder/inicio.html", contexto)

    
@login_required
def cartillas(request):
    if request.method != "POST":
        return render(request, "AppCoder/cartilla.html")
    
    cartillas = Cartillas(prestador=request.POST["prestador"], direccion=request.POST["direccion"], email=request.POST["email"])
    cartillas.save()
    return render(request, "AppCoder/datos_guardados.html")

@login_required
def plan(request):
    if request.method != "POST":
        return render(request, "AppCoder/plan.html")
    
    plan = Plan(nombre_del_plan=request.POST["nombre_del_plan"], descripcion=request.POST["descripcion"], numero_de_afiliado=request.POST["numero_de_afiliado"])
    plan.save()
    return render(request, "AppCoder/datos_guardados.html")

@login_required
def autorizaciones(request):
    if request.method != "POST":
        return render(request, "AppCoder/autorizaciones.html")
    
    autorizaciones = Autorizaciones(estudio_a_realizar=request.POST["estudio_a_realizar"], numero_de_afiliado=request.POST["numero_de_afiliado"], fecha_de_orden=request.POST["fecha_de_orden"])
    autorizaciones.save()
    return render(request, "AppCoder/datos_guardados.html")

@login_required
def seguro_al_viajero(request):
    if request.method != "POST":
        return render(request, "AppCoder/seguro_al_viajero.html")
    
    seguro_al_viajero = Seguro_al_viajero(numero_de_afiliado=request.POST["numero_de_afiliado"], plan=request.POST["plan"], destino=request.POST["destino"])
    seguro_al_viajero.save()
    return render(request, "AppCoder/datos_guardados.html")

@login_required
def busqueda_2(request):
    return render(request, "AppCoder/busqueda_2.html")

@login_required
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
from django.urls import reverse



from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from AppCoder.forms import AvatarForm, UserEditionForm
import datetime




class PlanList(LoginRequiredMixin, ListView):
    model = Plan
    template_name = "AppCoder/plan_list.html"

class PlanDetalle(LoginRequiredMixin, DetailView):
    model = Plan
    template_name = "AppCoder/plan_detalle.html"

class PlanCreacion(LoginRequiredMixin, CreateView):
    model = Plan
    success_url = "/AppCoder/plan/list"
    fields = ["nombre_del_plan", "descripcion", "numero_de_afiliado"]


class PlanUpdateView(LoginRequiredMixin, UpdateView):
    model = Plan
    success_url = "/AppCoder/plan/list"
    fields = ["nombre_del_plan", "descripcion"]

class PlanDelete(LoginRequiredMixin, DeleteView):
    model = Plan
    success_url = "/AppCoder/plan/list"



class MyLogin(LoginView):
    template_name = "AppCoder/login.html"

class MyLogout(LoginRequiredMixin, LogoutView):
    template_name = "AppCoder/logout.html"

#REGISTRO
def register(request):
    if request.method == "POST":
        form  = UserCreationForm(request.POST)
        if form.is_valid():
            username_capturado = form.cleaned_data["username"]
            form.save()

            return render(request, "AppCoder/inicio.html", {"mensaje": f"{username_capturado} se ha empadronado correctamente"})

    else:
        form = UserCreationForm()
    
    return render(request, "AppCoder/registro.html", {"form": form})


#EDITAR PERFIL
@login_required
def editar_perfil(request):
    user = request.user

    if request.method !="POST":
        form = UserEditionForm (initial={"email":user.email})

    else:
        form = UserEditionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user.email = data["email"]
            user.first_name = data ["first_name"]
            user.last_name = data ["last_name"]
            user.set_password (data["password1"])
            user.save()
            return render(request, "AppCoder/inicio.html")

    contexto = {"user":user, "form": form}
    return render (request, "AppCoder/editarPerfil.html", contexto)

#AVATAR
@login_required
def agregar_avatar(request):
    if request.method != "POST":
        form = AvatarForm()
    else:
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            Avatar.objects.filter(user=request.user).delete()
            form.save()
            return render(request, "AppCoder/inicio.html")

    contexto = {"form": form}
    return render(request, "AppCoder/avatar_form.html", contexto)

def fecha(request):
    momento="<h1> hoy es:{0}</h1>".format(datetime.datetime.now().strftime("%A %D/%m/%Y %H:%M:%S"))
    return HttpResponse(momento)
