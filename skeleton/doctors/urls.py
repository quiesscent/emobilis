from django.urls import path 
from . import views

app_name="doctors"

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('inpatient/<int:pk>', views.updateInPatient, name='inpatient'),
    path('outpatient/<int:pk>', views.updateOutPatient, name='outpatient'),
    path('patients/', views.patients, name='patients'),
    path('inpat/', views.inPatients, name='inpatients'),
    path('outpat/', views.outPatients, name='outpatients'),
    path('add_p/', views.updatePatient, name='add_patient'),
    path('update_p/<int:pk>', views.updatePatient, name='up_patient'),
    path('delete_p/<int:pk>', views.deletepatient, name='up_patient'),
    path('delete_in/<int:pk>', views.deleteInpatient, name='up_patient'),
    path('delete_out/<int:pk>', views.deleteOutpatient, name='up_patient'),
    path('delete_ap/<int:pk>', views.deleteappointments, name='up_patient'),
    path('appointments/', views.appointments, name='appointments'),
    
]
