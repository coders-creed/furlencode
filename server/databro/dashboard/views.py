from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from dashboard.models import *
import json
from model_helpers import get_loc_from_ip
from ipware.ip import get_ip
import json

from tld import get_tld

import hashlib 

def index(request):
	context = {}
	return render(request, 'dashboard/index.html', context)

def referrals(request):
	referrers = Referrer.objects.filter(company=1)
	referrers = json.dumps(list(referrers.values_list('referrer_title', 'referrer_count')))
	print referrers
	context = {"referrers": referrers}
	return render(request, 'dashboard/referrals.html', context)

def pageflow(request):
	user = request.user
	pageflows = PageFlow.objects.filter(company=1)

	outset = pageflows.values_list('from_url').distinct()
	inset = pageflows.values_list('to_url').distinct()

	outset = map(lambda x: x[0], outset)
	inset = map(lambda x: x[0], inset)

	nodes_list = list(set(outset) | set(inset))

	nodes = [{"id" : str(node)} for node in nodes_list]

	weights = [{"strength": pf.flow_count, 
				"source": nodes_list.index(pf.from_url),
				"target":  nodes_list.index(pf.to_url)} for pf in pageflows 
				if nodes_list.index(pf.to_url) != nodes_list.index(pf.from_url)]


	context = {"nodes": json.dumps(nodes), "weights": json.dumps(weights)}

	return render(request, 'dashboard/pageflow.html', context)

def heatmap(request):

	locations = json.dumps(list(UserInfo.objects.filter(company=1).values_list('latitude','longitude')))
	context = {"geo_info": locations}
	print context
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

		if any([track_info[r]["type"] == "page" for r in track_info]):
			company = get_company(track_info["domain"]["val"])

			to_domain = get_val(track_info, "domain")
			to_url = get_val(track_info, "page_url")
			to_title = get_val(track_info, "page_title")
			
			if "referrer" in track_info.keys() and get_val(track_info, "referrer"):
				referrer = get_val(track_info, "referrer")
				print "REFERRED"

				if "localhost" in referrer:
					from_domain = "localhost"
				else:
					from_domain = get_tld(referrer)

				print from_domain, to_domain
				if from_domain == to_domain:
					print "PAGEFLOW"
					try:
						pageflow = PageFlow.objects.get(
								company=company,
								from_url=referrer,
								from_title = from_domain,
								to_url = to_url,
								to_title = to_title
							)
						# update pageflow if from domain = to domain
						pageflow.flow_count += 1
						print "PAGEFLOW UPDATED"
						pageflow.save()
					except:
						# create object
						company.pageflow_set.create(
							from_url=referrer,
							from_title = from_domain,
							to_url = to_url,
							to_title = to_title,
							flow_count = 1
						)
						print "PAGEFLOW CREATED"

				# else update referrer
				
				elif from_domain != to_domain:
					print "REFERRER"

					try:
						referrer = Referrer.objects.get(
								company=company,
								referrer_url=referrer,
								referrer_title = from_domain,
							)
						# update pageflow if from domain = to domain
						referrer.referrer_count += 1
						print "REFERRER UPDATED"
						referrer.save()
					except:
						# create object
						company.referrer_set.create(
							referrer_url=referrer,
							referrer_title = from_domain,
							referrer_count = 1
						)
						print "REFERRER CREATED"
			# if pagetime in keys, update pagetime
			if "pageTime" in track_info.keys():
				try:
					print company, to_url, to_title
					pagetime = PageTime.objects.get(
							company = company,
							page_url = to_url,
							page_title = to_title
						)
					# update pagetime and count if from domain = to domain
					pagetime.page_time += get_val(track_info, "pageTime")
					pagetime.visit_count += 1
					pagetime.save()
				except Exception as e:
					# create object
					company.pagetime_set.create(
						page_url = to_url,
						page_title = to_title,
						page_time = get_val(track_info, "pageTime"),
						visit_count = 1
					)


	return HttpResponse("")


def get_company(domain):
	companyinfo = CompanyInfo.objects.get(domain_name = domain)
	return companyinfo.company

def get_val(track_info, key):
	return track_info[key]["val"]

