from django.contrib import admin
from .models import Client, Dog, DogClass, DogStudent, DayRunReservation, Reservation, DogDayRes
admin.site.register(Client)
admin.site.register(Dog)
admin.site.register(DogClass)
admin.site.register(DogStudent)
admin.site.register(DayRunReservation)
admin.site.register(Reservation)
admin.site.register(DogDayRes)
# Register your models here.
