from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from institutions.models import Patient, InPatientRecord, OutPatientRecord
from institutions.forms import InPatientRecordForm, OutPatientRecordForm
from .forms import PatientForm, AppointmentForm, MedicalReportForm
from .models import Appointment
# Create your views here.

def dashboard(request):

    return render(request, 'doc_dash.html')


def updateInPatient(request, pk=None):
    if pk:
        # If id is provided, get the existing object or 404
        patient = get_object_or_404(InPatientRecord, patient=pk)
        
    if request.method == "POST":
        form = InPatientRecordForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            messages.success(request, 'Patient Information Updated Successfully')
            
        else:
            form = InPatientRecordForm(instance=patient)
        
    return render(request, 'patient.html', {'form': form})


def updateOutPatient(request, pk=None):
    if pk:
        # If id is provided, get the existing object or 404
        patient = get_object_or_404(OutPatientRecord, patient=pk)
        
    if request.method == "POST":
        form = OutPatientRecordForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            messages.success(request, 'Patient Information Updated Successfully')
            
        else:
            form = OutPatientRecordForm(instance=patient)
    return render(request, 'patient.html', {'form': form})
    

def updatePatient(request, pk):
    
    if pk:
        # If id is provided, get the existing object or 404
        patient = get_object_or_404(Patient, id=pk)
    else:
        patient = None
        form = PatientForm(instance=patient)
        
    if request.method == "POST":
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            messages.success(request, 'Patient Information Updated Successfully')
            
        else:
            form = PatientForm(instance=patient)
            
    return render(request, 'patient.html', {'form': form})


def appointments(request):
    appointments = Appointment.objects.all().order_by('-id')
    context = {
        'appointments'
    }
    pass

def patients(request):
    patients = Patient.objects.all().order_by('-id')
    return render(request, 'patient.html', { 'patients': patients })


def outPatients(request):
    patients = OutPatientRecord.objects.all().order_by('-id')
    return render(request, 'patient.html', { 'patients': patients })


def inPatients(request):
    patients = InPatientRecord.objects.all().order_by('-id')
    return render(request, 'patient.html', { 'patients': patients })

def deleteappointments(request, pk):
    instance = get_object_or_404(Appointment, id=pk)
    instance.delete()
    messages.success(request, 'Record Deleted Successfuly')

def deleteInpatient(request, pk):
    instance = get_object_or_404(InPatientRecord, record_id=pk)
    instance.delete()
    messages.success(request, 'Record Deleted Successfuly')

def deletepatient(request, pk):
    instance = get_object_or_404(Patient, record_id=pk)
    instance.delete()
    messages.success(request, 'Record Deleted Successfuly')
    
def deleteOutpatient(request, pk):
    instance = get_object_or_404(OutPatientRecord, record_id=pk)
    instance.delete()
    messages.success(request, 'Record Deleted Successfuly')