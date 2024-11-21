from django.urls import path
from . import views

app_name="acc"

urlpatterns = [
    path('', views.login, name='login'),
    path('register', views.register, name='register')
    
]