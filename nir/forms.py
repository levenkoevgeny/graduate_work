from django.forms import ModelForm
from .models import NIR
from django import forms


myDateInput = forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date'})


class NIRForm(ModelForm):

    class Meta:
        model = NIR
        exclude = ['subdivisions', 'nir_leader_subdivision']
        widgets = {
            'start_date': myDateInput,
            'end_date': myDateInput,
            'approve_date': myDateInput,
        }