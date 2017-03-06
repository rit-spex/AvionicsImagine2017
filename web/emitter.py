import serial
import ctypes
import struct
import math

SOH = b'\x01'
NUM_FLOATS = 6
NUM_BYTES = NUM_FLOATS * 4
DECLINATION = 11.47


class Emitter:
    def __init__(self, port_name, baud_rate):
        self.port_name = port_name
        self.baud_rate = baud_rate
        self.port = serial.Serial(port_name, baudrate=baud_rate)

        def get_data(self):
            while True:
                if (self.port.read(1) == SOH):
                    break
            return (struct.unpack(('f' * NUM_FLOATS), port.read(NUM_BYTES)))

        def calculate_attitude(self):
            data = self.get_data()
            ax = data[0]
            ay = data[1]
            az = data[2]
            mx = data[3]
            my = data[4]
            mz = data[5]

            pitch = math.atan2(-ax, math.sqrt(ay * ay + az * az))
            roll = math.atan2(ay, az)
            heading = 0.0

            if(my == 0):
                heading = (mx < 0) if math.pi else 0
            else:
                heading = math.atan2(mx, my)

            heading -= DECLINATION * math.pi / 180.0

            if(heading > math.pi):
                heading -= 2 * math.pi
            elif(heading < 0):
                heading += 2 * math.pi

            pitch *= 180.0 / math.pi
            roll *= 180.0 / math.pi
            heading *= 180.0 / math.pi

            return pitch, roll, heading


if __name__ == '__main__':
    while True:
        print(calculate_attitude())
        # print(get_data())
