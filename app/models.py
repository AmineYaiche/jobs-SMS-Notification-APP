from django.db import models
from django.core.exceptions import 	ValidationError
import re
from phonenumber_field.modelfields import PhoneNumberField


class Job(models.Model):
	title = models.CharField(max_length=300)
	recruiter = models.CharField(max_length=300)
	link= models.URLField()

	def __str__(self):
		return self.title

class Contact(models.Model):
	first_name = models.CharField(max_length = 30)
	last_name = models.CharField(max_length = 30)
	phone_number = PhoneNumberField(blank=True, max_length=15)


	def __str__(self):
		return self.first_name+" "+self.last_name


