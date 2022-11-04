//----------------------Skeleton Code--------------------//
#include <WiFi.h>
#include <WiFiUdp.h>
#include <ArduinoOTA.h>
#include <BlynkSimpleStream.h>
//    Can be client or even host   //
#ifndef STASSID
#define STASSID "jeevan"  // Replace with your network credentials
#define STAPSK  "jeevan12345"
#endif

const char* ssid = STASSID;
const char* password = STAPSK;
char server[] = "blynk-cloud.com";  
char auth[] = "NsIU53F1oq1GlJLVGilptxkT-c0OOVST"; 
int A,B,C,D,Y;

void OTAsetup() {
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  while (WiFi.waitForConnectResult() != WL_CONNECTED) {
    delay(5000);
    ESP.restart();
  }
  ArduinoOTA.begin();
}

void OTAloop() {
  ArduinoOTA.handle();
}

//-------------------------------------------------------//

void setup(){
  OTAsetup();

  //-------------------//
  // Custom setup code //
  //-------------------//
  pinMode(2, INPUT);
  pinMode(4, INPUT);  
  pinMode(5, INPUT);
  pinMode(10, INPUT);  
  pinMode(33, OUTPUT);  
}

void loop() {
  OTAloop();
  delay(10);  // If no custom loop code ensure to have a delay in loop
  //-------------------//
  // Custom loop code  //
  //-------------------//
  A=digitalRead(2);
  B=digitalRead(4);
  C=digitalRead(5);
  D=digitalRead(10);
  Y=(A||B)&&(C||D);
  digitalWrite(33, Y);
}



