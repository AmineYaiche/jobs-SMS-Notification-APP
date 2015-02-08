from django.db import models
from django.core.exceptions import 	ValidationError
import re


class job(models.Model):
	title = models.CharField(max_length=300)
	recruiter = models.CharField(max_length=300)
	link= models.URLField()

	def __str__(self):
		return self.title


def validate_number(number):
	condition = re.compile("^+216[0-9]{6}$")
	if not condition.match(number):
		raise ValidationError("This is not a Tunisian number. Format +216XXXXXX")

class contact(models.Model):
	first_name = models.CharField(max_length = 30)
	last_name = models.CharField(max_length = 30)
#	phone_number = models.CharField(max_length = 12 , validators = [validate_number])
	

	phone_number = models.CharField(max_length = 12)
	def __str__(self):
		return self.first_name+" "+self.last_name


