/*
* @Author: Karthik
* @Date:   2016-03-12 20:09:31
* @Last Modified by:   Karthik
* @Last Modified time: 2016-03-13 03:38:22
*/


$(document).ready(function(){
// 'use strict';
// load jQuery if not loaded
SEND_INT = 5000;

FIELD_DESCS = {"userAgent":{"type":"session"}, 
			   "browser":{"type":"session"},
				"os" : {"type":"session"},
				"mobile":{"type":"session"},
				"screen_res": {"type":"session"},
				"referrer" : {"type":"page"},
				"sessionStart": {"type":"session"},
				"pageStart": {"type":"page"}
			};


// if(!window.jQuery)
// {
// 	var script = document.createElement('script');
// 	script.type = "text/javascript";
// 	script.src = "http://code.jquery.com/jquery-2.2.1.min.js";
// 	document.getElementsByTagName('head')[0].appendChild(script);
// };

function add_jscookie () {
	// var script = document.createElement('script');
	// script.type = "text/javascript";
	// script.src = "http://localhost:8000/lib/js_cookie.js";
	// script.src = "file:///home/karthik/Projects/Furlencode/client/js_cookie.js";
	script = $.getScript("http://localhost:8000/js_cookie.js");
	console.log(script);
	$('head').append('<script src="http://localhost:8000/js_cookie.js"></script>');
};
add_jscookie();

function add_tracklib () {
	var script = document.createElement('script');
	// script.type = "text/javascript";
	// script.src = "http://localhost:8000/lib/tracklib.js";
	// script.src = "file:///home/karthik/Projects/Furlencode/client/tracklib.js";
	// script = $.getScript("http://localhost:8000/tracklib.js");
	$('head').append('<script src="http://localhost:8000/tracklib.js"></script>');

	// $('head').append(script);
};
add_tracklib();

});



