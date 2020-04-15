import django_filters
from .models import PLD, PatentOwner
from authors.models import Author, Subdivision


class PLDFilter(django_filters.FilterSet):


    BOOLEAN_CHOICES = (
        (1, 'Да'),
        (0, 'Нет'),
    )

    authors = django_filters.ModelMultipleChoiceFilter(queryset=Author.objects.all())
    subdivisions = django_filters.ModelMultipleChoiceFilter(queryset=Subdivision.objects.all())
    patent_owner = django_filters.ModelMultipleChoiceFilter(queryset=PatentOwner.objects.all())
    pld_title = django_filters.CharFilter(lookup_expr='icontains')
    action_start_gte = django_filters.NumberFilter(field_name='action_start__year', lookup_expr='gte')
    action_start_lte = django_filters.NumberFilter(field_name='action_start__year', lookup_expr='lte')
    registration_date_gte = django_filters.NumberFilter(field_name='registration_date__year', lookup_expr='gte')
    registration_date_lte = django_filters.NumberFilter(field_name='registration_date__year', lookup_expr='lte')

    class Meta:
        model = PLD
        fields = [
            'kind',
            'pld_title',
            'authors',
            'subdivisions',
            'patent_owner',
            'panent_number',
        ]
