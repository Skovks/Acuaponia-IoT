import RPi.GPIO as GPIO
RB1 = 15 #Relay de la bomba de deposito
RB2 = 19 # Relay de la bomba de pecera
GPIO.setmode(GPIO.BOARD)
GPIO.setup(RB1, GPIO.OUT, initial = 1)
GPIO.setup(RB2, GPIO.OUT, initial = 1)
try:
    GPIO.output(RB2, 0) #prender bomba de pecera
    GPIO.output(RB1, 1) #apagar bomba deposito


except KeyboardInterrupt:            #Excepcion para atrapar las interrupciones
    GPIO.cleanup()                   #Con el teclado
