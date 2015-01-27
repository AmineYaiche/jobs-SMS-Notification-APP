from django.core.management.base import BaseCommand, CommandError
from app.models import job , contact
import requests
from bitly.models import Bittle

def bitlify(url):
	return Bittle.objects.bitlify(url).shortUrl


class Command(BaseCommand):
	def handle(self, *args , **options):

		url = "http://www.keejob.com/api/v1/najahni-jobs/?api_key=NajahniService"
		r = requests.get(url)
		parsed = r.json()
		jobs = parsed["objects"]

		job.objects.filter().delete()

		for j in jobs:
			elem = job()
			elem.title = str(j['title'].encode("utf-8"))
			elem.recruiter = str(j['recruiter'].encode("utf_8"))
			elem.link = bitlify(j['link'])
			elem.save()


