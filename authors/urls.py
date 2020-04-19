from django.urls import path
from . import views
from django.contrib.auth.decorators import permission_required

app_name = 'authors'

urlpatterns = [
    path('', views.author_list, name='list'),
    path('add/', permission_required('authors.add_author')(views.author_add), name='add'),
    path('update/<author_id>/change/', permission_required('authors.change_author')(views.author_update), name='update'),
    path('delete/<pk>/', permission_required('authors.delete_author')(views.AuthorDelete.as_view()), name='delete'),
]