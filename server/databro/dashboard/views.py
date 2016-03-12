from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json

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
		return HttpResponse("")
	else:
		return render(request, 'dashboard/index.html')
	return 

