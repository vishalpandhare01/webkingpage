from django.contrib import admin
from django.urls import path
from .import views

from django.views.static import serve
from django.conf.urls.static import url
from django.conf import settings

urlpatterns = [
    path('', views.index,name='index'),
    path('auth/reg', views.reg,name='reg'),
    path('auth/login', views.login,name='login'),
    path('home', views.home,name='home'),
    path('services', views.services,name='services'),
    path('contact', views.contact,name='contact'),

    url(r'^media/(?P<path>.*)$', serve,{'document_root':settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT})
]
