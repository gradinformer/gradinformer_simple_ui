var endPoint = 'http://85.143.221.107:1337/api/'

params = {};


var result = getEvents(params);
renderEvent(result);


function getEvents(params){

	request_string = "http://85.143.221.107:1337/api/event?type=energy";

	$.ajax({
		url: request_string,
		success: function(result){
			console_log(result);
			return result;
		}
	});
}


function renderEvent(event_json){
		
};