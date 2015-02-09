from app.models import job , contact
import requests
from bitly.models import Bittle
from twilio.rest import TwilioRestClient

def bitlify(url):
"""transforme the url to the bitly format"""
	return Bittle.objects.bitlify(url).shortUrl


def fetch(url):
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
		elem.link = bitlify(j['link'])
		elem.save()
	return job.objects.all()[:4] #returing the 5 recent jobs



def send(jobs):
""" send jobs passed by argument to the contact list"""
	contacts = contact.objects.all()

	for j in jobs:
		for c in contacts:
			message = "Hey {}, {} has published a new job {} {}".format(c.first_name , j.recruiter , j.title  , j.link)

			account_sid = "ACf71c0db239a537d8f4647ddabae65d12"
			auth_token = "86ca1e9472dd730c26552aea7cf44fa5"
			client = TwilioRestClient(account_sid , auth_token)
			client.messages.create(body=message , from_="+12055022576" , to = c.phone_number)










