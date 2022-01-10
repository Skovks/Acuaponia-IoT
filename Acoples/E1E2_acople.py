'''*Fecha 05 de enero del 2022
   *Autor: Skovks
   *
   *Esta es la segunda version del programa ya con el acople de luces
   *y flotatadores
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
from datetime import datetime

#Constantes 
GPIO.setmode(GPIO.BOARD)
FFL = 11 #Flotador del Filtro Nivel Low
FFH = 13 #Flotador del Filtro Nivel High
FPL = 16 #Flotador de la Pecera Nivel Low
FPH = 18 #Flotador de la Pecera Nivel High
RB = 15 #Relay de la bomba de agua
Hysteresis = 0 #Variable auxiliar para la hysteresis
RL = 40 #Relay de Luces 
BL=0; #bandera de luces 

#Cuerpo del programa
#Inicializamos los pines de entrada y salida
GPIO.setup(FFL, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(FFH, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(FPL, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(FPH, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(RB, GPIO.OUT, initial = 1)
GPIO.setup(RL, GPIO.OUT, initial = 1)

##setup de encendido de luces
print("Current Time =", datetime.now())
print("Establece la hora de encendido: En hora y minutos")
horaE=input('Introduce la hora:')
minutoE=input('Introduce el minuto:')

print("Establece la hora de apagado: En hora y minutos")
horaA=input('Introduce la hora:')
minutoA=input('Introduce el minuto:')

hE=int(horaE)
mE=int(minutoE)
hA=int(horaA)
mA=int(minutoA)

#Bucle infinito
try:
	while True:
		now=datetime.now()
		if now.hour == hE and now.minute == mE and BL==0:
			print("Temporizador iniciado")
			GPIO.output(RL, 0) #Prender luces
			BL=1
		elif now.hour==hA and now.minute==mA and BL==1:
			GPIO.output(RL, 1) #Apagar luces
			print("temporizador apagado:en espera")
			BL=0
		elif GPIO.input(FFL) == 1 and GPIO.input(FFH)==1: #Si hay agua en el deposito
			if GPIO.input(FPL) == 1 and GPIO.input(FPH) == 1 and Hysteresis == 0: 
				GPIO.output(RB, 0) #prender bomba
			elif GPIO.input(FPL) == 1 and GPIO.input(FPH) == 0 and Hysteresis == 0:
				GPIO.output(RB, 1)#Esta situacion no pasa pero apagamos
				print("Problemas con el sensor:Peces")
			elif GPIO.input(FPL) == 0 and GPIO.input(FPH) == 1 and Hysteresis == 0:
				GPIO.output(RB, 0) #prender bomba'''
			elif GPIO.input(FPL) == 0 and GPIO.input(FPH) == 0 and Hysteresis == 0: 
				GPIO.output(RB, 1) #Apagar bomba
				Hysteresis = 1
			elif GPIO.input(FPL) == 1 and GPIO.input(FPH) == 1 and Hysteresis == 1: 
				Hysteresis = 0
			elif GPIO.input(FPL) == 1 and GPIO.input(FPH) == 0 and Hysteresis == 1: 
				GPIO.output(RB, 1)#Esta situacion nunca pasa, pero apagamos
				print("Problemas con el sensor:Peces")
			elif GPIO.input(FPL) == 0 and GPIO.input(FPH) == 1 and Hysteresis == 1: 
				GPIO.output(RB, 1) #Apagar bomba
			else:
				GPIO.output(RB, 1) #Apagar bomba
		
		elif GPIO.input(FFL)==1 and GPIO.input(FFH)==0: #Deposito lleno
			if GPIO.input(FPL) == 1 and GPIO.input(FPH) == 1 and Hysteresis == 0: 
				GPIO.output(RB, 0) #prender bomba
			elif GPIO.input(FPL) == 1 and GPIO.input(FPH) == 0 and Hysteresis == 0:
				GPIO.output(RB, 1)#Esta situacion no pasa pero apagamos
				print("Problemas con el sensor:Peces")
			elif GPIO.input(FPL) == 0 and GPIO.input(FPH) == 1 and Hysteresis == 0:
				GPIO.output(RB, 0) #prender bomba 
			elif GPIO.input(FPL) == 0 and GPIO.input(FPH) == 0 and Hysteresis == 0: 
				GPIO.output(RB, 1) #Apagar bomba
				Hysteresis = 1
			elif GPIO.input(FPL) == 1 and GPIO.input(FPH) == 1 and Hysteresis == 1: 
				Hysteresis = 0
			elif GPIO.input(FPL) == 1 and GPIO.input(FPH) == 0 and Hysteresis == 1: 
				GPIO.output(RB, 1)#Esta situacion nunca pasa, pero apagamos
				print("Problemas con el sensor:Peces")
			elif GPIO.input(FPL) == 0 and GPIO.input(FPH) == 1 and Hysteresis == 1: 
				GPIO.output(RB, 1) #Apagar bomba
			else:
				GPIO.output(RB, 1) #Apagar bomba
		else:
			GPIO.output(RB, 1) #Apagar bomba
			
except KeyboardInterrupt:            #Excepcion para atrapar las interrupciones
    GPIO.cleanup()                   #Con el teclado
