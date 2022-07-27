/*
  Analog input, analog output, serial output

  Reads an analog input pin, maps the result to a range from 0 to 255 and uses
  the result to set the pulse width modulation (PWM) of an output pin.
  Also prints the results to the Serial Monitor.

  The circuit:
  - potentiometer connected to analog pin 0.
    Center pin of the potentiometer goes to the analog pin.
    side pins of the potentiometer go to +5V and ground
  - LED connected from digital pin 9 to ground through 220 ohm resistor

  created 29 Dec. 2008
  modified 9 Apr 2012
  by Tom Igoe

  This example code is in the public domain.

  https://www.arduino.cc/en/Tutorial/BuiltInExamples/AnalogInOutSerial
*/
// These constants won't change. They're used to give names to the pins used:
const int analogInPin = A0;  // Entrada de punta roja y resistencia
const int analogOutPin = 9; // Led indicador de intensidad de voltaje
//boton y electrovalvulas
const int buttonPin = 2;     // Push button de inicio 
const int Beer =  12;      // Relay de electrovalvula de cerveza
const int PistonesUp = 11;         //Relay de pistones de subida
const int PistonesDown=10;  //pistones de bajada
const int COIN = 7;         //relay de CO2 de entrada
const int COOUT= 8;         //relay de co2 de salida 
int bandera=0;
int sensorValue = 0;        // value read from the pot
int outputValue = 0;        // value output to the PWM (analog out)
int buttonState = 0;         // variable for reading the pushbutton status
void setup() {
  // initialize serial communications at 9600 bps:
  Serial.begin(9600);
  // initialize the pushbutton pin as an input:
  pinMode(buttonPin, INPUT);
  pinMode(Beer,OUTPUT);
  pinMode(PistonesUp,OUTPUT);
  pinMode(PistonesDown,OUTPUT);
  pinMode(COIN,OUTPUT);  
  pinMode(COOUT,OUTPUT);
  digitalWrite(Beer,HIGH);
  digitalWrite(COIN,HIGH);
  digitalWrite(COOUT,HIGH);
  digitalWrite(PistonesDown,HIGH); 
  digitalWrite(PistonesUp,LOW);
  delay(3000);
  digitalWrite(PistonesUp,HIGH);
}

void loop() {
  // read the state of the pushbutton value:
  buttonState = digitalRead(buttonPin);
  // check if the pushbutton is pressed. If it is, the buttonState is HIGH:
  if (buttonState == HIGH){
    while(true){
      // read the analog in value:
      sensorValue = analogRead(analogInPin);
      // map it to the range of the analog out:
      outputValue = map(sensorValue, 1023, 0, 0, 255);
      // change the analog out value:
      analogWrite(analogOutPin, outputValue);
      // print the results to the Serial Monitor:
      Serial.print("sensor = ");
      Serial.print(sensorValue);
      Serial.print("\t output = ");
      Serial.println(outputValue);
      if(bandera==0){
        //Baja los pistones
        digitalWrite(PistonesDown, LOW);
        Serial.println("Bajando pistones...");
        delay(3000);//espera a que baje el piston 3 segundos
        //activar electrovalvula de CO2 por 12 segundos
        Serial.println("Valvula de CO2 activada");
        digitalWrite(COIN,LOW);
        digitalWrite(COOUT,LOW);
        delay(12000);
        Serial.println("Valvula de CO2 desactivada");
        digitalWrite(COIN,HIGH);
        digitalWrite(COOUT,HIGH);
        delay(1000);
        //activar electrovalvula de cerveza
        Serial.println("Activacion de valvula de cerveza");
        digitalWrite(Beer, LOW);
        delay(1000);
        Serial.println("Activacion de valvula de co2 de salida");
        digitalWrite(COOUT,LOW);
        bandera=1; 
      }
      if(sensorValue<800){
        Serial.println("Deteccion de liquido: Apagado de valvula de cerveza");
        digitalWrite(Beer,HIGH); //apaga electrovalvula de cerveza
        delay(2000);
        digitalWrite(COOUT,HIGH); //apaga electrovalvula de CO2 de salida
        delay(1000);//espera estandar
        Serial.println("Apagado piston de bajada");        
        digitalWrite(PistonesDown, HIGH);//apagar pistones de bajada
        delay(1000);//espera estandar
        Serial.println("Encendido de piston de subida");        
        digitalWrite(PistonesUp,LOW); //Subir pistones
        delay(3000);//espera a que suban los pistones durante 3 segundos
        Serial.println("Apagado piston de subida");        
        digitalWrite(PistonesUp,HIGH);// apagar pistones de subida
        bandera=0;
        break;
      }
      delay(200);
    }
  } else {
    // turn LED off:
    Serial.println("Esperando");
    delay(200);
  }
  // wait 500 milliseconds before the next loop for the analog-to-digital
  // converter to settle after the last reading:
}
