from django.db import models
from django.contrib.auth.models import *
from users import models as users_models

# Create your models here.
class Pitch(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
   	title = models.CharField(max_length=200, unique=True)
   	date = models.DateField()
   	pitch = models.TextField()
	prog_langs = models.ManyToManyField(users_models.Programming_language)
	document = models.FileField(upload_to = upload_path, blank = True)
	dev_state = models.CharField(max_length=50)

	def __str__(self):
		return str(self.title)