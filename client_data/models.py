from django.db import models
import time
from django.urls import reverse
from django import forms
import datetime
dayToCheck = datetime.date.today()
numRuns = 15
# Create your models here.
class Client (models.Model):
    last_name = models.CharField(max_length = 50)
    first_name = models.CharField(max_length = 50)
    street_address = models.CharField(max_length=150)
    city = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=12)
    home_phone = models.CharField(max_length =12,blank=True)
    cell_phone = models.CharField(max_length =12, blank=True)
    email_address = models.EmailField()
    notes = models.TextField(max_length=512, blank=True, null=True)#for notes can be empty

    def __str__(self):
        return str(self.first_name + " " + self.last_name)

    def get_absolute_url(self):
        return reverse('client-detail', kwargs={'pk':self.pk})

        class Meta:
            ordering = ["last_name"]
            verbose_name = 'Client'
            verbose_name_plural = 'Clients'

class Dog (models.Model):
    name = models.CharField(max_length=256) #needed incase of long name e.g. AKC registered names
    owner = models.ForeignKey(Client,related_name='dog')#dogs owner, one owner can have multiple dogs
    breed = models.CharField(max_length=128)# allow long breed names/mixes of breeds
    size = models.CharField(max_length=64)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=64)
    weight = models.PositiveIntegerField()
    rabies_date = models.DateField()
    distemper_date = models.DateField()
    parvo_date = models.DateField()
    bordetello = models.DateField()
    notes = models.TextField(max_length=512, blank=True, null=True)
    check_date_report = models.PositiveSmallIntegerField(default = 1)
    def __str__(self):
        return self.name

    def check_date(self):
        today = datetime.date.today()
        todayPlus30 = today + datetime.timedelta(30)
        overdue = []
        CloseToDue = []
        if today > self.rabies_date:
            overdue.append("Rabies overdue:  " + str(self.rabies_date))
        if today > self.distemper_date:
            overdue.append("Distemper overdue: " + str(self.distemper_date))
        if today > self.parvo_date:
            overdue.append("Parvo overdue: " + str(self.parvo_date))
        if today > self.bordetello:
            overdue.append("bordetello overdue: " + str(self.bordetello))
        if len(overdue) == 0:
            if todayPlus30 > self.rabies_date:
                CloseToDue.append("Rabies close to due:  " + str(self.rabies_date))
            if todayPlus30 > self.distemper_date:
                CloseToDue.append("Distemper close to due: " + str(self.distemper_date))
            if todayPlus30 > self.parvo_date:
                CloseToDue.append("Parvo overdue close to due: " + str(self.parvo_date))
            if todayPlus30 > self.bordetello:
                CloseToDue.append("bordetello overdue close to due: " + str(self.bordetello))
            if len(CloseToDue) == 0:
                self.check_date_report = 1
                return "No overdue or Close to due Vaccinations"
            else:
                self.check_date_report = 2
                return ("Close to Due Vaccinations: " + str(len(CloseToDue))
                        + " are Close to Due" + str(CloseToDue))
        else:
            self.check_date_report = 3
            return ("Overdue: vaccinations: " + str(len(overdue))
                + " are overdue!"  + str(overdue))
    def getToday(self):
        return datetime.date.today()



    def get_absolute_url(self):
        return reverse('dog-detail', kwargs={
            'pk':self.pk
        })





class Reservation(models.Model):
    owner = models.ForeignKey(Client)
    today = datetime.date.today()
    timePlus30 = today + datetime.timedelta(30)
    check_in = models.DateField()
    check_out = models.DateField()
    dog = models.ForeignKey(Dog, null = True, blank =True, related_name='first') #According to website runs can contain up to 3 dogs
    dog2 = models.ForeignKey(Dog, null = True, blank = True, related_name='second')
    dog3 = models.ForeignKey(Dog, null = True, blank = True, related_name='third')
    bath = models.BooleanField()
    bathDate = models.DateField(null = True, blank = True)
    def __str__(self):
        return (str(self.owner) + " " + str(self.dog) + " " + str(self.check_in) + " " + str(self.check_out))
    def get_success_url(self):
        return 'index.html'
    def get_absolute_url(self):
        return reverse('reservation-detail', kwargs={
            'pk':self.pk
            })
    def thirtyDays(self):
        if self.check_in >= datetime.date.today():
            if (self.check_in <= (datetime.date.today() + datetime.timedelta(30))):
                return True
        else:
            return False
    def todaysDate(self):
        return datetime.date.today()



class DayRunReservation (models.Model):
    date = models.DateField(unique=True)
    available_runs = models.PositiveSmallIntegerField(default=30)
    def makeReservation(self):
        if self.available_runs > 0:
            self.available_runs -= 1
            return "Run can be reserved"
        else:
            return "No Runs Available"
    def CancelRes(self):
        if self.available_runs < 30:
            self.available_runs = self.available_runs + 1
            return "Run Cancelled"
        else:
            return "an Error has occured, runs over maximum"
    def runsAvailable(self):
        return available_runs
    def __str__(self):
        return str(str(self.date) + "Runs Available: " + str(self.available_runs))
    def get_absolute_url(self):
        return reverse('dayrun-detail', kwargs={
            'pk':self.pk
            })

class DogDayRes(models.Model):
    dayRun = models.ForeignKey(DayRunReservation, related_name='reserve')
    res = models.ForeignKey(Reservation)
    def __str__ (self):
        return str(self.dayRun) + " " + str(self.res)

class DogClass(models.Model):
    name = models.CharField(max_length = 64)
    today = datetime.date.today()
    classSize = models.PositiveSmallIntegerField()
    startDate = models.DateField()
    endDate = models.DateField()
    dayOfTheWeek = models.CharField(max_length=16)
    enrolled = models.PositiveIntegerField(default=0)
    def showEnrollment(self):
        return str(classSize - enrolled)
    def enrollDog(self):
        if self.classSize >= self.enrolled:
            self.enrolled += 1
            return 'enrolled'
        else:
            return 'class is full'
    classIsOver = models.BooleanField(default = False)
    def cancelEnrollment (self):
        if self.enrolled > 0:
            self.enrolled -= 1
            return ("Enrollment Cancelled")
        else:
            return "No Dogs enrolled class"

    def get_absolute_url(self):
        return reverse('dogclass-detail', kwargs={
            'pk':self.pk
        })

    def __str__ (self):
        return (self.name + " " + str(self.startDate) +
         ' Slots Available ' + str(self.classSize - self.enrolled))

class DogStudent(models.Model):
    dogId = models.ForeignKey(Dog)
    clientId = models.ForeignKey(Client)
    classId = models.ForeignKey(DogClass, related_name='dogstudent')
    def __str__(self):
        return str(self.dogId)
    def get_success_url(self):
        success_url = "/classes/"
        return success_url

    def get_absolute_url(self):
        return reverse('dogstudent-detail', kwargs={
            'pk':self.pk
            })
