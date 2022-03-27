from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('report/', views.report, name='report'),
    path('post/', views.post, name='post'),
    path('about/', views.about, name='about'),
    path('search_job/',views.search,name = 'search'),
    path('search_job/location/', views.search_job, name='search_job'),
    path('', views.home , name='home'),
]
#handler404 = views.page_404
#handler500 = views.page_500