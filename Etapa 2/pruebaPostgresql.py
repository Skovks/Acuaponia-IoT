import psycopg2
import time
from datetime import datetime


#Bucle infinito
try:
	conexion = psycopg2.connect(host="localhost", database="acuaponia", user="grafana", password="1234")
	cur = conexion.cursor()
	while True:
		cur.execute("SELECT hora_apagado, hora_encendido, minuto_apagado, minuto_encendido FROM public.\"controlLuces_programacion_luces\" WHERE id=(select max(id) from public.\"controlLuces_programacion_luces\")")
		now=datetime.now()
		for x in cur.fetchall():
			hora_apagado=x[0] 
			hora_encendido=x[1] 
			minuto_apagado=x[2]
			minuto_encendido=x[3]
		if now.hour == hora_encendido and now.minute == minuto_encendido:
			print("Temporizador iniciado")
			#GPIO.output(RL, 0) #Prender luces
		elif now.hour >= hora_apagado or now.hour<hora_encendido and now.minute >= minuto_apagado:
			#GPIO.output(RL, 1) #Apagar luces
			print("temporizador apagado:en espera")
			#GPIO.output(RB1, 1) #apagar bomba de deposito
			#GPIO.output(RB2, 1) #apagar bomba de pecera
			#bf=0
			#time.sleep(dormir)
		time.sleep(5)
	conexion.close()

except KeyboardInterrupt:            #Excepcion para atrapar las interrupciones
    GPIO.cleanup()                   #Con el teclado
