from django.urls import path
from . import views
from django.contrib.auth.decorators import permission_required

app_name = 'dissertation'

urlpatterns = [
    path('', views.dissertation_research_list, name='list'),
    path('add/', permission_required('dissertationresearch.add_dissertationresearch')(views.dissertation_research_add), name='add'),
    path('update/<dissertation_research_id>/change/', permission_required('dissertationresearch.change_dissertationresearch')(views.dissertation_research_update), name='update'),
    path('delete/<pk>/', permission_required('dissertationresearch.delete_dissertationresearch')(views.DissertationResearchDelete.as_view()), name='delete'),
]