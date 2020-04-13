import django_filters
from .models import ANR
from authors.models import Author, Subdivision
from django import forms


class ANRFilter(django_filters.FilterSet):

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
    is_student_participation = django_filters.ChoiceFilter(choices=PARTICIPATION_CHOICES, widget=forms.Select)
    half_year = django_filters.ChoiceFilter(choices=HALFYEAR_CHOICES, widget=forms.Select)
    year_gte = django_filters.NumberFilter(field_name='year', lookup_expr='gte')
    year_lte = django_filters.NumberFilter(field_name='year', lookup_expr='lte')

    class Meta:
        model = ANR
        fields = ['development_kind', 'introduction_kind', 'introduction_organization', 'approve_date', 'half_year',
                  'subdivisions', 'year', 'is_student_participation', 'authors']