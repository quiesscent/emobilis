from django.urls import path
from . import views

app_name = 'patients'
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('doctors/',views.doctors, name='doctors'),
    path('doctor/<str:name>',views.doctor, name='doctor'),
    path('institutions/', views.institutions, name='institutions'),
    path('institutions/<str:name>', views.institutions, name='institution'),
    path('appointments/', views.appointments, name='appointments'),
    path('appointments/<int:pk>', views.appointment, name='appointment'),
    path('book_appointments/', views.book_appointment, name='book_appointment'),
    path('delete/<int:pk>', views.delete_appointment, name='delete'),
   
]
