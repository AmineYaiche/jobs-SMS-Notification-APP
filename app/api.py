from app.models import job , contact
import requests
from django_bitly.models import Bittle
from twilio.rest import TwilioRestClient

def bitlify(url):
	"""transforme the url to the bitly format"""
	return Bittle.objects.bitlify(url).shortUrl


def pull(url):
	"""fetch new jobs from the API and add them to the database"""
	r = requests.get(url)
	parsed = r.json()
	jobs = parsed["objects"]

	for j in jobs:
		if len( job.objects.filter(title=j['title'].encode("utf-8")).filter(recruiter=j['recruiter'].encode("utf-8"))):
			break #in case the job already exist in the database we stop fetching

		elem = job()
		elem.title= str(j['title'].encode("utf-8"))
		elem.recruiter=str(j['recruiter'].encode("utf-8"))
#		elem.link = bitlify(j['link'])
		elem.link = j['link']
		elem.save()
	return job.objects.all()

def send(nbr):
	""" send jobs to the contact laist"""
	jobs = job.objects.all()[:nbr]
	contacts = contact.objects.all()
	for j in jobs:
		for c in contacts:
			print("x")
			message = "Hey {}, {} has published a new job {} {}".format(c.first_name , j.recruiter , j.title.encode("utf-8") , j.link)

			account_sid = "ACf71c0db239a537d8f4647ddabae65d12"
			auth_token = "86ca1e9472dd730c26552aea7cf44fa5"
			client = TwilioRestClient(account_sid , auth_token)
			client.messages.create(body=message , from_="+12055022576" , to = c.phone_number)










