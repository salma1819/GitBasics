from django.db import models

# Create your models here.
class Restaurant(models.Model):
	Rname = models.CharField(max_length=30)
	Nitems = models.IntegerField()
	timings = models.CharField(max_length=50)
	address = models.CharField(max_length=50)