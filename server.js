var express = require('express'),
  app = express(),
  port = process.env.PORT || 3000;
var bodyParser = require('body-parser');
app.use(bodyParser.json()); // support json encoded bodies
app.use(bodyParser.urlencoded({ extended: true })); // support encoded bodies
var api = require('./API.js');
var data=require("./web/data.json");

app.use(function(req,res,next){
  res.header("Access-Control-Allow-Origin","*");
  res.header('Access-Control-Allow-Methods','GET,POST');
  res.header('Access-Control-Allow-Headers','Content-Type');
  next();
});
api.initial();
app.get('/all', api.all);

app.get('/list', api.root);
app.get('/list/all',api.listall);
app.get('/list/:type',api.listAffliction);
app.get('/list/:type/:affliction',api.listAfflictionProfile);

app.get('/info/:type/:affliction',api.getInfo);

app.get('/data/:type/:affliction/',api.getData);
app.get('/data/:type/:affliction/rows',api.getDataRows);
app.get('/data/:type/:affliction/cols',api.getDataCols);

app.post('/edit/cols/:type/:affliction',api.editCols);
app.post('/edit/rows/:type/:affliction',api.editRows);
app.post('/edit/info/:type/:affliction',api.editInfo);
app.post('/edit/data/:type/:affliction',api.editData);

app.post('/edit/type/:type/:affliction',api.changeType);
app.post('/add/row/:type/:affliction', api.addRow);
app.post('/add/affliction/:type',api.addAffliction);

app.post('/delete/:type/:affliction', api.deleteAffliction);


app.listen(port);

console.log('Magic happens on ' + port);
