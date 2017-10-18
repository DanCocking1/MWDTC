from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import datetime
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (TemplateView,ListView, UpdateView, CreateView,
                        DetailView, FormView, DeleteView)
from .models import (Dog, Client, DogClass, DogStudent, DayRunReservation,
                        Reservation, DogDayRes, PrivateDogClass)
from .forms import (DogForm, DogFormUpdate, MakeAReservationForm, PickADate,
                        DogClassForm, SignUpForm, DogNonStaffForm,
                        DogStudentNonStaffForm, MakeAReservationNonStaffForm,
                        ReservationUpdateForm, NonStaffReservationUpdateForm,
                        PrivateClassForm, PrivateClassUpdateForm)
from django.http import Http404



# Create your views here.
class ClientListView(UserPassesTestMixin, LoginRequiredMixin, ListView):
    def test_func(self):
        return self.request.user.is_staff
    model = Client
    template_name = 'client_list.html'
    context_object_name = 'client_detail'
    ordering = ['last_name']
    paginate_by = 100
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    # res = send_mail('Test Send', 'Testing Sending to my email address', 'testMWDTC@yahoo.com', ['Dan.Cocking@gmail.com'])
class NoRoomView(LoginRequiredMixin, TemplateView):
    template_name = 'client_data/no_room.html'
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

class HomeView(LoginRequiredMixin, FormView):
    template_name = 'index.html'
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    form_class = PickADate
    success_url = '/'

    def form_valid(self, form):
        if 'checkRuns' in self.request.POST:
            todayDate = datetime.date.today()
            dateToCheck = form.cleaned_data['date']
            i, created = DayRunReservation.objects.get_or_create(date = dateToCheck)
            i.save()
            self.success_url = i.get_absolute_url()
            return super(HomeView, self).form_valid(form)
        elif 'checkClasses' in self.request.POST:
            todayDate = datetime.date.today()
            dateToCheck = form.cleaned_data['date']
            try:
                i = DogClass.objects.get(startDate = dateToCheck)
                self.success_url = i.get_absolute_url()
                return super(HomeView, self).form_valid(form)
            except:
                raise Http404("No classes start on given Date")
                self.success_url = '/'
                return super(HomeView, self).form_valid
        else:
            todayDate = datetime.date.today()
            dateToCheck = form.cleaned_data['date']
            try:
                i = Reservation.objects.get(bathDate=dateToCheck)
                self.success_url = i.get_absolute_url()
                return super(HomeView, self).form_valid(form)
            except:
                raise Http404("No Baths scheduled on given Date")
                self.success_url = '/'
                return super(HomeView, self).form_valid





class UserCreationView(FormView):
    template_name = 'client_data/signup.html'
    form_class = SignUpForm
    model = User
    success_url = '/addnonstaff/'

    def form_valid(self, form):
        email = form.cleaned_data['email_address']
        username=email
        raw_password = form.cleaned_data['password1']
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']

        user = User.objects.create_user(username = email,
                                    email = email,
                                    password = raw_password,
                                    first_name = first_name,
                                    last_name = last_name)
        #form.save()
        user.save()
        authentic_user = authenticate(username = email, password=raw_password)
        if authentic_user:
            login(request = self.request, user=user)
            self.success_url = '/addnonstaff/'
            return super(UserCreationView, self).form_valid(form)

class ClientUpdate(LoginRequiredMixin, UpdateView):
    model = Client
    fields = ['street_address', 'city',
        'zipcode', 'home_phone', 'cell_phone']
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get_success_url(self):
        return reverse('client-list')

