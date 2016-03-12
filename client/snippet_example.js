/*
* @Author: Karthik
* @Date:   2016-03-12 20:09:31
* @Last Modified by:   Karthik
* @Last Modified time: 2016-03-12 21:12:59
*/

'use strict';
// load jQuery if not loaded
SEND_INT = 5000;

field_descs = {"userAgent":{"type":"session"}};

if(!window.jQuery)
{
	var script = document.createElement('script');
	script.type = "text/javascript";
	script.src = "http://code.jquery.com/jquery-2.2.1.min.js";
	document.getElementsByTagName('head')[0].appendChild(script);
}

function add_tracklib () {
	var script = document.createElement('script');
	script.type = "text/javascript";
	script.src = "http://localhost:8000/lib/tracklib.js";
	document.getElementsByTagName('head')[-1].appendChild(script);
}();




