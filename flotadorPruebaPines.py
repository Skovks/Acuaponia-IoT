import RPi.GPIO as GPIO
FFL = 29 #Flotador del Filtro Nivel Low
FFH = 31 #Flotador del Filtro Nivel High
FPL = 36 #Flotador de la Pecera Nivel Low
FPH = 38 #Flotador de la Pecera Nivel High

GPIO.setmode(GPIO.BOARD)
GPIO.setup(FFL, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(FFH, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(FPL, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(FPH, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        print("Flotador Deposito Bajo:",GPIO.input(FFL),"Flotador Deposito Alto:", GPIO.input(FFH), "Flotador Pecera Bajo:", GPIO.input(FPL),"Flotador Pecera Alto:", GPIO.input(FPH))

except KeyboardInterrupt:            #Excepcion para atrapar las interrupciones
    GPIO.cleanup()                   #Con el teclado
