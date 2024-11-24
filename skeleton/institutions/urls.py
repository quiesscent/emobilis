from django.urls import path 
from . import views
app_name = 'institutions'
urlpatterns = [
    path('', views.index, name='dashboard'),
    path('doctors/', views.doctors, name='doctors'),
    path('patients/', views.patients, name='patients'),
    path('staff/', views.staff, name='staff'),
    path('inpat/', views.inPatients, name='inpatients'),
    path('outpat/', views.outPatients, name='outpatients'),
    
    # add urls
    path('add_p/', views.updatePatient, name='add_p'),
    path('add_s/', views.updateStaff, name='add_s'),
    path('add_d/', views.updateDoctor, name='add_d'),
    path('add_in/', views.updateInpatient, name='add_in'),
    path('add_out/', views.updateOutpatient, name='add_out'),
    
    # update urls
    path('update_s/<str:pk>', views.updateStaff, name='update_s'),
    path('update_p/<str:pk>', views.updatePatient, name='update_p'),
    path('update_d/<str:pk>', views.updateDoctor, name='update_d'),
    path('update_out/<int:pk>', views.updateOutpatient, name='update_out'),
    path('update_in/<int:pk>', views.updateInpatient, name='update_in'),
    
    # delete urls
    path('delete_s/<str:pk>', views.deletePatient, name='delete_p'),
    path('delete_p/<str:pk>', views.deleteDoctor, name='delete_d'),
    path('delete_d/<str:pk>', views.deleteStaff, name='delete_s'),
    path('delete_in/<int:pk>', views.deleteInpatient, name='delete_in'),
    path('delete_out/<int:pk>', views.deleteOutpatient, name='delete_out'),
    

]
