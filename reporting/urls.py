from django.urls import path
from . import views
from django.contrib.auth.decorators import permission_required

app_name = 'reporting'

urlpatterns = [
    path('employee/', permission_required('reporting.add_ratingemployee')(views.employee), name='employee'),
    path('subdivision/', permission_required('reporting.add_ratingemployee')(views.subdivision), name='subdivision'),
    path('magazines/', permission_required('reporting.add_ratingemployee')(views.magazines), name='magazines'),
    path('sciencetific_activities/', permission_required('reporting.add_ratingemployee')(views.sciencetific_activities), name='sciencetific_activities'),
    path('employee_rating/', permission_required('reporting.add_ratingemployee')(views.employee_rating), name='employee_rating'),
    path('employee_rating_all/', permission_required('reporting.add_ratingemployee')(views.employee_rating_table), name='employee_rating_all'),
    path('subdivision_rating/', permission_required('reporting.add_ratingemployee')(views.subdivision_rating), name='subdivision_rating'),
    path('subdivision_rating_all/', permission_required('reporting.add_ratingemployee')(views.subdivision_rating_table), name='subdivision_rating_all'),
    # path('effectivenessnid/', login_required(views.effectivenessnid), name='effectivenessnid'),
]
