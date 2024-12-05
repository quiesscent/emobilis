from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient, Doctor, InPatientRecord, OutPatientRecord, Staff
from datetime import datetime
from acc.models import CustomUser, InstitutionProfile, InstitutionDoctorProfile
from django.contrib import messages
from acc.forms import InstitutionProfileForm
from .forms import DoctorForm, PatientForm, OutPatientRecordForm, InPatientRecordForm, StaffForm
from .identifications import *
# Create your views here.

def index(request):

    profile = get_object_or_404(InstitutionProfile, institution=request.user.username)
        
    context = {
        'profile':profile
    }
    return render(request, 'inst_dash.html', context)

def profile(request):
    try:
        institution = get_object_or_404(InstitutionProfile, institution=request.user.username)
    except:
        institution = None
        
    if request.method == 'POST':
        form = InstitutionProfileForm(request.POST, request.FILES, instance=institution)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Updated Successful')
            return redirect('institutions:profile')  # Change 'success_url' to your desired success URL
    else:
        form = InstitutionProfileForm(instance=institution, initial={'institution': request.user.username, 'email': request.user.email})
     
    return render(request, 'inst_profile.html', {'form':form, 'profile': institution}, )

# view data
def doctors(request):
    doctors = Doctor.objects.filter(institution=request.user.username).order_by('-id')
    return render(request, 'inst_doctor.html', { 'doctors': doctors })

def patients(request):
    patients = Patient.objects.filter(institution=request.user.username).order_by('-id')
    return render(request, 'inst_patient.html', { 'patients': patients })

def outPatients(request):
    patients = OutPatientRecord.objects.filter(institution=request.user.username).order_by('-id')
    return render(request, 'inst_outpatient.html', { 'patients': patients })

def inPatients(request):
    patients = InPatientRecord.objects.filter(institution=request.user.username).order_by('-id')
    return render(request, 'inst_inpatient.html', { 'patients': patients })

def staffs(request):
    staffs = Staff.objects.filter(institution=request.user.username).order_by('-id')
    return render(request, 'staff.html', { 'staffs': staffs })
# end view

# add views 
def addPatient(request):
    patient_id = generate_patient_id()
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save() 
            messages.success(request, 'Staff Added Successfully')
            return redirect('institutions:patients')  
        else:
            print('invalid form')
    else:
        
        form = PatientForm(initial={'patient_id': patient_id, 'institution': request.user.username }) 
        
    return render(request, 'add_patient.html', {'form': form })

def addDoctor(request):
    employee_id = generate_doctor_id()
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            # get the cleaned data and create a user
            doc = CustomUser.objects.create_user(username=form.cleaned_data['name'], password=form.cleaned_data['email'], email=form.cleaned_data['email'], user_type='doctor', institution=request.user.username)
            profile = InstitutionDoctorProfile.objects.create(doctor=form.cleaned_data['name'], email=form.cleaned_data['email'], employee_id=form.cleaned_data['employee_id'], department=form.cleaned_data['department'], specialization=form.cleaned_data['specialization'], institution=request.user.username)
            doc.save()
            profile.save()
            form.save()
            messages.success(request, 'System change Success')
            return redirect("institutions:doctors")
        else:
            print('invalid form')
    else:
        form = DoctorForm(initial={'employee_id': employee_id, 'institution': request.user.username })
        
    return render(request, 'add_doctor.html', {'form':form})


def addStaff(request):
    employee_id = generate_staff_id()
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save() 
            messages.success(request, 'Staff Added Successfully')
            return redirect('institutions:staffs')  
        else:
            print('invalid form')
    else:
        form = StaffForm(initial={'employee_id': employee_id, 'institution': request.user.username})   
    
    return render(request, 'add_staff.html', {'form': form})


def addInpatient(request):
    record_id = generate_inpatient_record_id()
    if request.method == 'POST':
        form = InPatientRecordForm(request.POST)
        if form.is_valid():
            form.save() 
            messages.success(request, 'Staff Added Successfully')
            return redirect('institutions:inpatients')  
        else:
            print('invalid form')
    else:
        form = InPatientRecordForm(initial={'record_id': record_id, 'institution': request.user.username}) 
        
    return render(request, 'add_inpatient.html', {'form': form })

def addOutpatient(request, pk=None):
    record_id = generate_inpatient_record_id()
    
    if request.method == 'POST':
        form = OutPatientRecordForm(request.POST)
        if form.is_valid():
            form.save() 
            messages.success(request, 'Staff Added Successfully')
            return redirect('institutions:outpatients')  
        else:
            print('invalid form')
    else:
        form = OutPatientRecordForm(initial={'record_id': record_id, 'institution': request.user.username}) 
        
    return render(request, 'add_outpatient.html',{'form': form})


# end add

# start update views
def doctor(request, name):
    
    name = name.replace('-', ' ').replace("_", ".")
   
    profile = get_object_or_404(Doctor, name__iexact=name)
    form = DoctorForm(instance=profile)
        
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Update Complete')
            return redirect("institutions:doctors")
        
    context = {
        'doctor': profile,
        'form': form
    }
    return render(request, 'view_doctor.html', context)

def patient(request, name):
    name = name.replace('-', ' ').replace("_", ".")
    profile = get_object_or_404(Patient, name__iexact=name)
    form = PatientForm(instance=profile)
        
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Update Complete')
            return redirect("institutions:patients")
        
    context = {
        'patient': profile,
        'form': form
    }     
    return render(request, 'view_patient.html', context)


def outPatient(request, pk):
    profile = get_object_or_404(OutPatientRecord, id=pk)
    form = OutPatientRecordForm(instance=profile)
        
    if request.method == 'POST':
        form = OutPatientRecordForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record  Update Complete')
            return redirect("institutions:outpatients")
    context = {
        'outpatient': profile,
        'form': form
    }
    return render(request, 'view_outpatient.html', context)

def inPatient(request, pk):

    profile = get_object_or_404(InPatientRecord, id=pk)
    form = InPatientRecordForm(instance=profile)
        
    if request.method == 'POST':
        form = InPatientRecordForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record Update Complete')
            return redirect("institutions:inpatients")
    context = {
        'inpatient': profile,
        'form': form
    }
    return render(request, 'view_inpatient.html', context)

def staff(request, name):
    name = name.replace('-', ' ').replace("_", ".")
   
    profile = get_object_or_404(Staff, name__iexact=name)
    form = StaffForm(instance=profile)
        
    if request.method == 'POST':
        form = StaffForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Update Complete')
            return redirect("institutions:staffs")
    
    context = {
        'staff': profile,
        'form': form
    }       
    return render(request, 'view_staff.html', context)

# end update


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
    instance = get_object_or_404(Doctor, id=pk)
    acc_instance = get_object_or_404(CustomUser, email=instance.email)
    instance.delete()
    #delete access to login
    acc_instance.delete()
    
    messages.success(request, 'Record Deleted Successfuly')
    return redirect('institutions:doctors')

def deleteInpatient(request, pk):
    instance = get_object_or_404(InPatientRecord, record_id=pk)
    instance.delete()
    messages.success(request, 'Record Deleted Successfuly')

def deleteOutpatient(request, pk):
    instance = get_object_or_404(OutPatientRecord, record_id=pk)
    instance.delete()
    messages.success(request, 'Record Deleted Successfuly')