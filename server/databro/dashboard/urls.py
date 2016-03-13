from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^referrals$', views.referrals, name='referrals'),
	url(r'^pageflow$', views.pageflow, name='pageflow'),
	url(r'^heatmap$', views.heatmap, name='heatmap'),
	url(r'^events$', views.events, name='events'),
	url(r'^logger$', views.logger, name='logger'),
]