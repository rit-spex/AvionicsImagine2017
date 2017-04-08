## Requires
* [Python 3](https://www.python.org)
  * [socketIO-client](https://pypi.python.org/pypi/socketIO-client)
  * [pySerial](https://pythonhosted.org/pyserial/)
  * [NumPy](http://www.numpy.org)
* [Node.js](https://nodejs.org)
  * [Express](http://expressjs.com)
  * [Socket.io](http://socket.io)

### Getting them

[socketIO-client](https://pypi.python.org/pypi/socketIO-client):
(this assumes Python is already installed)
````
pip install -U socketIO-client
````
Make sure this installs for Python 3, not Python 2
If you're having issues try
````
apt-get install python3-pip
pip3 install -U socketIO-client
````

[NumPy](https://www.scipy.org/scipylib/download.html):
````
pip install -U numpy
````
[pySerial](https://pypi.python.org/pypi/pyserial):
````
pip install -U pyserial
````

[Node.js](https://nodejs.org/en/download/):
````
curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
sudo apt-get install -y nodejs
````

[Express](http://expressjs.com/en/starter/installing.html):
````
npm install --save express
````

[Socket.io](http://socket.io/download/):
````
npm install --save socket.io
````

## Running
(recommended order)
````
node index.js
````

````
python pysockets.py [delay/period-in-ms]
````
If you have both Python 2 & Python 3 installed (such as on a Raspberry Pi), Python 3 is likely `python3` in your PATH, so you will need to change the previous command to:
````
python3 pysockets.py [delay/period-in-ms]
````

[delay/period-in-ms]
This optional argument will change the delay between each update (read & transmit) to the desired value (in milliseconds). If this option is not provided, the default delay is 500 ms (0.5 s).
