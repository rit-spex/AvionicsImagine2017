#include <Wire.h>

#include <SparkFunLSM9DS1.h>

LSM9DS1 imu;
void setup() {
    init();
    Serial.begin(9600);
}

void loop() {
    imu.readAccel(); 
    Serial.write("===============================")
    Serial.write(String(imu.calcAccel(imu.ax), precision));
    Serial.write(String(imu.calcAccel(imu.ay), precision));
    Serial.write(String(imu.calcAccel(imu.az), precision));
    Serial.write("===============================")
    sleep(1); 
}

void init() {
    //////////////////////////////////////////////////////////////////////////
    /// Setup IMU
    imu.settings.device.commInterface = IMU_MODE_I2C;
    imu.settings.device.mAddress = LSM9DS1_M;
    imu.settings.device.agAddress = LSM9DS1_AG;
    
    // TODO: error check and handle imu failing to init
}

