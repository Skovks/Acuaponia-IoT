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
const int Beer =  7;      // Relay de electrovalvula de cerveza
const int PistonesUp = 11;         //Relay de pistones de subida
const int PistonesDown=10;  //pistones de bajada
const int CO = 6;         //relay de CO2 
int bandera=0;
int sensorValue = 0;        // value read from the pot
int outputValue = 0;        // value output to the PWM (analog out)
int buttonState = 0;         // variable for reading the pushbutton status
int inicio=0;
void setup() {
  // initialize serial communications at 9600 bps:
  Serial.begin(9600);
  // initialize the pushbutton pin as an input:
  pinMode(buttonPin, INPUT);
  pinMode(Beer,OUTPUT);
  pinMode(PistonesUp,OUTPUT);
  pinMode(PistonesDown,OUTPUT);
  pinMode(CO,OUTPUT);  
}

void loop() {
  // read the state of the pushbutton value:
  if(inicio==0){
    digitalWrite(Beer,HIGH);
    digitalWrite(CO,HIGH);
    digitalWrite(PistonesUp,HIGH);
    digitalWrite(PistonesDown,HIGH); 
    inicio=1;
  }
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
        digitalWrite(PistonesUp, LOW);
        Serial.println("Bajando pistones...");
        delay(3000);//espera a que baje el piston 3 segundos
        //activar electrovalvula de CO2 por 12 segundos
        Serial.println("Valvula de CO2 activada");
        digitalWrite(CO,LOW);
        delay(12000);
        Serial.println("Valvula de CO2 desactivada");
        digitalWrite(CO,HIGH);
        delay(1000);
        //activar electrovalvula de cerveza
        Serial.println("Activacion de valvula de cerveza");
        digitalWrite(Beer, LOW);
        bandera=1; 
      }
      if(sensorValue<800){
        Serial.println("Deteccion de liquido: Apagado de valvula de cerveza");
        digitalWrite(Beer,HIGH); //apaga electrovalvula de cerveza
        delay(1000);//espera estandar
        digitalWrite(PistonesUp, HIGH);//apagar pistones de bajada
        delay(1000);//espera estandar
        digitalWrite(PistonesDown,LOW); //Subir pistones
        delay(3000);//espera a que suban los pistones durante 3 segundos
        digitalWrite(PistonesDown,HIGH);// apagar pistones de subida
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
