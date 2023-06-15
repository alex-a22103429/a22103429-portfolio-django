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
    path('indexpresentation', views.home6_page_view, name='indexpresentation')
]
