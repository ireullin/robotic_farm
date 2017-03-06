
#include "DHT.h"
#include <Wire.h>
#include <BH1750.h>


#define LED_PIN 13
#define DHT_PIN 12
#define DHTTYPE DHT22   // DHT 22  (AM2302), AM2321

//int heartBeat = 0;
DHT dht(DHT_PIN, DHTTYPE);
BH1750 lightMeter;

void setup() {
  
  pinMode(LED_PIN,OUTPUT);
  digitalWrite(LED_PIN,LOW);
  
  dht.begin();
  Serial.println("DHT_OK");
  
  lightMeter.begin();
  Serial.println("LUX_OK");
  
  Serial.begin(9600);
  while (!Serial) {delay(5);}
  Serial.println("READY");
  Serial.flush();
}

void loop() {
  /*
  heartBeat++;
  if(heartBeat==30000){
    Serial.println("ALIVE");
    heartBeat=0;
  }
  */

  String szCmd = readCmd();
  if(szCmd==""){
    return;
  }

  if(szCmd=="LED_ON"){
    Serial.println("LED_ON");
    Serial.flush();
    digitalWrite(LED_PIN,HIGH);
    delay(3);
    return;
  }

  if(szCmd=="LED_OFF"){
    Serial.println("LED_OFF");
    Serial.flush();
    digitalWrite(LED_PIN,LOW);
    delay(3);
    return;
  }

  if(szCmd=="INFO"){
    float airHum = dht.readHumidity();
    float airTmp = dht.readTemperature();
    uint16_t lux = lightMeter.readLightLevel();
    int soilHum = analogRead(A0);

    String buff = "{";
    buff += String("\"airHum\":\"") + airHum + String("\",");
    buff += String("\"airTmp\":\"") + airTmp + String("\",");
    buff += String("\"lux\":\"") + lux + String("\",");
    buff += String("\"soilHum\":\"") + soilHum + String("\"");
    buff += String("}");
    Serial.println(buff);
    return;
  }


  Serial.println("UNKNOWN_CMD '"+szCmd+"'");
  Serial.flush();
}

String readCmd(){
  String szCmd = "";
  if(Serial.available()<=0){
      return szCmd;
  }
  
  char c;
  while(true){
    if(Serial.available()<=0){
      continue;
    }
    
    c = Serial.read(); 
    if(c=='\n'){
      break;
    }
    else{
      szCmd += c;
    }
  }

  return szCmd;
}



