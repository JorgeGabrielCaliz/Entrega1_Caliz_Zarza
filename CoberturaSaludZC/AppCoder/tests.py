from django.test import TestCase

from AppCoder.models import Plan, Seguro_al_viajero

class ViewTestCase(TestCase):
    def test_crear_plan(self):
        plan = Plan.objects.create(nombre_del_plan= "test", descripcion= "test123", numero_de_afiliado= "999")
        todos_los_planes = Plan.objects.all()

        assert len(todos_los_planes) == 1
        assert todos_los_planes[0].nombre_del_plan == "test"
        assert todos_los_planes[0].descripcion == "test123"

class ViewTestCase(TestCase):
    def test_crear_Seguro(self):
        seguro = Seguro_al_viajero.objects.create(numero_de_afiliado= "1234", plan= "PLUS", destino= "mexico")
        todos_los_seguros = Seguro_al_viajero.objects.all()


        assert todos_los_seguros[0].plan == "PLUS"