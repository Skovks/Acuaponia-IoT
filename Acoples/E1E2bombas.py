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
import psycopg2 #biblioteca para base de datos postgresql


#Constantes 
GPIO.setmode(GPIO.BOARD)
FFL = 29 #Flotador del Filtro Nivel Low
FFH = 31 #Flotador del Filtro Nivel High
FPL = 36 #Flotador de la Pecera Nivel Low
FPH = 38 #Flotador de la Pecera Nivel High
RB1 = 15 #Relay de la bomba de deposito
RB2 = 19 # Relay de la bomba de pecera
RL = 40 #Relay de Luces  
bf=0 #bandera de inicio bombas
bl=0 #bandera de inicio de luces

#Cuerpo del programa
#Inicializamos los pines de entrada y salida
GPIO.setup(FFL, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(FFH, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(FPL, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(FPH, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(RB1, GPIO.OUT, initial = 1)
GPIO.setup(RB2, GPIO.OUT, initial = 1)
GPIO.setup(RL, GPIO.OUT, initial = 0)

#Bucle infinito
try:
	conexion = psycopg2.connect(host="localhost", database="acuaponia", user="grafana", password="1234")
	cur = conexion.cursor()
	while True:
		cur.execute("SELECT hora_apagado, hora_encendido, minuto_apagado, minuto_encendido FROM public.\"controlLuces_programacion_luces\" WHERE id=(select max(id) from public.\"controlLuces_programacion_luces\")")
		for x in cur.fetchall():
			hora_apagado=x[0] 
			hora_encendido=x[1] 
			minuto_apagado=x[2]
			minuto_encendido=x[3]
		now=datetime.now()
		#print(hora_encendido,hora_apagado)
		#print("Flotador Deposito Bajo:",GPIO.input(FFL),"Flotador Deposito Alto:", GPIO.input(FFH), "Flotador Pecera Bajo:", GPIO.input(FPL),"Flotador Pecera Alto:", GPIO.input(FPH))
		if now.hour == hora_encendido and now.minute == minuto_encendido:
			print("Temporizador iniciado")
			GPIO.output(RL, 0) #Prender luces
		elif hora_apagado<=now.hour or hora_encendido>now.hour and minuto_apagado<=now.minute:
			GPIO.output(RL, 1) #Apagar luces
			print("temporizador apagado:en espera")
			GPIO.output(RB1, 1) #apagar bomba de deposito
			GPIO.output(RB2, 1) #apagar bomba de pecera
			bf=0
			dormir=abs(hora_apagado-hora_encendido-24)*60*60
			time.sleep(dormir)
		elif GPIO.input(FFL) == 0 and GPIO.input(FFH) == 0 and GPIO.input(FPL) == 0: #DEPOSITO LLENO y con nivel bajo asegurado en pecera
			GPIO.output(RB1, 0) #prender bomba de deposito
			GPIO.output(RB2, 1) #apagar bomba de pecera
			bf=1
		elif GPIO.input(FPL) == 0 and GPIO.input(FPH) == 0 and GPIO.input(FFL) == 0: #PECERA LLENA y con nivel bajo asegurado en deposito
			GPIO.output(RB1, 1) #apagar bomba de deposito
			GPIO.output(RB2, 0) #prender bomba de pecera
			bf=0
		elif GPIO.input(FFL) == 0 and GPIO.input(FFH) == 1 and GPIO.input(FPL) == 0 and GPIO.input(FPH) == 1 and bf==0: #inicio
			GPIO.output(RB1, 1) #prender bomba de deposito
			GPIO.output(RB2, 0) #apagar bomba de pecera
		elif GPIO.input(FFL) == 0 and GPIO.input(FFH) == 1 and GPIO.input(FPL) == 0 and GPIO.input(FPH) == 1 and bf==1: #segundo
			GPIO.output(RB1, 0) #apagar bomba de deposito
			GPIO.output(RB2, 1) #prender bomba de pecera
		elif GPIO.input(FFL) == 1 and GPIO.input(FFH) == 1: #deposito casi vacio
			print("agregar mas agua al deposito: Niveles bajos")
			GPIO.output(RB1, 1) #apagar bomba de deposito
			GPIO.output(RB2, 1) #apagar bomba de pecera
		elif GPIO.input(FPL) == 1 and GPIO.input(FPH) == 1: #pecera casi vacia
			print("agregar mas agua a la pecera: Niveles bajos")
			GPIO.output(RB1, 1) #apagar bomba de deposito
			GPIO.output(RB2, 1) #apagar bomba de pecera
		elif GPIO.input(FPL) == 0 and GPIO.input(FPH)== 0 and GPIO.input(FFL) == 0 and GPIO.input(FFH)== 0: #Ambos llenos
			GPIO.output(RB1, 1) #apagar bomba de deposito
			GPIO.output(RB2, 1) #apagar bomba de pecera
			print("Pecera y deposito llenos: desborde del deposito por condicion externa")
		time.sleep(5)
		

except KeyboardInterrupt:            #Excepcion para atrapar las interrupciones
    GPIO.cleanup()                   #Con el teclado
