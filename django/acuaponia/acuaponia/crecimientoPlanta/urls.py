from django.urls import include, path, re_path
from django.views import View
from . import views

app_name="crecimientoPlanta_app"

urlpatterns=[
    path('foto/', views.tomar_foto),
    path('registro-referencia/',views.Registrar_Altura_Referencia.as_view()),
    path('referencia-guardado/',views.ReferenciaGuardada.as_view()),
    path('registro-planta/',views.RegistroPlantas.as_view()),
    path('registro-siembra/',views.RegistroSiembra.as_view()),
    path('planta-guardado/',views.PlantaGuardada.as_view()),
    path('siembra-guardado/',views.SiembraGuardada.as_view()),
]