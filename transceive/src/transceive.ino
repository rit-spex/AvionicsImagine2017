#include <Arduino.h>


// LoRa 9x_TX
// -*- mode: C++ -*-
// Example sketch showing how to create a simple messaging client (transmitter)
// with the RH_RF95 class. RH_RF95 class does not provide for addressing or
// reliability, so you should only use RH_RF95 if you do not need the higher
// level messaging abilities.
// It is designed to work with the other example LoRa9x_RX

#include <SPI.h>
#include <RH_RF95.h>
#include <Wire.h>
#include <math.h>
#include <SparkFunLSM9DS1.h>
#include <string.h>

//
// LSM9DS1 I2C
#define LSM9DS1_M   0x1E
#define LSM9DS1_AG  0x6B

#define RFM95_CS 10
#define RFM95_RST 9
#define RFM95_INT 2

// Change to 434.0 or other frequency, must match RX's freq!
#define RF95_FREQ 915.0

// Singleton instance of the radio driver
RH_RF95 rf95(RFM95_CS, RFM95_INT);

LSM9DS1 imu;

float pitch, roll, heading;
float ax, ay, az, mx, my, mz;

void setup()
{
  pinMode(RFM95_RST, OUTPUT);
  digitalWrite(RFM95_RST, HIGH);

  while (!Serial);
  Serial.begin(9600);
  delay(100);

  Serial.println("Arduino LoRa TX Test!");

  // manual reset
  digitalWrite(RFM95_RST, LOW);
  delay(10);
  digitalWrite(RFM95_RST, HIGH);
  delay(10);

  while (!rf95.init()) {
    Serial.println("LoRa radio init failed");
    while (1);
  }
  Serial.println("LoRa radio init OK!");

  // Defaults after init are 434.0MHz, modulation GFSK_Rb250Fd250, +13dbM
  if (!rf95.setFrequency(RF95_FREQ)) {
    Serial.println("setFrequency failed");
    while (1);
  }
  Serial.print("Set Freq to: "); Serial.println(RF95_FREQ);

  // Defaults after init are 434.0MHz, 13dBm, Bw = 125 kHz, Cr = 4/5, Sf = 128chips/symbol, CRC on

  // The default transmitter power is 13dBm, using PA_BOOST.
  // If you are using RFM95/96/97/98 modules which uses the PA_BOOST transmitter pin, then
  // you can set transmitter powers from 5 to 23 dBm:
  rf95.setTxPower(23, false);
  Serial.print("Calling _init");
  _init();
  Serial.println("_init passed");
}

int16_t packetnum = 0;  // packet counter, we increment per xmission

void loop()
{
  readIMU();
  Serial.println("Sending to rf95_server");
  // Send a message to rf95_server

  char data[4];
  Serial.println(ax);
  memcpy(&data, &ax, sizeof(data));
  Serial.print("Sending "); Serial.println(data);

  Serial.println("Sending..."); delay(10);
  rf95.send((uint8_t *)data, sizeof(data));

  Serial.println("Waiting for packet to complete..."); delay(10);
  rf95.waitPacketSent();
  delay(1000);
}

void _init() {
    //////////////////////////////////////////////////////////////////////////
    /// Setup IMU
    imu.settings.device.commInterface = IMU_MODE_I2C;
    imu.settings.device.mAddress = LSM9DS1_M;
    imu.settings.device.agAddress = LSM9DS1_AG;
    imu.begin();

    // TODO: error check and handle imu failing to init
}

void readIMU() {
    imu.readGyro();
    imu.readAccel();
    imu.readMag();

    ax = imu.ax;
    ay = imu.ay;
    az = imu.az;
    mx = imu.mx;
    my = imu.my;
    mz = imu.mz;
}
