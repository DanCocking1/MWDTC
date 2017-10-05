# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import sendgrid
import os
from sendgrid.helpers.mail import *
from .models import (Dog, Client, DogClass, DogStudent, DayRunReservation,
                        Reservation, DogDayRes)
import datetime


todayDate = datetime.date.today()
Threedays = todayDate + datetime.timedelta(3)


sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
from_email = Email("Dan.Cocking@yahoo.com")
to_email = Email("Dan.Cocking@yahoo.com")
subject = "Sending with SendGrid is Fun"
content = Content("text/plain", "and easy to do anywhere, even with Python")
mail = Mail(from_email, subject, to_email, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)
