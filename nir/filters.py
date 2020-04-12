import django_filters
from nir.models import NIR, ReasonNIR
from authors.models import Author, Subdivision
from django import forms


myDateInput = forms.DateInput(format=('%Y-%m-%d'), attrs={'type':'date'})


class NIRFilter(django_filters.FilterSet):
    authors = django_filters.ModelMultipleChoiceFilter(queryset=Author.objects.all())
    subdivisions = django_filters.ModelMultipleChoiceFilter(queryset=Subdivision.objects.all())
    reason = django_filters.ModelMultipleChoiceFilter(queryset=ReasonNIR.objects.all())
    start_date_since = django_filters.NumberFilter(lookup_expr='gte', field_name='start_date__year')
    start_date_till = django_filters.NumberFilter(lookup_expr='lte', field_name='start_date__year')
    end_date_since = django_filters.NumberFilter(lookup_expr='gte', field_name='end_date__year')
    end_date_till = django_filters.NumberFilter(lookup_expr='lte', field_name='end_date__year')
    approve_date = django_filters.DateFilter(widget=myDateInput)
    nir_leader = django_filters.ModelMultipleChoiceFilter(queryset=Author.objects.all())
    leader_subdivision = django_filters.ModelMultipleChoiceFilter(queryset=Subdivision.objects.all())
    nir_title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = NIR
        fields = ['nir_title', 'reason', 'plan_item', 'result', 'approve_date', 'authors', 'subdivisions', 'nir_leader', 'leader_subdivision', 'start_date_since',
                  'start_date_till', 'end_date_since', 'end_date_till']
