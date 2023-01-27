"""Defines URL patterns for users"""
from django.urls import path, include
from .import views


app_name = 'profiles_app'
urlpatterns = [
   
    path('', include('django.contrib.auth.urls')),  #the login and logout are in here
   
    path('register/', views.register, name='register'),
    
  
    
]