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
#include <transceive.hpp>
#include <Wire.h>
#include <math.h>
#include <SparkFunLSM9DS1.h>
#include <string.h>
// #include <elapsedMillis.h>

#define MESSAGE_SIZE 36

// Singleton instance of the radio driver
RH_RF95 rf95(RFM95_CS, RFM95_INT);

LSM9DS1 imu;
// ax ay az mx my mz gx gy gz
float imuRegister[9];
uint8_t message[MESSAGE_SIZE];


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

void loop()
{
  readIMU();
  sendMessage();
  Serial.println("Sending to rf95_server");
  delay(1000);
}

void _init() {
    //////////////////////////////////////////////////////////////////////////
    /// Setup IMU
    imu.settings.device.commInterface = IMU_MODE_SPI;
    imu.settings.device.mAddress = LSM9DS1_M_CS;
    imu.settings.device.agAddress = LSM9DS1_AG_CS;
    imu.begin();

    // TODO: error check and handle imu failing to init
}

void readIMU() {
    imu.readGyro();
    imu.readAccel();
    imu.readMag();

    imuRegister[AX] = imu.calcAccel(imu.ax);
    imuRegister[AY] = imu.calcAccel(imu.ay);
    imuRegister[AZ] = imu.calcAccel(imu.az);
    imuRegister[MX] = imu.calcMag(imu.mx);
    imuRegister[MY] = imu.calcMag(imu.my);
    imuRegister[MZ] = imu.calcMag(imu.mz);
    imuRegister[GX] = imu.calcGyro(imu.gx);
    imuRegister[GY] = imu.calcGyro(imu.gy);
    imuRegister[GZ] = imu.calcGyro(imu.gz);
}

void sendMessage() {
    memcpy(&message, &imuRegister, sizeof(imuRegister));
    rf95.send(message, sizeof(message));
    rf95.waitPacketSent();
}
