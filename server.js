var express = require('express'),
  app = express(),
  port = process.env.PORT || 3000;
var api = require('./API.js');
app.get('/list', api.root);
app.get('/list/:type',api.listAffliction);
app.get('/list/:type/:affliction',api.listAfflictionDistrict);
app.get('/info/:type/:affliction/:district',api.getInfo);
app.get('/data/:type/:affliction/',api.getData);
app.get('/data/:type/:affliction/rows',api.getDataRows);
app.get('/data/:type/:affliction/cols',api.getDataCols);
app.listen(port);

console.log('Magic happens on ' + port);
