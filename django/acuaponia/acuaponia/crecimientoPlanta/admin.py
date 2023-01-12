from django.contrib import admin

# Register your models here.
from .models import TipoPlanta , Plantas, Monitoreo, Referencia_Medicion 
admin.site.register(TipoPlanta)
admin.site.register(Plantas)
admin.site.register(Monitoreo)
admin.site.register(Referencia_Medicion)

