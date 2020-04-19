from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView


app_name = 'index'

urlpatterns = [
    path('', TemplateView.as_view(template_name="index/index.html"), name='index'),
    path('about/', TemplateView.as_view(template_name="index/about.html"), name='about'),
]