var data = require("./web/data.json");
module.exports={
	root: function (req, res) {
		response=[];
		for (key in data){
	    	//console.log(key);
	    	response.push(key);
	  	}
	  	res.json(response);
	},
	listall: function(req,res){
		response=[];
		for (key in data){
			for (affliction in data[key]){
				//console.log(key);
	    		response.push(
	    			{
	    				"type":key,
	    				"affliction":affliction
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
	listAfflictionDistrict: function(req,res){
		var type=String(req.params.type);
		var affliction=String(req.params.affliction);
		response=[];
		for (key in data[type][affliction]){
	    	response.push(key);
	  	}
	  	res.json(response);
	},
	getInfo: function(req,res){
		//needs type, affliction,district
		var type= String(req.params.type);
		var affliction=String(req.params.affliction);
		var district=String(req.params.district);
		res.json(data[type][affliction][district]["info"]);
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
	}
	
}
