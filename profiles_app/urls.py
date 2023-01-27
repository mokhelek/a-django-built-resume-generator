"""Defines URL patterns for users"""
from django.urls import path, include
from .import views


app_name = 'profiles_app'
urlpatterns = [
    path('register/', views.register, name='register'),
    
    path('', include('django.contrib.auth.urls')),

]