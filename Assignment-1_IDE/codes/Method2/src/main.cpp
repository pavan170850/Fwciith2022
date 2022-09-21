#include <Wire.h>
#include <Arduino.h>


// C++ code
int D=0,C=0,B=0,A=0;     //A,B,C,D are Inputs
int Y;           //Y is Output

void setup()
{
  pinMode(LED_BUILTIN, OUTPUT); //pin 13 in arduino is LED_BUILTIN ,configured it as output
}

void loop(){
    Y=(A||B)&&(C||D);
    if (Y==1){
        digitalWrite(LED_BUILTIN, HIGH);}
    else{
        digitalWrite(LED_BUILTIN, LOW);
  }
  }
