import serial
import ctypes
import struct

SOH = b'\x01'

port = serial.Serial("/dev/ttyACM2")

def get_data():
    # wait on SOH character to read in all data values
    while True:
        if (port.read(1) == SOH):
            break
    return(struct.unpack('fffffffff', port.read(36)))

if __name__ == '__main__':
    while True:
        print(get_data())
