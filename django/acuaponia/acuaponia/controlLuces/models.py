from pickle import TRUE
from tabnanny import verbose
from django.db import models
import datetime as dt

from django.utils import timezone

# Create your models here.
import datetime
HOUR_CHOICES = [(x, '{:02d}'.format(x)) for x in range(0, 24)]
MINUTES_CHOICES = [(y, '{:02d}'.format(y)) for y in range(0, 60)]

class Programacion_luces(models.Model):
    hora_encendido=models.PositiveSmallIntegerField(blank=TRUE,null=TRUE, choices=HOUR_CHOICES, default=6)
    minuto_encendido=models.PositiveSmallIntegerField(blank=True, null=TRUE, choices=MINUTES_CHOICES,default=0)
    hora_apagado=models.PositiveSmallIntegerField(blank=TRUE,null=TRUE, choices=HOUR_CHOICES,default=21)
    minuto_apagado=models.PositiveSmallIntegerField(blank=TRUE, null=TRUE, choices=MINUTES_CHOICES,default=0)
    class Meta():
        verbose_name_plural='Programacion de luces'

    def __str__(self) -> str:
        txt="hora de encendido: {:02d}:{:02d} y hora de apagado: {:02d}:{:02d}"
        return txt.format(self.hora_encendido, self.minuto_encendido,self.hora_apagado,self.minuto_apagado)


