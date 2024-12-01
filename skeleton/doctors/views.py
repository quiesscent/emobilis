from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from institutions.models import InPatientRecord, OutPatientRecord, doctorAppointment
from institutions.forms import InPatientRecordForm, OutPatientRecordForm
from .forms import PatientForm, MedicalReportForm
from .models import Patient, MedicalReport
from acc.models import DoctorProfile, CustomUser, InstitutionDoctorProfile
from patients.models import patientAppointment
from acc.forms import DoctorProfileForm, InstitutionDoctorProfileForm
from patients.forms import PatientAppointmentForm
# Create your views here.

def dashboard(request):
    # profile = get_object_or_404(DoctorProfile, doctor=request.user.id)
    if request.user.institution != 'Private':
        doc = get_object_or_404(InstitutionDoctorProfile, doctor=request.user.username)
        appointments = {}
    else:
        doc = get_object_or_404(DoctorProfile, doctor=request.user.username) 
        appointments = patientAppointment.objects.filter(doctor=doc).order_by('-id')
    
    context = {
        'profile': doc,
        'appointments': appointments,
    }
    return render(request, 'doc_dash.html', context)

def profile(request):
    if request.user.institution != 'Private':
        
        doctor = get_object_or_404(InstitutionDoctorProfile, doctor=request.user.username)
        if request.method == 'POST':
            form = InstitutionDoctorProfileForm(request.POST, request.FILES, instance=doctor)
            if form.is_valid():
                form.save()
                messages.success(request, 'Profile Updated Successful')
                return redirect('doctors:profile')  # Change 'success_url' to your desired success URL
        else:
            form = InstitutionDoctorProfileForm(instance=doctor)

        return render(request, 'inst_doc_profile.html', {'form': form, 'profile': doctor})
    
    else:
        
        doctor = get_object_or_404(DoctorProfile, doctor=request.user.username)
        if request.method == 'POST':
            form = DoctorProfileForm(request.POST, request.FILES, instance=doctor)
            if form.is_valid():
                form.save()
                messages.success(request, 'Profile Updated Successful')
                return redirect('doctors:profile')  # Change 'success_url' to your desired success URL
        else:
            form = DoctorProfileForm(instance=doctor)

        return render(request, 'doc_profile.html', {'form': form, 'profile': doctor})

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
        
    return render(request, 'doc_update_inpatient.html', {'form': form})


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
    return render(request, 'doc_update_outpatient.html', {'form': form})
    

def updatePatient(request):
    form = PatientForm(initial={ 'doctor': request.user.username })
        
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Patient Information Updated Successfully')
            return redirect('doctors:patients')
        else:
            print("invalid")
            
    return render(request, 'doc_add_patient.html', {'form': form})

def patient(request, pk=None):
        
    if pk:
        # If id is provided, get the existing object or 404
        patient = get_object_or_404(Patient, id=pk)

    if request.method == "POST":
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            messages.success(request, 'Patient Information Updated Successfully')
            
    else:
        
        form = PatientForm(instance=patient, initial={ 'doctor': request.user.username })
        
    context = {
        'patient': patient,
        'form': form
    }
    
    return render(request, 'doc_update_patient.html', context)

def appointments(request):
    
    if request.user.institution == 'Private':
        
        doc = get_object_or_404(DoctorProfile, doctor=request.user.username) 
        appointments = patientAppointment.objects.filter(doctor=doc).order_by('-id')
        
    else:
        
        doctor = get_object_or_404(InstitutionDoctorProfile, doctor=request.user.username)
        appointments = doctorAppointment.objects.filter(doctor=doctor).order_by('-id')
    
    context = {
        'appointments':appointments
    }
    
    return render(request, 'doc_appointments.html', context)

def appointment(request, pk):
    if pk:
        patient = get_object_or_404(patientAppointment, id=pk)

    if request.method == "POST":
        form = PatientAppointmentForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            messages.success(request, 'Patient Information Updated Successfully')
                        
    else:
        
        form = PatientAppointmentForm(instance=patient)
    
    context = {
        'patient': patient,
        'form': form
    }
    
    return render(request, 'doc_appointment.html', context)

def add_record(request):
    
    if request.method == 'POST':
        
        form = MedicalReportForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Record Uploaded Successfully')
            return redirect('doctors:records')
         
    else:
        
        form = MedicalReportForm(initial={ 'doctor': request.user.username })
            
    return render(request, 'doc_add_record.html', {'form': form})

def record(request, pk):

    record = get_object_or_404(MedicalReport, id=pk)
    
    if request.method == "POST":
        form = MedicalReportForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record Information Updated Successfully')
            
    else:
        form = MedicalReportForm(instance=record)
    
    context = {
        'record': record,
        'form': form
    }
    return render(request, 'doc_record.html', context)

def records(request):
    
    doctor = get_object_or_404(DoctorProfile, doctor=request.user.username)
    records = MedicalReport.objects.filter(doctor=doctor).order_by('-id')
    return render(request, 'records.html', { 'records': records })

def patients(request):
    doctor = get_object_or_404(DoctorProfile, doctor=request.user.username)
    patients = Patient.objects.filter(doctor=doctor).order_by('-id')
    return render(request, 'patient.html', { 'patients': patients })


def outPatients(request):
    doctor = get_object_or_404(InstitutionDoctorProfile, doctor=request.user.username)
    patients = OutPatientRecord.objects.filter(assigned_doctor=doctor).order_by('-id')
    return render(request, 'outpatient.html', { 'patients': patients })


def inPatients(request):
    doctor = get_object_or_404(InstitutionDoctorProfile, doctor=request.user.username)
    patients = InPatientRecord.objects.filter(assigned_doctor=doctor).order_by('-id')
    return render(request, 'inpatient.html', { 'patients': patients })

    
def deleteappointments(request, pk):
    instance = get_object_or_404(Appointment, id=pk)
    instance.delete()
    messages.success(request, 'Record Deleted Successfuly')
    return redirect('doctors:dashboard')

def deleterecord(request, pk):
    instance = get_object_or_404(MedicalReport, id=pk)
    instance.delete()
    messages.success(request, 'Record Deleted Successfuly')
    return redirect('doctors:dashboard')

def deleteInpatient(request, pk):
    instance = get_object_or_404(InPatientRecord, record_id=pk)
    instance.delete()
    messages.success(request, 'Record Deleted Successfuly')
    return redirect('doctors:dashboard')


def deletepatient(request, pk):
    instance = get_object_or_404(Patient, id=pk)
    instance.delete()
    messages.success(request, 'Record Deleted Successfuly')
    return redirect('doctors:dashboard')
    
    
def deleteOutpatient(request, pk):
    instance = get_object_or_404(OutPatientRecord, record_id=pk)
    instance.delete()
    messages.success(request, 'Record Deleted Successfuly')
    return redirect('doctors:dashboard')