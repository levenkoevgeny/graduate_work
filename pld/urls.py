from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'pld'

urlpatterns = [
    path('', login_required(views.pld_list), name='list'),
    path('add/', login_required(views.pld_add), name='add'),
    path('update/<anr_id>/change/', views.pld_update, name='update'),
    path('delete/<pk>/', views.PLDDelete.as_view(), name='delete'),
]
