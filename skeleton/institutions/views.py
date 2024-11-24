from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient, Doctor, InPatientRecord, OutPatientRecord, Staff
from datetime import datetime
from acc.models import CustomUser
from django.contrib import messages
from .forms import DoctorForm, PatientForm, OutPatientRecordForm, InPatientRecordForm, StaffForm
# Create your views here.

def index(request):
    
    return render(request, 'inst_dash.html')


def doctors(request):
    doctors = Doctor.objects.all().order_by('-id')
    return render(request, 'doctor.html', { 'doctors': doctors })

def patients(request):
    patients = Patient.objects.all().order_by('-id')
    return render(request, 'patient.html', { 'patients': patients })


def outPatients(request):
    patients = OutPatientRecord.objects.all().order_by('-id')
    return render(request, 'patient.html', { 'patients': patients })


def inPatients(request):
    patients = InPatientRecord.objects.all().order_by('-id')
    return render(request, 'patient.html', { 'patients': patients })


def staff(request):
    staffs = Staff.objects.all().order_by('-id')
    return render(request, 'patient.html', { 'staffs': staffs })


# update functions
def updatePatient(request, pk=None):
    if pk:
        # If id is provided, get the existing object or 404
        patient = get_object_or_404(Patient, patient_id=pk)
    else:
        # Create a new instance for adding
        patient = None
        form = PatientForm()
        
    if request.method == "POST":
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            messages.success(request, 'System change Success')
        else:
            form = PatientForm(instance=patient)
        
    context = {
            'form': form
        }
    
    return render(request, 'patient.html', context)

def updateDoctor(request, pk=None):
    if pk:
        # If id is provided, get the existing object or 404
        doctor = get_object_or_404(Doctor, employee_id=pk)
    else:
        # Create a new instance for adding
        doctor = None
        form = DoctorForm()
        
    if request.method == "POST":
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            # get the cleaned data and create a user
            username=form.cleaned_data['name']
            password=form.cleaned_data['password']
            email=form.cleaned_data['email']
            user_type='doctor'
            doc = CustomUser.objects.create_user(username=username, password=password, email=email, user_type=user_type, institution=request.user.username)
            doc.save()
            form.save()
            messages.success(request, 'System change Success')
        else:
            form = DoctorForm(instance=doctor)
        
    context = {
            'form': form
        }
    
    return render(request, 'doctor.html', context)


def updateStaff(request, pk=None):
    if pk:
        # If id is provided, get the existing object or 404
        staff = get_object_or_404(Staff, employee_id=pk)
    else:
        # Create a new instance for adding
        staff = None
        form = StaffForm()
        
    if request.method == "POST":
        form = PatientForm(request.POST, instance=staff)
        if form.is_valid():
            form.save()
            messages.success(request, 'System change Success')
        else:
            form = StaffForm(instance=staff)
        
    context = {
            'form': form
        }
    
    return render(request, 'staff.html', context)


def updateInpatient(request, pk=None):
    if pk:
        # If id is provided, get the existing object or 404
        inpatient = get_object_or_404(InPatientRecord, record_id=pk)
    else:
        # Create a new instance for adding
        inpatient = None
        form = InPatientRecordForm()
        
    if request.method == "POST":
        form = InPatientRecordForm(request.POST, instance=inpatient)
        if form.is_valid():
            form.save()
            messages.success(request, 'System change Success')
        else:
            form = PatientForm(instance=patient)
        
    context = {
            'form': form
        }
    
    return render(request, 'inpatient.html', context)

def updateOutpatient(request, pk=None):
    
    if pk:
        # If id is provided, get the existing object or 404
        outpatient = get_object_or_404(OutPatientRecord, record_id=pk)
    else:
        # Create a new instance for adding
        outpatient = None
        form = OutPatientRecordForm()
        
    if request.method == "POST":
        form = OutPatientRecordForm(request.POST, instance=outpatient)
        if form.is_valid():
            form.save()
            messages.success(request, 'System change Success')
        else:
            form = OutPatientRecordForm(instance=outpatient)
        
    context = {
            'form': form
        }
    
    return render(request, 'outpatient.html', context)


# delete functions
def deletePatient(request, pk):
    instance = get_object_or_404(Patient, patient_id=pk)
    instance.delete()
    messages.success(request, 'Record Deleted Successfuly')

def deleteStaff(request, pk):
    instance = get_object_or_404(Staff, employee_id=pk)
    instance.delete()
    messages.success(request, 'Record Deleted Successfuly')

def deleteDoctor(request, pk):
    instance = get_object_or_404(Doctor, employee_id=pk)
    acc_instance = get_object_or_404(CustomUser, email=instance.email)
    instance.delete()
    
    #delete access to login
    acc_instance.delete()
    
    messages.success(request, 'Record Deleted Successfuly')

def deleteInpatient(request, pk):
    instance = get_object_or_404(InPatientRecord, record_id=pk)
    instance.delete()
    messages.success(request, 'Record Deleted Successfuly')

def deleteOutpatient(request, pk):
    instance = get_object_or_404(OutPatientRecord, record_id=pk)
    instance.delete()
    messages.success(request, 'Record Deleted Successfuly')