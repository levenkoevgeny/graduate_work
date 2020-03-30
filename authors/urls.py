from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'authors'

urlpatterns = [
    path('', login_required(views.author_list), name='list'),
    path('add/', login_required(views.author_add), name='add'),

    #
    #
    #
    #
    #
    #
    #
    # path('addauthor/', login_required(views.addauthor), name='addauthor'),
    # path('input/getallauthorsajaxforcheck', views.getallauthorsajaxforcheck, name='getallauthorsajaxforcheck'),
    #
    # path('update/update/<pk>/change', login_required(views.AuthorUpdate.as_view()), name='authorchange'),
    # path('delete/<pk>/', login_required(views.AuthorDelete.as_view()), name='authordelete'),
]