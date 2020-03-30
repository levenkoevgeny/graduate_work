from django import forms
from django.forms import ModelForm
from django.forms.fields import CheckboxInput

myDateInput = forms.DateInput(format=('%Y-%m-%d'), attrs={'type':'date'})


class AuthorForm(ModelForm):
    class Meta:
        fields = '__all__'
        widgets = {
            'date_of_birth': myDateInput,
            'position_date': myDateInput,
            'docentvak_date': myDateInput,
            'professor_date': myDateInput,
            'candidate_date': myDateInput,
            'doctor_date': myDateInput,
        }
