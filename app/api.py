from app.models import job , contact
import requests
from django_bitly.models import Bittle
from twilio.rest import TwilioRestClient
from django.conf import settings

def bitlify(url):
	"""transforme the url to the bitly format"""
	return Bittle.objects.bitlify(url).shortUrl


def pull(url):
	"""fetch new jobs from the API and add them to the database"""
	r = requests.get(url)
	parsed = r.json()
	jobs = parsed["objects"]
	print(len(jobs))
	i = 0
	for j in jobs:

		elem = job()
		elem.title= str(j['title'].encode("utf-8"))
		elem.recruiter=str(j['recruiter'].encode("utf-8"))
		#elem.link = bitlify(j['link'])
		elem.link = j['link']
		elem.save()
		i +=1
	print("i = "+str(i))
	return job.objects.all()

def send(nbr):
	""" send jobs to the contact laist"""
	jobs = job.objects.all()[:nbr]
	contacts = contact.objects.all()
	for j in jobs:
		for c in contacts:
			print("x")
			message = "Hey {}, {} has published a new job {} {}".format(c.first_name , j.recruiter , j.title.encode("utf-8") , j.link)

			client = TwilioRestClient(settings.ACCOUNT_ID , settings.AUTH_TOKEN)
			client.messages.create(body=message , from_="+12055022576" , to = c.phone_number)










