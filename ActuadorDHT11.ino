#include "DHT.h"

#define DHTPIN 7
#define DHTTYPE DHT11

int pinEnergia = 13;

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
  pinMode(pinEnergia, OUTPUT);
}

void loop() {
  char data = Serial.read();
  if(data == '0'){
    digitalWrite(pinEnergia, HIGH);
    delay(5000);
    printTemp();
  }else if (data=='1'){
    digitalWrite(pinEnergia, HIGH);
    delay(5000);
    printHum();
  }
  digitalWrite(pinEnergia, LOW);
}

void printTemp(){
  float t = dht.readTemperature();
  if(isnan(t)){
    Serial.println("Error: 0");
  }else{
    Serial.println(t);
  }
}

void printHum(){
  float h = dht.readHumidity();
  if(isnan(h)){
    Serial.println("Error: 1");
  }else{
    Serial.println(h);
  }
}
