from socketIO_client import SocketIO
import time
import sys
import random
import math
import numpy as np
from emitter import Emitter

HOST = 'localhost'
PORT = 3000
DELAY = 0.5 #default time

# Def of points on cube
CUBE_SIZE = 5
V1 = -CUBE_SIZE, CUBE_SIZE, -CUBE_SIZE
V2 = CUBE_SIZE, CUBE_SIZE, -CUBE_SIZE
V3 = -CUBE_SIZE, -CUBE_SIZE, -CUBE_SIZE
V4 = CUBE_SIZE, -CUBE_SIZE, -CUBE_SIZE
V5 = -CUBE_SIZE, CUBE_SIZE, CUBE_SIZE
V6 = CUBE_SIZE, CUBE_SIZE, CUBE_SIZE
V7 = -CUBE_SIZE, -CUBE_SIZE, CUBE_SIZE
V8 = CUBE_SIZE, -CUBE_SIZE, CUBE_SIZE
SUN = 10, 10, 10

def unit_vector(vector):
    """ Returns the unit vector of the vector.  """
    return vector / np.linalg.norm(vector)

def angle_between(v1, v2):
    """ Returns the angle in radians between vectors 'v1' and 'v2'::

            >>> angle_between((1, 0, 0), (0, 1, 0))
            1.5707963267948966
            >>> angle_between((1, 0, 0), (1, 0, 0))
            0.0
            >>> angle_between((1, 0, 0), (-1, 0, 0))
            3.141592653589793
    """
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))


def getDelay(val):
  try:
    return float(val)/1000.0
  except ValueError:
    return DELAY #default time

def rotate(x, y, z, pitch, roll, yaw):
    return x * math.sin(yaw) * math.cos(pitch), y * math.sin(pitch) * math.cos(roll), z * math.sin(roll) * math.cos(yaw)

def getNormalVector(v1, v2):
    return tuple(x+y for x, y in zip(v1, v2)) 

def getPlanes(v1, v2, v3, v4, v5, v6, v7, v8):
    return (getNormalVector(v1, v7), getNormalVector(v1, v6), getNormalVector(v6, v7), getNormalVector(v6, v4), getNormalVector(v4, v7), getNormalVector(v1, v4))

def getSolarPower(pitch, roll, yaw):
    verticies = (V1, V2, V3, V4, V5, V6, V7, V8)
    verticies = tuple(rotate(*v, pitch, roll, yaw) for v in verticies)
    planes = getPlanes(*verticies)
    angles = tuple(angle_between(v, SUN) for v in planes)
    angles = tuple(num for num in angles if num >= 0)
    intensities = tuple(math.cos(angle) for angle in angles)
    return sum(intensities)

def main(e):
  if(len(sys.argv) > 1): #in seconds
    delay = getDelay(sys.argv[1])

  socketIO = SocketIO(HOST, PORT)
  while(True):
    print("here")
    xChange, yChange, zChange = e.calculate_attitude()
    solarPower = getSolarPower(xChange, yChange, zChange)
    socketIO.emit('fromIMU', {'x':xChange, 'y':yChange, 'z':zChange, 'solar':solarpower})
    time.sleep(delay)

def readData():
  x = random.uniform(-0.01,0.01);
  y = random.uniform(-0.01,0.01);
  z = random.uniform(-0.01,0.01);
  return x, y, x;

if __name__ == '__main__':
  e = Emitter("/dev/ttyAMA0", 9600)
  main(e)
