from django.core.management.base import BaseCommand, CommandError
from app.api import send


class Command(BaseCommand):
	def handle(self, *args , **options):

		send(jobs)


