import RPi.GPIO as GPIO
RB1 = 15 #Relay de la bomba de deposito
RB2 = 19 # Relay de la bomba de pecera
FPL = 16 #Flotador de la Pecera Nivel Low
FPH = 18 #Flotador de la Pecera Nivel High
GPIO.setmode(GPIO.BOARD)
GPIO.setup(FPL, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(FPH, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(RB1, GPIO.OUT, initial = 0)
GPIO.setup(RB2, GPIO.OUT, initial = 1)
try:
    while True:
        print("Flotador Pecera Bajo:", GPIO.input(FPL),"Flotador Pecera Alto:", GPIO.input(FPH))
        if GPIO.input(FPL) == 0 and GPIO.input(FPH) == 0: #agua nivel bajo en pecera y en deposito
            GPIO.output(RB1, 1) #apagar bomba de deposito
            GPIO.output(RB2, 1) #encender bomba de pecera

except KeyboardInterrupt:            #Excepcion para atrapar las interrupciones
    GPIO.cleanup()                   #Con el teclado