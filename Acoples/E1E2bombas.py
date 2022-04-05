'''*Fecha 11 de diciembre del 2021
   *Autor: Skovks
   *
   *Este programa sirve para el control de de llenado de una pecera
   *con su deposito de agua a travez de 2 sensores flotadores sencillos
   *y 1 flotador doble.
   *Flotadores verticales 1 es abajo y 0 arriba
   *Flotador horizontal 1 es arriba y 0 es abajo
   *relay 1 es apagado y 0 es prendido
   *
   '''
#Bibliotecas   
import RPi.GPIO as GPIO
import time
from datetime import datetime

#Constantes 
GPIO.setmode(GPIO.BOARD)
FFL = 11 #Flotador del Filtro Nivel Low
FFH = 13 #Flotador del Filtro Nivel High
FPL = 16 #Flotador de la Pecera Nivel Low
FPH = 18 #Flotador de la Pecera Nivel High
RB1 = 15 #Relay de la bomba de deposito
RB2 = 19 # Relay de la bomba de pecera
RL = 40 #Relay de Luces 
#BL=0; #bandera de luces 

#Cuerpo del programa
#Inicializamos los pines de entrada y salida
GPIO.setup(FFL, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(FFH, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(FPL, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(FPH, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(RB1, GPIO.OUT, initial = 1)
GPIO.setup(RB2, GPIO.OUT, initial = 1)
GPIO.setup(RL, GPIO.OUT, initial = 0)

horaE="06" #Hora de encendido
minutoE="15" #minuto de apagado
horaA="21" #Hora de apagado
minutoA="15" #minuto de apagado

hE=int(horaE)
mE=int(minutoE)
hA=int(horaA)
mA=int(minutoA)
dormir=abs(hA-hE-24)*60
#Bucle infinito
try:
	while True:
		now=datetime.now()
		if now.hour == hE and now.minute == mE:
			print("Temporizador iniciado")
			GPIO.output(RL, 0) #Prender luces
		elif now.hour==hA and now.minute==mA:
			GPIO.output(RL, 1) #Apagar luces
			print("temporizador apagado:en espera")
			GPIO.output(RB1, 1) #apagar bomba de deposito
			GPIO.output(RB2, 1) #apagar bomba de pecera
			time.sleep(dormir)
		elif GPIO.input(FFL) == 0 and GPIO.input(FFH) == 0 and GPIO.input(FPL) == 0: #DEPOSITO LLENO y con nivel bajo asegurado en pecera
			GPIO.output(RB1, 0) #prender bomba de deposito
			GPIO.output(RB2, 1) #apagar bomba de pecera
		elif GPIO.input(FPL) == 0 and GPIO.input(FPH) == 0 and GPIO.input(FFL) == 0: #PECERA LLENA y con nivel bajo asegurado en deposito
			GPIO.output(RB1, 1) #apagar bomba de deposito
			GPIO.output(RB2, 0) #prender bomba de pecera
		elif GPIO.input(FFL) == 1 and GPIO.input(FFH) == 1 and GPIO.input(FPL) == 0 and GPIO.input(FPH)== 0:
			print("agregar mas agua al deposito")
			GPIO.output(RB1, 1) #apagar bomba de deposito
			GPIO.output(RB2, 1) #apagar bomba de pecera
		elif GPIO.input(FPL) == 0 and GPIO.input(FPH)== 0 and GPIO.input(FFL) == 0 and GPIO.input(FFH)== 0: #Ambos llenos
			GPIO.output(RB1, 1) #apagar bomba de deposito
			GPIO.output(RB2, 1) #apagar bomba de pecera
			print("Pecera y deposito llenos: desborde del deposito por condicion externa")
		elif GPIO.input(FFL) == 1 and GPIO.input(FPL) == 1: #agua nivel bajo en pecera y en deposito
			GPIO.output(RB1, 1) #apagar bomba de deposito
			GPIO.output(RB2, 0) #encender bomba de pecera
			

except KeyboardInterrupt:            #Excepcion para atrapar las interrupciones
    GPIO.cleanup()                   #Con el teclado
