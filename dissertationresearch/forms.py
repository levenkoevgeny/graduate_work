from django.forms import ModelForm
from .models import DissertationResearch
from django import forms


myDateInput = forms.DateInput(format=('%Y-%m-%d'), attrs={'type':'date'})


class DissertationResearchForm(ModelForm):

    class Meta:
        model = DissertationResearch
        exclude = ['leader_subdivision', 'research_place_subdivision']
        widgets = {
            'date_protect': myDateInput,
        }