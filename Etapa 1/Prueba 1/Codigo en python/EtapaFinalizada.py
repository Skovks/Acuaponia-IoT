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

#Constantes 
GPIO.setmode(GPIO.BOARD)
FFL = 11 #Flotador del Filtro Nivel Low
FFH = 13 #Flotador del Filtro Nivel High
FPL = 16 #Flotador de la Pecera Nivel Low
FPH = 18 #Flotador de la Pecera Nivel High
RB = 15 #Relay de la bomba de agua
Hysteresis = 0 #Variable auxiliar para la hysteresis

#Cuerpo del programa
#Inicializamos los pines de entrada y salida
GPIO.setup(FFL, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(FFH, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(FPL, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(FPH, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(RB, GPIO.OUT, initial = 0)

#Bucle infinito
try:
	while True:
		if  GPIO.input(FFL) == 1 and GPIO.input(FFH)==1: #Si hay agua en el deposito
			if GPIO.input(FPL) == 1 and GPIO.input(FPH) == 1 and Hysteresis == 0: 
				GPIO.output(RB, 0) #prender bomba
			elif GPIO.input(FPL) == 1 and GPIO.input(FPH) == 0 and Hysteresis == 0:
				GPIO.output(RB, 1)#Esta situacion no pasa pero apagamos
			elif GPIO.input(FPL) == 0 and GPIO.input(FPH) == 1 and Hysteresis == 0:
				GPIO.output(RB, 0) #prender bomba 
			elif GPIO.input(FPL) == 0 and GPIO.input(FPH) == 0 and Hysteresis == 0: 
				GPIO.output(RB, 1) #Apagar bomba
				Hysteresis = 1
			elif GPIO.input(FPL) == 1 and GPIO.input(FPH) == 1 and Hysteresis == 1: 
				Hysteresis = 0
			elif GPIO.input(FPL) == 1 and GPIO.input(FPH) == 0 and Hysteresis == 1: 
				GPIO.output(RB, 1)#Esta situacion nunca pasa, pero apagamos
			elif GPIO.input(FPL) == 0 and GPIO.input(FPH) == 1 and Hysteresis == 1: 
				GPIO.output(RB, 1) #Apagar bomba
			else:
				GPIO.output(RB, 1) #Apagar bomba
		elif GPIO.input(FFL)==1 and GPIO.input(FFH)==0:
			print("Deposito lleno: Advertencia")
		else:  #No hay agua en el deposito
			GPIO.output(RB, 1) #Apagar bomba
			
except KeyboardInterrupt:            #Excepcion para atrapar las interrupciones
    GPIO.cleanup()                   #Con el teclado
