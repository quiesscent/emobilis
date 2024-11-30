from django.urls import path 
from . import views
app_name = 'institutions'
urlpatterns = [
    path('', views.index, name='dashboard'),
    path('doctors/', views.doctors, name='doctors'),
    path('patients/', views.patients, name='patients'),
    path('staff/', views.staffs, name='staffs'),
    path('inpat/', views.inPatients, name='inpatients'),
    path('outpat/', views.outPatients, name='outpatients'),
    path('profile/', views.profile, name='profile'),
    
    # add urls
    path('add_p/', views.addPatient, name='add_p'),
    path('add_s/', views.addStaff, name='add_s'),
    path('add_d/', views.addDoctor, name='add_d'),
    path('add_in/', views.addInpatient, name='add_in'),
    path('add_out/', views.addOutpatient, name='add_out'),
    
    # update urls
    path('view_s/<str:name>', views.staff, name='staff'),
    path('view_p/<str:name>', views.patient, name='patient'),
    path('view_d/<str:name>', views.doctor, name='doctor'),
    path('view_out/<int:pk>', views.outPatient, name='outpatient'),
    path('view_in/<int:pk>', views.inPatient, name='inpatient'),
    
    # delete urls
    path('delete_s/<int:pk>', views.deletePatient, name='delete_p'),
    path('delete_d/<int:pk>', views.deleteDoctor, name='delete_d'),
    path('delete_d/<int:pk>', views.deleteStaff, name='delete_s'),
    path('delete_in/<int:pk>', views.deleteInpatient, name='delete_in'),
    path('delete_out/<int:pk>', views.deleteOutpatient, name='delete_out'),
    
    
]
