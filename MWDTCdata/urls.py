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
from django.conf.urls import url, include
from django.contrib import admin
from client_data.views import (HomeView, ClientListView, ClientUpdate, ClientCreate,
                ClientDetailView, DogCreateView, DogDetailView, DogUpdateView,
                DogClassListView, DogClassCreateView, DogClassDetailView,
                DogStudentCreateView, DogStudentDetailView, MakeAReservationView,
                ReservationList, ReservationDetailView, DayRunReservationDetailView,
                DogStudentDeleteView)
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view()),
    url(r'^add/$', ClientCreate.as_view(), name='client-add'),
    url(r'^clients/$', ClientListView.as_view(), name = 'client-list'),
    url(r'^clients/(?P<pk>[0-9]+)/$', ClientDetailView.as_view(),name='client-detail'),
    url(r'^clients/update/(?P<pk>[0-9]+)/$', ClientUpdate.as_view(), name='client-update'),
    url(r'^dog/add/$', DogCreateView.as_view(), name ='dog-add'),
    url(r'^dog/(?P<pk>[0-9]+)/$', DogDetailView.as_view(), name = 'dog-detail'),
    url(r'^dog/update/(?P<pk>[0-9]+)/$', DogUpdateView.as_view(), name='dog-update'),
     url('^', include('django.contrib.auth.urls')),
     url(r'^classes/$', DogClassListView.as_view(), name='dog-class-list'),
     url(r'^classes/add/$', DogClassCreateView.as_view(), name='dog-class-add'),
     url(r'^classes/(?P<pk>[0-9]+)/$', DogClassDetailView.as_view(), name = 'dogclass-detail'),
     url(r'^student/(?P<pk>[0-9]+)/$', DogStudentDetailView.as_view(), name ='dogstudent-detail'),
     url(r'^student/add/$', DogStudentCreateView.as_view(), name = 'dogstudent-add'),
     url(r'^reservation/add/$', MakeAReservationView.as_view(), name='reservation-add'),
     url(r'^reservation/$', ReservationList.as_view(), name='reservation-list'),
     url(r'^reservation/(?P<pk>[0-9]+)/$', ReservationDetailView.as_view(), name='reservation-detail'),
     url(r'^dayrun/(?P<pk>[0-9]+)/$', DayRunReservationDetailView.as_view(), name='dayrun-detail'),
     url(r'^student/delete/(?P<pk>[0-9]+)/$', DogStudentDeleteView.as_view(), name='dogstudent-delete')
]
