import sendgrid
import os
from sendgrid.helpers.mail import *
from client_data.models import (Dog, Client, DogClass, DogStudent, DayRunReservation,
                        Reservation, DogDayRes)
from django.core.management.base import BaseCommand, CommandError
import datetime


todayDate = datetime.date.today()
Fivedays = todayDate + datetime.timedelta(5)
twodays = todayDate + datetime.timedelta(2)

classReminders = DogClass.objects.filter(startDate=twodays)
bathReminders = Reservation.objects.filter(bathDate=todayDate)
ReservationReminders = Reservation.objects.filter(check_in=Fivedays)
class Command(BaseCommand):
    help = 'Sends email Reports each morning'
    def handle(self, *args, **options):
        sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
        from_email = Email("noreply@midwestdogcenter.com")
        to_email = Email("Dan.Cocking@yahoo.com")
        subject = "Sending needs to be completed"
        content = Content("text/plain", "Test Test Test!!!")
        mail = Mail(from_email, subject, to_email, content)
        response = sg.client.mail.send.post(request_body=mail.get())
        print(response.status_code)
        print(response.body)
        print(response.headers)
