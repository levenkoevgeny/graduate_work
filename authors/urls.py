from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'authors'

urlpatterns = [
    path('', login_required(views.author_list), name='list'),
    path('add/', login_required(views.author_add), name='add'),
    path('update/<author_id>/change/', views.author_update, name='update'),
    path('delete/<pk>/', views.AuthorDelete.as_view(), name='delete'),
]