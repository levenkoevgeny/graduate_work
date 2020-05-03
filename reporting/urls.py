from django.urls import path
from . import views
from django.contrib.auth.decorators import permission_required

app_name = 'reporting'

urlpatterns = [
    path('employee/', permission_required('reporting')(views.employee), name='employee'),
    path('subdivision/', permission_required('reporting')(views.subdivision), name='subdivision'),
    path('magazines/', permission_required('reporting')(views.magazines), name='magazines'),
    path('sciencetific_activities/', permission_required('reporting')(views.sciencetific_activities), name='sciencetific_activities'),
    # path('employee_rating/', login_required(views.employee_rating), name='employee_rating'),
    # path('employee_rating_all/', login_required(views.employee_rating_table), name='employee_rating_all'),
    # path('subdivision_rating/', login_required(views.subdivision_rating), name='subdivision_rating'),
    # path('subdivision_rating_all/', login_required(views.subdivision_rating_table), name='subdivision_rating_all'),
    # path('subdivision/', login_required(views.subdivision), name='subdivision'),
    # path('effectivenessnid/', login_required(views.effectivenessnid), name='effectivenessnid'),
]
