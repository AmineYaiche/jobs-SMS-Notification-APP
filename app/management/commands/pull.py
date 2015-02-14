from django.core.management.base import BaseCommand, CommandError
from app.api import fetch , send


class Command(BaseCommand):
	def handle(self, *args , **options):

		url = "http://www.keejob.com/api/v1/najahni-jobs/?api_key=NajahniService"
		jobs = fetch(url)

		send(jobs)


