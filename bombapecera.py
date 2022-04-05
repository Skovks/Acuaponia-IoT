import RPi.GPIO as GPIO
RB2 = 19 # Relay de la bomba de pecera
GPIO.setmode(GPIO.BOARD)
GPIO.setup(RB2, GPIO.OUT, initial = 1)
try:
    GPIO.output(RB2, 0) #prender bomba de pecera


except KeyboardInterrupt:            #Excepcion para atrapar las interrupciones
    GPIO.cleanup()                   #Con el teclado
