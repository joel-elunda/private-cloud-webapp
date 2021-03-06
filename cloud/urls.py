"""cloud_intern cloud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
""" 
from django.urls import path
from django.views.generic.base import TemplateView
from . import views


app_name = 'cloud'

urlpatterns = [
    #URLs relatives to cloud features
    path('', views.home, name='home'),
    path('about/', TemplateView.as_view(template_name='index.html'), name='about'),
    path('upload/', views.upload, name='upload'),
    path('main/', TemplateView.as_view(template_name='main.html'), name='main'),
]  
