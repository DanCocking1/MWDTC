from django.db import models
import time
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django import forms
import datetime
dayToCheck = datetime.date.today()
numRuns = 15
# Create your models here.
dogSize = (
    ('toy', 'TOY'),
    ('medium', 'MEDIUM'),
    ('large', 'LARGE'),
    ('extra large', 'EXTRA LARGE')
)
class Client (models.Model):
    created = models.ForeignKey(User, null=True, blank=True)
    last_name = models.CharField(max_length = 50)
    first_name = models.CharField(max_length = 50)
    street_address = models.CharField(max_length=150)
    city = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=12)
    home_phone = models.CharField(max_length =12,blank=True)
    cell_phone = models.CharField(max_length =12, blank=True)
    email_address = models.EmailField(unique=True)
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
    created = models.ForeignKey(User, null=True, blank=True)
    name = models.CharField(max_length=256) #needed incase of long name e.g. AKC registered names
    owner = models.ForeignKey(Client,related_name='dog')#dogs owner, one owner can have multiple dogs
    breed = models.CharField(max_length=128)# allow long breed names/mixes of breeds
    size = models.CharField(max_length=64)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=64)
    rabies_date = models.DateField()
    parvo_distemper_date = models.DateField()
    fecal_date = models.DateField()
    bordetella = models.DateField()
    notes = models.TextField(max_length=512, blank=True, null=True)
    check_date_report = models.PositiveSmallIntegerField(default = 1)
    def __str__(self):
        return self.name

    def check_date(self):
        today = datetime.date.today()
        todayPlus30 = today + datetime.timedelta(30)
        todayPlusOneYear = today + datetime.timedelta(365)
        todayPlusSixMonths = today + datetime.timedelta(180)
        overdue = []
        CloseToDue = []
        if today > (self.rabies_date + datetime.timedelta(365)):
            overdue.append("Rabies overdue:  " + str(self.rabies_date))
        if today > (self.parvo_distemper_date + datetime.timedelta(365)):
            overdue.append("Parvo/Distemper overdue: " + str(self.parvo_distemper_date))
        if today > (self.bordetella + datetime.timedelta(180)):
            overdue.append("bordetella overdue: " + str(self.bordetella))
        if len(overdue) == 0:
            if todayPlus30 > (self.rabies_date + datetime.timedelta(365)):
                CloseToDue.append("Rabies close to due:  " + str(self.rabies_date))
            if todayPlus30 > (self.parvo_distemper_date + datetime.timedelta(365)):
                CloseToDue.append("Parvo overdue close to due: " + str(self.parvo_distemper_date))
            if todayPlus30 > (self.bordetella + datetime.timedelta(180)):
                CloseToDue.append("bordetella overdue close to due: " + str(self.bordetella))
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
    def getOneYear(self):
        return (datetime.date.today() + datetime.timedelta(365))
    def getSixMonths(self):
        return (datetime.date.today()+ datetime.timedelta(180))
    def getFiveMonths(self):
        return (datetime.date.today()+ datetime.timedelta(150))
    def getElevenMonths(self):
        return (datetime.date.today()+ datetime.timedelta(335))


    def get_absolute_url(self):
        return reverse('dog-detail', kwargs={
            'pk':self.pk
        })

timeChoice = (
    ('before noon', 'BEFORE NOON'),
    ('after noon', 'AFTER NOON')
)


