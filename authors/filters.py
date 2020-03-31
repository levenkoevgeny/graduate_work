import django_filters
from .models import Author, Subdivision, Position, Candidatespecialty, Doctorspecialty, Rank
from django import forms


class AuthorFilter(django_filters.FilterSet):

    DOCENT_VAK_CHOICES = (
        (1, 'Да'),
        (0, 'Нет'),
    )

    subdivision = django_filters.ModelMultipleChoiceFilter(queryset=Subdivision.objects.all())
    lastname = django_filters.CharFilter(field_name='lastname', lookup_expr='icontains')
    is_docentvak = django_filters.ChoiceFilter(choices=DOCENT_VAK_CHOICES, widget=forms.Select)
    is_professor = django_filters.ChoiceFilter(choices=DOCENT_VAK_CHOICES, widget=forms.Select)
    is_candidate = django_filters.ChoiceFilter(choices=DOCENT_VAK_CHOICES, widget=forms.Select)
    is_doctor = django_filters.ChoiceFilter(choices=DOCENT_VAK_CHOICES, widget=forms.Select)

    class Meta:
        model = Author
        fields = [
            'rank',
            'position',
            'doctor_specialty'
        ]