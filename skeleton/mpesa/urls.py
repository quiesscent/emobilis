from django.urls import path
from . import views

urlpatterns = [
    path('', views.lipa_na_mpesa_online, name='pay')
]