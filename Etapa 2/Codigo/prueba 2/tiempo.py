import RPi.GPIO as GPIO
from datetime import datetime

#Constantes 
GPIO.setmode(GPIO.BOARD)
RL = 12 #Relay de Luces 


#Inicializamos los pines de entrada y salida
GPIO.setup(RL, GPIO.OUT, initial = 0)

print("Current Time =", datetime.now())
hora=input('Introduce la hora:')
minuto=input('Introduce el minuto:')
a=int(hora)
b=int(minuto)
print("Temporizador iniciado")
    

#Bucle infinito
try:
    while True:
        now=datetime.now();
        if now.hour == a and now.minute == b:
            #print("Tmporizador apagado")
            GPIO.output(RL, 1) #Apagar bomba
            break
        else:
            GPIO.output(RL, 0) #Prender bomba
			
    
    
except KeyboardInterrupt:            #Excepcion para atrapar las interrupciones
    GPIO.cleanup()                   #Con el teclado
