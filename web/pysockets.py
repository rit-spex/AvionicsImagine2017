from socketIO_client import SocketIO
import time
import random

def main():
  HOST = 'localhost'
  PORT = 3000
  DELAY = 0.5 #in seconds

  socketIO = SocketIO(HOST, PORT)
  while(True):
    xChange, yChange, zChange = readData()
    socketIO.emit('fromIMU', {'x':xChange, 'y':yChange, 'z':zChange})
    time.sleep(DELAY)
def readData():
  x = random.uniform(-0.01,0.01);
  y = random.uniform(-0.01,0.01);
  z = random.uniform(-0.01,0.01);
  return x, y, x;

if __name__ == '__main__':
  main()
