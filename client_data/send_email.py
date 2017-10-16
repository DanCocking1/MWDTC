# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import sendgrid
import os
from sendgrid.helpers.mail import *
from .models import (Dog, Client, DogClass, DogStudent, DayRunReservation,
                        Reservation, DogDayRes)
import datetime


todayDate = datetime.date.today()
Fivedays = todayDate + datetime.timedelta(5)
twodays = todayDate + datetime.timedelta(2)

classReminders = DogClass.objects.filter(startDate=twodays)
bathReminders = Reservation.objects.filter(bathDate=todayDate)
ReservationReminders = Reservation.objects.filter(check_in=Fivedays)
'''
class reminders
'''
for student in classReminders:
    dogsToRemind = DogStudent.objects.filter(classId=student)
    for dog in dogsToRemind:
        Clients = Clients.objects.filter(ClientId=dog.clientId)
        sg = sendgrid.SendGridAPIClient(apikey=os.environ.get(SENDGRID_API_KEY))
        from_email = Email("No-reply@midwestdogcenter.com")
        to_email = Email(Clients.email_address)
        subject = "Reminder, Class is coming up for " + dog.dogId
        content = Content("text/plain", 'This is a courtesy reminder that your class is coming up in two days on: ' +
        str(twodays) +  '\n if you have any questions, or need to change anything please contact us at: \n' +
        'Phone: (316) 300-6893\n Email: lyneisa@midwestdogcenter.com' )
        mail = Mail(from_email, subject, to_email, content)
        response = sq.client.mail.send.post(request_body=mail.get())

'''
bath reminders
'''
baths =[]
for bath in bathReminders:
    bath.append(bath.dog)
if bath.len() != 0: #don't send if no baths for the day
    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get(SENDGRID_API_KEY))
    from_email = Email('No-reply@midewestdogcenter.com')
    to_email = Email('lynesia@midwestdogcenter.com')
    subject = "Baths for " + str(todayDate)
    content = Content ("text/plain", "Baths: " + str(bath))
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())

'''
Reservation Reminders
'''
for Res in ReservationReminders:
    ClientstoRemind = Clients.objects.filter(ClientId = dog.clientId)
    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get(SENDGRID_API_KEY))
    from_email = Email("No-reply@midwestdogcenter.com")
    to_email = Email(ClientstoRemind.email_address)
    subject = "Reminder, Class is coming up for " + Res.dog
    content = Content("text/plain", 'This is a courtesy reminder that your Kennel Reservation is coming up in Five days on: ' +
    str(Fivedays) +  '\n if you have any questions, or need to change anything please contact us at: \n' +
    'Phone: (316) 300-6893\n Email: lyneisa@midwestdogcenter.com' )
    mail = Mail(from_email, subject, to_email, content)
    response = sq.client.mail.send.post(request_body=mail.get())


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
