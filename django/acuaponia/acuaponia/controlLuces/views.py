from . models import Programacion_luces
# Create your views here.
from django.views.generic import (
    TemplateView,
    CreateView,
)

class Guardado(TemplateView):
    template_name="luces/guardado.html"

class Registro_Luces(CreateView):
    template_name= "luces/registro.html"
    model= Programacion_luces
    fields= ['hora_encendido', 'minuto_encendido', 'hora_apagado', 'minuto_apagado']
    success_url= "/guardado/"  

