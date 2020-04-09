from django.forms import ModelForm
from .models import Sciencework
from django import forms
from django.forms.fields import CheckboxInput, Select


class ScienceworkForm(ModelForm):

    class Meta:

        CHOICES = [('1', 'Первое'), ('2', 'Второе')]

        model = Sciencework

        exclude = ['in_vak', 'in_internationals', 'author_count', 'subdivisions', 'org_founder']
        widgets = {'sciencework_student_participation': CheckboxInput(),
                   'work_is_foreignauthors': CheckboxInput(),
                   'half_year': Select(choices=CHOICES),
                   }


# class ConferenceForm(ModelForm):
#
#     class Meta:
#         model = Conference
#         fields = '__all__'
#         widgets = {'forumdate': myDateInput,
#                    }