var data = require("./web/data.json");
module.exports={
	initial: function(){
		var d=new Date();
		var n=d.getTime();
	  	for(type in data){
		    for (affliction in data[type]){
		      data[type][affliction]["info"]={
		        "name":affliction,
		        "date":n,
		        "views":0,
		        "description":affliction
		      };
		    }
	  	};
	  	console.log("HELLO");
	},
	all:function(req,res){
		res.json(data);
	},
	root: function (req, res) {
		response=[];
		for (key in data){
	    	//console.log(key);
	    	response.push(key);
	  	}
	  	res.json(response);
	},
	listall: function(req,res){
		var d=new Date();
		var n=d.getTime();
		response=[];
		for (key in data){
			for (affliction in data[key]){
				//console.log(key);
				var temp=data[key][affliction]["info"]
	    		response.push(
	    			{
	    				"type":key,
	    				"affliction":affliction,
	    				"name":temp["name"],
	    				"date":temp["date"],
	    				"views":temp["views"],
	    				"description":temp["description"]
	    			}
	    		);
			}
	    	
	  	}
	  	res.json(response);
	},
	listAffliction: function(req,res){
		var type=String(req.params.type);
		response=[];
		for (key in data[type]){
	    	response.push(key);
	  	}
	  	res.json(response);
	},
	listAfflictionProfile: function(req,res){
		var type=String(req.params.type);
		var affliction=String(req.params.affliction);
		response=[];

		/*for (key in data[type][affliction]){
	    	response.push(key);
	  	}*/
	  	res.json(data[type][affliction]);
	},
	getInfo: function(req,res){
		//needs type, affliction
		var type= String(req.params.type);
		var affliction=String(req.params.affliction);
		res.json(data[type][affliction]["info"]);
	},
	getData: function(req,res){
		//needs type, affliction,district
		var type= String(req.params.type);
		var affliction=String(req.params.affliction);
		res.json(data[type][affliction]["Data"]);
	},
	getDataRows: function(req,res){
		var type= String(req.params.type);
		var affliction=String(req.params.affliction);
		res.json(data[type][affliction]["Data"]["rows"]);
	},
	getDataCols: function(req,res){
		var type= String(req.params.type);
		var affliction=String(req.params.affliction);
		res.json(data[type][affliction]["Data"]["cols"]);
	},
	editCols: function(req,res){
		/*
		{
			[col1,col2,col3...]
		}
		*/
		var type= String(req.params.type);
		var affliction=String(req.params.affliction);
		data[type][affliction]["Data"]["cols"]=req.body;
		res.send("SUCCESS");
	},
	editRows: function(req,res){
		/*
			{			
				"0": Name
				"1": Year
				"2": Value
				"index":0
			}
		*/
		var type= String(req.params.type);
		var affliction=String(req.params.affliction);
		var index=req.body.index;
		var temp=JSON.parse(data[type][affliction]["Data"]["rows"]);
		temp[index]={
						"Latitude":temp[index].Latitude,
						"Longitude": temp[index].Longitude
					};
		for (key in req.body){
			if (key!="index" && !isNaN(key)){
				temp[index][key]=req.body[key]
			}
		}
		data[type][affliction]["Data"]["rows"]=JSON.stringify(temp);
		res.send(req.body);
	},
	editInfo: function(req,res){
		/*
		{
			"name":"X",
			"date":Y,
			"views":Z,
			"description":"new description"
		}
		*/
		var type= String(req.params.type);
		var affliction=String(req.params.affliction);
		data[type][affliction]["info"]={
			"name":req.body.name,
			"date":req.body.date,
			"views":req.body.views,
			"description":req.body.description
		};
		res.json(data[type][affliction]["info"]);
	},
	addRow: function(req,res){
		/*
		{
			"0":Name,
			"1":Year,
			"2":Value,
			"Latitude":Lat,
			"Longitude":Long
		}
		*/
		var type= String(req.params.type);
		var affliction=String(req.params.affliction);
		tempData={};
		for (key in req.body){
			if (key=="Longitude"||key=="Latitude" || !isNaN(key)){
				tempData[key]=req.body[key];
			}
		}
		temp=JSON.parse(data[type][affliction]["Data"]["rows"]);
		temp.push(tempData);
		data[type][affliction]["Data"]["rows"]=JSON.stringify(temp);
		res.send("SUCCESSFUL ADD");
	},
	addAffliction: function(req,res){
		/*
		{
		    "name": Name,
		    "description": description
		}
		*/
		var d=new Date();
		var n=d.getTime();
		var type= String(req.params.type);
		temp={
			"Data":{
				"cols":[],
				"rows":[]
			},
			"info": {
			    "name": req.body.name,
			    "date": n,
			    "views": 0,
			    "description": req.body.description
			}	
		};
		data[type][req.body.name]=temp;
		res.send("SUCCESSFUL ADD");
	},
	changeType: function(req,res){
		/*
		{
			"type": new type
		}
		*/
		var type= String(req.params.type);
		var affliction=String(req.params.affliction);
		var newtype=String(req.body.type);
		data[newtype][affliction]=data[type][affliction];
		delete data[type][affliction];
		res.send("SUCCESSFUL CHANGE");
	}
	
}
