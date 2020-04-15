from django.forms import ModelForm
from .models import PLD
from django import forms


myDateInput = forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date'})


class PLDForm(ModelForm):

    class Meta:

        model = PLD
        exclude = ['subdivisions']
        widgets = {
            'action_start': myDateInput,
            'registration_date': myDateInput,
            'request_date': myDateInput,
        }
