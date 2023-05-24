from django.urls import path
from django.shortcuts import render
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('home', views.products_view, name='home'),
]
#  hello/urls.py

from django.shortcuts import render
