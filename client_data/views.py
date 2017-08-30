from django.shortcuts import render
from django.urls import reverse
import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView,ListView, UpdateView, CreateView,
                        DetailView, FormView, DeleteView)
from .models import (Dog, Client, DogClass, DogStudent, DayRunReservation,
                        Reservation, DogDayRes)
from .forms import DogForm, DogFormUpdate, MakeAReservationForm, PickADate

# Create your views here.
class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'client_list.html'
    context_object_name = 'client_detail'
    ordering = ['last_name']
    paginate_by = 100
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

class HomeView(LoginRequiredMixin, FormView):
    template_name = 'index.html'
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    form_class = PickADate
    success_url = '/'

    def form_valid(self, form):
        todayDate = datetime.date.today()
        dateToCheck = form.cleaned_data['date']
        print(dateToCheck)
        i, created = DayRunReservation.objects.get_or_create(date = dateToCheck)
        i.save()
        self.success_url = i.get_absolute_url()
        return super(HomeView, self).form_valid(form)



class ClientUpdate(LoginRequiredMixin, UpdateView):
    model = Client
    fields = ['last_name', 'first_name', 'street_address', 'city',
        'zipcode', 'email_address', 'home_phone', 'cell_phone', 'notes']
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get_success_url(self):
        return reverse('client-list')


class ClientCreate(LoginRequiredMixin, CreateView):
    model = Client
    fields = ['last_name', 'first_name', 'street_address', 'city',
        'zipcode', 'email_address', 'home_phone', 'cell_phone', 'notes']
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

class DogCreateView(LoginRequiredMixin, CreateView):
    model = Dog
    form_class = DogForm
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

class DogUpdateView(LoginRequiredMixin, UpdateView):
    model = Dog
    form_class = DogFormUpdate
    login_url = '/login/'
    redirect_field_name = 'redirect_to'


class DogDetailView(LoginRequiredMixin, DetailView):
    model = Dog
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

class DogClassListView(LoginRequiredMixin, ListView):
    model = DogClass
    ordering = ['startDate']
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

class DogClassCreateView(LoginRequiredMixin, CreateView):
    model = DogClass
    fields = ['name', 'startDate', 'endDate', 'classSize', 'dayOfTheWeek']
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

class DogClassDetailView(LoginRequiredMixin, DetailView):
    model = DogClass
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

class DogStudentCreateView(LoginRequiredMixin, CreateView):
    model = DogStudent
    fields = ['dogId', 'clientId', 'classId']
    def form_valid(self, form):
        my_student = form.instance
        myenroll = my_student.classId.enrollDog()
        my_student.classId.save()
        if myenroll == 'enrolled':
            return super(DogStudentCreateView, self).form_valid(form)
        else:
            return super(DogStudentCreateView, self).form_invalid(form)


class DogStudentDetailView(LoginRequiredMixin, DetailView):
    model = DogStudent

class ReservationDetailView(LoginRequiredMixin, DetailView):
    model = Reservation

class MakeAReservationView(LoginRequiredMixin, CreateView):
    model = Reservation
    template_name = 'reservation_form.html'
    form_class = MakeAReservationForm
    def form_valid(self, form):
        dateRes = form.instance
        dateRes.save()
        ownerRes = dateRes.owner
        dogRes = dateRes.dog
        dogRes2 = dateRes.dog2
        dogRes3 = dateRes.dog3
        dateStart = dateRes.check_in
        dateEnd = dateRes.check_out
        dates = []
        if dateStart == dateEnd:
            dates.append(dateStart)#In case of one day stay
        while dateStart < dateEnd:
            dates.append(dateStart)
            dateStart = dateStart + datetime.timedelta(1)
        for days in dates:
            i, created = DayRunReservation.objects.get_or_create(date=days)
            if created == False:
                if i.available_runs > 0:
                    i.save()
                    i.makeReservation()
                    i.save()
                    x, wasCreated = DogDayRes.objects.get_or_create(res = dateRes, dayRun= i)
                    x.save()

                else:
                    return super(MakeAReservationView, self).form_invalid(form)
            else:
                i.save()
                i.makeReservation()
                i.save()
                x, wasCreated = DogDayRes.objects.get_or_create(res = dateRes, dayRun= i)
                x.save()
                i.save()
        return super(MakeAReservationView, self).form_valid(form)

class ReservationList(LoginRequiredMixin, ListView):
    model = Reservation

class ReservationDetailView(LoginRequiredMixin, DetailView):
    model = Reservation

class DayRunReservationDetailView(LoginRequiredMixin, DetailView):
    model = DayRunReservation

class DogStudentDeleteView(LoginRequiredMixin, DeleteView):
    model = DogStudent
    success_url = "/classes/"
    def delete(request, *args, **kwargs):
        student = DogStudent.objects.get(id = kwargs['pk'])
        i = DogClass.objects.get(id = student.classId.id)
        i.cancelEnrollment()
        i.save()
        student.delete()
        return self.success_url
