#include <Adafruit_NeoPixel.h>
#define BRIGHTNESS 50
#define PIN      6
#define NUMPIXELS 24
// Parameter 1 = number of pixels in strip
// Parameter 2 = pin number (most are valid)
// Parameter 3 = pixel type flags, add together as needed:
//   NEO_KHZ800  800 KHz bitstream (most NeoPixel products w/WS2812 LEDs)
//   NEO_KHZ400  400 KHz (classic 'v1' (not v2) FLORA pixels, WS2811 drivers)
//   NEO_GRB     Pixels are wired for GRB bitstream (most NeoPixel products)
//   NEO_RGB     Pixels are wired for RGB bitstream (v1 FLORA pixels, not v2)
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);

void setup() {
Serial.begin(115200);              //Starting serial communication
strip.begin();                      
Serial.setTimeout(50);             //czas jaki serial czeka na dane (domyślnie 1 sekunda)
}

void loop() {
  if(Serial.available()){         //
      String s=Serial.readString();
      if(s[0]=='r')
        turnOn(s.substring(1).toInt());
      else 
        turnOff(s.substring(1).toInt());
      }
}

void turnOn(int ledNumber) {
  if(ledNumber>0 && ledNumber<=NUMPIXELS) {
  strip.setPixelColor(ledNumber-1, strip.Color(0,230,0));
  strip.show(); }
}

void turnOff(int ledNumber){
  if(ledNumber>0 && ledNumber<=NUMPIXELS) {
  strip.setPixelColor(ledNumber-1, strip.Color(0,0,0));
  strip.show(); }
}


