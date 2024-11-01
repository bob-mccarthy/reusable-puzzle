#include <Arduino.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128 // OLED display width, in pixels
#define SCREEN_HEIGHT 32 // OLED display height, in pixels

#define OLED_RESET     -1 // Reset pin # (or -1 if sharing Arduino reset pin)
#define SCREEN_ADDRESS 0x3C ///< See datasheet for Address; 0x3D for 128x64, 0x3C for 128x32
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);


void setup() {
  Wire.begin();
  Serial.begin(115200);

  if(!display.begin(SSD1306_SWITCHCAPVCC, SCREEN_ADDRESS)) {
    Serial.println(F("SSD1306 allocation failed"));
    for(;;); // Don't proceed, loop forever
  }

  display.clearDisplay();
  // Draw a single pixel in white
  display.drawPixel(10, 10, SSD1306_WHITE);
  display.display();
}

void loop() {
  for (int i = 1; i <= 9; i++)
  {
    Wire.beginTransmission(i);
    uint8_t error = Wire.endTransmission();
    if (error != 0)
    {
      Serial.println("Puzzle Piece not found at address: " + (String) i);
      continue;
    }
    Wire.requestFrom(i, 1);
    while(Wire.available())
    {
      uint8_t position = Wire.read();
      Serial.println(position);
    }
  }
  delay(1000);
  
}

