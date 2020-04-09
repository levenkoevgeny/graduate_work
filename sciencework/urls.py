from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'sciencework'

urlpatterns = [
    path('', login_required(views.sciencework_list), name='list'),
    path('add/', login_required(views.sciencework_add), name='add'),
    path('update/<sciencework_id>/change/', views.sciencework_update, name='update'),
    path('delete/<pk>/', views.ScienceworkDelete.as_view(), name='delete'),
]