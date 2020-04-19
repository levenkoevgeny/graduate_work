import django_filters
from django import forms
from .models import DashBoard
from django.contrib.auth.models import User


myDateInput = forms.DateInput(format=('%Y-%m-%d'), attrs={'type':'date'})


class DashBoardItemFilter(django_filters.FilterSet):

    user = django_filters.ModelChoiceFilter(queryset=User.objects.all())
    activity_date_since = django_filters.DateFilter(widget=myDateInput, field_name='activity_date', lookup_expr='gte')
    activity_date_till = django_filters.DateFilter(widget=myDateInput, field_name='activity_date', lookup_expr='lte')

    class Meta:
        model = DashBoard
        fields = [
            'user',
            'activity_date_since',
            'activity_date_till',
        ]