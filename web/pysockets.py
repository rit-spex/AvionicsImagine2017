import time
import sys
import random
import math
import numpy as np

from socketIO_client import SocketIO
from solarpower import getSolarPower
from emitter import Emitter

HOST = 'localhost'
PORT = 3000
DELAY = 0.5 #default time

def get_delay(val):
    """returns a delay of the given value."""
    try:
        return float(val)/1000.0
    except ValueError:
        return DELAY #default time

def main(emitter):
    """Main functionality of the pysocket client."""
    delay = DELAY
    if len(sys.argv) > 1: #in seconds
        delay = get_delay(sys.argv[1])

    socket = SocketIO(HOST, PORT)
    while True:
        print("here")
        x_change, y_change, z_change = emitter.calculate_attitude()
        solar_power = getSolarPower(x_change, y_change, z_change)
        socket.emit('fromIMU',
                    {
                        'pitch':x_change,
                        'roll':y_change,
                        'yaw':z_change,
                        'isDeg':False,
                        'solarPower':solar_power
                    }
                   )
        time.sleep(delay)

if __name__ == '__main__':
    EMITTER = Emitter("/dev/ttyACM0", 9600)
    main(EMITTER)
