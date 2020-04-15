from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView


app_name = 'index'

urlpatterns = [
    path('', login_required(TemplateView.as_view(template_name="index/index.html")), name='index'),
    path('about/', login_required(TemplateView.as_view(template_name="index/about.html")), name='about'),
]