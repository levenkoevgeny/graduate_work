from django.urls import path
from . import views
from django.contrib.auth.decorators import permission_required

app_name = 'dashboard'

urlpatterns = [
    path('', permission_required('dashboard.add_dashboard')(views.dashboard), name='main'),
    path('<user_id>/activity/', permission_required('anr.add_dashboard')(views.dashboard_item), name='item'),
]