from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'nir'

urlpatterns = [
    path('', login_required(views.nir_list), name='list'),
    path('add/', login_required(views.nir_add), name='add'),
    path('update/<nir_id>/change/', views.nir_update, name='update'),
    path('delete/<pk>/', views.NIRDelete.as_view(), name='delete'),
]