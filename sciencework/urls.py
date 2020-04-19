from django.urls import path
from . import views
from django.contrib.auth.decorators import permission_required

app_name = 'sciencework'

urlpatterns = [
    path('', views.sciencework_list, name='list'),
    path('add/', permission_required('sciencework.add_sciencework')(views.sciencework_add), name='add'),
    path('update/<sciencework_id>/change/', permission_required('sciencework.change_sciencework')(views.sciencework_update), name='update'),
    path('delete/<pk>/', permission_required('sciencework.delete_sciencework')(views.ScienceworkDelete.as_view()), name='delete'),
]