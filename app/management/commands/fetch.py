from django.core.management.base import BaseCommand, CommandError
from app.models import job , contact
import requests

class Command(BaseCommand):
	def handle(self, *args , **options):

		url = "http://www.keejob.com/api/v1/najahni-jobs/?api_key=NajahniService"
		r = requests.get(url)
		parsed = r.json()
		jobs = parsed["objects"]

		for j in jobs:
			elem = job()
			elem.title = j['title'].encode("utf-8")
			elem.recruiter = j['recruiter'].encode("utf-8")
			elem.link = j['link']
			elem.save()
