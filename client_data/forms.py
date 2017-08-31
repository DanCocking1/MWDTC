from django import forms
from django.forms import ModelForm
from .models import Dog, Reservation, DayRunReservation
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
from django.forms import widgets

class DateInput(forms.DateInput):
    input_type = 'date'

class DogForm(ModelForm):
    class Meta:
        model = Dog
        fields = ['name', 'owner', 'breed', 'size', 'date_of_birth', 'gender', 'weight',
         'notes', 'rabies_date', 'distemper_date', 'parvo_date', 'bordetello']
        widgets = {
            'date_of_birth': DateInput(),
            'rabies_date': DateInput(),
            'distemper_date': DateInput(),
            'parvo_date': DateInput(),
            'bordetello': DateInput(),
         }
class DogFormUpdate(ModelForm):
    class Meta:
        model = Dog
        fields = ['weight', 'rabies_date', 'parvo_date', 'distemper_date',
            'bordetello', 'notes']
        widgets = {
            'rabies_date': DateInput(),
            'distemper_date': DateInput(),
            'parvo_date': DateInput(),
            'bordetello': DateInput(),
        }
class MakeAReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = [
            'owner', 'check_in', 'check_out', 'bath', 'bathDate', 'dog', 'dog2',
            'dog3'
        ]
        widgets = {
            'check_in':DateInput(),
            'check_out':DateInput(),
            'bathDate':DateInput(),
        }

class PickADate(forms.Form):
    date = forms.DateField(widget = DateInput)
