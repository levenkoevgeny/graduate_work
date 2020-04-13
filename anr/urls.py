from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'anr'

urlpatterns = [
    path('', login_required(views.anr_list), name='list'),
    path('add/', login_required(views.anr_add), name='add'),
    path('update/<anr_id>/change/', views.anr_update, name='update'),
    path('delete/<pk>/', views.ANRDelete.as_view(), name='delete'),
]