class ReservationUpdate(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    def test_func(self):
        return self.request.user.is_staff
    model = Reservation
    form_class = ReservationUpdateForm
    # template_name = "client_data/reservation_form.html"
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    def get_success_url(self):
        return reverse('reservation-list')

class ReservationUpdateNonStaff(LoginRequiredMixin, UpdateView):
    model = Reservation
    form_class = NonStaffReservationUpdateForm
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

class ClientCreate(UserPassesTestMixin, LoginRequiredMixin, CreateView):
    def test_func(self):
        return self.request.user.is_staff
    model = Client
    fields = ['last_name', 'first_name', 'street_address', 'city',
        'zipcode', 'email_address', 'home_phone', 'cell_phone', 'notes']
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

class ClientNonStaffCreate(LoginRequiredMixin, CreateView):
    model = Client
    fields = ['street_address', 'city', 'zipcode', 'home_phone', 'cell_phone']
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        request = self.request
        form.instance.created = request.user
        form.instance.first_name = request.user.first_name
        form.instance.last_name = request.user.last_name
        form.instance.email_address = request.user.username
        form.instance.street_address = form.cleaned_data['street_address']
        form.instance.city = form.cleaned_data['city']
        form.instance.zipcode = form.cleaned_data['zipcode']
        form.instance.home_phone = form.cleaned_data['home_phone']
        form.instance.cell_phone = form.cleaned_data['cell_phone']
        # newClient, created = Client.objects.get_or_create(
        #         created = created, first_name = first, last_name = last,
        #         email_address = email, street_address = street_add,
        #         city = city, zipcode = zipcode, home_phone= home_phone,
        #         cell_phone = cell_phone, notes = notes
        # )
        # newClient.save()
        return super(ClientNonStaffCreate, self).form_valid(form)


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

class PrivateDogClassCreate(UserPassesTestMixin, LoginRequiredMixin, CreateView):
    def test_func(self):
        return self.request.user.is_staff
    model = PrivateDogClass
    form_class = PrivateClassUpdateForm
    template_name = 'client_data/private_dog_class_form.html'
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

class PrivateDogClassUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    def test_func(self):
        return self.request.user.is_staff
    model = PrivateDogClass
    form_class = PrivateClassUpdateForm
    template_name = 'client_data/private_dog_class_form.html'
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

class PrivateDogDetailView(UserPassesTestMixin, LoginRequiredMixin, DetailView):
    def test_func(self):
        return self.request.user.is_staff
    model = PrivateDogClass
    template_name = 'client_data/private_dog_class_detail.html'
    login_url = '/login/'
    redirect_field_name = 'redirect_to'



class ClientHistoryDetailView(LoginRequiredMixin, DetailView):
    model = Client
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'client_data/client_detail_history.html'

class DogCreateView(UserPassesTestMixin, LoginRequiredMixin, CreateView):
    def test_func(self):
        return self.request.user.is_staff
    model = Dog
    form_class = DogForm
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

class DogNonStaffCreateView(LoginRequiredMixin, CreateView):
    model = Dog
    form_class = DogNonStaffForm
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    def form_valid(self, form):
        request = self.request
        form.instance.created = request.user
        form.instance.owner = Client.objects.get(created = request.user)
        form.instance.breed = form.cleaned_data['breed']
        form.instance.size = form.cleaned_data['size']
        form.instance.date_of_birth = form.cleaned_data['date_of_birth']
        form.instance.gender = form.cleaned_data['gender']
        form.instance.weight = form.cleaned_data['weight']
        form.instance.notes = form.cleaned_data['notes']
        now = datetime.date.today()
        form.instance.rabies_date = now
        form.instance.parvo_distemper_date = now
        form.instance.bordetello = now
        return super(DogNonStaffCreateView, self).form_valid(form)

class DogUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    def test_func(self):
        return self.request.user.is_staff
    model = Dog
    form_class = DogFormUpdate
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

class DogUpdateNonStaff(LoginRequiredMixin, UpdateView):
    model = Dog
    fields = ['weight', 'notes']


class DogDetailView(LoginRequiredMixin, DetailView):
    model = Dog
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

class DogClassListView(LoginRequiredMixin, ListView):
    model = DogClass
    ordering = ['startDate']
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

class DogClassCreateView(UserPassesTestMixin, LoginRequiredMixin, CreateView):
    def test_func(self):
        return self.request.user.is_staff
    model = DogClass
    form_class = DogClassForm
    # fields = ['name', 'startDate', 'endDate', 'classSize', 'dayOfTheWeek', 'privateClass']
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    def form_valid(self, form):
        form.instance.name = form.cleaned_data['name']
        form.instance.startDate = form.cleaned_data['startDate']
        form.instance.endDate = form.cleaned_data['endDate']
        form.instance.classSize = form.cleaned_data['classSize']
        form.instance.startTime = form.cleaned_data['startTime']
        form.instance.dayOfTheWeek = form.cleaned_data['dayOfTheWeek']
        form.instance.privateClass = form.cleaned_data['privateClass']
        form.instance.enrollmentSlots = form.cleaned_data['classSize']
        form.instance.enrolled = 0
        return super (DogClassCreateView, self).form_valid(form)

class DogClassDetailView(LoginRequiredMixin, DetailView):
    model = DogClass
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

class DogStudentNonStaffCreateView(LoginRequiredMixin, CreateView):
    def get_form_kwargs(self):
        user = self.request.user
        form_kwargs = super(DogStudentNonStaffCreateView, self).get_form_kwargs()
        form_kwargs.update({
            'initial': {
                'uperall': User.objects.filter(username=user.username)
            }
        })
        return form_kwargs

    form_class = DogStudentNonStaffForm
    model = DogStudent

    def form_valid(self, form):
        request = self.request
        form.instance.created = request.user
        form.instance.clientId = Client.objects.get(created=request.user)
        form.instance.classId = form.cleaned_data['classId']
        form.instance.dogId = form.cleaned_data['dogId']
        my_student = form.instance
        students = my_student.classId.enrolled
        slots = my_student.classId.classSize
        x = slots - students
        my_student.classId.enrollmentSlots = x
        myenroll = my_student.classId.enrollDog()
        my_student.classId.save()
        if myenroll == 'enrolled':
            return super(DogStudentNonStaffCreateView, self).form_valid(form)
        else:
            return super(DogStudentNonStaffCreateView, self).form_invalid(form)


class DogStudentCreateView(UserPassesTestMixin, LoginRequiredMixin, CreateView):
    def test_func(self):
        return self.request.user.is_staff
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

class MakeAReservationNonStaffView(LoginRequiredMixin, CreateView):
    model = Reservation
    template_name='reservation_form.html'
    form_class = MakeAReservationNonStaffForm
    def get_form_kwargs(self):
        user = self.request.user
        form_kwargs = super(MakeAReservationNonStaffView, self).get_form_kwargs()
        form_kwargs.update({
            'initial': {
                'uperall': User.objects.filter(username=user.username)
            }
        })
        return form_kwargs
    def form_valid(self, form):
        dateRes = form.instance
        request = self.request
        form.instance.created = request.user
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
                    if days == dateRes.check_in:
                        raise Http404 #x would not have been created
                    else:
                        daysCancelling = []
                        dateStart = dateRes.check_in
                        while dateStart < days:
                            daysCancelling.append(dateStart)
                            datestart = datestart + datetime.timedelta(1)
                        for daysToCancel in daysCancelling:
                            j = DayRunReservation.objects.get(date=daysToCancel)
                            j.save()
                            j.CancelRes()
                            j.save()
                            try:
                                k = DogDayRes.objects.get(res=dateRes, dayRun = j)
                                k.dogDayResCancelled = True
                            except:
                                print ("Error finding reservation")
                    return super(MakeAReservationNonStaffView, self).form_invalid(form)
            else:
                i.save()
                i.makeReservation()
                i.save()
                x, wasCreated = DogDayRes.objects.get_or_create(res = dateRes, dayRun= i)
                x.save()
                i.save()
        return super(MakeAReservationNonStaffView, self).form_valid(form)


class MakeAReservationView(UserPassesTestMixin, LoginRequiredMixin, CreateView):
    def test_func(self):
        return self.request.user.is_staff
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
                    success_url = '/noroom/'
                    if days == dateRes.check_in:
                        raise Http404 #x would not have been created
                    else:
                        daysCancelling = []
                        dateStart = dateRes.check_in
                        while dateStart < days:
                            daysCancelling.append(dateStart)
                            datestart = datestart + datetime.timedelta(1)
                        for daysToCancel in daysCancelling:
                            j = DayRunReservation.objects.get(date=daysToCancel)
                            j.save()
                            j.CancelRes()
                            j.save()
                            try:
                                k = DogDayRes.objects.get(res=dateRes, dayRun = j)
                                k.dogDayResCancelled = True
                            except:
                                print ("Error finding reservation")
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



class DayRunReservationDetailView(LoginRequiredMixin, DetailView):
    model = DayRunReservation
    def get_context_data(self, **kwargs):
        context = super(DayRunReservationDetailView, self).get_context_data(**kwargs)
        context['dayRun'] = DayRunReservation.objects.all()
        context['classes'] = DogClass.objects.all()
        return context

class DogStudentDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    def test_func(self):
        return self.request.user.is_staff
    model = DogStudent
    success_url = "/classes/"
    def delete(request, *args, **kwargs):
        student = DogStudent.objects.get(id = kwargs['pk'])
        i = DogClass.objects.get(id = student.classId.id)
        i.cancelEnrollment()
        i.save()
        student.delete()
        return self.success_url
