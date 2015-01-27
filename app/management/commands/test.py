from django.core.management.base import BaseCommand, CommandError
from twilio.rest import TwilioRestClient

class Command(BaseCommand):
	def handle(self, *args , **options):
		
		account_sid = "ACf71c0db239a537d8f4647ddabae65d12"

		auth_token = "86ca1e9472dd730c26552aea7cf44fa5"

		client = TwilioRestClient(account_sid , auth_token)

		message = client.messages.create(body="Hello, my name is amine",

			from_="+12055022576", to ="+21623190452")



