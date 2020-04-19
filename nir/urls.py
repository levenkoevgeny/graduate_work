from django.urls import path
from . import views
from django.contrib.auth.decorators import permission_required

app_name = 'nir'

urlpatterns = [
    path('', views.nir_list, name='list'),
    path('add/', permission_required('nir.add_nir')(views.nir_add), name='add'),
    path('update/<nir_id>/change/', permission_required('nir.change_nir')(views.nir_update), name='update'),
    path('delete/<pk>/', permission_required('nir.delete_nir')(views.NIRDelete.as_view()), name='delete'),
]