class Reservation(models.Model):
    created = models.ForeignKey(User, blank=True, null=True)
    owner = models.ForeignKey(Client, related_name='reservation')
    today = datetime.date.today()
    kennel_num = models.PositiveSmallIntegerField(blank=True, null=True)
    timePlus30 = today + datetime.timedelta(30)
    PickUpTime = models.CharField(max_length=12, choices=timeChoice, default='before noon')
    check_in = models.DateField()
    check_out = models.DateField()
    feedingInstructions = models.TextField(max_length=512, blank=True, null=True)
    medicationInstructions = models.TextField(max_length=512, blank=True, null=True)
    notes = models.TextField(max_length=512, blank=True, null = True)
    dog = models.ForeignKey(Dog, null = True, blank =True, related_name='first') #According to website runs can contain up to 3 dogs
    dog2 = models.ForeignKey(Dog, null = True, blank = True, related_name='second')
    dog3 = models.ForeignKey(Dog, null = True, blank = True, related_name='third')
    bath = models.BooleanField(default=False)
    bath_dog_size = models.CharField(max_length = 12, choices=dogSize, default = 'medium')
    nails = models.BooleanField(default=False)
    bathDate = models.DateField(null = True, blank = True)
    cancelled = models.BooleanField(default=False)
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
    def get_estimated_price(self):
        dates = self.check_in
        i = 0
        estimation = 0
        price = 0
        while dates < self.check_out:
            i += 1
            dates = dates + datetime.timedelta(1)
        if self.PickUpTime == 'after noon':
            i += 1
        if self.bath:
            if self.bath_dog_size == 'toy':
                estimation = estimation + 18
            elif self.bath_dog_size == 'medium':
                estimation = estimation + 25
            elif self.bath_dog_size == 'large':
                estimation = estimation + 30
            else:
                estimation = estimation + 35
        if self.dog3:
            price = (57 * i) + estimation
        elif self.dog2:
            price = (43 * i) + estimation
        else:
            price = (24 * i) + estimation
        return price








class DayRunReservation (models.Model):
    date = models.DateField(unique=True)
    available_runs = models.PositiveSmallIntegerField(default=30)
    def makeReservation(self):
        if self.available_runs > 0:
            self.available_runs -= 1
            return "Run can be reserved"
        else:
            return "No Runs Available on "+ str(date) + ", Please Call (316) 300-6893"
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
    dogDayResCancelled = models.BooleanField(default=False)
    def __str__ (self):
        return str(self.dayRun) + " " + str(self.res)

class DogClass(models.Model):
    name = models.CharField(max_length = 64)
    today = datetime.date.today()
    classSize = models.PositiveSmallIntegerField()
    startDate = models.DateField()
    endDate = models.DateField()
    startTime = models.CharField(max_length=12, default='6 pm')
    dayOfTheWeek = models.CharField(max_length=16)
    enrolled = models.PositiveIntegerField(default=0)
    privateClass = models.BooleanField(default = False)
    enrollmentSlots = models.PositiveIntegerField(default=0)
    def showEnrollment(self):
        return (classSize - enrolled)
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
         ' Slots Available:  ' + str(self.classSize - self.enrolled))


class DogStudent(models.Model):
    created = models.ForeignKey(User, null=True, blank=True)
    dogId = models.ForeignKey(Dog)
    clientId = models.ForeignKey(Client, related_name='student')
    classId = models.ForeignKey(DogClass, related_name='dogstudent')
    cancelledEnrollment = models.BooleanField(default=False)
    def __str__(self):
        return str(self.dogId)
    def get_success_url(self):
        success_url = "/classes/"
        return success_url

    def get_absolute_url(self):
        return reverse('dogstudent-detail', kwargs={
            'pk':self.pk
            })
private_selection = (
    ('Boarding/Train', 'BOARDING/TRAIN'),
    ('Private', 'PRIVATE'),
    ('Protection', 'Protection')
)


class PrivateDogClass(models.Model):
    classId = models.ForeignKey(DogClass, related_name='classtaken')
    clientId = models.ForeignKey(Client)
    dogId = models.ForeignKey(Dog)
    class_type = models.CharField(max_length = 16, choices = private_selection, default='Boarding/Train')
    kennel_num = models.PositiveSmallIntegerField(blank=True, null=True)
    sessions = models.PositiveSmallIntegerField(default = 0)
    check_in = models.DateField()
    check_out = models.DateField()
    Bath = models.BooleanField(default=False)
    nails = models.BooleanField(default=False)
    bath_Date = models.DateField(null=True, blank=True)
    follow_Up_Appointment = models.CharField(max_length= 32, blank=True, null=True)
    pick_up_time_and_date = models.CharField(max_length=32, blank=True, null=True)
    feeding = models.TextField(max_length=128, blank=True, null=True)
    Medication = models.TextField(max_length=128, blank=True, null=True)
    Contanct_Phone = models.CharField(max_length=16)
    Prong_Collar = models.BooleanField(default=False)
    Treats = models.BooleanField(default=False)
    Ecollar = models.BooleanField(default=False)
    Extra_Boarding_days = models.CharField(max_length = 32, null=True, blank= True)
    Personal_Protection_Items = models.TextField(max_length=128, default = 'none')
    Notes = models.TextField(max_length=128, default = 'none')
