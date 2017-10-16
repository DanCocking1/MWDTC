"""MWDTCdata URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import django.contrib.auth.urls
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.conf.urls import url, include
from django.contrib import admin
from client_data.views import (HomeView, ClientListView, ClientUpdate, ClientCreate,
                ClientDetailView, DogCreateView, DogDetailView, DogUpdateView,
                DogClassListView, DogClassCreateView, DogClassDetailView,
                DogStudentCreateView, DogStudentDetailView, MakeAReservationView,
                ReservationList, ReservationDetailView, DayRunReservationDetailView,
                DogStudentDeleteView, UserCreationView, ClientNonStaffCreate,
                DogNonStaffCreateView, DogUpdateNonStaff, DogStudentNonStaffCreateView,
                MakeAReservationNonStaffView, ReservationUpdate)
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^signup/$', UserCreationView.as_view(), name = 'user-add'),
    url(r'^addnonstaff/$', ClientNonStaffCreate.as_view(), name= 'nonstaff-add'),
    url(r'^dogaddnonstaff/$', DogNonStaffCreateView.as_view(), name='dogadd-nonstaff'),
    url(r'^$', HomeView.as_view()),
    url(r'^add/$', ClientCreate.as_view(), name='client-add'),
    url(r'^clients/$', ClientListView.as_view(), name = 'client-list'),
    url(r'^clients/(?P<pk>[0-9]+)/$', ClientDetailView.as_view(),name='client-detail'),
    url(r'^clients/update/(?P<pk>[0-9]+)/$', ClientUpdate.as_view(), name='client-update'),
    url(r'^dog/add/$', DogCreateView.as_view(), name ='dog-add'),
    url(r'^dog/(?P<pk>[0-9]+)/$', DogDetailView.as_view(), name = 'dog-detail'),
    url(r'^dog/update/(?P<pk>[0-9]+)/$', DogUpdateView.as_view(), name='dog-update'),
    url(r'^dog/update/nonstaff/(?P<pk>[0-9]+)/$', DogUpdateNonStaff.as_view(), name='dog-update-nonstaff'),
     url('^', include('django.contrib.auth.urls')),
     url(r'^classes/$', DogClassListView.as_view(), name='dog-class-list'),
     url(r'^classes/add/$', DogClassCreateView.as_view(), name='dog-class-add'),
     url(r'^classes/(?P<pk>[0-9]+)/$', DogClassDetailView.as_view(), name = 'dogclass-detail'),
     url(r'^student/(?P<pk>[0-9]+)/$', DogStudentDetailView.as_view(), name ='dogstudent-detail'),
     url(r'^student/add/$', DogStudentCreateView.as_view(), name = 'dogstudent-add'),
     url(r'^studentNonStaff/add/$', DogStudentNonStaffCreateView.as_view(), name='dogStudentNonStaff'),
     url(r'^reservation/add/$', MakeAReservationView.as_view(), name='reservation-add'),
     url(r'^reservationnonstaff/add/$', MakeAReservationNonStaffView.as_view(), name = 'reservation-add-non-staff'),
     url(r'^reservation/$', ReservationList.as_view(), name='reservation-list'),
     url(r'^reservation/update/(?P<pk>[0-9]+)/$', ReservationUpdate.as_view(), name='reservation-update'),
     url(r'^reservation/(?P<pk>[0-9]+)/$', ReservationDetailView.as_view(), name='reservation-detail'),
     url(r'^dayrun/(?P<pk>[0-9]+)/$', DayRunReservationDetailView.as_view(), name='dayrun-detail'),
     url(r'^student/delete/(?P<pk>[0-9]+)/$', DogStudentDeleteView.as_view(), name='dogstudent-delete'),
]
