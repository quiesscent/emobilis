from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from acc.models import CustomUser
from .models import patientAppointment
from .forms import PatientAppointmentForm
from institutions.models import Doctor

# Create your views here.

def dashboard(request):

    return render(request, 'pat_index.html')

def profile(request):
    
    appointment = get_object_or_404(patientAppointment, id=request.user.id)

    if request.method == "POST":
        form = PatientAppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            messages.success(request, 'System change Success')
            
    else:
        form = PatientAppointmentForm(instance=appointment)
        
    context = {
        'form': form,
        'appointment': appointment
    }
    
def doctor(request, name):
    pass

def doctors(request):
    private_doctors = CustomUser.objects.filter(institution='Private')
    # non_private_doctors = CustomUser.objects.exclude(institution="Private").exclude(institution='None')
    non_private_doctors = Doctor.objects.all()
    
    context = {
        'privates': private_doctors,
        'covered': non_private_doctors,
    }
    
    return render(request, 'pat_doctors.html', context)

def institutions(request):
    institutions = CustomUser.objects.filter(user_type='institution')
    
    context = {
        'institutions': institutions
        
    }
    return render(request, 'pat_institutions.html', context)


def institution(request, name):
    name = name.replace('-', ' ').replace('_', '\'')
    institution = get_object_or_404(CustomUser, username__iexact='name')
    context = {
        'institution': institution        
    }
    
    return render(request, 'pat_institution.html', context)

def appointments(request):
    appointments = patientAppointment.objects.filter(patient=request.user.username)
    context = {
        'appointments': appointments
    }
    return render(request, 'pat_appointments.html', context)

def appointment(request, pk):
    if pk:
        # If id is provided, get the existing object or 404
        appointment = get_object_or_404(patientAppointment, id=pk)

    if request.method == "POST":
        form = PatientAppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            messages.success(request, 'System change Success')
            
    else:
        form = PatientAppointmentForm(instance=appointment)
        
    context = {
        'form': form,
        'appointment': appointment
    }
    return render(request, 'pat_appointment.html', context)

def book_appointment(request):
    form = PatientAppointmentForm()
    form.fields['patient'].initial = request.user.username
    
    if request.method == "POST":
        form = PatientAppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            print('Success')
            messages.success(request, 'Appointment Booked Successfully')
            return redirect('patients:appointments')
            
        else:
            messages.success(request, 'Booking not Successful')
            print("not successful ")
            return redirect('patients:book_appointment')
            
             
        
    context = {
            'form': form
        }
    
    return render(request, 'pat_make_appointment.html', context)

def delete_appointment(request, pk):
    appointment = get_object_or_404(patientAppointment, id=pk)
    appointment.delete()
    messages.success(request, "Appoitment Deleted Successfuly")
    return redirect('patients:appointments')