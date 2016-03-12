from django.http import HttpResponse
from django.shortcuts import render

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
		print request.POST
		return render(request, 'dashboard/index.html')
	else:
		return render(request, 'dashboard/index.html')


def logger(request):
	return 

