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
    PlanList,
    PlanDelete,
    PlanDetalle,
    PlanUpdateView,
    PlanCreacion,
    inicio,
    cartillas,
    autorizaciones,
    seguro_al_viajero,
    plan,
    busqueda_2,
    buscar_2,
    #Login
    MyLogin,
    MyLogout,
    #Registrat y Editar Perfil
    register,
    editar_perfil,
    #AVATAR
    agregar_avatar,
    about,
)

urlpatterns = [
    path('inicio/',inicio, name="inicio"),
    path('cartillas/', cartillas, name="cartillas"),
    path('autorizaciones/', autorizaciones, name="autorizaciones"),
    path('seguro_al_viajero/', seguro_al_viajero, name="seguro_al_viajero"),
    path('plan/', plan, name="plan"),
    path("busqueda_2/", busqueda_2, name="busqueda_2"),
    path("buscar_2/", buscar_2),
    #
    path("plan/list", PlanList.as_view(), name="Planlist"),
    path("r'(?P<pk>\d+)^$'", PlanDetalle.as_view(), name="PlanDetail"),
    path("plan-nuevo/", PlanCreacion.as_view(), name="PlanNew"),
    path("r'editar/(?P<pk>\d+)^$'", PlanUpdateView.as_view(), name="PlanUpdate"),
    
    path("r'borrar/(?P<pk>\d+)^$'", PlanDelete.as_view(), name="PlanDelete"),
    path('',inicio,),

    #LOGIN
    path("login/", MyLogin.as_view(), name="login"),
    #LOGOUT
    path("logout/", MyLogout.as_view(), name="logout"),
    #REGISTRO
    path("register/", register, name="Register"),

    #EDITAR PERFL USUARIO
    path ("editar-perfil/", editar_perfil, name = "EditarPerfil"),

    #AGREGAR AVATAR
    path ("agregar-avatar/", agregar_avatar, name="AgregarAvatar"),
    

    #acerca de mi
    path("about/", about, name="AboutMe"),

    path("", inicio, name="inicio"),


]


