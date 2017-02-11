#include <Wire.h>
#include <Math.h>
#include <SparkFunLSM9DS1.h>

// LSM9DS1 I2C
#define LSM9DS1_M   0x1E
#define LSM9DS1_AG  0x6B
#define GRAVITY     9.807
#define DECLINATION 11.48 //Magnetic declination in Rochester, NY
#define DELAY       1000

//float lightResistance;
float pitch, roll, heading;
float ax, ay, az, mx, my, mz;

LSM9DS1 imu;
void setup() {
    _init();
    Serial.begin(9600);
}

void loop() {
    //IMU
    printAttitude();
    printRawIMU();
    delay(DELAY);
    
    //Light Sensor
    /*int sensorVal = analogRead(0);
    lightResistance = (float) (1023-sensorVal) * 10 / sensorVal;
    Serial.println("================================");
    Serial.println("Analog read: " + sensorVal);
    Serial.println("Resistance: " + lightResistance, DEC);
    Serial.println("================================");
    delay(500);*/

    
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

void calculateAttitude() {
    readIMU();
    pitch = atan2(-ax, sqrt(ay * ay + az * az));
    roll = atan2(ay, az);
    heading;

    if(my == 0) {
        heading = (mx < 0) ? PI : 0;
    }
    else {
        heading = atan2(mx, my);
    }

    heading -= DECLINATION * PI / 180;

    if(heading > PI) {
        heading -= 2 * PI;
    }
    else if(heading < 0) {
        heading += 2 * PI;
    }

    pitch *= 180.0 / PI;
    roll *= 180.0 / PI;
    heading *= 180.0 / PI;
}

void printAttitude() {
    calculateAttitude();
    Serial.println("======Pitch, Roll, Heading======");
    Serial.print("Pitch: ");
    Serial.println(pitch, 2);
    Serial.print("Roll: ");
    Serial.println(roll, 2);
    Serial.print("Heading: ");
    Serial.println(heading, 2);
}

void printRawIMU() {
    readIMU();
    float accelX = imu.calcAccel(imu.ax) * GRAVITY;
    float accelY = imu.calcAccel(imu.ay) * GRAVITY;
    float accelZ = imu.calcAccel(imu.az) * GRAVITY;
    
    Serial.println("============Raw Data============");
    Serial.print(imu.calcAccel(imu.ax));
    Serial.println(" G");
    Serial.print(accelX);
    Serial.println(" m/s");
    Serial.print(imu.calcAccel(imu.ay));
    Serial.println(" G");
    Serial.print(accelY);
    Serial.println(" m/s");
    Serial.print(imu.calcAccel(imu.az));
    Serial.println(" G");
    Serial.print(accelZ);
    Serial.println(" m/s");
    Serial.println("================================");
    Serial.println("");
}

