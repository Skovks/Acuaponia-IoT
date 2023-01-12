from pickle import TRUE
from tabnanny import verbose
from django.db import models
from django.utils import timezone

# Create your models here.

class TipoPlanta(models.Model):
    tipo_planta=models.CharField(max_length=80)
    class Meta():
        verbose_name_plural='Tipo de plantas'
    def __str__(self) -> str:
        return self.tipo_planta

class Plantas(models.Model):
    tipo=models.ForeignKey(TipoPlanta,on_delete=models.CASCADE)
    fecha_siembra=models.DateTimeField(default=timezone.now)   # debe de ser del tipo de fecha y hora

    class Meta():
        verbose_name_plural='Plantas'
    def __str__(self) -> str:
        return str(self.fecha_siembra)

class Monitoreo(models.Model):
    id_planta=models.ForeignKey(Plantas,on_delete=models.CASCADE)
    timestamp_muestra=models.DateTimeField(auto_now=True, null=True)
    altura=models.FloatField(blank=TRUE)

    def __str__(self) -> str:
        return str(self.altura)
    class Meta():
        verbose_name_plural='Monitoreo'

class Referencia_Medicion(models.Model):
    altura_referencia=models.FloatField(default=81.5)
    class Meta():
        verbose_name_plural='Referencia de Medicion'
    def __str__(self) -> str:
        return str(self.altura_referencia)
    
    