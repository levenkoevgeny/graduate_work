import django_filters
from .models import DissertationResearch
from authors.models import Author


class DissertationResearchFilter(django_filters.FilterSet):

    author = django_filters.ModelMultipleChoiceFilter(queryset=Author.objects.all())
    dissertation_theme = django_filters.CharFilter(lookup_expr='icontains')
    result = django_filters.CharFilter(lookup_expr='icontains')
    date_begin = django_filters.NumberFilter(lookup_expr='gte')
    date_end = django_filters.NumberFilter(lookup_expr='lte')

    class Meta:
        model = DissertationResearch
        fields = ['kind',
                  'status',
                  'dissertation_theme',
                  'reason',
                  'result',
                  'author',
                  'leader',
                  'leader_subdivision',
                  'research_place',
                  'research_place_subdivision',
                  'date_begin',
                  'date_end'
                  ]