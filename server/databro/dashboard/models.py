from django.db import models
from django.contrib.auth.models import *

from datetime import datetime

class CompanyInfo(models.Model):
	company = models.ForeignKey(User, on_delete=models.CASCADE)
	domain_name = models.CharField(max_length=50, unique=True)

class ClickConfig(models.Model):
	company = models.ForeignKey(User, on_delete=models.CASCADE)

	name = models.CharField(max_length=50)
	selector = models.CharField(max_length=100)
	events = models.CharField(max_length=100, default="click")

# Create your models here.
class UserInfo(models.Model):
	company = models.ForeignKey(User, on_delete=models.CASCADE)

	mobile = models.BooleanField()
	user_hash = models.CharField(max_length=200)
	os = models.CharField(max_length=75)
	screen_res = models.CharField(max_length=75)
	ip_addr = models.CharField(max_length=25)
	browser = models.CharField(max_length=25)

	latitude = models.FloatField(blank=True)
	longitude = models.FloatField(blank=True)


class PageFlow(models.Model):
	company = models.ForeignKey(User, on_delete=models.CASCADE)

	from_url =  models.URLField(max_length=200)
	from_title =  models.CharField(max_length=100, blank=True)

	to_url =  models.URLField(max_length=200)
	to_title =  models.CharField(max_length=100, blank=True)

	flow_count = models.IntegerField(default=0)

class PageTime(models.Model):
	company = models.ForeignKey(User, on_delete=models.CASCADE)

	page_url =  models.URLField(max_length=200, unique=True)
	page_title =  models.CharField(max_length=100, blank=True)

	page_time = models.IntegerField(default=0)
	visit_count = models.IntegerField(default=0)


class Referrer(models.Model):
	company = models.ForeignKey(User, on_delete=models.CASCADE)

	referrer_url =  models.URLField(max_length=200)
	referrer_title =  models.CharField(max_length=100, blank=True)
	referrer_count = models.IntegerField()

class ClickInfo(models.Model):
	click_config = models.ForeignKey(ClickConfig, 
					on_delete=models.CASCADE)

	count = models.IntegerField(default=0)










