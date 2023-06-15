from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('about-me', views.aboutme_page_view, name='about-me'),
    path('index-copy', views.home1_page_view, name='index-copy'),
    path('index', views.home2_page_view, name='index'),
    path('indexcadeiras', views.home3_page_view, name='indexcadeiras'),
    path('indexcalculadora', views.home4_page_view, name='indexcalculadora'),
    path('indeximagem', views.home7_page_view, name='indeximagem'),
    path('indexcopy', views.home5_page_view, name='indexcopy'),
    path('index1', views.home8_page_view, name='index1'),
    path('index2', views.home9_page_view, name='index2'),
    path('index3', views.home10_page_view, name='index3'),
    path('index4', views.home11_page_view, name='index4'),
    path('index5', views.home12_page_view, name='index5'),
    path('index6', views.home13_page_view, name='index6'),
    path('index21', views.home14_page_view, name='index21'),
    path('index31', views.home15_page_view, name='index31'),
    path('index41', views.home16_page_view, name='index41'),
    path('index51', views.home17_page_view, name='index51'),
    path('index61', views.home18_page_view, name='index61'),


    path('indexpresentation', views.home6_page_view, name='indexpresentation')
]
