from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^overview$', views.overview, name='overview'),
	url(r'^pageflow$', views.pageflow, name='pageflow'),
	url(r'^heatmap$', views.heatmap, name='heatmap'),
	url(r'^events$', views.events, name='events'),
]