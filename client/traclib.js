/*
* @Author: Karthik
* @Date:   2016-03-12 15:19:08
* @Last Modified by:   Karthik
* @Last Modified time: 2016-03-12 16:52:51
*/

var track_info = []
'use strict';
// compiles the tracking info to be sent to the analytics server
function compile_tracking_info(track_list){
	for (var i = track_list.length - 1; i >= 0; i--) {
		set_field(track_list[i]);
	};
	return track_info;
}

// sets fields based on information already sent/to be sent
function set_field (field) {
	field_attrs = field_descs[field];
	switch(field_attrs[type]){
		case "session":
			{
				if 
			}
	}
}
