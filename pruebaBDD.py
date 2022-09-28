import psycopg2 #Comunicacion para base de datos postgresql
from datetime import datetime #Acceso a la hora actual
import time #Para uso de la funcion sleep

now=datetime.now() #Guardar hora actual en la variable now
conexion = psycopg2.connect(host="localhost", database="acuaponia", user="grafana", password="1234")
cur = conexion.cursor() #Funcion para poder accesar a los datos

cur.execute("SELECT hora_apagado, hora_encendido, minuto_apagado, minuto_encendido FROM public.\"controlLuces_programacion_luces\" WHERE id=(select max(id) from public.\"controlLuces_programacion_luces\")")
for x in cur.fetchall(): #Ciclo para recorrer el arreglo de datos
	hora_apagado=x[0]
	hora_encendido=x[1] 
	minuto_apagado=x[2]
	minuto_encendido=x[3]
	print(hora_apagado, hora_encendido, minuto_apagado, minuto_encendido)
print(hora_apagado<=now.hour or hora_encendido>now.hour and minuto_apagado<=now.minute)
