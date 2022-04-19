from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    path('', views.index,name='index'),
    path('auth/reg', views.reg,name='reg'),
    path('auth/login', views.login,name='login'),
    path('home', views.home,name='home'),
    path('services', views.services,name='services'),
    path('contact', views.contact,name='contact'),

   
]
