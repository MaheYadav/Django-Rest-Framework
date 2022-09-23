from django.db import models

class subject(models.Model):
	number= models.IntegerField()
	name=models.CharField(max_length=100)

	def __str__():
	     number