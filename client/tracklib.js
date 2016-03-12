/*
* @Author: Karthik
* @Date:   2016-03-12 15:19:08
* @Last Modified by:   Karthik
* @Last Modified time: 2016-03-12 23:42:29
*/

// FIELD_DESCS = window.FIELD_DESCS;
// var SEND_INT = window.SEND_INT;

console.log(FIELD_DESCS);


(function get_agent_info(window) {
    {
        var unknown = '-';

        // screen
        var screenSize = '';
        if (screen.width) {
            width = (screen.width) ? screen.width : '';
            height = (screen.height) ? screen.height : '';
            screenSize += '' + width + " x " + height;
        }

        // browser
        var nVer = navigator.appVersion;
        var nAgt = navigator.userAgent;
        var browser = navigator.appName;
        var version = '' + parseFloat(navigator.appVersion);
        var majorVersion = parseInt(navigator.appVersion, 10);
        var nameOffset, verOffset, ix;

        // Opera
        if ((verOffset = nAgt.indexOf('Opera')) != -1) {
            browser = 'Opera';
            version = nAgt.substring(verOffset + 6);
            if ((verOffset = nAgt.indexOf('Version')) != -1) {
                version = nAgt.substring(verOffset + 8);
            }
        }
        // Opera Next
        if ((verOffset = nAgt.indexOf('OPR')) != -1) {
            browser = 'Opera';
            version = nAgt.substring(verOffset + 4);
        }
        // MSIE
        else if ((verOffset = nAgt.indexOf('MSIE')) != -1) {
            browser = 'Microsoft Internet Explorer';
            version = nAgt.substring(verOffset + 5);
        }
        // Chrome
        else if ((verOffset = nAgt.indexOf('Chrome')) != -1) {
            browser = 'Chrome';
            version = nAgt.substring(verOffset + 7);
        }
        // Safari
        else if ((verOffset = nAgt.indexOf('Safari')) != -1) {
            browser = 'Safari';
            version = nAgt.substring(verOffset + 7);
            if ((verOffset = nAgt.indexOf('Version')) != -1) {
                version = nAgt.substring(verOffset + 8);
            }
        }
        // Firefox
        else if ((verOffset = nAgt.indexOf('Firefox')) != -1) {
            browser = 'Firefox';
            version = nAgt.substring(verOffset + 8);
        }
        // MSIE 11+
        else if (nAgt.indexOf('Trident/') != -1) {
            browser = 'Microsoft Internet Explorer';
            version = nAgt.substring(nAgt.indexOf('rv:') + 3);
        }
        // Other browsers
        else if ((nameOffset = nAgt.lastIndexOf(' ') + 1) < (verOffset = nAgt.lastIndexOf('/'))) {
            browser = nAgt.substring(nameOffset, verOffset);
            version = nAgt.substring(verOffset + 1);
            if (browser.toLowerCase() == browser.toUpperCase()) {
                browser = navigator.appName;
            }
        }
        // trim the version string
        if ((ix = version.indexOf(';')) != -1) version = version.substring(0, ix);
        if ((ix = version.indexOf(' ')) != -1) version = version.substring(0, ix);
        if ((ix = version.indexOf(')')) != -1) version = version.substring(0, ix);

        majorVersion = parseInt('' + version, 10);
        if (isNaN(majorVersion)) {
            version = '' + parseFloat(navigator.appVersion);
            majorVersion = parseInt(navigator.appVersion, 10);
        }

        // mobile version
        var mobile = /Mobile|mini|Fennec|Android|iP(ad|od|hone)/.test(nVer);

        // cookie
        var cookieEnabled = (navigator.cookieEnabled) ? true : false;

        if (typeof navigator.cookieEnabled == 'undefined' && !cookieEnabled) {
            document.cookie = 'testcookie';
            cookieEnabled = (document.cookie.indexOf('testcookie') != -1) ? true : false;
        }

        // system
        var os = unknown;
        var clientStrings = [
            {s:'Windows 10', r:/(Windows 10.0|Windows NT 10.0)/},
            {s:'Windows 8.1', r:/(Windows 8.1|Windows NT 6.3)/},
            {s:'Windows 8', r:/(Windows 8|Windows NT 6.2)/},
            {s:'Windows 7', r:/(Windows 7|Windows NT 6.1)/},
            {s:'Windows Vista', r:/Windows NT 6.0/},
            {s:'Windows Server 2003', r:/Windows NT 5.2/},
            {s:'Windows XP', r:/(Windows NT 5.1|Windows XP)/},
            {s:'Windows 2000', r:/(Windows NT 5.0|Windows 2000)/},
            {s:'Windows ME', r:/(Win 9x 4.90|Windows ME)/},
            {s:'Windows 98', r:/(Windows 98|Win98)/},
            {s:'Windows 95', r:/(Windows 95|Win95|Windows_95)/},
            {s:'Windows NT 4.0', r:/(Windows NT 4.0|WinNT4.0|WinNT|Windows NT)/},
            {s:'Windows CE', r:/Windows CE/},
            {s:'Windows 3.11', r:/Win16/},
            {s:'Android', r:/Android/},
            {s:'Open BSD', r:/OpenBSD/},
            {s:'Sun OS', r:/SunOS/},
            {s:'Linux', r:/(Linux|X11)/},
            {s:'iOS', r:/(iPhone|iPad|iPod)/},
            {s:'Mac OS X', r:/Mac OS X/},
            {s:'Mac OS', r:/(MacPPC|MacIntel|Mac_PowerPC|Macintosh)/},
            {s:'QNX', r:/QNX/},
            {s:'UNIX', r:/UNIX/},
            {s:'BeOS', r:/BeOS/},
            {s:'OS/2', r:/OS\/2/},
            {s:'Search Bot', r:/(nuhk|Googlebot|Yammybot|Openbot|Slurp|MSNBot|Ask Jeeves\/Teoma|ia_archiver)/}
        ];
        for (var id in clientStrings) {
            var cs = clientStrings[id];
            if (cs.r.test(nAgt)) {
                os = cs.s;
                break;
            }
        }

        var osVersion = unknown;

        if (/Windows/.test(os)) {
            osVersion = /Windows (.*)/.exec(os)[1];
            os = 'Windows';
        }

        switch (os) {
            case 'Mac OS X':
                osVersion = /Mac OS X (10[\.\_\d]+)/.exec(nAgt)[1];
                break;

            case 'Android':
                osVersion = /Android ([\.\_\d]+)/.exec(nAgt)[1];
                break;

            case 'iOS':
                osVersion = /OS (\d+)_(\d+)_?(\d+)?/.exec(nVer);
                osVersion = osVersion[1] + '.' + osVersion[2] + '.' + (osVersion[3] | 0);
                break;
        }

        // flash (you'll need to include swfobject)
        /* script src="//ajax.googleapis.com/ajax/libs/swfobject/2.2/swfobject.js" */
        var flashVersion = 'no check';
        if (typeof swfobject != 'undefined') {
            var fv = swfobject.getFlashPlayerVersion();
            if (fv.major > 0) {
                flashVersion = fv.major + '.' + fv.minor + ' r' + fv.release;
            }
            else  {
                flashVersion = unknown;
            }
        }
    }

    window.jscd = {
        screen: screenSize,
        browser: browser,
        browserVersion: version,
        browserMajorVersion: majorVersion,
        mobile: mobile,
        os: os,
        osVersion: osVersion,
        cookies: cookieEnabled,
        flashVersion: flashVersion
    };
}(this));


