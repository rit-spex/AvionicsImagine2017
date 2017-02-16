## Requires
* [Python 3](https://www.python.org)
  * [socketIO-client](https://pypi.python.org/pypi/socketIO-client)
* [Node.js](https://nodejs.org)
  * [Socket.io](http://socket.io)

### Getting them

[socketIO-client](https://pypi.python.org/pypi/socketIO-client):
(this assumes Python is already installed)
````
pip install -U socketIO-client
````


[Node.js](https://nodejs.org/en/download/):
````
curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
sudo apt-get install -y nodejs
````

[Socket.io](http://socket.io/download/):
````
npm install socket.io
````

## Running
(recommended order)
````
node index.js
````

````
python pysockets.py
````
If you have both Python 2 & Python 3 installed (such as a Raspberry Pi), Python 3 is likely `python3` in your PATH, so you will need to change the previous command to:
````
python3 pysockets.py
````
