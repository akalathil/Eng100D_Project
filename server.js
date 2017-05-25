var express = require('express'),
  app = express(),
  port = process.env.PORT || 3000;
app.get('/', function (req, res) {
  res.send('Hello World!')
})
app.listen(port);

console.log('Magic happens on ' + port);
