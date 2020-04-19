from django.urls import path
from . import views
from django.contrib.auth.decorators import permission_required

app_name = 'pld'

urlpatterns = [
    path('', views.pld_list, name='list'),
    path('add/', permission_required('pld.add_pld')(views.pld_add), name='add'),
    path('update/<pld_id>/change/', permission_required('pld.change_pld')(views.pld_update), name='update'),
    path('delete/<pk>/', permission_required('pld.delete_pld')(views.PLDDelete.as_view()), name='delete'),
]
