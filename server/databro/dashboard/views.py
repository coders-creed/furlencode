from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from dashboard.models import *
from model_helpers import get_loc_from_ip
from ipware.ip import get_ip
import json

import hashlib 

def index(request):
	context = {}
	return render(request, 'dashboard/index.html', context)

def overview(request):
	context = {}
	return render(request, 'dashboard/overview.html', context)

def pageflow(request):
	context = {}
	return render(request, 'dashboard/pageflow.html', context)

def heatmap(request):
	context = {}
	return render(request, 'dashboard/heatmap.html', context)

def events(request):
	if request.method == 'POST':
		return render(request, 'dashboard/index.html')
	else:
		return render(request, 'dashboard/index.html')

@csrf_exempt
def logger(request):
	if request.method == 'POST':
		track_info = json.loads(request.body)
		print track_info
		if any([track_info[r]["type"]== "session" for r in track_info]):
			# update session models
			company = get_company(track_info["domain"]["val"])
			os = get_val(track_info, "os")
			browser = get_val(track_info, "browser")
			ip_addr = get_ip(request)
			latitude,longitude = get_loc_from_ip(ip_addr)
			screen_res = get_val(track_info, "screen_res")
			mobile = get_val(track_info, "mobile")

			user_hash = hashlib.md5(os
				+ browser
				+ ip_addr
				+ screen_res).hexdigest()

			print [user_hash,
					os,
					browser,
					ip_addr,
					latitude,
					longitude,
					screen_res,
					mobile]

			company.userinfo_set.create(
					user_hash=user_hash,
					os=os,
					browser=browser,
					ip_addr=ip_addr,
					latitude=latitude,
					longitude=longitude,
					screen_res = screen_res,
					mobile=mobile
				)

			return HttpResponse("")
			
		if any([track_info[r]["type"]== "page" for r in track_info]):
		else:
			return render(request, 'dashboard/index.html')
			return 


def get_company(domain):
	companyinfo = CompanyInfo.objects.get(domain_name = domain)
	return companyinfo.company

def get_val(track_info, key):
	return track_info[key]["val"]

