var sys  = require('sys')
var exec = require('child_process').exec;

function puts(error, stdout, stderr) { sys.puts(stdout); sys.puts(stderr); }

//Instatiate server
var express = require('express');
var app     = module.exports = express();
 
// Setup a route that matches the following url: http://localhost:3000/
app.get("/", function (req, res, next) {
  
  // Respond to the request with hello.
  res.send("hello");
});

// Setup a route that matches the following urls: http://localhost:3000/api/ and anything after this.
app.get("/pandas", function(req, res, next) {
  console.log("CMD");
  exec("python ../script.py", puts);
  console.log("RAN CODE");
  var json = require('./data.json'); 

  // Respond to the request with a JSON object.
  res.send({ status: 200, response: json });
});

// Start listening on port 3000 on localhost
app.listen(3000, "localhost");
console.log("[ OK ] Listening on port 3000");
