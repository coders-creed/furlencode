# -*- coding: utf-8 -*-
# @Author: Karthik
# @Date:   2016-03-13 02:08:44
# @Last Modified by:   Karthik
# @Last Modified time: 2016-03-13 03:10:31

from urllib2 import urlopen
from contextlib import closing
import json

def get_loc_from_ip(ip_addr):
	url = 'http://freegeoip.net/json/'
	try:
		with closing(urlopen(url)) as response:
			location = json.loads(response.read())
			lat = location_city = location['latitude']
			lon = location_state = location['longitude']
			return lat,lon
	except:
		return (None,None)