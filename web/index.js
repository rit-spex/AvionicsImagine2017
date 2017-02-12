var express = require('express');
var app = express();
var http = require('http').Server(app);
var io = require('socket.io')(http);

app.get('/', function(req,res)
{
  res.sendFile(__dirname + '/index.html');
});

app.use(express.static(__dirname + '/public'));

io.on('connection',function(socket){
  console.log('a user connected');
  socket.on('disconnect', function() {
    console.log('user disconnected');
  });

  socket.on('fromIMU', function(data){
    console.log(Object.keys(data));
    io.emit('toClient', all={x:data['x'], y:data['y'], z:data['z']});
    console.log(data);
  });
});

http.listen(3000, function(){
  console.log('listending on *:3000');
});
