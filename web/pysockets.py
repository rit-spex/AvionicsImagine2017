from socketIO_client import SocketIO
import time
from datetime import datetime
import sys
import json
import random
import math
import numpy as np
from solarpower import getSolarPower
from emitter import Emitter

HOST = 'localhost'
PORT = 3000
DELAY = 0.5 #default time
NODE_NAME = 'AVIONICS'
UUID = 'helloasd'

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

    print("HERE")
    socketIO = SocketIO(HOST, PORT)
    print('sad')
    time.sleep(0.5)
    socketIO.emit('join', {'name': UUID, 'type': 'dataSource'})
    while(True):
        print("here")
        x_change, y_change, z_change = emitter.calculate_attitude()
        solar_power = getSolarPower(x_change, y_change, z_change)
        dataPacket = {
          'dateCreated': time.time(),
          'name': NODE_NAME,
          'payload':  {'isDeg':False, 'hasAvionics':True, 'roll':x_change, 'pitch':y_change, 'yaw':z_change, 'solar':solar_power}
        }
        
        print(dataPacket)
        socketIO.emit('sensorData', json.dumps(dataPacket))
        time.sleep(.010)

def readData():
  x = random.uniform(-0.01,0.01);
  y = random.uniform(-0.01,0.01);
  z = random.uniform(-0.01,0.01);
  return x, y, x;

if __name__ == '__main__':
    EMITTER = Emitter("/dev/ttyACM0", 9600)
    main(EMITTER)
