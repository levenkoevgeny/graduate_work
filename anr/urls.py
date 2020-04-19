from django.urls import path
from . import views
from django.contrib.auth.decorators import permission_required

app_name = 'anr'

urlpatterns = [
    path('', views.anr_list, name='list'),
    path('add/', permission_required('anr.add_anr')(views.anr_add), name='add'),
    path('update/<anr_id>/change/', permission_required('anr.change_anr')(views.anr_update), name='update'),
    path('delete/<pk>/', permission_required('anr.delete_anr')(views.ANRDelete.as_view()), name='delete'),
]