function get_ip () {
	// ip;
	// var promise = $.getJSON("http://jsonip.com/?callback=?");
	// promise.success(function (data){
	// 	ip = data.ip;
	// });
	$.ajax({
	  url: "http://jsonip.com/?callback=?",
	  dataType: 'json',
	  async: false,
	  success: function(data) {
	  	console.log(data.ip)
	  	window.ip = data.ip;
	  }
	});
	return;

}

console.log(get_ip());

var field_getter = {"userAgent": window.navigator.userAgent, 
					"browser" : jscd.browser,
					"os" : jscd.os,
				    "mobile":jscd.mobile,
					"screen": jscd.screen,
					"ip" : window.ip,
					"referrer" : document.referrer,
					"sessionStart": $.now(),
					"pageStart": $.now()
};


PAGE_FLAG = 0;
TRACK_INFO = [];
'use strict';
// compiles the tracking info to be sent to the analytics server
function compile_stat_track_info (){
	for (field in FIELD_DESCS) {
		set_stat_field(field);
	};
	return;
}

// sets fields based on information already sent/to be sent
function set_stat_field (field) {
	field_type = FIELD_DESCS[field]["type"];
	
	// set field value based on type (session/page/event)
	switch(field_type){
		
		case "session":
			if (Cookies.get(field) == undefined){
				var field_val = field_getter[field];
				Cookies.set(field, field_val);
				TRACK_INFO[field] = field_val;
			};
			break;

		case "page":
			if (!PAGE_FLAG){
				TRACK_INFO[field] = field_getter[field];
				PAGE_FLAG = 1;
			};
			break;
	}
}

// tracks events on selectors
function track_events (FIELD_DESCS) {
	// track all events 
	for (field in FIELD_DESCS) {
		field_type = FIELD_DESCS[field]["type"];
		if (field_type == "event") {
			var target = FIELD_DESCS[field]["sel"];
			var triggers = FIELD_DESCS[field]["events"];
			$(target).on(triggers, function(e) {
				if (typeof(TRACK_INFO[field]) == undefined){
					TRACK_INFO[field] = [e];
				}
				else{
					TRACK_INFO[field].push(e);
				}
			});
		};
	};
};


function send_track_info (TRACK_INFO) {
	$.post("localhost:8001/logger", TRACK_INFO,
	function(){
		return;
	});
	return;
}

track_events();


function main (FIELD_DESCS) {
	compile_stat_track_info();
	console.log(TRACK_INFO);
	send_track_info(TRACK_INFO)
	TRACK_INFO = [];
	setTimeout(main, SEND_INT);
}

main(FIELD_DESCS);

$(window).unload(function() {
	compile_stat_track_info();
	TRACK_INFO["pageTime"] = $.now() - field_getter["pageStart"];
	send_track_info(TRACK_INFO);
});

