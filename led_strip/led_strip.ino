#include <FastLED.h>
#define NUM_LEDS 50
#define DATA_PIN 11
#define CLOCK_PIN 13


#define MY_PINK CRGB(97, 33, 45)
#define MY_PURPLE CRGB(51, 13, 51)

CRGB leds[NUM_LEDS];
uint8_t *ledsRaw = (uint8_t *)leds;



void showAll(CRGB color) {
  for (int led = 0; led < NUM_LEDS; led = led + 1) {
    leds[led] = color;
    FastLED.show();
  }
}

void setOneLed(uint8_t led_num, CRGB color) {
  leds[led_num] = color;
  FastLED.setBrightness(50);
  FastLED.show();
}

void setup() {
  delay(200);

  FastLED.addLeds<WS2801, DATA_PIN, CLOCK_PIN, RGB>(leds, NUM_LEDS);

  showAll(CRGB::Black);

}

uint8_t offset = 0;

void loop() {
  if (offset == NUM_LEDS-7) {
    offset = 0;
    showAll(CRGB::Black);
  }
  setOneLed(0+offset, CRGB::Black);
  // red
  setOneLed(1+offset, CRGB::Red);
  // orange
  setOneLed(2+offset, CRGB::OrangeRed);
  // yellow 
  setOneLed(3+offset, CRGB::Yellow);
  // green
  setOneLed(4+offset, CRGB::Green);
  // blue
  setOneLed(5+offset, CRGB::Blue);
  // purple
  setOneLed(6+offset, MY_PURPLE);
  // pink
  setOneLed(7+offset, MY_PINK);

  delay(30);
  
  offset++;
}
