import django_filters
from .models import Sciencework, InternationalBase
from authors.models import Author, Subdivision
from django import forms


class ScienceWorkFilter(django_filters.FilterSet):

    HALFYEAR_CHOICES = (
        (1, 'Первое'),
        (2, 'Второе'),
    )

    PARTICIPATION_CHOICES = (
        (1, 'Да'),
        (0, 'Нет'),
    )

    authors = django_filters.ModelMultipleChoiceFilter(queryset=Author.objects.all())
    subdivisions = django_filters.ModelMultipleChoiceFilter(queryset=Subdivision.objects.all())
    half_year = django_filters.ChoiceFilter(choices=HALFYEAR_CHOICES, widget=forms.Select)
    work_is_foreignauthors = django_filters.ChoiceFilter(choices=PARTICIPATION_CHOICES, widget=forms.Select)
    sciencework_student_participation = django_filters.ChoiceFilter(choices=PARTICIPATION_CHOICES, widget=forms.Select)
    in_vak = django_filters.ChoiceFilter(choices=PARTICIPATION_CHOICES, widget=forms.Select)
    year_gte = django_filters.NumberFilter(field_name='year', lookup_expr='gte')
    year_lte = django_filters.NumberFilter(field_name='year', lookup_expr='lte')
    in_internationals = django_filters.ModelChoiceFilter(queryset=InternationalBase.objects.all())
    output_data = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Sciencework
        fields = [
            'authors',
            'subdivisions',
            'half_year',
            'work_is_foreignauthors',
            'sciencework_student_participation',
            'in_vak',
            'year_gte',
            'year_lte',
            'in_internationals',
            'output_data',
            'kind',
            'subspecies',
            'publisher',
            'grif',
            'interest'
        ]
