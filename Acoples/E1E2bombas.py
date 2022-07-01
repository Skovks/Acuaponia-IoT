'''*Fecha 11 de diciembre del 2021
   *Autor: Skovks
   *
   *Este programa sirve para el control de de llenado de una pecera
   *con su deposito de agua a travez de 2 sensores flotadores dobles
   *Flotadores convencion de funcionamiento para este programa
   *Cuando en el sofware sea '1' digital indicara que el flotador esta abajo(No detecta agua) 
   *Cuando en el sofware sea '0' digital indicara que el flotador esta arriba(Detecta agua) 
   *Cuando a el relay se le envie un '1' digital este estara apagado(Bomba apagada)
   *Cuando a el relay se le envie un '0' digital este estara prendido(Bomba encendida)
   *
   '''
#Bibliotecas   
import RPi.GPIO as GPIO #Comunicacion para los pines GPIO
import time #Para uso de la funcion sleep
from datetime import datetime #Acceso a la hora actual
import psycopg2 #Comunicacion para base de datos postgresql


#Constantes 
GPIO.setmode(GPIO.BOARD) #Funcion para usar los pines por orden de numeracion(1-40)
FFL = 29 #Flotador del Filtro para el Nivel Bajo 
FFH = 31 #Flotador del Filtro para el Nivel Alto
FPL = 36 #Flotador de la Pecera para el Nivel Bajo
FPH = 38 #Flotador de la Pecera para el Nivel Alto
RB1 = 15 #Relay para prender/apagar la bomba del deposito
RB2 = 19 #Relay para prender/apagar la bomba de la pecera
RL = 40 #Relay para el encendido/apagado de Luces  
bf=0 #bandera de bombas para generar histeresis con el control on-off
bl=0 #bandera de inicio para luces

