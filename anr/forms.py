from django.forms import ModelForm
from .models import ANR
from django import forms
from django.forms.fields import Select

myDateInput = forms.DateInput(format=('%Y-%m-%d'), attrs={'type':'date'})


class ANRForm(ModelForm):

    class Meta:

        CHOICES = [('1', 'Первое'), ('2', 'Второе')]

        model = ANR
        exclude = ['subdivisions']
        widgets = {
            'approve_date': myDateInput,
            'half_year': Select(choices=CHOICES),
        }