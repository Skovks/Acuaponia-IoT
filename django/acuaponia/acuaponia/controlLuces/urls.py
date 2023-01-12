from django.urls import include, path, re_path
from django.views import View
from . import views

app_name="controlLuces_app"

urlpatterns=[
    path('luces/',views.Registro_Luces.as_view()),
    path('guardado/',views.Guardado.as_view()),
]