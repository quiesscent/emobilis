from django.urls import path 
from . import views

app_name="core"

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
    path('blog', views.blog, name='blog')
]
