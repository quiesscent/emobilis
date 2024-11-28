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
    path('update_p/<int:pk>', views.patient, name='up_patient'),
    path('delete_p/<int:pk>', views.deletepatient, name='del_patient'),
    path('delete_in/<int:pk>', views.deleteInpatient, name='del_inpatient'),
    path('delete_out/<int:pk>', views.deleteOutpatient, name='del_outpatient'),
    path('delete_ap/<int:pk>', views.deleteappointments, name='up_apppointment'),
    path('appointments/', views.appointments, name='appointments'),
    path('appointments/<int:pk>', views.appointment, name='appointment'),
    path('record/<int:pk>', views.record, name='record'),
    path('records/', views.records, name='records'),
    path('add_record/', views.add_record, name='add_record'),
    path('delete_record/<int:pk>', views.deleterecord, name='del_record'),
    path('profile/', views.profile, name="profile")
    
]