Bibliotecas   
import RPi.GPIO as GPIO

#Constantes 
GPIO.setmode(GPIO.BOARD)
FFL = 11 #Flotador del Filtro Nivel Low
FFH = 13 #Flotador del Filtro Nivel High
FPL = 16 #Flotador de la Pecera Nivel Low
FPH = 18 #Flotador de la Pecera Nivel High
RB1 = 15 #Relay de la bomba de deposito
RB2 = 19 # Relay de la bomba de pecera

#Inicializamos los pines de entrada y salida
GPIO.setup(FFL, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(FFH, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(FPL, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(FPH, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(RB1, GPIO.OUT, initial = 1)
GPIO.setup(RB2, GPIO.OUT, initial = 1)

class ControlAgua:
  def __init__(self):
   
  def FlotadorFiltroUp(self):
    GPIO.input(FFL)
    
  def FlotadorFiltroDown(self):
    GPIO.input(FFH)
  
  def FlotadorPeceraUp(self):
    GPIO.input(FPL)
    
  def FlotadorPeceraDown(self):
    GPIO.input(FPH)
    
    
  def OnBombaPecera(self):
    GPIO.output(RB2, 0) #enciende bomba de pecera
	
  def OffBombaPecera(self):
    GPIO.output(RB2, 1) #apaga bomba de pecera
	
  def OnBombaDeposito(self):
    GPIO.output(RB1, 0) #apagar bomba de deposito

  def OffBombaDeposito(self):
    GPIO.output(RB1, 1) #apagar bomba de deposito
	
  def DepositoLLeno(self): #DEPOSITO LLENO y con nivel bajo asegurado en pecera
    GPIO.input(FFL) == 0 and GPIO.input(FFH) == 0 and GPIO.input(FPL) == 0
  
  def PeceraLLena(self): #PECERA LLENA y con nivel bajo asegurado en deposito
    GPIO.input(FPL) == 0 and GPIO.input(FPH) == 0 and GPIO.input(FFL) == 0

  def DepositoVacio(self): #Deposito vacio
    GPIO.input(FFL) == 1 and GPIO.input(FFH) == 1 and GPIO.input(FPL) == 0 and GPIO.input(FPH)== 0

  def PeceraDepositoLLenos(self):
    GPIO.input(FPL) == 0 and GPIO.input(FPH)== 0 and GPIO.input(FFL) == 0 and GPIO.input(FFH)== 0

  def PeceraDepositoMedio(self):
    GPIO.input(FFL) == 1 and GPIO.input(FPL) == 1

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
