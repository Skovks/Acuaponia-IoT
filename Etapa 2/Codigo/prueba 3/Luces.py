import RPi.GPIO as GPIO
from datetime import datetime

#Constantes 
GPIO.setmode(GPIO.BOARD)
RL = 40 #Relay de Luces 
BL=0; #bandera de luces 

#Inicializamos los pines de entrada y salida
GPIO.setup(RL, GPIO.OUT, initial = 1)

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
            
            
    
            
except KeyboardInterrupt:            #Excepcion para atrapar las interrupciones
    GPIO.cleanup()                   #Con el teclado
