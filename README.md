jobs-SMS-Notification-APP
=========================

This app aims to send SMS to the contact list that contains announcements fetched from the [Keejob's API]


Installation
------------

Just lunch the command `pip -r requirement.txt`

Commands
--------

This project have two commands:

- `python manage.py pull` to pull the new announcements from the [Keejob's API] to the database
- `python manage.py send <nbr_announcements>` to send the last `nbr_announcements` to the contact list. By default `nbr_anouncements` is 5.




[Keejob's API]: http://www.keejob.com/api/v1/najahni-jobs/?api_key=NajahniService

