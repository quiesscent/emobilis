from django.urls import path 
from . import views
app_name = 'institutions'
urlpatterns = [
    path('', views.index, name='dashboard')
]
