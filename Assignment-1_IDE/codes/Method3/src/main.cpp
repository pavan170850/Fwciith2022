#include <Wire.h>
#include <Arduino.h>


// C++ code
int D,C,B,A;     //A,B,C,D are Inputs
int Y;           //Y is Output

void setup()
{
  pinMode(LED_BUILTIN, OUTPUT); //pin 13 in arduino is LED_BUILTIN ,configured it as output
  pinMode(2,INPUT); 
  pinMode(3,INPUT);        
  pinMode(4,INPUT);  //pins 2,3,4,5 are configured as inputs
  pinMode(5,INPUT);

}

void loop(){
     A=digitalRead(2);
     B=digitalRead(3);
     C=digitalRead(4);
     D=digitalRead(5);
     Y=(A||B)&&(C||D);
    if (Y==1){
    	digitalWrite(LED_BUILTIN, HIGH);}
    else{
    	digitalWrite(LED_BUILTIN, LOW);
  }
  }
