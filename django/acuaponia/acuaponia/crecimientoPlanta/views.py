from django.shortcuts import render
from django.http import HttpResponse
from Raspberry.camara import AlturaPlanta
from Raspberry.camara.webcam import AlturaPlantaCam
import cv2
#from Raspberry.camara import AlturaPlanta
from . models import Monitoreo, Plantas, Referencia_Medicion, TipoPlanta

# Create your views here.
from django.views.generic import(
    TemplateView,
    CreateView,
)

def tomar_foto(request):
    planta_default=Plantas.objects.get(id=1)
    #image = cv2.imread('Raspberry/camara/Fotos/flower1.jpg')
    #Altura_planta=AlturaPlanta.capturar_altura(image)
    referencia = Referencia_Medicion.objects.last().altura_referencia
    Altura_planta=AlturaPlantaCam.cam_altura(referencia)
    if Altura_planta == 0.0:
        html="<html><title>Altura capturada</title><body>La camara no detecta ningun objeto: Coloque la guia dentro del angulo de la camara y posicionada a la izquierda de la planta a capturar</body></html>" 
        return HttpResponse(html)
    elif Altura_planta == 0.1:
        html="<html><title>Altura capturada</title><body>La camara solo detecta la guia: actualmente no se detecta ninguna planta</body></html>" 
        return HttpResponse(html)
    else:
        Monitoreo.objects.create(id_planta=planta_default, altura=Altura_planta)
        html = "<html><title>Altura capturada</title><body>Se guardo la altura correctamente: %s </body></html>" %Altura_planta 
        return HttpResponse(html)

class ReferenciaGuardada(TemplateView):
    template_name= "capturar/AlturaReferenciaGuardado.html"

class Registrar_Altura_Referencia(CreateView):
    template_name="capturar/registroReferencia.html"
    model= Referencia_Medicion
    fields=['altura_referencia']
    success_url="/referencia-guardado/"

class PlantaGuardada(TemplateView):
    template_name= "capturar/plantaGuardada.html"

class RegistroPlantas(CreateView):
    template_name="capturar/plantas.html"
    model= TipoPlanta
    fields=['tipo_planta']
    success_url="/planta-guardado/"

class SiembraGuardada(TemplateView):
    template_name= "capturar/siembraGuardada.html"

class RegistroSiembra(CreateView):
    template_name="capturar/siembra.html"
    model=Plantas
    fields=['tipo','fecha_siembra']
    success_url="/siembra-guardado/"