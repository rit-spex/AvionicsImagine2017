from socketIO_client import SocketIO
import time
from datetime import datetime
import sys
import random
import math
import numpy as np
from solarpower import getSolarPower
from emitter import Emitter

HOST = 'localhost'
PORT = 3000
DELAY = 0.5 #default time
NODE_NAME = 'AvionicsImagine1'

def getDelay(val):
  try:
    return float(val)/1000.0
  except ValueError:
    return DELAY #default time

def main(e):
  if(len(sys.argv) > 1): #in seconds
    delay = getDelay(sys.argv[1])

  socketIO = SocketIO(HOST, PORT)
  while(True):
    print("here")
    xChange, yChange, zChange = e.calculate_attitude()
    solarPower = getSolarPower(xChange, yChange, zChange)
    dataPacket = {
      dateCreated: datetime.utcnow(),
      name: NODE_NAME,
      payload:  {'isDeg':false, 'hasAvionics':true, 'roll':xChange, 'pitch':yChange, 'yaw':zChange, 'solar':solarPower}
    };
      
    socketIO.emit('sensorData': dataPacket)
    time.sleep(delay)

def readData():
  x = random.uniform(-0.01,0.01);
  y = random.uniform(-0.01,0.01);
  z = random.uniform(-0.01,0.01);
  return x, y, x;

if __name__ == '__main__':
  e = Emitter("/dev/ttyACM0", 9600)
  main(e)
