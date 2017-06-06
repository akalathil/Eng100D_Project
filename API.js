var data = require("./web/data.json");
module.exports={
	root: function (req, res) {
		response=[];
		for (key in data){
	    	console.log(key);
	    	response.push(key);
	  	}
	  	res.json(response);
	}
	
}