#Cuerpo del programa
#Inicializamos los pines de entrada y salida
GPIO.setup(FFL, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #GPIO.setup(sensor,Entrada, resistencia interna en modo pull down)
GPIO.setup(FFH, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(FPL, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(FPH, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(RB1, GPIO.OUT, initial = 1) #GPIO.setup(actuador, Salida, condicion inicial)
GPIO.setup(RB2, GPIO.OUT, initial = 1)
GPIO.setup(RL, GPIO.OUT, initial = 0)

#Inicio del programa Principal
try: #Intentar todo el codigo principal
	#Conexion a la base de datos de POSTGRESQL para leer datos
	#Primer parametro host=(IP de la base de datos o en su defecto localhost)
	#Segundo parametro database=(nombre de la base de datos)
	#Tercer parametro user=(usuario que tenga acceso a la base datos seleccionada)
	#Cuarto párametro password=(Contraseña del usuario) 
	conexion = psycopg2.connect(host="localhost", database="acuaponia", user="grafana", password="1234")
	cur = conexion.cursor() #Funcion para poder accesar a los datos
	while True: #Bucle infinito
		'''En la siguiente linea de codigo se especifican los datos a los cuales se quiere acceder a traves de la tabla
		con los ultimos registros guardados. Lo que esta dentro de la funcion es una cadena de caracteres con una 
		sentencia SQL para acceder a los datos solicitados'''
		cur.execute("SELECT hora_apagado, hora_encendido, minuto_apagado, minuto_encendido FROM public.\"controlLuces_programacion_luces\" WHERE id=(select max(id) from public.\"controlLuces_programacion_luces\")")
		for x in cur.fetchall(): #Ciclo para recorrer el arreglo de datos
			hora_apagado=x[0]
			hora_encendido=x[1] 
			minuto_apagado=x[2]
			minuto_encendido=x[3]
		now=datetime.now() #Guardar hora actual en la variable now
		#Las siguiente linea es para depurar el programa en caso de que se quiera ver  los estados de los sensores
		#print("Flotador Deposito Bajo:",GPIO.input(FFL),"Flotador Deposito Alto:", GPIO.input(FFH), "Flotador Pecera Bajo:", GPIO.input(FPL),"Flotador Pecera Alto:", GPIO.input(FPH))
		if now.hour == hora_encendido and now.minute == minuto_encendido: #Revisa si los datos de hora para encendido son iguales
			print("Temporizador iniciado") 
			GPIO.output(RL, 0) #Prender luces
		elif hora_apagado<=now.hour or hora_encendido>now.hour and minuto_apagado<=now.minute: #Revisa si la hora de apagado esta dentro del rango de encendido para que el control se duerma
			GPIO.output(RL, 1) #Apagar luces
			print("temporizador apagado:en espera")
			GPIO.output(RB1, 1) #apagar bomba de deposito
			GPIO.output(RB2, 1) #apagar bomba de pecera
			bf=0 #Reincio de bandera de hysteresis
			dormir=abs(hora_apagado-hora_encendido-24)*60*60 #Tiempo total para dormir al control
			time.sleep(dormir) #Ejecuta la funcion para dormir, con el tiempo que se establecio
		elif GPIO.input(FFL) == 0 and GPIO.input(FFH) == 0 and GPIO.input(FPL) == 0: #Solo pasa con el DEPOSITO LLENO y con nivel bajo asegurado en pecera
			GPIO.output(RB1, 0) #prender bomba de deposito
			GPIO.output(RB2, 1) #apagar bomba de pecera
			bf=1 #Cambio de estado de la bandera para generar hysteresis con el control on-off
		elif GPIO.input(FPL) == 0 and GPIO.input(FPH) == 0 and GPIO.input(FFL) == 0: #Solo pasa con la PECERA LLENA y con nivel bajo asegurado en deposito
			GPIO.output(RB1, 1) #apagar bomba de deposito
			GPIO.output(RB2, 0) #prender bomba de pecera
			bf=0 #Cambio de estado de la bandera para generar hystereis con el control on-off
		elif GPIO.input(FFL) == 0 and GPIO.input(FFH) == 1 and GPIO.input(FPL) == 0 and GPIO.input(FPH) == 1 and bf==0: #Condicion de inicio para el flujo de agua
			GPIO.output(RB1, 1) #prender bomba de deposito
			GPIO.output(RB2, 0) #apagar bomba de pecera
		elif GPIO.input(FFL) == 0 and GPIO.input(FFH) == 1 and GPIO.input(FPL) == 0 and GPIO.input(FPH) == 1 and bf==1: #Condicion auxiliar para el flujo de agua
			GPIO.output(RB1, 0) #apagar bomba de deposito
			GPIO.output(RB2, 1) #prender bomba de pecera
		elif GPIO.input(FFL) == 1 and GPIO.input(FFH) == 1: #Solo pasa con el deposito casi vacio
			print("agregar mas agua al deposito: Niveles bajos")
			GPIO.output(RB1, 1) #apagar bomba de deposito
			GPIO.output(RB2, 1) #apagar bomba de pecera
		elif GPIO.input(FPL) == 1 and GPIO.input(FPH) == 1: #Solo pasa con la pecera casi vacia
			print("agregar mas agua a la pecera: Niveles bajos")
			GPIO.output(RB1, 1) #apagar bomba de deposito
			GPIO.output(RB2, 1) #apagar bomba de pecera
		elif GPIO.input(FPL) == 0 and GPIO.input(FPH)== 0 and GPIO.input(FFL) == 0 and GPIO.input(FFH)== 0: #Solo pasa con ambos llenos
			GPIO.output(RB1, 1) #apagar bomba de deposito
			GPIO.output(RB2, 1) #apagar bomba de pecera
			print("Pecera y deposito llenos: desborde del deposito por condicion externa")
		time.sleep(5) #Duerme el sistema de control por 5 segundos para que no se ejecute todo el tiempo
		

except KeyboardInterrupt:            #Excepcion para atrapar las interrupciones con el teclado
    GPIO.cleanup()                   
