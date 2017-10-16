from django import forms
from django.forms import ModelForm
from .models import Dog, Reservation, DayRunReservation, DogClass, Client, DogStudent
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.fields import DateField
from django.forms import widgets
import datetime

class SignUpForm(UserCreationForm):
    model=User
    first_name=forms.CharField(max_length=30, required=True, help_text = 'required')
    last_name = forms.CharField(max_length=30, required=True, help_text = 'required')
    email_address = forms.EmailField(required= True)
    #notes = forms.TextField(max_length=512, null=True, help_text="anything else we need to know")


    class Meta:
        model = User
        fields = ('email_address', 'first_name', 'last_name',
        'password1', 'password2')


class DateInput(forms.DateInput):
    input_type = 'date'

class DogForm(ModelForm):
    class Meta:
        model = Dog
        fields = ['name', 'owner', 'breed', 'size', 'date_of_birth', 'gender',
         'notes', 'rabies_date',  'parvo_distemper_date', 'bordetella', 'fecal_date']
        widgets = {
            'date_of_birth': DateInput(),
            'rabies_date': DateInput(),
            'parvo_distemper_date': DateInput(),
            'bordetella': DateInput(),
            'fecal_date':DateInput()
         }

class DogClassForm(ModelForm):
    class Meta:
        model = DogClass
        fields = ['name', 'startTime', 'startDate', 'endDate', 'classSize', 'dayOfTheWeek', 'privateClass']
        widgets = {
            'startDate': DateInput(),
            'endDate': DateInput(),
        }
        def __init__(self, *args, **kwargs):
            self.fields['classId'].queryset = DogClass.objects.filter(
            endDate__gte=datetime.date.today(), privateClass=False, enrollmentSlots__gt=0)

class DogNonStaffForm(ModelForm):
    class Meta:
        model = Dog
        fields = ['name', 'breed', 'size', 'date_of_birth', 'gender', 'notes']
        widgets = {
        'date_of_birth': DateInput(),
        }

class DogStudentNonStaffForm(forms.ModelForm):
    class Meta:
        model = DogStudent
        fields = ['classId', 'dogId']
    def __init__(self, *args, **kwargs):
        super(DogStudentNonStaffForm, self).__init__(*args, **kwargs)
        user = kwargs['initial']['uperall']
        self.fields['classId'].queryset = DogClass.objects.filter(
                endDate__gte=datetime.date.today(),
                privateClass=False, enrollmentSlots__gt=0)
        self.fields['dogId'].queryset = Dog.objects.filter(created = user)
        #self.fields['clientId'].queryset = Client.objects.filter(created = user)

class DogFormUpdate(ModelForm):
    class Meta:
        model = Dog
        fields = ['rabies_date', 'parvo_distemper_date',
            'bordetella', 'notes']
        widgets = {
            'rabies_date': DateInput(),
            'parvo_distemper_date': DateInput(),
            'bordetella': DateInput(),
        }
class MakeAReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = [
            'owner', 'check_in', 'check_out', 'bath', 'bathDate', 'dog', 'dog2',
            'dog3', 'PickUpTime', 'kennel_num', 'nails', 'medicationInstructions',
            'feedingInstructions'

        ]
        widgets = {
            'check_in':DateInput(),
            'check_out':DateInput(),
            'bathDate':DateInput(),
        }

class ReservationUpdateForm(ModelForm):
    class Meta:
        model = Reservation
        fields = [
            'bath', 'bathDate', 'dog', 'dog2',
            'dog3', 'PickUpTime', 'kennel_num', 'nails', 'medicationInstructions',
            'feedingInstructions'
        ]
        widgets = {
            'bathDate':DateInput(),
        }

class MakeAReservationNonStaffForm(ModelForm):
    class Meta:
        model = Reservation
        fields = [
            'owner', 'check_in', 'check_out', 'bath', 'bathDate', 'dog', 'dog2', 'dog3',
            'PickUpTime', 'medicationInstructions', 'feedingInstructions'
        ]
        widgets = {
            'check_in':DateInput(),
            'check_out':DateInput(),
            'bathDate':DateInput(),
        }
    def __init__(self, *args, **kwargs):
        super(MakeAReservationNonStaffForm, self).__init__(*args, **kwargs)
        user = kwargs['initial']['uperall']
        self.fields['owner'].queryset = Client.objects.filter(created= user)
        self.fields['dog'].queryset = Dog.objects.filter(created = user)
        self.fields['dog2'].queryset = Dog.objects.filter(created = user)
        self.fields['dog3'].queryset = Dog.objects.filter(created = user)


class PickADate(forms.Form):
    date = forms.DateField(widget = DateInput)
