# Welcome to Lesson #4: GPS Sensor

## Working with GPS sensor data using the Arduino language

#### Pre-requisites:
- It is recommended that you have successfully completed the [blinky lights lesson](https://github.com/StateFarm-STEM/pyinthesky/tree/main/lesson2#welcome-to-lesson-2)

#### Objectives:
- Wire up the GPS to the Arduino
- Read GPS sensor data
- Print the GPS sensor data to the serial port
- Monitor data on the serial monitor in the Arduino IDE

#### What you will be using:
- [Arduino IDE](https://github.com/StateFarm-STEM/hablogger/blob/main/c/arduino/lesson5/screenshots/arduino-ide.png)
- [Arduino Uno](https://github.com/StateFarm-STEM/hablogger/blob/main/c/arduino/lesson5/screenshots/arduino-uno-r3.png)
- [GPS GT-U7 Sensor (GPS NEO 6M clone)](https://github.com/StateFarm-STEM/hablogger/blob/main/c/arduino/lesson4/screenshots/gps-gt-u7.png)
- [5 pin connector](https://github.com/StateFarm-STEM/hablogger/blob/main/c/arduino/lesson4/screenshots/5-pin-connector.png)
- [Breadboard](https://github.com/StateFarm-STEM/hablogger/blob/main/c/arduino/lesson5/screenshots/breadboard.png)
- [Jumper Wires](https://github.com/StateFarm-STEM/hablogger/blob/main/c/arduino/lesson3/screenshots/1956-02.jpg)

#### Note: I had some issues using the GPS module from inside my garage. If you do not get data on your serial monitor. Here are some things you can try to get good results...<br>
- Try working near a window with the best view of the sky
- Try taking your laptop outside along with the Arduino and all of its components that are connected
- If it works where you like to work, then great

#### What you will be learning:
- How to connect the GPS GT-U7 to the Arduino without using a breadboard (changes it up just a little here compared to lesson 3)
- How to create a new Arduino Sketch project using the TinyGPSPlus Library
- Write the code in the Arduino IDE and upload it to the Arduino
  - Read Latitude, Longitude, Altitude, speed, and the number of satellites you are connected to from the GPS module
  - Print your results to the Arduino's serial port
- Watch your code run on the Arduino using Arduino IDE's serial monitor

## Guide
Click this link and watch this YouTube video [How to use the GT U7 GPS module](https://youtu.be/7zw2ULu73DY)


#### Helpful video shortcuts
- [Connect the GPS GT-U7 to the Arduino](https://youtu.be/7zw2ULu73DY?t=54)

**Video on how to install the library**

https://user-images.githubusercontent.com/91698286/181350144-9dad1089-92e9-4f3b-83c9-cef32049bd07.mp4


#### Tips
- **Unplug the Arduino from the computer before doing this**
- Make sure everything is wired correctly, if you did not catch the wiring in the video, use the chart below. 
- The color of the wires do not matter as long as they are connected to the right pins



<img src=https://github.com/StateFarm-STEM/hablogger/blob/main/c/arduino/lesson4/screenshots/GPSback.jpg width="500">
<img src=https://github.com/StateFarm-STEM/hablogger/blob/main/c/arduino/lesson4/screenshots/ArduinoBackGPS.jpg width="500">

<img src=https://github.com/StateFarm-STEM/hablogger/blob/main/c/arduino/lesson4/screenshots/ArdiunoFrountGPS.jpg width="500">


### Pinout chart

  **Pin on the GPS module** | **Pin on the Arduino**
  --------------- | --------------- 
  TXD   | Digital pin 11
  RXD   | Digital pin 10
  GND  | Any Ground pin 
  VDC   | 5 volts
  
  
  
#### How to get the TinyGPSPlus library:
- Navigate to the sketch menu and hover over include library and then click manage libraries
- Type in TinyGPSPlus and install the library and then restart the IDE
- Copy and paste this code into a sketch and run it
``` 
#include "TinyGPSPlus.h"
#include <SoftwareSerial.h>

// Create the serial_connection
//
// Connect the GT-U7 RX and TX to the Arduino
// using the following connections...
// RX=pin --> Arduino analog 10
// TX pin --> Arduino analog 11
//
// In the code below on line 14 is the constructor.
// use the TX pin number as the first argument
// use the RX pin number as the second argument
SoftwareSerial serial_connection(11, 10);

TinyGPSPlus gps;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  serial_connection.begin(9600);
  Serial.println("GPS Start");
}

void loop() {
  // put your main code here, to run repeatedly:
  while(serial_connection.available())
  {
    gps.encode(serial_connection.read());
  }
  if(gps.location.isUpdated())
  {
    Serial.println("Satellite Count:");
    Serial.println(gps.satellites.value());
    Serial.println("Latitude:");
    Serial.println(gps.location.lat(), 6);
    Serial.println("Longitude:");
    Serial.println(gps.location.lng(), 6);
    Serial.println("Speed MPH:");
    Serial.println(gps.speed.mph());
    Serial.println("Altitude Feet:");
    Serial.println(gps.altitude.feet());
    Serial.println("");
  }
}
  ```


## Troubleshooting 
- If your GPS is not reading out coordinates on the COM port you may have to move outside
- You need to have the TinyGPSPlus library installed in order for the code to work, refer to the video further up this page for more help

### Review
- Learned how to connect the GPS GT-U7 to the Arduino without using a breadboard (changes it up just a little here compared to lesson 3)
- How to create a new Arduino Sketch project using the TinyGPSPlus Library


### [Need help?](https://github.com/StateFarm-STEM/pyinthesky#need-some-help)

