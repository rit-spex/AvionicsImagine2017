from socketIO_client import SocketIO
import time
import sys
import random
from serial_in import calculate_attitude

HOST = 'localhost'
PORT = 3000
DELAY = 0.5 #default time



def getDelay(val):
  try:
    return float(val)/1000.0
  except ValueError:
    return DELAY #default time

def main():
  if(len(sys.argv) > 1): #in seconds
    delay = getDelay(sys.argv[1])

  socketIO = SocketIO(HOST, PORT)
  while(True):
    print("here")
    xChange, yChange, zChange = calculate_attitude()
    socketIO.emit('fromIMU', {'x':xChange, 'y':yChange, 'z':zChange})
    time.sleep(delay)

def readData():
  x = random.uniform(-0.01,0.01);
  y = random.uniform(-0.01,0.01);
  z = random.uniform(-0.01,0.01);
  return x, y, x;

if __name__ == '__main__':
  main()
