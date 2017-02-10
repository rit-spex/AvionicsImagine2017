#include <Wire.h>

#include <SparkFunLSM9DS1.h>

// LSM9DS1 I2C
#define LSM9DS1_M   0x1E
#define LSM9DS1_AG 0x6B

LSM9DS1 imu;
void setup() {
    _init();
    Serial.begin(9600);
}

void loop() {
    imu.readAccel(); 
    Serial.println("===============================");
    Serial.println(imu.calcAccel(imu.ax));
    Serial.println(imu.calcAccel(imu.ay));
    Serial.println(imu.calcAccel(imu.az));
    Serial.println("===============================");
    delay(1); 
}

void _init() {
    //////////////////////////////////////////////////////////////////////////
    /// Setup IMU
    imu.settings.device.commInterface = IMU_MODE_I2C;
    imu.settings.device.mAddress = LSM9DS1_M;
    imu.settings.device.agAddress = LSM9DS1_AG;
    
    // TODO: error check and handle imu failing to init
}

