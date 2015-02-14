from django.db import models
from django.core.exceptions import 	ValidationError
import re


class Job(models.Model):
	title = models.CharField(max_length=300)
	recruiter = models.CharField(max_length=300)
	link= models.URLField()

	def __str__(self):
		return self.title

class Contact(models.Model):
	first_name = models.CharField(max_length = 30)
	last_name = models.CharField(max_length = 30)
	phone_number = models.CharField(max_length = 12)

	def __str__(self):
		return self.first_name+" "+self.last_name


