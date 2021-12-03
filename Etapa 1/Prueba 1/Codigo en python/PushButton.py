'''*Fecha 2 de diciembre del 2021
   *Autor: Skovks
   *
   *Este programa sirve para controlar un led a travez de un switch
   *con la raspberry pi 
   *
   *Raspberry pi   LED
   *Raspbeery pi   Switch
   *GND            Catodo de led 
   *3.3v           Resistencia de 200ohms
   *GPIO11         Switch  
   *GPIO13         Resistencia de 200hms de led
   '''
#Bibliotecas   
import RPi.GPIO as GPIO
#Constantes
GPIO.setmode(GPIO.BOARD)
boton = 11
led = 13

#Cuerpo del programa
#Inicializamos los pines de entrada y salida
GPIO.setup(boton, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(led, GPIO.OUT, initial = 0)

#Bucle infinito
try:
	while True:
		level_bt = GPIO.input(boton) #Asignacion de una variable auxiliar
		if level_bt == 0:            #Si el switch esta apagado
			GPIO.output(led, 0)      #El led esta apagado
		else:                        #Si el switch esta encendido
			GPIO.output(led, 1)      #El led esta apagado
		     
except KeyboardInterrupt:            #Excepcion para atrapar las interrupciones
    GPIO.cleanup()                   #Con el teclado
