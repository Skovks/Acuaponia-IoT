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
const int analogInPin = A0;  // Analog input pin that the potentiometer is attached to
const int analogOutPin = 9; // Analog output pin that the LED is attached to
//boton y relay
const int buttonPin = 2;     // the number of the pushbutton pin
const int ledPin =  12;      // the number of the LED pin

int sensorValue = 0;        // value read from the pot
int outputValue = 0;        // value output to the PWM (analog out)
int buttonState = 0;         // variable for reading the pushbutton status
void setup() {
  // initialize serial communications at 9600 bps:
  Serial.begin(9600);
  // initialize the LED pin as an output:
  pinMode(ledPin, OUTPUT);
  // initialize the pushbutton pin as an input:
  pinMode(buttonPin, INPUT);
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
      digitalWrite(ledPin, LOW);
      // turn LED on:
      if(sensorValue<800){
        Serial.println("Deteccion de liquido");
        break;
      }
      delay(200);
    }
  } else {
    // turn LED off:
    Serial.println("Esperando");
    digitalWrite(ledPin, HIGH);
    delay(200);
  }
  // wait 500 milliseconds before the next loop for the analog-to-digital
  // converter to settle after the last reading:
}
