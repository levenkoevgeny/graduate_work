from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'dissertation'

urlpatterns = [
    path('', login_required(views.dissertation_research_list), name='list'),
    path('add/', login_required(views.dissertation_research_add), name='add'),
    path('update/<dissertation_research_id>/change/', views.dissertation_research_update, name='update'),
    path('delete/<pk>/', views.DissertationResearchDelete.as_view(), name='delete'),
]