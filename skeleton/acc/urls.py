from django.urls import path
from . import views

app_name="acc"

urlpatterns = [
    path('', views.login_, name='login'), 
    path('register', views.register, name='register'),
    path('register/inst', views.register_inst, name='register_inst'),
    path('register/doc', views.register_doc, name='register_doc'),
    path('logout', views.logout_, name='logout')
    
]