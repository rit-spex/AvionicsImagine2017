import serial
import ctypes
import struct
import math

SOH = b'\x01'

port = serial.Serial("/dev/ttyACM2")
declination = 11.48

def get_data():
    # wait on SOH character to read in all data values
    while True:
        if (port.read(1) == SOH):
            break
    return(struct.unpack('fffffffff', port.read(36)))

def calculate_attitude():
    data = get_data()
    ax = data[0]
    ay = data[1]
    az = data[2]
    mx = data[3]
    my = data[4]
    mz = data[5]

    pitch = math.atan2(-ax, math.sqrt(ay * ay + az * az))
    roll = math.atan2(ay, az)
    heading

    if(my == 0)
        heading = (mx < 0) ? math.pi : 0
    else
        heading = math.atan2(mx, my)

    heading -= declination * math.pi / 180.0

    if(heading > math.pi)
        heading -= 2 * math.pi
    else if(heading < 0)
        heading += 2 * math.pi

    pitch *= 180.0 / math.pi
    roll *= 180.0 / math.pi
    heading *= 180.0 / math.pi

    tup = (pitch, roll, heading)
    return tup

if __name__ == '__main__':
    while True:
        print(calculate_attitude())
