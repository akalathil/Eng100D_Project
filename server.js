var express = require('express'),
  app = express(),
  port = process.env.PORT || 3000;
var data=require("./web/data.json");
var api= require("./API.js");
app.get('/', api.root);
app.listen(port);

console.log('Magic happens on ' + port);
